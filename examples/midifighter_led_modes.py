#!/usr/bin/env python
#
# Just a quick LED mode example.
# Works with Midi Figther 64
# 
#
# FMMT666(ASkr) 7/2013..8/2020
# www.askrprojects.net
#

import sys
import random
from pygame import time


try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading launchpad.py")


def main():

	mode = None

	if launchpad.MidiFighter64().Check( 0 ):
		lp = launchpad.MidiFighter64()
		if lp.Open( 0 ):
			print("Midi Fighter 64")
			mode = "F64"

	if mode is None:
		print("Did not find any devices, meh...")
		return


	# all red but off
	for x in range(8):
		for y in range(8):

			# Additionally there are these vars which can be used to change the animation:
			#   MODE_SQUARE
			#   MODE_CIRCLE
			#   MODE_STAR
			#   MODE_TRIANGLE

			# using if/elifs for better visibility:

			# --- BRIGHTNESS 0..15
			if   y == 0:
				color = 5
				mode = lp.MODE_BRIGHT[1]
			elif y == 1:
				mode = lp.MODE_BRIGHT[5]
			elif y == 2:
				mode = lp.MODE_BRIGHT[10]
			elif y == 3:
				mode = lp.MODE_BRIGHT[15]
			# --- TOGGLING 0..7
			elif y == 4:
				color = 25
				mode = lp.MODE_TOGGLE[4]
			elif y == 5:
				mode = lp.MODE_TOGGLE[x]
			# --- PULSING 0..7
			elif y == 6:
				color = 78
				mode = lp.MODE_PULSE[5]
			elif y == 7:
				mode = lp.MODE_PULSE[x]

			lp.LedCtrlXY( x, y, color, mode )


	print("bye ...")

	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

