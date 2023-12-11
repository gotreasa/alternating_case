import pytest

from modules import alternate_case


def describe_alternating_case():
    def should_error_when_not_string():
        """🧪 should give an error message when something other than a string is passed"""
        with pytest.raises(ValueError, match="❗️ The input should be a string"):
            alternate_case.to_alternating_case(1234)

    def should_hanle_lower_case_hello_world():
        """🧪 should convert 'hello world' to 'HELLO WORLD'"""
        assert alternate_case.to_alternating_case("hello world") == "HELLO WORLD"
