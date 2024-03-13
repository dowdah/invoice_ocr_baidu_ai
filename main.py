import requests
import urllib.parse
import os
import base64
import json
import time
import csv
import argparse

API_KEY = os.environ.get('BAIDU_API_KEY')
SECRET_KEY = os.environ.get('BAIDU_SECRET_KEY')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
SLEEP_TIME = 1  # Avoid exceeding QPS Unit: second
BAIDU_ACCESS_TOKEN_API = "https://aip.baidubce.com/oauth/2.0/token"
BAIDU_INVOICE_OCR_API = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice"
INVOICE_MAPPING = {'InvoiceCode': '发票代码', 'InvoiceNum': '发票号码', 'InvoiceDate': '开票日期',
                   'TotalAmount': '发票金额(不含税)', 'AmountInFiguers': '发票金额(含税)', 'CheckCode': '校验码',
                   'SellerRegisterNum': '纳税人识别号(销售方)', 'InvoiceTypeOrg': '发票类型'}

if not (API_KEY and SECRET_KEY):
    print('[Error] BAIDU_API_KEY or BAIDU_SECRET_KEY missing! Please set environment variables properly.')
    exit(1)


def get_access_token():
    """
    获取百度云OCR API的access_token。若本地已有未过期的access_token则直接返回，否则重新获取。
    :return: access_token
    """
    flag = False
    try:
        with open(os.path.join(BASE_DIR, "access_token.json"), "r") as f:
            access_token_info = json.load(f)
    except FileNotFoundError:
        flag = True
    else:
        if access_token_info["expiration_time"] < int(time.time()):
            flag = True
    if flag:
        r = requests.post(BAIDU_ACCESS_TOKEN_API, params={
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": SECRET_KEY
        }, headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }, data="")
        access_token_info = dict()
        access_token_info["access_token"] = r.json()["access_token"]
        access_token_info["expiration_time"] = r.json()["expires_in"] + int(time.time())
        with open(os.path.join(BASE_DIR, "access_token.json"), "w") as f:
            json.dump(access_token_info, f, ensure_ascii=False)
    return access_token_info["access_token"]


def invoice_file_to_info(invoice_file_path):
    """
    识别发票文件并返回发票信息
    :param invoice_file_path: 发票文件路径
    :return: 发票信息
    """
    ext = invoice_file_path.split('.')[-1]
    with open(invoice_file_path, "rb") as f:
        file_content_processed = urllib.parse.quote_plus(base64.b64encode(f.read()).decode('utf8'))
    if ext in ['ofd', 'OFD']:
        data = f"ofd_file={ file_content_processed }&seal_tag=false"
    elif ext in ['pdf', 'PDF']:
        data = f"pdf_file={ file_content_processed }&seal_tag=false"
    else:
        data = f"image={ file_content_processed }&seal_tag=false"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    params = {
        "access_token": get_access_token(),
    }
    try:
        response_json = requests.post(BAIDU_INVOICE_OCR_API, params=params, headers=headers, data=data).json()
    except:
        print("[Error] Network error")
        return None
    else:
        if 'words_result' in response_json.keys():
            invoice_info = response_json["words_result"]
            return invoice_info
        elif 'error_code' in response_json.keys():
            print(f"[Error] Baidu: {response_json['error_msg']}")
            return None
        else:
            print("[Error] Unknown error")
            return None


def output_invoice_info(raw_file_path, invoice_info, output_format="csv"):
    """
    输出发票信息到文件
    :param raw_file_path: 原始文件路径，用于生成输出文件名
    :param invoice_info: 发票信息
    :param output_format: 输出格式
    :return: None
    """
    # output_file_name = f"{invoice_info['InvoiceCode']}_{invoice_info['InvoiceNum']}.{output_format}"
    output_file_name = f"{raw_file_path.split('/')[-1].split('.')[0]}.{output_format}"
    output_file_path = os.path.join(OUTPUT_DIR, output_file_name)
    match output_format:
        case 'csv':
            with open(output_file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(INVOICE_MAPPING.values())
                writer.writerow([invoice_info.get(key, "") for key in INVOICE_MAPPING.keys()])
        case 'json':
            with open(output_file_path, "w") as f:
                json.dump(invoice_info, f, ensure_ascii=False)
        case _:
            print("[Error] Unsupported output format")
            return
    print(f"[Info] Output to {output_file_path}")
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='OCR for invoice files (img, pdf, or ofd) using Baidu API with batch processing support.')
    # 添加文件路径参数，允许多个值，但是这个参数是可选的
    parser.add_argument('--files', metavar='FILE', type=str, nargs='+',
                        help='Path(s) to the invoice file(s).')
    # 添加文件夹路径参数，这个参数也是可选的
    parser.add_argument('--folder', type=str, help='Directory path to process all invoice files within.')
    # 添加格式参数
    parser.add_argument('--format', choices=['csv', 'json'], default='csv',
                        help='Output format: csv or json (default: csv).')
    # 解析命令行参数
    args = parser.parse_args()
    if args.folder:
        # 如果提供了文件夹路径，遍历该文件夹下的所有文件
        file_paths = [os.path.join(args.folder, f) for f in os.listdir(args.folder) if
                      os.path.isfile(os.path.join(args.folder, f))]
    elif args.files:
        # 如果提供了文件路径列表，直接使用该列表
        file_paths = args.files
    else:
        # 如果没有提供文件或文件夹路径，打印帮助信息并退出
        parser.print_help()
        exit(1)
    # 创建输出文件夹
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    # 处理每个文件
    total_files = len(file_paths)
    current_file = 0
    for file_path in file_paths:
        current_file += 1
        print(f"[Info] Processing file {current_file}/{total_files}: {file_path}")
        invoice_info = invoice_file_to_info(file_path)
        if invoice_info:
            output_invoice_info(file_path, invoice_info, args.format)
        if current_file < total_files:
            time.sleep(SLEEP_TIME)
    print("[Info] Done")
