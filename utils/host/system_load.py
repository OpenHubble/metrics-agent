"""
system_load.py

This script provides the system load average over the last 1, 5, and 15 minutes.
It uses the `os` module to retrieve load averages, which are typically used to gauge the system's workload.

Functions:
----------
- get_system_load(): 
    Returns a dictionary containing the system's load averages over the last 1, 5, and 15 minutes:
    - 1_min (float): Load average over the last 1 minute.
    - 5_min (float): Load average over the last 5 minutes.
    - 15_min (float): Load average over the last 15 minutes.
    If the system doesn't support retrieving load averages, it returns a message indicating that the information is not available.

Example Output:
---------------
{'1_min': 1.36669921875, 
 '5_min': 2.0283203125, 
 '15_min': 2.39404296875}

Dependencies:
-------------
- os: A built-in Python module, no installation required.

"""

import os


def get_system_load():
    if hasattr(os, 'getloadavg'):
        load1, load5, load15 = os.getloadavg()

        return {'1_min': load1, '5_min': load5, '15_min': load15}
    else:
        return "System load average not available on this platform."
