import os
import logger

SCRATCPAD_DIR = "scratchpad"

def create_scratchpad():
    if not os.path.exists(SCRATCPAD_DIR):
        os.makedirs(SCRATCPAD_DIR)
        logger.log(logger.LogType.SUCCESS, "Scratchpad created successfully")

def delete_scratchpad():
    if os.path.exists(SCRATCPAD_DIR):
        os.rmdir(SCRATCPAD_DIR)
        logger.log(logger.LogType.SUCCESS, "Scratchpad deleted successfully")