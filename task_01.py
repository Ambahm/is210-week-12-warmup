#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """
    Examples:
        >>> simple_lookup({}, 'banana')
        Warning: Your index/key doesn't exist.
        {}
        >>> simple_lookup([1,2], 4)
        Warning: Your index/key doesn't exist.
        [1, 2]
    """
    try:
        return var1[var2]
    except (IndexError, KeyError):  # Error types tuple
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
