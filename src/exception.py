import sys
import os
from typing import Any

# Add the src directory to the path so we can import our logger
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from logger import log_error, log_info

def error_message_detail(error: Exception, error_detail: sys.exc_info) -> str:
  
    
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    return error_message

class CustomException(Exception):
    """
    Custom exception class that provides detailed error information
    """
    def __init__(self, error_message: str, error_detail: sys.exc_info):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        # Log the error using our custom logger
        log_error(self.error_message)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    # Test the custom exception
    try:
        # This will actually cause a division by zero error
        a = 1 /0
    except Exception as e:
        log_info("Testing CustomException with division by zero error")
        raise CustomException(str(e), sys.exc_info())