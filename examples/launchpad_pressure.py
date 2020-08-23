#!/usr/bin/env python
#
# Quick demo of the new, optional "pressure events" for supported Launchpads.
# Works with: Pro, X
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

	mode = None

	lp = launchpad.LaunchpadPro()
	if lp.Check( 0 ):
		if lp.Open( 0 ):
			mode = "pro"
	else:
		lp = launchpad.LaunchpadLPX()
		if lp.Check( 1 ):
			if lp.Open( 1 ):
				mode = "lpx"

	if mode is None:
		print("no compatible Launchpad found ...")	
		return

	while(True):
		# enable the "pressure" feature by calling ButtonStateRaw with
		# "returnPressure" set to True
		events = lp.ButtonStateRaw( returnPressure = True )
		if events != []:
			# a dummy button code of 255 indicates that this is a pressure value
			if events[0] >= 255:
				# The pressure events are different for the Pro and X:
				# PRO:
				#   The pressure value is not related to a specific button. It always returns
				#   a fake button number of "255", so that the pressure events can be distinguished
				#   from the standard button-press events.
				#   If two or more buttons are hold at the same time, the biggest value will be returned.
				# LPX:
				#   Returns a per-button pressure event.
				#   To distinguish pressure events from button events, "255" is added to the button number.
				if mode == "pro":
					print(" PRESSURE: " + str(events[1]) )
				else:
					print(" PRESSURE: " + str(events[0]-255) + " " + str(events[1]) )

			else:
				# the standard button events
				if events[1] > 0:
					print(" PRESSED:  ", end='')
				else:
					print(" RELEASED: ", end='')
				print( str(events[0]) + " " + str(events[1]) )

	
if __name__ == '__main__':
	main()

