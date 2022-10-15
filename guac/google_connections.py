import os
import json
from loguru import logger
from dotenv import load_dotenv
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()


def get_service_account(credentials_format='path'):
    """
    Retrieves the service account credentials

    Parameters
    format: string
        The format of the returned credentials.
        Accepts "path" (default) or "json"

    Return
    service_account_credentials_file (as type specified)
    """
    logger.info('Loading credentials...')
    if credentials_format == 'path':
        logger.info(os.getenv('GUAC_PIT'))
        return os.getenv('GUAC_PIT')

    elif credentials_format == 'json':
        with open(os.getenv('GUAC_PIT'), encoding='UTF-8') as service_account_credentials_file:
            service_account_credentials = json.load(service_account_credentials_file)
            service_account_credentials_file.close()
            return service_account_credentials
    else:
        raise NameError(f'Unsupported return type: {credentials_format}')


def connect_reporting_api():
    """Connect to a Google Analytics Account via the Reporting API"""
    logger.info('Calling to Google Analystics...')
    scopes = ['https://www.googleapis.com/auth/analytics.readonly']
    key_file_location = os.getenv('GUAC_PIT')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(key_file_location, scopes)
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    # pylint: disable=maybe-no-member
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': '277792780',
                    'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                    'metrics': [{'expression': 'ga:sessions'}],
                    'dimensions': [{'name': 'ga:country'}]
                }]
        }
    ).execute()

def get_analytics_reporting_resource():
    """Returns an Analytics Reporting API V4 Resource object"""
    logger.info('Calling to Google Analystics...')
    scopes = ['https://www.googleapis.com/auth/analytics.readonly']
    key_file_location = os.getenv('GUAC_PIT')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(key_file_location, scopes)
    return build('analyticsreporting', 'v4', credentials=credentials)
