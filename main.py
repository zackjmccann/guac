import sys
from dotenv import load_dotenv
from loguru import logger


# Logger and Environment Variables Configuration
load_dotenv()
logger.remove()
logger.add(sys.stderr,
    format="<g>[{time:HH:mm:ss!UTC} | {function: ^20}]</> {message}",
    level="INFO"
    )


if __name__ == '__main__':
    logger.info(f'Running process on {__name__}.')

    logger.info('exiting main.')
    sys.exit(0)
