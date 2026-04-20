def greet(name: str) -> str:
    """Return a greeting string for the given name.

    If name is empty, 'World' is used as the default name.
    """
    display_name = name if name else "World"
    return f"Hello, {display_name}!"
