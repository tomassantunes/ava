import datetime
from enum import Enum

class LogType(Enum):
    INFO = 1
    WARNING = 2
    SUCCESS = 3
    ERROR = 4
    CRITICAL = 5

def log(log_type: LogType, message: str):
    print(f"[{log_type.name}] [{datetime.datetime.now()}] - {message}")