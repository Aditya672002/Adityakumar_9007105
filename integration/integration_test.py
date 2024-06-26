# integration_test.py
import pytest


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def test_add():
    assert add(3, 4) == 7

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(2, 3) == 7

def test_divide():
    assert divide(10, 2) == 8
