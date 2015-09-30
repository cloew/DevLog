from .commands import commands
from kao_command import Driver

def DevLog(scriptName):
    return Driver(scriptName, commands)