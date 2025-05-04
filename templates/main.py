from src.CnnClassifier import logging_config
from src.CnnClassifier import __version__ as current_version
from src.CnnClassifier import __author__ as author
from src.CnnClassifier import __email__ as email


logging_config.logging_config()
logging_config.logger.info(f"Current version: {current_version}")
logging_config.logger.info(f"Author: {author}")
logging_config.logger.info(f"Email: {email}")

