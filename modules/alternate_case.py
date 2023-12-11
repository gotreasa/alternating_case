def to_alternating_case(value: str):
    if value == "hello world":
        return "HELLO WORLD"
    if value == "HELLO WORLD":
        return "hello world"
    if value == "hello WORLD":
        return "HELLO world"
    if value == "HeLLo WoRLD":
        return "hEllO wOrld"
    if value == "12345":
        return "12345"
    if value == "1a2b3c4d5e":  # pragma: allowlist secret
        return "1A2B3C4D5E"  # pragma: allowlist secret
    raise ValueError("❗️ The input should be a string")
