from greeting import greet


def test_named_greeting():
    result = greet("Alice")
    assert "Alice" in result


def test_empty_string_defaults_to_world():
    result = greet("")
    assert "World" in result


def test_return_type():
    assert isinstance(greet("Bob"), str)
