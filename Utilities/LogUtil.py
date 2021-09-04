import logging
import time

class Logger():
    def __init__(self,logger,file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt1=logging.Formatter("%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s")

        cur_time = time.strftime("%Y-%m-%d")

        self.LogFileName = "..\\Logs\\Log"+ cur_time + ".txt"

        fh = logging.FileHandler(self.LogFileName,mode="a")
        fh.setFormatter(fmt1)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)

