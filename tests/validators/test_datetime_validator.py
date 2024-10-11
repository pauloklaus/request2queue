from validators.datetime_validator import is_datetime_valid

def test_valid_datetime():
    assert is_datetime_valid("2022-06-02T16:17:18")

def test_not_valid_datetime():
    assert not is_datetime_valid("2022-02-31T16:17:18")
    assert not is_datetime_valid("2022-06")
