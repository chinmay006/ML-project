import sys

def error_messege_detail(error,error_details:sys) :
    _,_,exc_tb=error_details.exc_info()   ## gets the information about the occurence of error in which particular line

    file_name=exc_tb.tb_frame.f_code.co_filename  ## custom exception handaing in python  

    error_messege="error occured in python script name [{0}] line number [{1}] error message [{2}]" .format()
    file_name,exc_tb.tb_lineno,str(error)

    return error_messege

class Custom_Exception(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)   ##inherit from Exception class
        self.error_messege=error_message_detail(error_message,error_details=error_details)

        def __str__(self):
            return self.error_messege
        
        if __name__ == "__main__":
            try:
                a=1/0
            except Exception as e:

                logging.info("Divide by zero")
                raise Custom_Exception(e,sys)

