#!/usr/bin/env python3
"""
url_extractor.py - Extracts and validates URLs from clipboard or file input.
"""

import re
import sys
import argparse
import pyperclip


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Define the URL regex pattern here
URL_PATTERN = re.compile(r'''(
    (?:https?)                                  # http or https                      
    ://                                         # literal ://
    (?:www\.)?                                  # optional www.
    [a-z0-9-]{1,63}                             # domain name
    \.                                          # lieral .
    (?:[a-z]{2,6}\.)?                           # optional second-level TLD (co.uk)
    [a-z]{2,6}                                  # top-level domain
    (?:/[a-zA-Z0-9/\-._~:@!$&'()*+,;=%?#]+)?    # optional path
)''', re.VERBOSE)


# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

def get_input(args):
    if args.file:
        with open(args.file, 'r') as f:
            return f.read()
    return pyperclip.paste()


def extract_urls(text):
    return URL_PATTERN.findall(text)


def remove_duplicates(urls):
    seen = set()
    unique_urls = []
    for url in urls:
        if url.lower() not in seen:
            seen.add(url.lower())
            unique_urls.append(url)
    return unique_urls


def sort_and_split(urls):
    http_urls = []
    https_urls = []
    for url in urls:
        if url.startswith('https://'):
            https_urls.append(url)
        elif url.startswith('http://'):
            http_urls.append(url)
    http_urls.sort() 
    https_urls.sort()
    return http_urls, https_urls


def format_output(http_urls, https_urls):
    lines = []
    lines.append('HTTP')
    lines.append('-' * 30)
    for url in http_urls:
        lines.append(url)
    lines.append('')
    lines.append('HTTPS')
    lines.append('-' * 30)
    for url in https_urls:
        lines.append(url)
    return '\n'.join(lines)


def deliver_output(output, source):
    if source == 'clipboard':
        pyperclip.copy(output)
    else:
        print(output)


def main():
    parser = argparse.ArgumentParser(
        description='Extract and validate URLs from clipboard or file'
    )
    parser.add_argument(
        'file',
        nargs='?',
        help='Path to a text file containing URLs'
    )
    args = parser.parse_args()

    text = get_input(args)
    source = 'file' if args.file else 'clipboard'
    urls = extract_urls(text)
    unique_urls = remove_duplicates(urls)
    http_urls, https_urls = sort_and_split(unique_urls)
    output = format_output(http_urls, https_urls)
    deliver_output(output, source)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()