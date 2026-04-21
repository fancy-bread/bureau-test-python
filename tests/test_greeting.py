from src.greeting import greet


def test_named_greeting_includes_name():
    result = greet("Alice")
    assert "Alice" in result


def test_named_greeting_returns_str():
    result = greet("Alice")
    assert isinstance(result, str)


def test_empty_string_uses_world():
    result = greet("")
    assert "World" in result


def test_empty_string_returns_str():
    result = greet("")
    assert isinstance(result, str)
