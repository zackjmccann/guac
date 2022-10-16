import pandas as pd
from guac.google_reporting_api import GoogleReportingAPI
from guac.raw_data_builder import build_raw_data_df, get_report_dates, convert_report_to_df


def test_build_raw_data_df():
    """Test the 'build_raw_data_df' function of GUAC"""

    all_web_site_data_view_id = '277792780'
    start_date = '2022-10-10'
    end_date = '2022-10-16'
    dimensions = [{'name': 'ga:country'} ]
    metrics = [{'expression': 'ga:sessions'}]

    report_request = {
        'viewId': all_web_site_data_view_id,
        'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
        'dimensions': dimensions,
        'metrics': metrics
        }

    raw_data_df = build_raw_data_df(report=report_request)
    assert isinstance(raw_data_df[0], object)
    assert len(raw_data_df) > 1

def test_get_report_dates():
    """Testing the 'get_report_dates' function of GUAC"""
    date_range = {'startDate': '2022-10-01', 'endDate': '2022-10-16'}
    dates = get_report_dates(date_range)

    assert len(dates) == 16
    assert dates[0] == '2022-10-01'
    assert dates[1] == '2022-10-02'
    assert dates[-2] == '2022-10-15'
    assert dates[-1] == '2022-10-16'

def test_convert_report_to_df():
    """Test the 'convert_report_to_df' function of GUAC"""
    service = GoogleReportingAPI('GUAC_PIT', 'GOOGLE_REPORTING_API_SCOPES')

    all_web_site_data_view_id = '277792780'
    start_date = '2022-10-10'
    end_date = '2022-10-16'
    dimensions = [{'name': 'ga:country'} ]
    metrics = [{'expression': 'ga:sessions'}]

    response = service.get_report(
        view_id=all_web_site_data_view_id,
        start_date=start_date,
        end_date=end_date,
        dimensions=dimensions,
        metrics=metrics
    )

    report_response = response['reports'][0]

    report_df = convert_report_to_df(report_response=report_response, report_date=start_date)

    assert isinstance(report_df, pd.DataFrame)
