import logging
import logging.config

logging.config.fileConfig("src/configs/logging.conf")
logger = logging.getLogger(__name__)