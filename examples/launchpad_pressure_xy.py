#!/usr/bin/env python
#
# Quick demo of the new, optional "pressure events" for supported Launchpads.
# Works with: Pro, Pro Mk3, X
# 
#
# FMMT666(ASkr) 7/2013..9/2020
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

	if launchpad.LaunchpadProMk3().Check( 0 ):
		lp = launchpad.LaunchpadProMk3()
		if lp.Open( 0 ):
			mode = "promk3"
	elif launchpad.LaunchpadPro().Check( 0 ):
		lp = launchpad.LaunchpadPro()
		if lp.Open( 0 ):
			mode = "pro"
	elif launchpad.LaunchpadLPX().Check ( 1 ):
		lp = launchpad.LaunchpadLPX()
		if lp.Open( 1 ):
			mode = "lpx"

	if mode is None:
		print("no compatible Launchpad found ...")	
		return

	while(True):
		# enable the "pressure" feature by calling ButtonStateXY with
		# "returnPressure" set to True
		events = lp.ButtonStateXY( returnPressure = True )
		if events != []:
			# x and y button codes of >=255 indicate that this is a pressure value
			if events[0] >= 255 and events[1] >= 255:
				# The pressure events are different for the Pro and X:
				# PRO:
				#   The pressure value is not related to a specific button. It always returns
				#   a fake coordinate of "255", so that the pressure events can be distinguished
				#   from the standard button-press events.
				#   If two or more buttons are hold at the same time, the biggest value will be returned.
				#   Because this is the XY methods, X and Y contain 255.
				# LPX:
				#   Returns a per-button pressure event.
				#   To distinguish pressure events from button events, "255" is added to the X/Y coordinates.
				if mode == "pro" or mode == "promk3":
					print(" PRESSURE: " + str(events[2]) )
				else:
					print(" PRESSURE: " + str(events[0]-255) + " " + str(events[1]-255) + " " + str(events[2]) )

			else:
				# the standard button events
				if events[2] > 0:
					print(" PRESSED:  ", end='')
				else:
					print(" RELEASED: ", end='')
				# TODO
				print( str(events[0]) + " " + str(events[1]) + " " + str(events[2]) )

	
if __name__ == '__main__':
	main()
