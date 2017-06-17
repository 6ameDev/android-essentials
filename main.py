from uiautomator import device as d
import apps
import androidSystem
import time

INSTALL_RES_ID = "com.android.vending:id/buy_button"
ACCEPT_RES_ID = "com.android.vending:id/continue_button"
UPDATE_RES_ID = "com.android.vending:id/update_button"
UNINSTALL_RES_ID = "com.android.vending:id/uninstall_button"
CANCEL_DOWNLOAD_RES_ID = "com.android.vending:id/cancel_download"
OPEN_RES_ID = "com.android.vending:id/launch_button"
TITLE_BG_RES_ID = "com.android.vending:id/title_background"

INCOMPATIBLE_DEVICE_ERROR = "Your device isn't compatible with this version."
APP_NOT_FOUND_ERROR = "Item not found."

RETRY_COUNT = 5

def log_duration(block, *args):
	start_time = time.time()
	block(*args)
	current_time = time.time()
	print 'Time taken (s) : {:.3f}'.format(current_time - start_time)
 
def install():
	d.watcher("INSTALL").when(resourceId=INSTALL_RES_ID).click(resourceId=INSTALL_RES_ID)
	d.watchers.run()
	d.watchers.remove()

def update():
	d.watcher("UPDATE").when(resourceId=UPDATE_RES_ID).click(resourceId=UPDATE_RES_ID)
	d.watchers.run()
	d.watchers.remove()

def wait_for_resource(resource_id, timeout):
	d(resourceId=resource_id).wait.exists(timeout=timeout)

def accept():
	d.watcher("ACCEPT").when(resourceId=ACCEPT_RES_ID).click(resourceId=ACCEPT_RES_ID)
	log_duration(wait_for_resource, ACCEPT_RES_ID, 2000)
	d.watchers.run()
	d.watchers.remove()	

def install_app_with_package_name(app):
	for count in range(RETRY_COUNT):
		androidSystem.openApp(app.package_name())

		log_duration(wait_for_resource, TITLE_BG_RES_ID, 5000)

		if d.exists(text=INCOMPATIBLE_DEVICE_ERROR):
			print INCOMPATIBLE_DEVICE_ERROR
			break

		if d.exists(text=APP_NOT_FOUND_ERROR):
			print APP_NOT_FOUND_ERROR
			break

		if not d.exists(resourceId=OPEN_RES_ID):
		 	if d.exists(resourceId=INSTALL_RES_ID):
				install()
				accept()
				if d.exists(resourceId=CANCEL_DOWNLOAD_RES_ID):
					log_duration(wait_for_resource, UNINSTALL_RES_ID, 60000)
					print '{} was installed successfully.'.format(app.name())
					break

			elif d.exists(resourceId=UPDATE_RES_ID):
				update()
		else:
			print '{} is already installed and updated.'.format(app.name())
			break
	 
		d.press.back()
		print 'Retry count for {}: {}'.format(app.name(), count)

for app in apps.all():
	print "---------------------"
	print 'Installing {}'.format(app.name())
	print "---------------------"
   	install_app_with_package_name(app)
