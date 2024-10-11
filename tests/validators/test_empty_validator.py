from validators.empty_validator import is_empty

def test_is_none():
    assert is_empty(None)

def test_is_empty_string():
    assert is_empty("")

def test_not_none_or_empty_string():
    assert not is_empty("test")
