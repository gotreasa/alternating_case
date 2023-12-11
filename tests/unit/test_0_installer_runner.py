import pytest

from modules import alternate_case


def describe_alternating_case():
    def should_error_when_not_string():
        """🧪 should give an error message when something other than a string is passed"""
        with pytest.raises(ValueError, match="❗️ The input should be a string"):
            alternate_case.to_alternating_case(1234)

    def should_handle_lower_case_hello_world():
        """🧪 should convert 'hello world' to 'HELLO WORLD'"""
        assert alternate_case.to_alternating_case("hello world") == "HELLO WORLD"

    def should_handle_upper_case_hello_world():
        """🧪 should convert 'HELLO WORLD' to 'hello world'"""
        assert alternate_case.to_alternating_case("HELLO WORLD") == "hello world"

    def should_handle_mixed_case_for_words_hello_world():
        """🧪 should convert 'hello WORLD' to 'HELLO world'"""
        assert alternate_case.to_alternating_case("hello WORLD") == "HELLO world"

    def should_handle_mixed_case_hello_world():
        """🧪 should convert 'HeLLo WoRLD' to 'hEllO wOrld'"""
        assert alternate_case.to_alternating_case("HeLLo WoRLD") == "hEllO wOrld"

    def should_handle_1234():
        """🧪 should convert '12345' to '12345'"""
        assert alternate_case.to_alternating_case("12345") == "12345"
