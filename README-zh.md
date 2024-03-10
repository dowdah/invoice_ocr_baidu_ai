# 百度发票OCR工具

这个Python工具利用百度OCR API提取图片、PDF或OFD文件中的发票细节，并将信息输出为CSV或JSON格式。

## 特性

- 从图片、PDF或OFD文件中识别发票信息。
- 将识别出的发票信息输出为CSV或JSON格式。
- 命令行界面用于指定格式。

## 前提条件

在使用这个工具之前，请确保你已经：

1. 在你的系统上安装了Python 3.10+。
2. 拥有一个百度云账号，从[百度AI](https://ai.baidu.com/)获取API密钥和秘密密钥。
3. 将`BAIDU_API_KEY`和`BAIDU_SECRET_KEY`设置为环境变量。

## 安装和设置

这个项目使用Pipenv来管理依赖关系。如果你还没有安装Pipenv，可以全局安装：

```bash
pip install pipenv
```

按照以下步骤设置项目环境：

1. 克隆仓库或将脚本下载到你的本地机器。
2. 导航到项目目录并运行`pipenv install`来安装依赖。

## 使用方法

使用以下命令激活Pipenv shell并运行脚本：

```bash
pipenv run python main.py <path_to_invoice_file> [--format <output_format>]
```

参数：

- `<path_to_invoice_file>`：待处理的发票文件的完整路径。
- `<output_format>`：可选。指定输出格式（`csv`或`json`）。默认为`csv`。

### 示例

处理一个发票并以JSON格式输出：

```bash
pipenv run python main.py /path/to/invoice.pdf --format json
```

## 输出

脚本将以指定的格式将识别出的发票信息保存在与脚本相同的目录中。输出文件以发票代码和号码命名。

## 错误处理

该脚本包含对缺失API密钥、网络错误以及百度OCR API响应错误的错误处理。确保你的API密钥配置正确。

## 许可证

该项目在MIT许可证下授权。详情见LICENSE文件。
