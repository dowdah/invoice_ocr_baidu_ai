# Baidu OCR Invoice Processing

![Version: 1.1](https://img.shields.io/badge/Version-1.1-brightgreen?style=for-the-badge) [![中文文档](https://img.shields.io/badge/中文文档-brightgreen?style=for-the-badge)](README-zh.md)

This script utilizes the Baidu OCR API to recognize and extract information from invoice documents, including images, PDFs, or OFD files. It offers the flexibility to process individual files, multiple files at once, or all files within a specified directory. The extracted invoice data can be saved in either CSV or JSON format.

## Features

- Process individual or multiple files simultaneously.
- Batch process all invoice files within a specified directory.
- Support for CSV and JSON output formats.

## Prerequisites

- Python 3.10+(Developed with Python 3.11).
- Pipenv for managing project dependencies.

## Setup

### Dependencies

The project uses `pipenv` for managing dependencies. To install `pipenv` if you haven't already, run:

```bash
pip install pipenv
```

After installing `pipenv`, navigate to the project directory and install the required dependencies:

```bash
pipenv install
```

If you are not using Python 3.11, you may ignore pipfile when installing dependencies. **Note that this may lead to compatibility issues and under any circumstances, you must use Python 3.10+.**

```bash
pipenv install --ignore-pipfile
```



### Environment Variables

You must set the `BAIDU_API_KEY` and `BAIDU_SECRET_KEY` environment variables with your Baidu OCR API credentials. You can set these variables in your shell or add them to a `.env` file in the project root:

```env
BAIDU_API_KEY='your_api_key_here'
BAIDU_SECRET_KEY='your_secret_key_here'
```

## Usage

Activate the pipenv shell:

```bash
pipenv shell
```

### Processing Single or Multiple Files

To process a single file or multiple files, use the `--files` argument followed by the path(s) to the file(s):

```bash
python main.py --files path/to/invoice1.pdf path/to/invoice2.jpg
```

### Directory Processing

To process all invoice files within a directory, use the `--folder` argument:

```bash
python main.py --folder path/to/invoices_directory
```

### Output Format

The script outputs data in CSV format by default. To output in JSON format, use the `--format` option:

```bash
python main.py --files path/to/invoice.pdf --format json
```

## Output

Processed invoice data will be saved in the `output` directory within the project folder. The output files are named after the original files with an appropriate extension based on the chosen format.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer

This tool is intended for educational and research purposes only. Please use it responsibly and ethically, adhering to the Baidu OCR API terms of service.
