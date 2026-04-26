def greet(name: str) -> str:
    """Return a greeting string for the given name.

    If name is empty, defaults to 'World'.
    """
    return f"Hello, {name or 'World'}!"
