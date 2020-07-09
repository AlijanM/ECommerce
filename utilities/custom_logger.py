import inspect
import logging

# It's explained in lecture 146
def customLogger(logLevel):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    # to append all logs in one log file, i.e. automation.log
    # fileHandler = logging.FileHandler("automation.log", mode='w')

    # creates and overwrites a log file for each class calling logger
    fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='w')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
