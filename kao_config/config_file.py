from kao_decorators import proxy_for
import os

def CreateFileIfItDoesNotExist(filename):
    """ Creates the given file if it does not exist """
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass
            
@proxy_for('finder', ['path'])
class ConfigFile:
    """ Represents a configuration file """
    
    def __init__(self, finder, create=False):
        """ Initialize with the finder """
        self.finder = finder
        if create:
            CreateFileIfItDoesNotExist(self.path)