#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#

import time
import zmq
import sys

port = "5555"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)
context = zmq.Context()
socket = context.socket(zmq.REP)
#   Sending messages on this port
socket.bind("tcp://*:port")
while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Client: %s" % message.decode())

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b'Responded', port)
