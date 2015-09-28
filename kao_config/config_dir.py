from kao_decorators import proxy_for
import os

@proxy_for('finder', ['path'])
class ConfigDir:
    """ Represents a Config Directory """
    
    def __init__(self, finder, create=False):
        """ Initialize with the finder to use """
        self.finder = finder
        if create:
            CreateDirectoryIfItDoesNotExist(self.path)
        
    def getFilename(self, filename, create=False):
        """ Return the path to the requested filename """
        filename = os.path.join(self.path, filename)
        if create:
            CreateFileIfItDoesNotExist(filename)
        return filename