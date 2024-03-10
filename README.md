# Baidu Invoice OCR Utility

![Version: 1.0](https://img.shields.io/badge/Version-1.0-brightgreen?style=for-the-badge) [![中文文档](https://img.shields.io/badge/中文文档-brightgreen?style=for-the-badge)](README-zh.md)

This Python utility leverages the Baidu OCR API to extract invoice details from image, PDF, or OFD files and outputs the information in CSV or JSON format.

## Features

- OCR recognition of invoices from images, PDFs, or OFD files.
- Outputs recognized invoice information in CSV or JSON format.
- Command line interface for format specification.

## Prerequisites

Before using this utility, ensure you have:

1. Python 3.10+ installed on your system.
2. A Baidu Cloud account to obtain an API Key and Secret Key from the [Baidu AI](https://ai.baidu.com/).
3. Set the `BAIDU_API_KEY` and `BAIDU_SECRET_KEY` as environment variables.

## Setup and Installation

This project uses Pipenv for managing dependencies. If you haven't installed Pipenv yet, install it globally with:

```bash
pip install pipenv
```

To set up the project environment, follow these steps:

1. Clone the repository or download the script to your local machine.
2. Navigate to the project directory and run `pipenv install` to install dependencies.

## Usage

Activate the Pipenv shell and run the script with the following command:

```bash
pipenv run python main.py <path_to_invoice_file> [--format <output_format>]
```

Parameters:

- `<path_to_invoice_file>`: The full path to the invoice file to be processed.
- `<output_format>`: Optional. Specify the output format (`csv` or `json`). Default is `csv`.

### Example

To process an invoice and output in JSON format:

```bash
pipenv run python main.py /path/to/invoice.pdf --format json
```

## Output

The script saves the recognized invoice information in the specified format in the same directory as the script. The output file is named using the invoice code and number.

## Error Handling

The script includes error handling for missing API keys, network errors, and Baidu OCR API response errors. Make sure your API keys are correctly configured.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
