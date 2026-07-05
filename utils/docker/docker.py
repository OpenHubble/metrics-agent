import docker


def calculate_cpu_percentage(current_usage, previous_usage, system_cpu_usage, previous_system_cpu_usage, online_cpus):
    delta_cpu_usage = current_usage - previous_usage
    delta_system_cpu_usage = system_cpu_usage - previous_system_cpu_usage
    if delta_system_cpu_usage > 0 and online_cpus > 0:
        cpu_percentage = (delta_cpu_usage / delta_system_cpu_usage) * online_cpus * 100
        return cpu_percentage
    return 0


def get_docker_metrics():
    client = docker.from_env()
    containers = client.containers.list(all=True)

    containers_metrics = []

    for container in containers:
        container_id = container.id
        container_name = container.name
        container_status = container.attrs['State']['Status']
        container_exit_code = container.attrs['State'].get('ExitCode', None)
        health_status = container.attrs['State'].get('Health', {}).get('Status', 'unknown')

        container_metrics = {
            "id": container_id,
            "name": container_name,
            "status": container_status,
            "exitcode": container_exit_code,
            "health": health_status
        }

        if container_status == "running":
            stats = container.stats(stream=False)
            cpu_stats = stats.get('cpu_stats', {})
            memory_stats = stats.get('memory_stats', {})
            blkio_stats = stats.get('blkio_stats', {}).get('io_service_bytes_recursive', [])
            net_stats = stats.get('networks', {})
            pids = stats.get('pids_stats', {}).get('current', 0)

            memory_usage = memory_stats.get('usage', 0)
            memory_limit = memory_stats.get('limit', 0)
            memory_percentage = (memory_usage / memory_limit) * 100 if memory_limit > 0 else 0

            previous_cpu_usage = cpu_stats.get('precpu_stats', {}).get('cpu_usage', {}).get('total_usage', 0)
            current_cpu_usage = cpu_stats.get('cpu_usage', {}).get('total_usage', 0)
            previous_system_cpu_usage = cpu_stats.get('precpu_stats', {}).get('system_cpu_usage', 0)
            current_system_cpu_usage = cpu_stats.get('system_cpu_usage', 0)
            online_cpus = cpu_stats.get('online_cpus', 0)

            cpu_percentage = calculate_cpu_percentage(
                current_cpu_usage, previous_cpu_usage, current_system_cpu_usage, previous_system_cpu_usage, online_cpus
            )

            container_metrics.update({
                "memory": {
                    "memory_usage": memory_usage,
                    "memory_limit": memory_limit,
                    "memory_percentage": round(memory_percentage, 2),
                },
                "cpu": {
                    "cpu_percentage": round(cpu_percentage, 2),
                    "cpu_usage": current_cpu_usage,
                },
                "blkio_stats": {
                    "read_bytes": sum(blkio.get('value', 0) for blkio in blkio_stats if
                                      blkio.get('op') == 'read') if blkio_stats else 0,
                    "write_bytes": sum(blkio.get('value', 0) for blkio in blkio_stats if
                                       blkio.get('op') == 'write') if blkio_stats else 0,
                },
                "networks": {
                    net_name: {
                        "rx_bytes": net_data.get('rx_bytes', 0),
                        "tx_bytes": net_data.get('tx_bytes', 0),
                        "rx_packets": net_data.get('rx_packets', 0),
                        "tx_packets": net_data.get('tx_packets', 0),
                    }
                    for net_name, net_data in net_stats.items()
                },
                "pids": pids,
            })

        containers_metrics.append(container_metrics)

    return containers_metrics
