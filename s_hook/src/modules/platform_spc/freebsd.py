import subprocess


SYSCTL   = '/sbin/sysctl'
SWAPINFO = '/usr/sbin/swapinfo'

def physmem():
	mem = _get_data_sysctl("hw.physmem")
	return int(mem)

def swapinfo():
	p = subprocess.Popen([SWAPINFO], stdout=subprocess.PIPE)
	v = p.communicate()
	v = v[0].split()
	return (v[-2],v[-3],) # Return total and used swap


def meminfo():
	pagesize = inf(_get_data_sysctl('hw.pagesize'))
	
	v_free_count = inf(_get_data_sysctl('vm.stats.vm.v_free_count'))
	v_page_count = inf(_get_data_sysctl('vm.stats.vm.v_page_count'))

	mem_size = v_page_count*pagesize
	mem_free = v_free_count*pagesize
	mem_used = mem_size-mem_free

	return (physmem(), mem_size, mem_used, ) # Return total memory and used memory


def _get_data_sysctl(param):
	p = subprocess.Popen([SYSCTL, param], stdout=subprocess.PIPE)
	v = p.communicate()[0]
	v = v.split(": ")
	v = v[1].strip()
	return v