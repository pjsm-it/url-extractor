import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from url_extractor import (
    extract_urls,
    remove_duplicates,
    sort_and_split,
    format_output
)


# ---------------------------------------------------------------------------
# extract_urls
# ---------------------------------------------------------------------------

def test_extract_urls_finds_http():
    text = "visit http://google.com for more"
    assert extract_urls(text) == ['http://google.com']

def test_extract_urls_finds_https():
    text = "visit https://github.com for more"
    assert extract_urls(text) == ['https://github.com']

def test_extract_urls_ignores_malformed():
    text = "broken htp://broken.com and www.nodomain.com"
    assert extract_urls(text) == []

def test_extract_urls_finds_multiple():
    text = "https://github.com and http://google.com"
    assert sorted(extract_urls(text)) == ['http://google.com', 'https://github.com']

def test_extract_urls_finds_path():
    text = "https://github.com/nomore451/url-extractor"
    assert extract_urls(text) == ['https://github.com/nomore451/url-extractor']

def test_extract_urls_finds_co_uk():
    text = "http://www.example.co.uk/blog"
    assert extract_urls(text) == ['http://www.example.co.uk/blog']


# ---------------------------------------------------------------------------
# remove_duplicates
# ---------------------------------------------------------------------------

def test_remove_duplicates_removes_exact():
    urls = ['http://google.com', 'http://google.com', 'http://github.com']
    assert remove_duplicates(urls) == ['http://google.com', 'http://github.com']

def test_remove_duplicates_case_insensitive():
    urls = ['http://Google.com', 'http://google.com']
    assert remove_duplicates(urls) == ['http://Google.com']

def test_remove_duplicates_preserves_order():
    urls = ['http://zebra.com', 'http://apple.com', 'http://zebra.com']
    assert remove_duplicates(urls) == ['http://zebra.com', 'http://apple.com']

def test_remove_duplicates_empty():
    assert remove_duplicates([]) == []


# ---------------------------------------------------------------------------
# sort_and_split
# ---------------------------------------------------------------------------

def test_sort_and_split_separates_http_https():
    urls = ['https://github.com', 'http://google.com']
    http_urls, https_urls = sort_and_split(urls)
    assert http_urls == ['http://google.com']
    assert https_urls == ['https://github.com']

def test_sort_and_split_sorts_alphabetically():
    urls = ['http://zebra.com', 'http://apple.com', 'http://mango.com']
    http_urls, https_urls = sort_and_split(urls)
    assert http_urls == ['http://apple.com', 'http://mango.com', 'http://zebra.com']

def test_sort_and_split_empty():
    http_urls, https_urls = sort_and_split([])
    assert http_urls == []
    assert https_urls == []


# ---------------------------------------------------------------------------
# format_output
# ---------------------------------------------------------------------------

def test_format_output_contains_headers():
    output = format_output(['http://google.com'], ['https://github.com'])
    assert 'HTTP' in output
    assert 'HTTPS' in output

def test_format_output_contains_urls():
    output = format_output(['http://google.com'], ['https://github.com'])
    assert 'http://google.com' in output
    assert 'https://github.com' in output

def test_format_output_contains_separator():
    output = format_output(['http://google.com'], ['https://github.com'])
    assert '-' * 30 in output

def test_format_output_empty_lists():
    output = format_output([], [])
    assert 'HTTP' in output
    assert 'HTTPS' in output
