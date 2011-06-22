#coding=utf-8
import psutil

from util import data_from_pipe, l_split
# Implementations for Mac OS X system

def physmem():
	return psutil.TOTAL_PHYMEM

def swapinfo():
	return (psutil.total_virtmem(),psutil.used_virtmem(),) # Return total and used swap

def meminfo():
	return (physmem(), psutil.avail_phymem(), psutil.used_phymem())

def cpuinfo():
	return (psutil.NUM_CPUS, psutil.cpu_percent())

def iostat():
	out = data_from_pipe('/usr/sbin/iostat','-d')
	disks = out[0].split()
	data = {}
	
	values = out[2].split()
	for i,a in enumerate(l_split(values, 3)):
		data[disks[i]]={'kbs':a[0],'tps':a[1],'mbs':a[2]}
	
	# Зачем это нужно?
	# Флаг 'style' может принимать значение MacOS, Linux, FreeBSD 
	# Это свзяно с тем, что команда iostat выдает разную информация в разных ОС
	# И чтобы аггрегатор знал с чем работает добавлен этот флаг
	data['style'] = 'MacOS'
	
	
	return (data)

def diskinfo(raw=False):
	out = data_from_pipe('/bin/df','-a')[1:]
	data = {}
	if raw:
		data['raw'] = out
		
	for line in out:
		line = line.split()
		if line:		
			data[line[5]] = [line[1],line[2],line[3]]
	print data
	return (data)