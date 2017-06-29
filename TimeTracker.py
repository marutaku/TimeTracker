import sys
from command import CommandController

args = sys.argv
command_array = [args[1], args[2]]
command = CommandController(command_array)
