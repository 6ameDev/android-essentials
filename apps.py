import app
import asset_reader

def read_apps(filename):
	read_apps = []
	lines = asset_reader.read_file(filename)
	for line in lines.splitlines():
		split_line = [i.strip() for i in line.split("-")]
		if len(split_line) < 2:
			split_line.extend(split_line)
		read_apps.append(app.App(split_line[0], split_line[1]))
	return read_apps

def all():
	# return asset_reader.read_apps('app_list.txt')
	return read_apps('test_app_list.txt')