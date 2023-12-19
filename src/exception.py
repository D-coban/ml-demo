import sys
# import logging
from src.logger import logging

#if you want to understand the details about custom exceptions, like whats exec_info etc, read the documentation
def error_message_details(error, error_details:sys):
    _, _, exc_tb = error_details.exc_info() # we returned element contains info about in what file and line error occurred.
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_msg = 'Error occurred in Python Script {0} in line number {1} with the message: {2}'.format(file_name, line_no, str(error))
    return error_msg
    
class CustomException(Exception):
    def __init__(self, error_msg, error_detail:sys):
        super().__init__(error_msg)
        self.error_msg = error_message_details(error_msg, error_detail)

    def __str__(self):
        return self.error_msg        
    
    
if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divided by zero!")
        raise CustomException(e, sys)