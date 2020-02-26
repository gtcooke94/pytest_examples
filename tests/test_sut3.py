import mod3
from mod3 import sut3
from mod3.sut3 import hello
import mod
from mod.sut import return_name
import mod

import mock
import pytest

def test_hello():
    assert "Hello GREG" == sut3.hello()

#  def test_hello_override(override_default_name):
#      assert "Hello TEST" == sut3.hello()

def test_hello_again():
    assert "Hello GREG" == sut3.hello()

#  def test_hello_override_different_import(override_default_name):
#      assert "Hello TEST" == hello()

def mock_return_name():
    return return_name(name="TEST")

@pytest.mark.xfail
def test_hello_override_mock_different_import_fail():
    with mock.patch("mod.sut.return_name", side_effect=mock_return_name):
        assert "Hello TEST" == hello()

@pytest.mark.xfail
def test_hello_override_mock_fail():
    with mock.patch("mod.sut.return_name", side_effect=mock_return_name):
        assert "Hello TEST" == sut3.hello()

def test_hello_override_mock():
    with mock.patch("mod3.sut3.return_name", side_effect=mock_return_name):
        assert "Hello TEST" == sut3.hello()

def test_hello_override_mock_different_import():
    with mock.patch("mod3.sut3.return_name", side_effect=mock_return_name):
        assert "Hello TEST" == hello()
