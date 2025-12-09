# THis logger.py file will have all the code related to logging configuration for the project
# we will set up the logging configuration here so that we can use it across the entire project 
# for example setting log format, log level, log file location etc. will be done here

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log" # Here we are creating a log file name with current timestamp
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # creating logs directory inside current working directory
os.makedirs(logs_path, exist_ok=True) # creating logs directory if it does not exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # complete log file path 

logging.basicConfig(
    # Here we are setting up the basic configuration for logging 
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # we are setting the log format
    level=logging.INFO, # setting the log level to INFO
)

