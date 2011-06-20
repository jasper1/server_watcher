'''
Created on Jun 18, 2011

@author: konstantin
'''

from configs_loader import ConfigLoader

class Controller(object):
    '''
    Controller prototype class
    '''
    errors = []
    ret_data = []
    configs_cache = None
    
    def __init__(self, params):
#        c = ConfigLoader()
#        self.configs_cache = c.cache 
        self.params = params
        self.errors = []
    
        # Debug
        self.ret_data = params

    def set_error(self, error):
        self.errors.append(error) 

    def done(self):
        if self.errors:
            return self.errors
        else:
            return self.ret_data
        