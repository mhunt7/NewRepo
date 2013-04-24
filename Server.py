import socket

class Controller(object):

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


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
