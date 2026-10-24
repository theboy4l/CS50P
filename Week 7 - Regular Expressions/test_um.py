from um import count


def test_word():
    assert count("um") == 1


def test_question_mark_comma():
    assert count("um?") == 1
    assert count("Um,") == 1


def test_sentence():
    assert count("Um, thanks, um...") == 2


def test_word_again():
    assert count("yummy") == 0
    assert count("ALBUM") == 0


def test_caps():
    assert count("UM") == 1
