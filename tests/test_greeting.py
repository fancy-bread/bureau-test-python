from src.greeting import greet


def test_greet_named():
    result = greet("Alice")
    assert "Alice" in result


def test_greet_empty_string_uses_world():
    result = greet("")
    assert "World" in result
    assert len(result) > 0


def test_greet_return_type():
    result = greet("Bob")
    assert isinstance(result, str)
