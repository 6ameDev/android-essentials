import pkg_resources

def read_file(filename):
	resource_package = __name__
	resource_path = '/'.join(('asset', filename))
	return pkg_resources.resource_string(resource_package, resource_path)