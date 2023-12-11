def to_alternating_case(string: str) -> str:
    if not isinstance(string, str):
        raise ValueError("❗️ The input should be a string")
    return string.swapcase()
