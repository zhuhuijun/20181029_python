import logging

class MyLog(object):
    def __init__(self):
        logger = logging.getLogger()
        logfile = 'test.log'
        hdlr = logging.FileHandler(logfile)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.NOTSET)
    def logDebug(self,msg):
        logging.debug(msg)