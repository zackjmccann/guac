import sys
from dotenv import load_dotenv
from loguru import logger

from guac.google_reporting_api import GoogleReportingAPI
from guac.raw_data_builder import build_raw_data_df

# Logger and Environment Variables Configuration
load_dotenv()
logger.remove()
logger.add(sys.stderr,
    format="<g>[{time:HH:mm:ss!UTC} | {function: ^20}]</> {message}",
    level="INFO"
    )


if __name__ == '__main__':
    logger.info(f'Running process on {__name__}.')
    service = GoogleReportingAPI('GUAC_PIT', 'GOOGLE_REPORTING_API_SCOPES')

    ALL_WEBSITE_SITE_DATA_VIEW_ID = '277792780'
    START_DATE = '2022-10-10'
    END_DATE = '2022-10-16'

    dimensions = [
        {'name': 'ga:country'},
        {'name': 'ga:city'},
        {'name': 'ga:browser'},
        {'name': 'ga:operatingSystem'},
        ]
    metrics = [
        {'expression': 'ga:sessions'},
        {'expression': 'ga:users'},
        {'expression': 'ga:pageviews'},
        {'expression': 'ga:timeOnPage'},
        ]

    report_request = {
            'viewId': ALL_WEBSITE_SITE_DATA_VIEW_ID,
            'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
            'dimensions': dimensions,
            'metrics': metrics
            }
    raw_data_df = build_raw_data_df(report=report_request)
    logger.success(raw_data_df)

    logger.info('exiting main.')
    sys.exit(0)
