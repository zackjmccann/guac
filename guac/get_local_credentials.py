import os
import json
from loguru import logger
from dotenv import load_dotenv

load_dotenv()


def get_local_credentials(credentials_name: str, credentials_format='value'):
    """
    Retrieves local credentials under the provided name

    Parameters
    credentials_name: str
        The name of the environmental variable storing the credentials
    credentials_format: string
        The format of the returned credentials.
        Accepts "value" (default) or "json"

    Return
    service_account_credentials_file (as type specified)
    """
    logger.info('Loading credentials...')
    if credentials_format == 'value':
        return os.getenv(credentials_name)

    elif credentials_format == 'json':
        with open(os.getenv(credentials_name), encoding='UTF-8') as service_account_credentials_file:
            service_account_credentials = json.load(service_account_credentials_file)
            service_account_credentials_file.close()
            return service_account_credentials
    else:
        raise NameError(f'Unsupported return type: {credentials_format}')
