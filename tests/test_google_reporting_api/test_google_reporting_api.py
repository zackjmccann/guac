from guac.google_reporting_api import GoogleReportingAPI
from guac.get_local_credentials import get_local_credentials

def test_google_reporting_api_method_connect():
    """Test the 'connect' method of the GoogleReportingAPI Class"""
    ga_service = GoogleReportingAPI('GUAC_PIT', 'GOOGLE_REPORTING_API_SCOPES')
    assert isinstance(ga_service, object)

def test_google_reporting_api_method_get_report():
    """Test the 'get_report' method of the GoogleReportingAPI Class"""
    all_web_site_data_view_id = get_local_credentials('ALL_WEBSITE_SITE_DATA_VIEW_ID')
    start_date = '2022-10-15'
    end_date = '2022-10-15'
    ga_service = GoogleReportingAPI('GUAC_PIT', 'GOOGLE_REPORTING_API_SCOPES')
    dimensions = [{'name': 'ga:country'}]
    metrics = [{'expression': 'ga:sessions'}]

    response = ga_service.get_report(
        view_id=all_web_site_data_view_id,
        start_date=start_date,
        end_date=end_date,
        dimensions=dimensions,
        metrics=metrics
        )

    reports = response['reports']

    assert len(reports) == 1
