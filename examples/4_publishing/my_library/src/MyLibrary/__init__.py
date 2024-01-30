from robot.api.deco import keyword
from .libcore import MyLibCore
from ...version import VERSION


class MyLibrary(MyLibCore):
    """
    Some common library docs.
    Here can be also some static keywords
    """

    ROBOT_LIBRARY_VERSION = VERSION
    ROBOT_LIBRARY_SCOPE = "TEST SUITE"

    @keyword
    def some_static_keyword(self):
        pass
