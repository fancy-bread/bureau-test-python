def greet(name: str) -> str:
    """Return a greeting string for the given name.

    If name is empty, defaults to 'World'.
    """
    effective_name = name if name else "World"
    return f"Hello, {effective_name}!"
