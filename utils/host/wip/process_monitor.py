import psutil


def get_process_info():
    process_data = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        process_data.append(proc.info)
    return process_data


print(get_process_info())
