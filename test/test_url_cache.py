# SPDX-FileCopyrightText: 2024 Nicco Kunzmann and Open Web Calendar Contributors <https://open-web-calendar.quelltext.eu/>
#
# SPDX-License-Identifier: GPL-2.0-only

"""
Test the caching functionality which will be used by subsequent tests.

"""
from app import cache_url, get_text_from_url, requests
from collections import namedtuple
import pytest

# use the content property
# see https://stackoverflow.com/a/18810889/1320237
MockRequestResult = namedtuple("MockRequestResult", "content")

def test_requests_are_automatically_cached(monkeypatch, mock):
    mock.return_value = MockRequestResult("trallala")
    monkeypatch.setattr(requests, "get", mock)
    assert get_text_from_url("https://asd.asd") == "trallala"
    assert get_text_from_url("https://asd.asd") == "trallala"
    mock.assert_called_once()

def test_tests_can_cache_values():
    cache_url("http://asd.asd", "test123")
    assert get_text_from_url("http://asd.asd") == "test123"

def test_caching_twice_works():
    cache_url("http://asd.asd", "test123")
    cache_url("http://asd.asd", "asd")
    assert get_text_from_url("http://asd.asd") == "asd"

def test_requests_are_forbidden():
    import requests
    with pytest.raises(RuntimeError):
        requests.get("https://duckduckgo.com")
