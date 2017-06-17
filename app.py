class App(object):

    def __init__(self, name, package_name):
        self._name = name
        self._package_name = package_name

    def name(self):
        return self._name

    def package_name(self):
        return self._package_name