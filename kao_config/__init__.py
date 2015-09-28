from .config_dir import ConfigDir
from .config_file import ConfigFile
from .global_finder import GlobalFinder
from .local_finder import LocalFinder

def GlobalConfigDir(directory, create=False):
    """ Represents a global config directory """
    return ConfigDir(GlobalFinder(directory), create=create)

def GlobalConfigFile(filename, create=False):
    """ Represents a global config file """
    return ConfigFile(GlobalFinder(filename), create=create)

def LocalConfigDir(directory, create=False, startFrom=None):
    """ Represents a local config directory """
    return ConfigDir(LocalFinder(directory, startFrom=None), create=create)

def LocalConfigFile(filename, create=False, startFrom=None):
    """ Represents a local config file """
    return ConfigFile(LocalFinder(filename, startFrom=None), create=create)