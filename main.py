import os
import sys
import json
from dotenv import load_dotenv
from loguru import logger

# Logger and Environment Variables Configuration
load_dotenv()
logger.remove()
logger.add(sys.stderr, format="<g>[{time:HH:mm:ss!UTC} | {function: ^20}]</> {message}", level="INFO")

def get_service_account():
    """Retrieves the service account credentials"""
    logger.info('Loading credentials...')
    with open(os.getenv('SERVICE_CREDS')) as service_account_creds_file:
        service_account_creds = json.load(service_account_creds_file)
        service_account_creds_file.close()

    return service_account_creds

if __name__ == '__main__':
    logger.info(f'Running process on {__name__}.')
    
    service_account_creds = get_service_account()
    logger.info(service_account_creds)
    logger.info('exiting main.')
    sys.exit(0)