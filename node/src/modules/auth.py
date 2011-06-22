'''
Created on Jun 18, 2011

@author: konstantin
'''
from modules.i_controller import Controller


class Auth(Controller):
    '''
    Auth responser
    '''
    
    good_ips = []
    bad_ips  = []
    
    def __init__(self,params):
        super(Auth, self).__init__(params)
        
        # Get configs from preloaded storage
        self.good_ips = self.configs_cache['auth.conf']._sections['IP']['good'].split(",")
        self.bad_ips  = self.configs_cache['auth.conf']._sections['IP']['bad'].split(",")
        
        print self.good_ips, self.bad_ips