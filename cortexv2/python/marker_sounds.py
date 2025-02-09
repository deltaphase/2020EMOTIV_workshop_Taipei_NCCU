from cortex import Cortex
import time
import psychtoolbox as ptb
from psychopy import sound, core

class Marker():
	def __init__(self):
		self.c = Cortex(user, debug_mode=True)
		self.c.do_prepare_steps()

	def add_markers(self, marker_numbers):
		now = ptb.GetSecs()

		for m in range(marker_numbers):
			mySound = sound.Sound('1000')
			marker_time = time.time()*1000
			print('add marker at : ', marker_time)
			
			marker = {
				"label":str(m),
				"value":"sound-erp",
				"port":"python-app",
				"time":marker_time
			}
			mySound.play(when=now+0.5)  # play in EXACTLY 0.5s
			self.c.inject_marker_request(marker)

			# add marker each seconds
			time.sleep(1.5)


	def demo_add_marker(self, record_export_folder, marker_numbers):
		# create record
		record_name = 'demo marker'
		record_description = 'demo marker'
		self.c.create_record(record_name, record_description)

		self.add_markers(marker_numbers)

		self.c.stop_record()

		self.c.disconnect_headset()

		# export record
		record_export_data_types = ['EEG', 'MOTION', 'PM', 'BP']
		record_export_format = 'CSV'
		record_export_version = 'V2'
		self.c.export_record(record_export_folder,
							record_export_data_types,
							record_export_format,
							record_export_version,
							[self.c.record_id])

# -----------------------------------------------------------
# 
# SETTING
# 	- replace your license, client_id, client_secret to user dic
# 	- specify infor for record and export
# 	- connect your headset with dongle or bluetooth, you should saw headset on EmotivApp
#
# RESULT
# 	- this demo add marker each 3 seconds
# 	- export data file should contain marker added
#
# -----------------------------------------------------------
user = {
	"license" : "84c9139c-1c31-482c-adbe-4af2bd7c6e07",
	"client_id" : "FBu7yCnXYQYWZSQQXtom8VuQtsWySSUGDZpGoUyV",
	"client_secret" : "ad25CI1QDqiMAuSfpsZxeGgiPDCadhvgnKoFj6ByTjijRo34SodS7oMumcYF3Uza1ewPJfBPuv6Y2Y4MCoipzn9aINM0v44pxwQTQXSjCoU9b5dceKIcmZx0wBuSvRWr",
	"debit" : 100
}

m = Marker()


# start record --> add marker --> stop record --> disconnect headset --> export record
record_export_folder = '/Users/kevinhsu/cortexv2/'
marker_numbers = 200
m.demo_add_marker(record_export_folder, marker_numbers)
# ----------------------------------------------