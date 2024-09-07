# # this are 5 logger codes used in entire project 
# logger.debug("This is a DEBUG message.")
# logger.info("This is an INFO message.")
# logger.warning("This is a WARNING message.")
# logger.error("This is an ERROR message.")
# logger.critical("This is a CRITICAL message.")


import logging
import os
from datetime import datetime

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a log directory if it doesn't exist
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Create a log file with a timestamp
log_file = os.path.join(log_directory, f"log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")

# File handler to write log messages to a file
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Formatter to define the layout of log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Also add a console handler to print logs to the terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
