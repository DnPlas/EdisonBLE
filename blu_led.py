#!/usr/bin/python
# -*- mode: python; coding: utf-8 -*-

# Copyright (C) 2014, Oscar Acena <oscaracena@gmail.com>
# This software is under the terms of Apache License v2 or later.

from __future__ import print_function

import sys
from gattlib import GATTRequester


class Reader(object):
    def __init__(self, address):
        self.requester = GATTRequester(address , False)
        self.connect()
        self.send_data()

    def connect(self):
        print("Connecting...", end=' ')
        sys.stdout.flush()

        self.requester.connect(True)
        print("OK!")

    def send_data(self):
        self.requester.write_by_handle(0xb, str(bytearray([1]))) # You can find the bluetooth handle using
                                                                 # requester.discover_characteristics()
                                                                 # In this case, my Arduino's handle is 0xb

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <addr>".format(sys.argv[0]))
        sys.exit(1)

    Reader(sys.argv[1])
    print("Done.")
