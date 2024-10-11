import re

def is_aws_region_valid(aws_region: str) -> bool:
    return bool(re.match(r"^[a-z]{2}-[a-z]*-[0-9]{1}$", aws_region))
