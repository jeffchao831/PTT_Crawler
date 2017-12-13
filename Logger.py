import logging
import time

FORMAT = '%(asctime)-10s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def log_warning(function_name, message):
    """Logging Warning"""
    logger.warning(function_name+' Warning: '+message)

def log_info(function_name, message):
    """Logging Info"""
    logger.info(function_name+' Info: '+message)

def log_exception(function_name, message):
    """Logging Exception"""
    logger.exception(function_name+' Exception: '+message)

