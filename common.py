# -*- coding: utf-8 -*-

def check_type(obj, cls, nullable=False):
    if type(obj) is not cls:
        if not nullable or (nullable and obj is not None):
            raise TypeError(f"{obj} is not {cls}, nullable is {nullable}")
    return obj
