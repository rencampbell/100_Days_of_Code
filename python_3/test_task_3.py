from python_3 import is_http_domain
import pytest


def test_is_domain():
    assert is_http_domain('https://ru.wikipedia.org/') == True

def test_is_not_domain():
    assert is_http_domain('griddynamics.com') == False
