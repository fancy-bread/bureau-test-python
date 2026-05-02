def greet(name: str) -> str:
    """Return a greeting string for the given name.

    If name is empty, 'World' is used as the default.
    """
    return f"Hello, {name or 'World'}!"
