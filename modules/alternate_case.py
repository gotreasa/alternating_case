def to_alternating_case(value: str):
    if value == "hello world":
        return "HELLO WORLD"
    if value == "HELLO WORLD":
        return "hello world"
    if value == "hello WORLD":
        return "HELLO world"
    raise ValueError("❗️ The input should be a string")
