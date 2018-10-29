import pytest
@pytest.fixture
def driver_args():
    return ['--log-level=Debug']