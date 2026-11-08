import pytest

def add(x, y):
    return x + y

def test_add_success():
    assert add(1,2) == 3

def test_add_fail():
    assert add(1,3) == 667