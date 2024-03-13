# 百度 OCR 发票处理

此脚本使用百度 OCR API 识别和提取发票文件（包括图片、PDF 或 OFD 文件）中的信息。它可以灵活处理单个文件、同时处理多个文件或处理指定目录下的所有文件。提取的发票数据可以保存为 CSV 或 JSON 格式。

## 功能

- 同时处理单个或多个文件。
- 批量处理指定目录下的所有发票文件。
- 支持 CSV 和 JSON 输出格式。

## 先决条件

- Python 3.10+（开发时使用 Python 3.11）。
- 安装 Pipenv 模块

## 设置

### 依赖

该项目使用 `pipenv` 管理依赖。如果您尚未安装 `pipenv`，请运行以下命令进行安装：

```bash
pip install pipenv
```

安装 `pipenv` 后，导航到项目目录并安装所需的依赖：

```bash
pipenv install
```

如果您没有使用 Python 3.11，可以在安装依赖时忽略 Pipfile。**请注意，这可能会导致兼容性问题，并且在任何情况下，您的 Python 版本必须不小于3.10。**

```bash
pipenv install --ignore-pipfile
```

### 环境变量

您必须设置 `BAIDU_API_KEY` 和 `BAIDU_SECRET_KEY` 环境变量，使用您的百度 OCR API 凭证。您可以在[百度AI开放平台](https://ai.baidu.com/)获取这些内容。您可以在 shell 中设置这些变量，或将它们添加到项目根目录中的 `.env` 文件(这样就能在执行`pipenv shell`后自动导入环境变量)。 

如下是`.env`文件的示例:

```env
BAIDU_API_KEY='your_api_key_here'
BAIDU_SECRET_KEY='your_secret_key_here'
```

## 使用

激活 pipenv shell：

```bash
pipenv shell
```

### 处理单个或多个文件

要处理单个文件或多个文件，请使用 `--files` 参数，后跟文件路径：

```bash
python main.py --files path/to/invoice1.pdf path/to/invoice2.jpg
```

### 目录处理

要处理目录中的所有发票文件，请使用 `--folder` 参数：

```bash
python main.py --folder path/to/invoices_directory
```

### 输出格式

脚本默认以 CSV 格式输出数据。要输出 JSON 格式，请使用 `--format` 选项：

```bash
python main.py --files path/to/invoice.pdf --format json
```

## 输出

处理后的发票数据将保存在项目文件夹内的 `output` 目录中。输出文件以原始文件命名，并根据所选格式添加适当的扩展名。

## 许可证

该项目根据 MIT 许可证授权。详情见 LICENSE 文件。

## 免责声明

此工具仅供教育和研究目的使用。请道德地使用它，并遵守百度 OCR API 服务条款。