#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#

import zmq
import sys

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)
port1 = "5555"
if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)
context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.10.10:%s" % port)
if len(sys.argv) > 2:
    socket.connect("tcp://192.168.10.11:%s" % port1)

#  Do 20 requests, waiting each time for a response
for request in range(20):
    print("Sent request to server %s …" % request)
    socket.send(b'Request')

    #  Get the reply.
    message = socket.recv()
    print("Server: %s [ %s ]" % (request, message.decode()))
