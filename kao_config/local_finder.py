import os

class LocalFinder:
    """ Represents a method of finding a file in the nearest parent directory """
    
    def __init__(self, filename, startFrom=None):
        """ Initialize the local config finder with the file to search for """
        self.filename = filename
        self.startFrom = startFrom
        self.fullPath = None
        
    @property
    def path(self):
        """ Return the path to the requested file """
        path = self.find()
        return path if path is not None else os.path.join(self.startDirectory, self.filename)
        
    def find(self):
        """ Return the path to the closest file by searching the startFrom 
            directory or the current directory up to the file root """
        if self.fullPath is not None:
            return self.fullPath
            
        self.fullPath = self.search(self.startDirectory)
        return self.fullPath
        
    def search(self, currentDirectory):
        """ Search for the file """
        while currentDirectory != '/':
            fullFilename = os.path.join(currentDirectory, self.filename)
            if os.path.exists(fullFilename):
                return fullFilename
            currentDirectory = os.path.dirname(currentDirectory)
            
    @property
    def startDirectory(self):
        """ Return the Start Directory """
        return os.getcwd() if self.startFrom is None else self.startFrom