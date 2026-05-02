from greeting import greet


def test_greet_named_returns_string_with_name() -> None:
    result = greet("Alice")
    assert isinstance(result, str)
    assert "Alice" in result


def test_greet_empty_string_returns_greeting_with_world() -> None:
    result = greet("")
    assert isinstance(result, str)
    assert "World" in result


def test_greet_return_type_is_str() -> None:
    result = greet("Bob")
    assert type(result) is str
