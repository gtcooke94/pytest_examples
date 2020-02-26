import mod
from mod import sut
from mod.sut import hello

import mock
import pytest

def test_hello():
    assert "Hello GREG" == sut.hello()

def test_hello_override(override_default_name):
    assert "Hello TEST" == sut.hello()

def test_hello_override_different_import(override_default_name):
    assert "Hello TEST" == hello()

def test_hello_again():
    assert "Hello GREG" == sut.hello()

@pytest.fixture()
def override_default_name():
    hold_default_name = mod.constants.DEFAULT_NAME
    mod.sut.DEFAULT_NAME = "TEST"
    yield
    mod.sut.DEFAULT_NAME = hold_default_name
