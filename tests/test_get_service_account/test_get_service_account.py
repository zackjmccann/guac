from guac.google_connections import get_service_account


def test_get_service_account_path():
    """Test retrievial of service account credential from path"""
    assert get_service_account('path') == './client_secrets.json'


def test_get_service_account_json():
    """Test retrievial of service account credentials from json"""
    assert isinstance(get_service_account('json'), dict)
