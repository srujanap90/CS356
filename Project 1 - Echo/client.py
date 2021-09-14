#! /usr/bin/env python3
# Echo Client
import sys
import socket
import time

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
count = int(sys.argv[3])
data = 'X' * count  # Initialize data to be sent

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to server
print("Sending data to " + host + ", " + str(port) + ": " + data)
clientsocket.sendto(data.encode(), (host, port))
clientsocket.settimeout(1)

tries = 1

# Loop up to 3 tries
while tries != 3:
    try:
        # Recieve the server response
        dataEcho, address = clientsocket.recvfrom(count)
        print("Recieve data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
        clientsocket.close()
        sys.exit()
    except socket.timeout:
        print("Message timed out")
        # Send data to server again after timeout
        print("Sending data to " + host + ", " + str(port) + ": " + data + " (" + str(count) + " characters)")
        clientsocket.sendto(data.encode(), (host, port))

# After 3 tries
if tries == 3:
    print("Message timed out")
    # Close the client socket
    clientsocket.close()