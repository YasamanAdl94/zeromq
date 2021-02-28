#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#

import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Client: %s" % message.decode())

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b'Responded')
