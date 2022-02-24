import os

import pytest
from awscm.awstools import get_aws_client, get_aws_session


@pytest.fixture
def test_setup(monkeypatch):
    def mock_expanduser(path):
        """Returns a new path that points to test_data folder."""
        # Return:
        # current dir of test file + folder in which dummy files exist + name of file being looked for.
        return os.path.dirname(__file__) + "/test_data/" + path.split("/")[-1]

    # Monkeypatch expanduser function so that the config and credentials
    # file from test_data folder are read instead of the actual files
    # present in '~/.aws/' dir.
    monkeypatch.setattr("os.path.expanduser", mock_expanduser)

    # Ensure stray default session isn't used.
    monkeypatch.setattr("boto3.DEFAULT_SESSION", None)


@pytest.fixture
def mock_session(test_setup):
    """Returns a mock aws session object."""
    return get_aws_session(profile_name="test_profile")
