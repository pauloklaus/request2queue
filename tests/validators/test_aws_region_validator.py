from validators.is_aws_region_valid import is_aws_region_valid

class TestAwsRegionValidator:
    def test_valid_aws_region(self):
        assert is_aws_region_valid("us-east-1")

    def test_not_valid_aws_region(self):
        assert not is_aws_region_valid("test")
