from guac.google_connections import get_analytics_reporting_resource


def test_get_analytics_reporting_resource():
    """Test retrievial of Google Analytics Reporting API V4 Resource"""
    assert isinstance(get_analytics_reporting_resource(), object)
