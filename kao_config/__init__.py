import os

def GetUserHomeFolder():
    """ Return the User's Home Directory """
    return os.path.expanduser("~")
    
def CreateDirectoryIfItDoesNotExist(directory):
    """ Creates the given directory if it does not exist """
    if not os.path.isdir(directory):
        os.mkdir(directory)
            
def CreateFileIfItDoesNotExist(filename):
    """ Creates the given file if it does not exist """
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass

class GlobalConfigDir:
    """ Represents a global config directory """
    
    def __init__(self, directory, create=False):
        """ Initialize with the directory to find """
        self.directory = os.path.join(GetUserHomeFolder(), directory)
        if create:
            CreateDirectoryIfItDoesNotExist(self.directory)
        
    def getFile(self, filename, create=False):
        """ Create the global directory if it does not exist """
        filename = os.path.join(self.directory, filename)
        if create:
            CreateFileIfItDoesNotExist(filename)
        return filename
    
class LocalConfigFinder:
    """ Class to help find a local config file """
    
    def __init__(self, filename):
        """ Initialize the local config finder with the file to search for """
        self.filename = filename
        self.fullPath = None
        
    def find(self, startFrom=None, reload=False):
        """ Return the path to the closest file by searching the startFrom 
            directory or the current directory up to the file root """
        if self.fullPath is not None and not reload:
            return self.fullPath
            
        if startFrom is None:
            currentDirectory = os.getcwd()
        else:
            currentDirectory = startFrom
    
        self.fullPath = self.search(currentDirectory)
        return self.fullPath
        
    def search(self, currentDirectory):
        """ Search for the file """
        while currentDirectory != '/':
            fullFilename = os.path.join(currentDirectory, self.filename)
            if os.path.exists(fullFilename):
                return fullFilename
            currentDirectory = os.path.dirname(currentDirectory)