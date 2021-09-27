import logging
import os


class LogData:

    @staticmethod
    def log_step():
        logging.basicConfig(filename=os.path.join(os.getcwd(), "report", "test_result.log"),
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger





