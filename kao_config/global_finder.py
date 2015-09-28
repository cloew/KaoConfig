
class GlobalFinder:
    """ Represents a method of fidning a requested Global File """
    
    def __init__(self, filename):
        """ Initialize with the filename to load """
        self.path = os.path.join(GetUserHomeFolder(), filename)