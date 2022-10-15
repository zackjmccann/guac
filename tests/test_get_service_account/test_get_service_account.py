from guac.google_connections import get_service_account


def test_get_service_account_path():
    assert get_service_account('path') == '/Users/zackmccann/JamesMatter/guac-dev/client_secrets.json'


def test_get_service_account_json():
    assert type(get_service_account('json')) == dict
