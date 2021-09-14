"""
Name: Srujana Paruchuri
UCID: sp2743
"""

import sys
import socket
import time
import struct

# Get the server hostname and port to start ping
host = sys.argv[1]
port = int(sys.argv[2])

# Create client socket. SOCK_DGRAM is used for UDP
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Time out
clientsocket.settimeout(1)

# Variables
dataEcho = ""
sequence_number = 0
rtt = []
time_taken = 0.0
start_time = 0.0
packets_recv = 0

# Print the host and port it is pining from
print("Pinging " + host + " " + str(port))

while True:
    start_time = time.time()
    sequence_number += 1

    # Pack
    data = struct.pack('!ii', 1, sequence_number)
    clientsocket.sendto(data, (host, port))

    try:
        dataEcho, address = clientsocket.recvfrom(1024)
        time_taken = time.time() - start_time
        rtt.append(time_taken)

        # Unpack
        message, sequence_recv = struct.unpack("!ii", dataEcho)
        print("Ping message number " + str(sequence_recv) + " RTT: " + str(time_taken) + " seconds")
        packets_recv += 1
    except Exception:
        print("Ping message number " + str(sequence_number) + " timed out")

    if sequence_number == 10:
        break

# Close the client socket
clientsocket.close()

# Calculate statistics (RTT)
packet = sequence_number
packets_lost = packet - packets_recv
lost_percent = ((float(packets_lost) / packet) * 100)
lost_percent = int(lost_percent)

# Print statistics
print("\nPing statistics for " + host)
print(str(packet) + " packets transmitted, " + str(packets_recv) + " recieved, " + str(lost_percent) + "% packet loss")
print("Min/Max/Avg RTT = " + (str(min(rtt))) + " / " + (str(max(rtt))) + " / " + (str((sum(rtt) / packets_recv))) + " secs")
