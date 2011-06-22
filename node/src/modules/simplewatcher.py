'''
Created on Jun 20, 2011

@author: jasper
'''

import os, time
import psutil

from modules.i_controller import Controller
#from modules.platform_spc import swapinfo, meminfo
from modules.platform_spc import *

class SimpleWatcher(Controller):
    '''
    Simple watcher plugin
    '''

    def __init__(self,params):
        super(SimpleWatcher, self).__init__(params)
        
        
    def done(self):

        server = {}
        # Get system variables
        #=======================================================================
        # server['load_average']  = os.getloadavg()
        # 
        # server['total_virtmem'],server['used_virtmem'] = swapinfo()
        # server['total_phymem'], server['avail_phymem'], server['used_phymem']   = meminfo()
        # server['cpu_count'], server['cpu_percent']   = cpuinfo()
        # server['disks'] = diskinfo()
        #=======================================================================
        server['iostat'] = iostat() 

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
        
        
        