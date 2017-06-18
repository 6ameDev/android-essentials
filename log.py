from colorama import init
from termcolor import colored
import os

def error(message):
	print(colored(message, 'red'))

def warn(message):
	print(colored(message, 'yellow'))

def info(message):
	print(colored(message, 'green'))

def debug(message):
	try:
    		if os.environ['DEBUG'] is not None:
    			print(colored(message))
	except Exception as e:
			return True
	