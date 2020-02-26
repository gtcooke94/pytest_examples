import mod2
from mod2 import sut2
from mod2.sut2 import hello

import mock
import pytest

def test_hello():
    assert "Hello GREG" == sut2.hello()

def test_hello_override(override_default_name):
    assert "Hello TEST" == sut2.hello()

def test_hello_again():
    assert "Hello GREG" == sut2.hello()

def test_hello_override_different_import(override_default_name):
    assert "Hello TEST" == hello()

@pytest.fixture()
def override_default_name():
    hold_default_name = mod2.sut2.DEFAULT_NAME
    mod2.sut2.DEFAULT_NAME = "TEST"
    yield
    mod2.sut2.DEFAULT_NAME = hold_default_name
