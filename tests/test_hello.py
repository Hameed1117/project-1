"""Contains Tests for Hello function"""
from app.hello import say_hello

def test_say_hello():
    """test hello function functionality"""
    assert say_hello() == "Hello, World!"
