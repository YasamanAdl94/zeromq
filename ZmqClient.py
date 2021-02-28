#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
# connecting to RPi's ip
socket.connect("tcp://192.168.10.10:5555")

#  Do 20 requests, waiting each time for a response
for request in range(20):
    print("Sent request to server %s …" % request)
    socket.send(b'Request')

    #  Get the reply.
    message = socket.recv()
    print("Server: %s [ %s ]" % (request, message.decode()))
