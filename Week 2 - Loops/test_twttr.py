from twttr import shorten


def test_lowercase():
    assert shorten("WHaTs My NaMe") == "WHTs My NM"


def test_uppercase():
    assert shorten("WHATS MY NAME") == "WHTS MY NM"


def test_no_vowels():
    assert shorten("WHTs My NM") == "WHTs My NM"


def test_with_numbers():
    assert shorten("WHT4 My NM") == "WHT4 My NM"
