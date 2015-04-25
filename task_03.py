#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Class to ccess files, to  login file names,
    along message and time stamp, catch IOError msg

    Attr:
        None
    """

    def __init__(self, logfilename):
        """Class constructor

        Attr:
            None

        Args:
            logfilename(str): File name
            msgs(list):stored messages' list
        """

        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """ Function to login IO Error

         Args:
            msg(str): Messages fr erors encountered
            timestamp(UNIX time):UNIX time stamp set to None

        Return:
            Returns IO error encountered related to file operations
        """

        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """ ``IOError``:Predictable errors are caught and are,
        themselves, logged.

        Args:
            None

        Returns:
          Errors caught

        Examples:
            open('filename')
        """
        handled = []

        try:
            fhandler = open(self.logfilename, 'a') # open file

        except IOError as error:     # file opening error
            self.log('file opening error') # log in error and re raise
            raise error


        for index, entry in enumerate(self.msgs):
            try:    # other errors
                fhandler.write(str(entry) + '\n')
                handled.append(index)

            except IOError:
                self.log('Another IO Error') # log error and continue program
                break


        try:
            for index in handled[::-1]:
                del self.msgs[index]

        except IOError as error:
            raise error


        finally:
            fhandler.close() # handler closed inspite exceptions

