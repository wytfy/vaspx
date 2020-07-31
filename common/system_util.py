import psutil


def _get_cpu_info():
    cpu_count = psutil.cpu_count()
    cpu_freq = int(psutil.cpu_freq().current)
    cpu_percent = psutil.cpu_percent(percpu=True)
    return {
        'cpu_count': cpu_count,
        'cpu_freq': cpu_freq,
        'cpu_percent': cpu_percent
    }


def _get_memory_info():
    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()
    return {
        'virtual_memory': {
            'total': virtual_memory.total,
            'percent': virtual_memory.percent
        },
        'swap_memory': {
            'total': swap_memory.total,
            'percent': swap_memory.percent
        }
    }


def _get_disk_info():
    disk_partitions = psutil.disk_partitions()
    disk_usage = {
        disk_partition.mountpoint: {'total': psutil.disk_usage(disk_partition.mountpoint).total,
                                    'percent': psutil.disk_usage(disk_partition.mountpoint).percent}
        for disk_partition in disk_partitions
    }
    return disk_usage


def get_system_info():
    return {
        'cpu': _get_cpu_info(),
        'memory': _get_memory_info(),
        'disk': _get_disk_info()
    }


if __name__ == '__main__':
    print(get_system_info())
