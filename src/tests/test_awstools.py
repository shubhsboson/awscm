import pytest
from awscm.awstools import get_aws_client, get_aws_session
from botocore.exceptions import ProfileNotFound
from moto import mock_sts


def test_get_aws_session(test_setup):
    """Tests the get_aws_session function with mocked config and credetails files."""

    # Check if it fails properly for profiles that don't exist
    with pytest.raises(ProfileNotFound):
        get_aws_session(profile_name="test_profile_which_doesn't_exist")

    # Check if it works for a mocked profile
    aws_session = get_aws_session(profile_name="test_profile")
    credentials = aws_session.get_credentials()
    assert credentials.access_key == "testing"
    assert credentials.secret_key == "testing"


@mock_sts
def test_get_aws_client(test_setup):
    """Tests the get_aws_client function with a mocked session object."""

    # The idea behind this test is that all this calls though mocked
    # wouldn't go through with out proper client object.
    mocked_session = get_aws_session(profile_name="test_profile")
    fake_client = get_aws_client(mocked_session, "sts", region="us-east-1")
    caller_identity = fake_client.get_caller_identity()
    assert caller_identity["Account"] == "123456789012"
