import os
import sys
import pytest
from datetime import datetime

sys.path.insert(0, f"{os.getcwd()}/app")

from vulnerability.vulnerability import Vulnerability


@pytest.fixture
def vulnerability_mock() -> Vulnerability:
    return Vulnerability(
        uid = "test-123",
        source = "source",
        environment = "environment",
        short_description = "short description",
        long_description = "large description",
        created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        severity = "high",
    )
