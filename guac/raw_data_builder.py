import datetime
import pandas as pd
from loguru import logger

from guac.google_reporting_api import GoogleReportingAPI

def build_raw_data_df(report: dict) -> pd.DataFrame:
    """
    Builds a pandas DataFrame representing the raw data of
    a Google Analytics Report.

    The a Google Reporting Analytics API v4 Report is built for each
    day between the provided start and end dates (inclusive). The reports
    are compiled into a single pd.DataFrame and returned.

    Parameters
    ---
    report: dict
        A dictionary representing a Google Reporting Analytics API v4 Report object

    Returns
    ---
    raw_data_df: pd.DataFrame
        A DataFrame representing the raw data of a Google
        Reporting Analytics API v4 Report.
    """
    logger.info(f'building raw data df for {report["viewId"]}...')
    service = GoogleReportingAPI('GUAC_PIT', 'GOOGLE_REPORTING_API_SCOPES')

    view_id = report['viewId']
    report_dates = get_report_dates(report['dateRanges'][0])
    dimensions = report['dimensions']
    metrics = report['metrics']

    reports = list()

    for date in report_dates:
        report_response = service.get_report(
            view_id=view_id,
            start_date=date,
            end_date=date,
            dimensions=dimensions,
            metrics=metrics
            )

        report_df = convert_report_to_df(
            report_response=report_response['reports'][0],
            report_date=date
            )

        reports.append(report_df)

    raw_data_df = pd.concat(reports)
    logger.success(f'Raw data compiled: {raw_data_df.info()}')
    return raw_data_df


def get_report_dates(report_date_range: dict) -> list:
    """
    Extracts all the dates between a Reports date range (inclusive), returning
    as a list.

    Parameters
    ---
    report_date_range: dict
        A dictionary representing a Reporting object's date range

    Return
    ---
    report_dates: list
        A list with each item as a string representation of a date
        within the reports date range
    """
    report_dates = list()
    start_date = report_date_range["startDate"]
    end_date = report_date_range["endDate"]
    logger.info(f'extracting dates betweeen {start_date} and {end_date}...')

    report_dates.append(start_date)

    pointer_date_string = start_date

    while pointer_date_string != end_date:
        pointer_dt = datetime.datetime.strptime(pointer_date_string, '%Y-%m-%d')
        next_date = pointer_dt + datetime.timedelta(days=1)
        pointer_date_string = next_date.strftime('%Y-%m-%d')
        report_dates.append(pointer_date_string)

    return report_dates

def convert_report_to_df(report_response: object, report_date: str) -> pd.DataFrame:
    """
    Convert the Google Reporting API Report Response object
    to a pd.DataFrame
    """
    logger.info('converting report to dataframe...')
    column_header = report_response["columnHeader"]
    column_header_dimensions = column_header['dimensions']
    column_header_metric_header = column_header['metricHeader']
    column_header_metric_header_entries = column_header_metric_header['metricHeaderEntries']
    data = report_response["data"]

    # Build DataFrame
    raw_df_headers = column_header_dimensions + \
        [i['name'] for i in  column_header_metric_header_entries]
    df_headers = [header.replace('ga:' , '').capitalize() for header in raw_df_headers]

    df_rows = list()

    if 'rows' in data:
        data_rows = data['rows']
    else:
        return pd.DataFrame() # Return empty DF for days that report no data

    for row in data_rows:
        dimensions = row['dimensions']
        for metrics in row['metrics']:
            df_rows.append(dimensions + metrics['values'])

    df = pd.DataFrame(data=df_rows, columns=df_headers)

    df['Date'] = report_date
    ordered_headers = ['Date'] + df_headers
    report_df = df.loc[:, ordered_headers]

    logger.success(f'{report_date} Report: {str(report_df.size)}')
    return report_df
