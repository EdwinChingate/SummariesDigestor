def maybe_int(s):
    """Cast '12' → 12, leave others as-is."""
    try:
        return int(s)
    except Exception:
        return s
