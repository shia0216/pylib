# -*- coding: utf-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


def get_logger(name, severity='debug', filename=None, at=(0, 0), backup=4):
    formatter = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    if severity == 'debug':
        level = logging.DEBUG
    elif severity == 'info':
        level = logging.INFO
    elif severity == 'warning':
        level = logging.WARNING
    elif severity == 'error':
        level = logging.ERROR
    elif severity == 'critical':
        level = logging.CRITICAL
    else:
        raise ValueError(f"{severity} is not defined")

    logging.basicConfig(format=formatter, level=level)
    logger = logging.getLogger(name)

    if filename:
        hour, minute = at
        today = datetime.today()
        at_time = datetime(today.year, today.month, today.day, hour, minute)
        handler = TimedRotatingFileHandler(
            filename,
            when='W5',
            backupCount=backup,
            atTime=at_time)
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter(formatter))
        logger.addHandler(handler)

    return logger


def check_type(obj, cls, nullable=False):
    if type(obj) is not cls:
        if not nullable or (nullable and obj is not None):
            raise TypeError(f"{obj} is not {cls}, nullable is {nullable}")
    return obj
