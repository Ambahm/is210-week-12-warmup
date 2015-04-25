#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Exception error handling, cathes particular type of error.
       Calling subclass Invalid age error from main
       class Exception

    """
    pass

def get_age(birthyear):
    """ Function to calculate age after checking enteredyear is >=0

    Args:
        birthyear(int): Birth year to check

    Return:
        mix: It can be int which is age or an error raised.

    Examples:
        >>> get_age(2099)

        Traceback (most recent call last):
        File "<pyshell#0>", line 1, in <module>
        get_age(2099)
        File "/home/vagrant/Desktop/is210-week-12-warmup/task_02.py", line 34,
        in get_age
        raise InvalidAgeError
        InvalidAgeError

        >>> get_age(2015)
        0

        >>> get_age(2007)
        8
    """

    age = datetime.datetime.now().year - birthyear

    if age >= 0:        # 0 or greater
        return age
    else:
        raise InvalidAgeError
