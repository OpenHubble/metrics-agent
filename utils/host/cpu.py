"""
cpu.py

This script provides detailed information about the CPU usage on the host machine.
It uses the `psutil` library to retrieve metrics related to CPU cores, usage, and frequency.

Functions:
----------
- get_cpu_usage(): 
    Returns a dictionary containing the following CPU metrics:
    - total_cores (int): Total number of logical CPU cores.
    - usage_per_core (list of float): Percentage CPU usage per core after a specified interval.
    - total_usage (float): Overall CPU usage percentage across all cores.
    - frequency_mhz (float): Current CPU frequency in MHz.

Example Output:
---------------
{'total_cores': 8, 
 'usage_per_core': [22.2, 20.0, 15.2, 14.0, 11.0, 7.0, 3.0, 2.0], 
 'total_usage': 35.3, 
 'frequency_mhz': 3504}
    
Dependencies:
-------------
- psutil: A Python library for system and process utilities. 
  Install it via `pip install psutil`.

"""

import psutil


def get_cpu_usage():
    total_cores = psutil.cpu_count(logical=True)
    usage_per_core = psutil.cpu_percent(interval=0, percpu=True)  # No delay
    total_usage = psutil.cpu_percent(interval=0)  # No delay
    freq = psutil.cpu_freq().max  # More stable than .current

    return {
        'total_cores': total_cores,
        'usage_per_core': usage_per_core,
        'total_usage': total_usage,
        'frequency_mhz': freq
    }
