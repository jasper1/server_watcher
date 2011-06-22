'''
Created on Jun 22, 2011

@author: konstantin
'''
import subprocess

def data_from_pipe(command, *args):
    exec_command = []
    exec_command.append(command)
    exec_command += args
    p = subprocess.Popen(exec_command, stdout=subprocess.PIPE)
    v = p.communicate()[0]
    v = v.split('\n')
    return v


def l_split(a, k):
    ret = []
    for i in xrange(0,len(a),k):
        ret.append(a[i:i+k])
    return ret
