"""illustrate generator"""


def accumulator():
	"""return the aggregate of numbers"""
	current_value = None
	total = 0
	while True:
		# would recieve the current total from the send argument
		current_value = yield total
		print('current_value', current_value)
		if current_value is None: break
		# add to current total
		total += current_value


acc = accumulator()

# we must send a None value first, either by next(test) which is equivalent to test.send(None)
next(acc) # or test.send(None) -> 0
acc.send(1) # -> current_value = 0, total = 0
acc.send(3) # -> current_value = 3, total = 4
acc.send(13) # -> current_value = 13, total = 17
next(acc, None) # the second param is the default value when the iteriable does not have a value
# next(acc) # or test.send(None)  would throw a stopIteration exception


# example: get all files in a diretory recursively

# import useful module
from os import listdir
from os.path import isfile, join, exists


def list_files_in_directory(path):
	"""list all the files in a directory and not subdirectory"""
	for file in listdir(path):
		file_path = join(path, file)
		if isfile(file_path):
			if exists(file_path):
				yield file

def list_directories_in_directory(path):
	"""list all the directories in a directory and not subdirectory"""
	for directory in listdir(path):
		file_path = join(path, directory)
		if not isfile(file_path):
			if exists(file_path):
				yield directory


def list_files_in_directory_recursive(path):
	"""list files in path and subdirectory only 1 step down"""

	# list files in root directory
	yield from list_files_in_directory(path)

	# list child directory and their files
	for directory in list_directories_in_directory(path):
		file_path = join(path, directory)
		yield from list_files_in_directory(file_path)



