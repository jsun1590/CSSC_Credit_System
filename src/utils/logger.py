import logging
import logging.config
import datetime
import inspect

current_time = datetime.datetime.now()
current_time_formatted = current_time.strftime("%Y-%m-%d")

logging.config.fileConfig("src/configs/logging.conf", defaults={'logfilename': f"src/logs/{current_time_formatted}.log"})
logger = logging.getLogger()