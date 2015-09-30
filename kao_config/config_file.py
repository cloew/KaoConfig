from kao_decorators import proxy_for
from contextlib import contextmanager
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
            
    @contextmanager
    def open(self, mode):
        """ Open the file in the given mode """
        with open(self.path, mode) as file:
            yield file
            
    def readlines(self):
        """ Return the lines from the file """
        lines = []
        with self.open('r') as file:
            lines = file.readlines()
        return lines
            
    def read(self):
        """ Return the data from the file """
        data = ''
        with self.open('r') as file:
            data = file.read()
        return data
            
    def write(self, text):
        """ Write the text to the file """
        with self.open('w') as file:
            file.write(text)