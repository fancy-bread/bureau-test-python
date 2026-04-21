from src.greeting import greet


def test_greet_named():
    result = greet("Alice")
    assert "Alice" in result


def test_greet_empty_name_uses_world():
    result = greet("")
    assert "World" in result


def test_greet_returns_str():
    result = greet("Alice")
    assert isinstance(result, str)
