import pytest

from modules import alternate_case


def describe_alternating_case():
    def should_error_when_not_string():
        """🧪 should give an error message when something other than a string is passed"""
        with pytest.raises(ValueError, match="❗️ The input should be a string"):
            alternate_case.to_alternating_case()
