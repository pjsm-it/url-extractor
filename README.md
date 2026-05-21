# URL Extractor

A Python CLI tool that extracts and validates URLs from clipboard text or a file using regex.

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## Features

- Extracts valid `http://` and `https://` URLs using regex
- Ignores malformed or incomplete URLs
- Removes duplicate URLs
- Sorts results alphabetically — HTTP first, HTTPS second
- Supports `.co.uk` and similar multi-part TLDs
- Two input modes: clipboard and file
- Clipboard mode returns results to clipboard for immediate pasting

---

## Requirements

- Python 3.x
- [pyperclip](https://pypi.org/project/pyperclip/)
- [pytest](https://pypi.org/project/pytest/) (for running tests)

Install dependencies:

```bash
pip install pyperclip pytest
```

---

## Installation

```bash
git clone https://github.com/nomore451/url-extractor.git
cd url-director
chmod +x url_extractor.py
```

---

## Usage

### Clipboard mode
Copy text containing URLs to your clipboard, then run:

```bash
./url_extractor.py
```

Results are copied back to your clipboard, ready to paste.

### File mode

```bash
# Print results to terminal
./url_extractor.py urls.txt

# Save results to a file
./url_extractor.py urls.txt > output.txt
```

---

## How It Works

The script uses a regular expression to match URLs that:

- Start with `http://` or `https://`
- Contain a valid domain name (letters, numbers, hyphens)
- Support multi-part TLDs such as `.co.uk`
- Follow standard URL structure

Invalid, incomplete, or malformed URLs are ignored. Results are grouped and sorted alphabetically — all HTTP URLs first, followed by all HTTPS URLs.

---

## License

MIT