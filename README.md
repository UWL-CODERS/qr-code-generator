<div align="center">

<img src="assets/logo.png" alt="CODERS Club QR Logo" width="20%" height="20%">

# CODERS Club: QR Code Generator

[![Discord][img-discord]][url-discord]
[![GitHub][img-github]][url-github]

A simple Python script to generate custom QR codes for the UWL-CODERS Club.

</div>

## Features

- Generate QR codes for any link
- Choose QR code version/density
- Embed a custom logo in the QR code
- Save output with a custom file name

## Requirements

- Python
- [qrcode](https://pypi.org/project/qrcode/)
- [pillow](https://pypi.org/project/pillow/)

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python generate_qr.py
```

You will be prompted for:
- Website link
- Output file name
- QR code version/density (optional)
- Logo file path (optional)

The generated QR code will be saved in the `output/` directory.

## Example

<img src="output/coders_website.png" alt="Example QR Code" width="50%">

[img-discord]: <https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fdiscord.com%2Fapi%2Finvites%2FUGupy2CVVq%3Fwith_counts%3Dtrue&query=%24.approximate_member_count&style=for-the-badge&label=Discord&color=5865F2&logoColor=white&labelColor=black&logo=discord>
[img-github]: <https://img.shields.io/github/stars/UWL-CODERS/CODERS_Website?style=for-the-badge&label=Stars&color=white&logoColor=white&labelColor=black&logo=github>
[url-discord]: <https://discord.gg/UGupy2CVVq>
[url-github]: <https://github.com/UWL-CODERS/CODERS_Website>