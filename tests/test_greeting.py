from src.greeting import greet


def test_greet_named():
    result = greet("Alice")
    assert isinstance(result, str)
    assert "Alice" in result


def test_greet_empty_string():
    result = greet("")
    assert isinstance(result, str)
    assert "World" in result


def test_greet_return_type():
    assert isinstance(greet("Bob"), str)
