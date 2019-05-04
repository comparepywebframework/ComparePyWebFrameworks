from enum import Enum

class ErrorMessage(Enum):
    CONNECTION_ERROR = "Connection error"

errors = {"error_message": ErrorMessage.CONNECTION_ERROR.value}