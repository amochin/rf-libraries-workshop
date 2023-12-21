"""
Using RF library interfaces might help implementing API methods.
Try creating a new method like defined in API (e.g. get_keyword_names)
and use code completion.
"""
from robot.api.interfaces import DynamicLibrary

class MyLib(DynamicLibrary):
    pass