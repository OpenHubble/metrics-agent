import subprocess


def get_gpu_usage():
    try:
        result = subprocess.check_output(
            ['nvidia-smi', '--query-gpu=utilization.gpu,memory.used,memory.total', '--format=csv,noheader,nounits'])
        gpu_data = []
        for line in result.decode().strip().split('\n'):
            usage, mem_used, mem_total = line.split(',')
            gpu_data.append({
                'gpu_usage_percent': int(usage.strip()),
                'memory_used_mb': int(mem_used.strip()),
                'memory_total_mb': int(mem_total.strip())
            })

        return gpu_data
    except FileNotFoundError:
        return "NVIDIA GPU monitoring is not available on this system."


print(get_gpu_usage())
