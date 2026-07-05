"""
network_io.py

This script provides information about network I/O (input/output) operations on the host machine.
It uses the `psutil` library to retrieve metrics related to network data transmission and reception.

Functions:
----------
- get_network_io():
    Returns a dictionary containing the following network I/O metrics:
    - bytes_sent (int): Total number of bytes sent over the network.
    - bytes_received (int): Total number of bytes received from the network.
    - packets_sent (int): Total number of packets sent.
    - packets_received (int): Total number of packets received.

Example Output:
---------------
{'bytes_sent': 2675965952, 
 'bytes_received': 3748928512, 
 'packets_sent': 48013411, 
 'packets_received': 52815362}
    
Dependencies:
-------------
- psutil: A Python library for system and process utilities.
  Install it via `pip install psutil`.

"""

import psutil

previous_network_io = None


def get_network_io():
    global previous_network_io
    network_io = psutil.net_io_counters()

    if previous_network_io is None:
        previous_network_io = network_io
        return {
            'bytes_sent': 0,
            'bytes_received': 0,
            'packets_sent': 0,
            'packets_received': 0
        }

    # Calculate the diff
    diff_bytes_sent = network_io.bytes_sent - previous_network_io.bytes_sent
    diff_bytes_received = network_io.bytes_recv - previous_network_io.bytes_recv
    diff_packets_sent = network_io.packets_sent - previous_network_io.packets_sent
    diff_packets_received = network_io.packets_recv - previous_network_io.packets_recv

    # Update the previous values for the next call
    previous_network_io = network_io

    return {
        'bytes_sent': diff_bytes_sent,
        'bytes_received': diff_bytes_received,
        'packets_sent': diff_packets_sent,
        'packets_received': diff_packets_received
    }
