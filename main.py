import os
import sys
import json
from dotenv import load_dotenv
from loguru import logger
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


# Logger and Environment Variables Configuration
load_dotenv()
logger.remove()
logger.add(sys.stderr, format="<g>[{time:HH:mm:ss!UTC} | {function: ^20}]</> {message}", level="INFO")

def get_service_account(format='path'):
    """
    Retrieves the service account credentials
    
    Parameters
    format: string
        The format of the returned credentials.
        Accepts "path" (default) or "json"
    
    Return
    service_account_creds (as type specified)
    """
    logger.info('Loading credentials...')
    if: format == 'path':
        return os.getenv('SERVICE_CREDS')

    elif format == 'json':
        with open(os.getenv('SERVICE_CREDS')) as service_account_creds_file:
            service_account_creds = json.load(service_account_creds_file)
            service_account_creds_file.close()

    return service_account_creds


@logger.catch
def reporting_api():
    """Initial interaction with Reporting API"""
    logger.info('Calling to Google Analystics')
    scopes = ['https://www.googleapis.com/auth/analytics.readonly']
    key_file_location = os.getenv('SERVICE_CREDS')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(key_file_location, scopes)
    analytics = build('analyticsreporting', 'v4', credentials=credentials)
    
    return analytics.reports().batchGet(
        body={
        'reportRequests': [
        {
            'viewId': "VIEW_ID",
            'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
            'metrics': [{'expression': 'ga:sessions'}],
            'dimensions': [{'name': 'ga:country'}]
        }]
        }
    ).execute()


if __name__ == '__main__':
    logger.info(f'Running process on {__name__}.')
    reporting_api()
    logger.info('exiting main.')
    sys.exit(0)
