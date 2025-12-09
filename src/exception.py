# This exception.py file will have custom exception class for the project
# we will define a custom exception class to handle exceptions in a more structured way
# for example we can create a class called CustomException which will inherit from the base Exception class
# and we can add additional attributes like error message, error code etc. to provide more context about the exception

import sys
import logging
from src.logger import logging # importing the logging module from logger.py file for logging the exceptions

def error_message_detail(error, error_detail:sys):
    """this function will return the detailed error message with file name and line number where the exception occurred"""
    _,_,exc_tb = error_detail.exc_info() # this talks about the exception details like type, value and traceback
    line_number = exc_tb.tb_lineno # this will give the line number where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename # this will give the file name where the exception occurred
    error_message = f"Error occurred in script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error) # converting the error to string to get the error message
    )
    return error_message
    

class CustomException(Exception):
    """this is a custom exception class which will inherit from the base Exception class
        and will have additional attributes like error message, error detail etc.
    """

    def __init__(self, error_message, error_detail:sys):
        """this is the constructor of the CustomException class
            it will take error message and error detail as input"""
        super().__init__(error_message) # calling the constructor of the base Exception class, for example Exception.__init__(self, error_message)
        self.error_message = error_message_detail(error_message, error_detail) # getting the detailed error message

    def __str__(self): 
        """this function will return the string representation of the CustomException class"""
        return self.error_message # returning the error message when the exception is printed
    
if __name__ == "__main__":
    try:
        a = 1 / 0 # this will raise a ZeroDivisionError
    except Exception as e:
        logging.info("Dividing by zero error occurred.")
        raise CustomException(e, sys) # raising the custom exception with the original exception and sys module