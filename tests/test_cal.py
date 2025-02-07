"""Contains Tests for different Calc Functions"""
from app import add, sub
def test_add():
    """test addition functionality"""
    assert add(2,2)==4

def test_sub():
    """test subtraction functionality"""
    assert sub(7,5)==2
