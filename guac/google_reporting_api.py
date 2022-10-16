from loguru import logger
from oauth2client.service_account import ServiceAccountCredentials

from dotenv import load_dotenv
from googleapiclient.discovery import build
from guac.get_local_credentials import get_local_credentials

load_dotenv()

class GoogleReportingAPI():
    """The Goolge Reporting API (V4) as an object"""
    def __init__(self, credentials_locations, credentials_scope) -> None:
        self.credentials_locations = get_local_credentials(credentials_locations, 'value')
        self.credentials_scope = get_local_credentials(credentials_scope, 'value')

    def connect(self):
        """Build the inital resource object (lazy connection)"""
        logger.info('creating Google Reporting API connection object...')
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.credentials_locations,
            self.credentials_scope
            )
        return build('analyticsreporting', 'v4', credentials=credentials)

    def get_report(self,
        view_id: str,
        start_date: str,
        end_date: str,
        dimensions: list,
        metrics: list
        ) -> object:
        """Retrieves a Report from the Google Reporting API"""
        logger.info(f'retrieving Google Analytics report for view {view_id}...')

        report = {
            'viewId': view_id,
            'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
            'dimensions': dimensions,
            'metrics': metrics
            }

        with self.connect() as ga_service:
            logger.info('requesting analytics data...')
            # pylint: disable=maybe-no-member
            response = ga_service.reports().batchGet(body={'reportRequests': [report]}).execute()
            ga_service.close()
            logger.info('request closed.')

        logger.success(f'retrieved {len(response["reports"])} reports.')
        return response
