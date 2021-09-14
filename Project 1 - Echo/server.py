import sys
import socket

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a UDP socket. Notice the use of SOCK_GRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

print("The server is ready to recieve on port: " + str(serverPort) + "\n")

# Loop forever listening for incoming UDP messages
while True:
    # Recieve and print the client data from "data" socket
    data, address = serverSocket.recvfrom(1024)
    print("Recieve data from client " + address[0] + ", " + str(address[1]) + ": " + data.decode())

    # Echo back to client
    print("Sending data to client " + address[0] + ", " + str(address[1]) + ": " + data.decode())
