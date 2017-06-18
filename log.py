from colorama import init
from termcolor import colored

def error(message):
	print(colored(message, 'red'))

def warn(message):
	print(colored(message, 'yellow'))

def info(message):
	print(colored(message, 'green'))

def debug(message):
	return True
	# print(colored(message))