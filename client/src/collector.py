import json
import cherrypy
import simplejson, urllib

class Collector(object):
    # Main page
    
    def get_json(self, **kwargs):
        cherrypy.response.headers['Content-Type'] = ' application/json'
        servers = ["127.0.0.1:8282",]
        
        server_log = {}
        
        for i,server in enumerate(servers):
            result = simplejson.load(urllib.urlopen("http://%s/" % server))
            server_log[i]={'memory_total':result['total_phymem'],
                           'memory_used' :result['used_phymem'],
                           "network"     : 23,
                           "disk"        : 34,
                           'cpu'         :result['cpu_percent'],
                           'cpu_count'   :result['cpu_count'],
                           'load_avg'    :result['load_average'],
                           }

        
        return json.dumps(server_log)
      
    get_json.exposed = True