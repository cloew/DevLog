import os

def contents(fn):
    """ Wrap the given function to return the contents of the returned directory """
    def getContents(*args, **kwargs):
        return GetDirContents(fn(*args, **kwargs))
    return wrapContents

def GetDirContents(directory):
    """ Return the contents of the given directory """
    return sorted([int(file) for file in os.listdir(directory)])