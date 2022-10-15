from guac.google_connections import connect_reporting_api


def test_connect_reporting_api():
    assert len(connect_reporting_api()['reports']) > 0
