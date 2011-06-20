import psutil

def physmem():
	return psutil.TOTAL_PHYMEM

def swapinfo():
	return (psutil.total_virtmem(),psutil.used_virtmem(),) # Return total and used swap

def meminfo():
	return (physmem(), psutil.avail_phymem(), psutil.used_phymem())