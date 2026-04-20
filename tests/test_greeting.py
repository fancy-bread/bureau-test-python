from src.greeting import greet


def test_greet_named_returns_greeting_with_name():
    result = greet("Alice")
    assert isinstance(result, str)
    assert "Alice" in result
    assert result == "Hello, Alice!"


def test_greet_empty_string_uses_world_as_default():
    result = greet("")
    assert isinstance(result, str)
    assert "World" in result
    assert result == "Hello, World!"


def test_greet_return_type_is_str():
    assert isinstance(greet("Bob"), str)
