
class GlobalFinder:
    """ Represents a method of fidning a requested Global File """
    
    def __init__(self, filename):
        """ Initialize with the filename to load """
        self.filename = os.path.join(GetUserHomeFolder(), filename)