def greet(name: str) -> str:
    """Return a greeting string for the given name.

    If name is empty, 'World' is used as the default.
    """
    if not name:
        name = "World"
    return f"Hello, {name}!"
