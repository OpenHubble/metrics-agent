"""
swap.py

This script provides information about the swap memory usage on the host machine.
It uses the `psutil` library to retrieve metrics related to swap memory.

Functions:
----------
- get_swap_usage(): 
    Returns a dictionary containing the following swap memory metrics:
    - total (int): Total swap memory in bytes.
    - used (int): Swap memory currently in use, in bytes.
    - free (int): Swap memory currently available, in bytes.
    - percent (float): Percentage of total swap memory currently being used.

Example Output:
---------------
{'total': 6442450944, 
 'used': 5343019008, 
 'free': 1099431936, 
 'percent': 82.9}
    
Dependencies:
-------------
- psutil: A Python library for system and process utilities. 
  Install it via `pip install psutil`.

"""

import psutil


def get_swap_usage():
    swap = psutil.swap_memory()  # Fetch once

    return {
        'total': swap.total,
        'used': swap.used,
        'free': swap.free,
        'percent': swap.percent
    }
