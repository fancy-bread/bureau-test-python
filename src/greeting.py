def greet(name: str) -> str:
    """Return a greeting string for the given name.

    If name is empty, uses 'World' as the default.
    """
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"
