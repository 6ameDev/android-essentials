from uiautomator import device as d
import androidSystem
import time

INSTALL_RES_ID = "com.android.vending:id/buy_button"
ACCEPT_RES_ID = "com.android.vending:id/continue_button"
UPDATE_RES_ID = "com.android.vending:id/update_button"
UNINSTALL_RES_ID = "com.android.vending:id/uninstall_button"
CANCEL_DOWNLOAD_RES_ID = "com.android.vending:id/cancel_download"
OPEN_RES_ID = "com.android.vending:id/launch_button"
TITLE_BG_RES_ID = "com.android.vending:id/title_background"

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
 

for count in range(RETRY_COUNT):
	package_name = "market://details?id=com.facebook.lite"
	androidSystem.openApp(package_name)

	log_duration(wait_for_resource, TITLE_BG_RES_ID, 5000)

	if not d.exists(resourceId=OPEN_RES_ID):
	 	if d.exists(resourceId=INSTALL_RES_ID):
			install()
			accept()
			if d.exists(resourceId=CANCEL_DOWNLOAD_RES_ID):
				log_duration(wait_for_resource, UNINSTALL_RES_ID, 60000)
				break

		elif d.exists(resourceId=UPDATE_RES_ID):
			update()
	else:
		break
 
	d.press.back()
	print "---------------------"
	print 'Retry count for {}: {}'.format(package_name, count)
	print "---------------------"
