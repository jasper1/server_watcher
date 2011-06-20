'''
Created on Jun 20, 2011

@author: jasper
'''

import os, psutil, time, platform
from modules.i_controller import Controller

if platform.system()=="FreeBSD":
    from modules.platform_spc.freebsd import *
else:
    if platform.system()=="Linux":
        from modules.platform_spc.linux import *
    else:
        from modules.platform_spc.mac import *



class SimpleWatcher(Controller):
    '''
    Simple watcher plugin
    '''

    def __init__(self,params):
        super(SimpleWatcher, self).__init__(params)
        
        
    def done(self):

        server = {}
        # Get system variables
        server['load_average']  = os.getloadavg()
        
        server['total_virtmem'],server['used_virtmem'] = swapinfo()
        server['total_phymem'], server['avail_phymem'], server['used_phymem']   = meminfo()
        
        server['cpu_percent']   = psutil.cpu_percent()
        server['cpu_count']     = psutil.NUM_CPUS
        # server['disks']         = 

        # Get process list
        f_processes = []

        
        processes = psutil.get_process_list()
        processes = filter(lambda x: not x.pid == 0, processes)
        # processes.sort(key=lambda x: x.get_cpu_times())
        # processes.reverse()
        for p in processes:
            try:
                f_processes.append([
                     p.name,
                     p.get_cpu_times(),
                     p.get_memory_percent(),
                     time.ctime(p.create_time)
                     ])
            except:
                pass
    
        server['processes'] = f_processes

        return server
        
        
        