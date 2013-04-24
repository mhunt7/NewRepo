import socket
import socket
import os
import sys
import signal
#import dbus
import numpy as np
import csv

class localClient(object):

    def __init__(self,
                 name,
                 plugged,
                 charge_percentage,
                 charge_rate,
                 charge_level):
        self.name = name
        self.plugged = plugged
        self.charge_percentage = charge_percentage
        self.charge_rate = charge_rate
        self.charge_level = charge_level

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = str(value)

#========================================================================
#========================================================================
# STORAGE PORTFOLIO SUMMARY
#========================================================================
#========================================================================
# Echo client program


HOST = '86.188.199.50'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)