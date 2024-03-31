"""Dummy tests."""
from llm_toolz.hello_world import message


def test_message():
    assert message() == "Hello, world!"
