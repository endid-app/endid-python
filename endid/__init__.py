from .endid import call, cli

__all__ = ['call', 'cli']

# We want a lot of entry points for this module:
# endid (command line installed via setup.py)
# from endid import call (within user python code)
# python -m endid.cmd (invoke from command line as module)
# We also want the endid.py file to work entirely standalone in python2 and 3

