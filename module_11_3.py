import sys
from pprint import pprint

class Object():

    def __init__(self, arg):
        self.arg = arg


def introspection_info(obj):
    info = {}
    info['obj_type'] = type(obj)
    info['attr'] = vars(obj)
    info['metod'] = dir(obj)
    info['module'] = obj.__module__
    return info

number_info = introspection_info(Object('string'))
pprint(number_info)