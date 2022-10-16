from guac.get_local_credentials import get_local_credentials


def test_get_service_account_value():
    """Test retrievial of local credentials as value"""
    assert get_local_credentials('GUAC_PIT', 'value') == './client_secrets.json'


def test_get_service_account_json():
    """Test retrievial of local credentials as json"""
    assert isinstance(get_local_credentials('GUAC_PIT', 'json'), dict)
