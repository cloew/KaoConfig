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

def LocalConfigDir(directory, create=False):
    """ Represents a local config directory """
    return ConfigDir(LocalFinder(directory), create=create)

def LocalConfigFile(filename, create=False):
    """ Represents a local config file """
    return ConfigFile(LocalFinder(filename), create=create)