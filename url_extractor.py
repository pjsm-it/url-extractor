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
    """
    Get text from clipboard or file depending on arguments.
    - If a file path is provided in args, read and return its contents.
    - Otherwise, return the current clipboard contents using pyperclip.
    """
    pass


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
    """
    Deliver the output depending on the input source.
    - If source is clipboard, copy output to clipboard using pyperclip.
    - If source is file, print output to terminal (stdout).
    """
    pass


def main():
    """
    Main function — orchestrates the full flow.
    1. Parse arguments with argparse.
    2. Call get_input() to retrieve text.
    3. Call extract_urls() on the text.
    4. Call remove_duplicates() on the matches.
    5. Call sort_and_split() on the unique URLs.
    6. Call format_output() with the two groups.
    7. Call deliver_output() with the result.
    """
    pass


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()