import os
import logging
import logging.handlers


def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(os.getenv('FORMAT'))
    ch.setFormatter(formatter)
    handler = logging.handlers.RotatingFileHandler(
              os.getenv('LOG_FILE'), maxBytes=int(os.getenv('MAX_BYTES')),
              backupCount=int(os.getenv('BACKUP_LOGS')))
    handler.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(handler)
    return logger
