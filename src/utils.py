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

def get_scratchpad_files():
    if not os.path.exists(SCRATCPAD_DIR):
        return "No files in scratchpad"
    
    ', '.join([f for f in os.listdir(SCRATCPAD_DIR) if os.path.isfile(os.path.join(SCRATCPAD_DIR, f))])