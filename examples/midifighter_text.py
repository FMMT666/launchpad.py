#!/usr/bin/env python
#
# Quick and dirty text test.
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


	lp.LedAllOn( 103 )
	time.wait(500)

	lp.LedCtrlString( '500BUCKS', 21, coloroff=103, direction=-1, waitms=10 )
	for i in range(10):
		lp.LedAllOn( random.randint(0,127) )
		time.wait(50)
	lp.LedCtrlString( 'LOL', 5, coloroff=21, direction=-0, waitms=50 )

	time.wait(50)
	lp.LedAllOn( 103 )

	print("bye ...")

	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

