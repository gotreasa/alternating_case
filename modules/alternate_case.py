def to_alternating_case(string: str) -> str:
    if not isinstance(string, str):
        raise ValueError("❗️ The input should be a string")
    result_string: str = ""
    for letter in string:
        if letter.isupper():
            result_string += letter.lower()
        else:
            result_string += letter.upper()
    return result_string
