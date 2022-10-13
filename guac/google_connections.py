import os
import json
from loguru import logger
from dotenv import load_dotenv

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
        logger.info(os.getenv('SERVICE_CREDENTIALS'))
        return os.getenv('SERVICE_CREDENTIALS')

    elif credentials_format == 'json':
        with open(os.getenv('SERVICE_CREDENTIALS')) as service_account_credentials_file:
            service_account_credentials = json.load(service_account_credentials_file)
            service_account_credentials_file.close()
            return service_account_credentials
    else:
        raise NameError(f'Unsupported return type: {credentials_format}')
