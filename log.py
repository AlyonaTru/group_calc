import logging


logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")



def log(op,res):
    logging.info(f"{op} successful with result: {res}.")

def write_log(op,res):
    print(f'{op} = {res}')
   
