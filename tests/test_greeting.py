from greeting import greet


def test_greet_named_returns_string_with_name():
    result = greet("Alice")
    assert isinstance(result, str)
    assert "Alice" in result


def test_greet_empty_string_returns_world():
    result = greet("")
    assert isinstance(result, str)
    assert "World" in result


def test_greet_return_type():
    assert isinstance(greet("Bob"), str)
