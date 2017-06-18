import subprocess

def openApp(package_name):
	subprocess.check_output(['adb', 'shell', 'am', 'start', '-a', 'android.intent.action.VIEW', '-d', package_name])