"""
memory.py

This script provides information about the memory usage on the host machine.
It uses the `psutil` library to retrieve metrics related to RAM usage.

Functions:
----------
- get_memory_usage(): 
    Returns a dictionary containing the following memory metrics:
    - total (int): Total physical memory (RAM) in bytes.
    - available (int): Memory currently available for new processes, in bytes.
    - used (int): Memory in use by processes, in bytes.
    - percent (float): Percentage of total memory currently being used.

Example Output:
---------------
{'total': 8589934592, 
 'available': 1116930048, 
 'used': 3696230400, 
 'percent': 87.0}
    
Dependencies:
-------------
- psutil: A Python library for system and process utilities. 
  Install it via `pip install psutil`.

"""

import psutil


def get_memory_usage():
    memory = psutil.virtual_memory()  # Fetch once

    return {
        'total': memory.total,
        'available': memory.available,
        'used': memory.used,
        'percent': memory.percent
    }
