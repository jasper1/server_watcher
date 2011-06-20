'''
Created on Jun 18, 2011

@author: konstantin
'''
import sys, os
import cherrypy

from collector import Collector

def _main_(argv):
    
    # Check configure file in ARGV dict
    conf_file = "server.conf"
        
    conf = os.path.join(os.path.dirname("."), conf_file)
    
    # Run CherryPy server
    print ("Clent-Server running...")
    
    try:
        cherrypy.quickstart(Collector(), config=conf)
        
    except:
        # Ooops! We have error...
        print (sys.exc_info())
        sys.exit()

if __name__ == '__main__':
    _main_(sys.argv)