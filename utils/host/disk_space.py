"""
disk_space.py

This script retrieves disk usage information for all mounted partitions on the system.
It uses the `psutil` module to get details on disk space usage, including total, used, free space, and usage percentage for each partition.

Functions:
----------
- get_disk_space(): 
    Retrieves the disk usage statistics for all mounted partitions on the system.
    It returns a dictionary where the keys are the device names (e.g., `/dev/sda1`), and the values are dictionaries containing:
    - total (int): Total space of the partition in bytes.
    - used (int): Used space on the partition in bytes.
    - free (int): Free space on the partition in bytes.
    - percent (float): Percentage of used space on the partition.

Example Output:
---------------
{
    '/dev/disk3s1s1': {'total': 245107195904, 'used': 10669703168, 'free': 26014027776, 'percent': 29.1},
    '/dev/disk3s6': {'total': 245107195904, 'used': 6443126784, 'free': 26014027776, 'percent': 19.9},
    '/dev/disk3s2': {'total': 245107195904, 'used': 7212998656, 'free': 26014027776, 'percent': 21.7},
    ...
}

Dependencies:
-------------
- psutil: A Python module for system and process utilities. It can be installed via `pip install psutil`.

"""

import psutil


def get_disk_space():
    return {
        p.device: {
            'total': usage.total,
            'used': usage.used,
            'free': usage.free,
            'percent': usage.percent
        }
        for p in psutil.disk_partitions()
        if not any(x in p.device for x in ('loop', 'overlay'))
           and (usage := psutil.disk_usage(p.mountpoint))
    }
