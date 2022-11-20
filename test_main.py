import json
import pytest
from main import http_requests


@pytest.mark.parametrize("text, result", [
    (['hello'], '"hello" - не является ссылкой'),
    (['world'], '"world" - не является ссылкой')])
def test_http_requests(text, result, capsys):
    http_requests(text)
    assert result in capsys.readouterr()[0]


@pytest.mark.parametrize("text, result", [
    (['https://www.facebook.com'], {"https://www.facebook.com": {"GET": 200, "HEAD": 200, "POST": 200,
                                                                 "PUT": 200, "DELETE": 200, "OPTIONS": 200}})])
def test_write_json(text, result):
    http_requests(text)
    with open('requests.json', 'r') as f:
        actual = json.load(f)
    assert result == actual
