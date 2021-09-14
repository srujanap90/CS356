"""
Name: Srujana Paruchuri
UCID: sp2743
"""

import sys
import socket
import time
import random
import struct

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

print('The server is ready to receive on port: ' + str(serverPort))

# Loop forever listening for incoming UDP messages
while True:
    # Initialize a random integer between 1 and 10
    num = random.randint(1, 10)

    # Receving the data sent over the client
    data, address = serverSocket.recvfrom(1024)

    # Unpack
    message, sequence_number = struct.unpack("!ii", data)

    time.sleep(0.5)

    # Respond back to client if num >=4
    if num >= 4:
        print("Responding to ping request with sequence number " + str(sequence_number))
        data = struct.pack('!ii', 2, sequence_number)
        serverSocket.sendto(data, address)
    else:
        print("Message with sequence number " + str(sequence_number) + " dropped")
