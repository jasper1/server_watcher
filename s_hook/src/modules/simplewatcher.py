'''
Created on Jun 20, 2011

@author: jasper
'''

import os, psutil, time
from modules.i_controller import Controller

class SimpleWatcher(Controller):
    '''
    Simple watcher plugin
    '''

    def __init__(self,params):
        super(SimpleWatcher, self).__init__(params)
        
        
    def done(self):
        server = {}
        server['load_average']  = os.getloadavg()
        server['total_phymem']  = psutil.TOTAL_PHYMEM
        server['total_virtmem'] = psutil.total_virtmem()
        server['used_phymem']   = psutil.used_phymem()
        server['used_virtmem']  = psutil.used_virtmem()
        server['cpu_percent']   = psutil.cpu_percent()
        server['cpu_count']     = psutil.NUM_CPUS
        
        f_processes = []
        processes = psutil.get_process_list()
        processes.sort(key=lambda x: x.get_cpu_times())
        processes.reverse()
        for p in processes[:10]:
            f_processes.append((p.name, p.get_cpu_times(), p.get_memory_percent(),time.ctime(p.create_time),))
        
        server['processes'] = f_processes
        return server
        
        
        