from .config_file import ConfigFile
from .specified_path_finder import SpecifiedPathFinder

from kao_decorators import proxy_for
import os
    
def CreateDirectoryIfItDoesNotExist(directory):
    """ Creates the given directory if it does not exist """
    if not os.path.isdir(directory):
        os.mkdir(directory)

@proxy_for('finder', ['path'])
class ConfigDir:
    """ Represents a Config Directory """
    
    def __init__(self, finder, create=False):
        """ Initialize with the finder to use """
        self.finder = finder
        if create:
            CreateDirectoryIfItDoesNotExist(self.path)
        
    def getFilename(self, filename):
        """ Return the path to the requested filename """
        return os.path.join(self.path, filename)
    
    def getFile(self, filename, create=False):
        """ Return the Config File Wrapper for the file specified """
        return ConfigFile(SpecifiedPathFinder(self.getFilename(filename)), create=create)