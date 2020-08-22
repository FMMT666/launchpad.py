#!/usr/bin/env python
#
# Quick demo of the new, optional "pressure events" for supported Launchpads.
# Works with: Pro
# 
#
# FMMT666(ASkr) 7/2013..8/2020
# www.askrprojects.net
#

import sys

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading launchpad.py")


def main():

	# only the original Pro for now
	lp = launchpad.LaunchpadPro()
	lp.Open( 0 )

	while(True):
		# enable the "pressure" feature by calling ButtonStateRaw with
		# "returnPressure" set to True
		events = lp.ButtonStateRaw( returnPressure = True )
		if events != []:
			# a dummy button code of 255 indicates that this is a pressure value
			if events[0] == 255:
				# Notice that the pressure value is not related to a specific button.
				# If you hold two buttons at the same time, the bigger value will be returned.
				print(" PRESSURE: " + str(events[1]) )
			else:
				# the standard button events
				if events[1] > 0:
					print(" PRESSED:  ", end='')
				else:
					print(" RELEASED: ", end='')
				print( str(events[0]) + " " + str(events[1]) )

	
if __name__ == '__main__':
	main()

