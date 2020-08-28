#!/usr/bin/python
#
# Stupid flashing/pulsing demo.
# Works with Mk2, Mini Mk3, Pro, X
# 
#
# FMMT666(ASkr) 10/2018..8/2020
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

import random
from pygame import time


def main():

	mode = None

	# create an instance
	lp = launchpad.Launchpad()

	# check what we have here and override lp if necessary
	if lp.Check( 0, "pad pro" ):
		lp = launchpad.LaunchpadPro()
		if lp.Open(0,"pad pro"):
			print("Launchpad Pro")
			mode = "Pro"

	elif lp.Check( 0, "promk3" ):
		lp = launchpad.LaunchpadProMk3()
		if lp.Open( 0 ):
			print("Launchpad Pro Mk3")
			mode = "ProMk3"
			

	elif lp.Check( 1, "minimk3" ):
		lp = launchpad.LaunchpadMiniMk3()
		if lp.Open( 1, "minimk3" ):
			print("Launchpad Mk3")
			mode = "Mk3"

	elif lp.Check( 1, "launchpad x" ) or lp.Check( 1, "lpx" ):
		lp = launchpad.LaunchpadLPX()
		if lp.Open( 1 ):
			print("Launchpad X")
			mode = "LPX"

	if mode is None:
		print("Did not find any compatible Launchpads, meh...")
		return

	# set flashing/pulsing frequency to 240bpm
	lp.LedCtrlBpm(240)

	# stupid lightshow from here on...
	for y in range(8):
		for x in range(8):
			lp.LedCtrlXYByCode( 7-x, 8-y, 5 if y < 4 else 13)
			lp.LedCtrlXYByCode( x, y+1, 21 if y < 4 else 13)
			time.wait(50)

	time.wait(1000)

	for y in range(8):
		for x in range(8):
			lp.LedCtrlFlashXYByCode( x, y+1, 0 )

	time.wait(3000)

	for y in range(8):
		for x in range(8):
			lp.LedCtrlPulseXYByCode( x, y+1, 53 )

	time.wait(3000)

	for x in range(4):
		for y in range(8):
			lp.LedCtrlXYByCode( 7-x, 8-y, random.randint(0, 127) )
			lp.LedCtrlFlashXYByCode( 7-x, 8-y, random.randint(0, 127) )
			lp.LedCtrlXYByCode( x, y+1, random.randint(0, 127) )
			lp.LedCtrlFlashXYByCode( x, y+1, random.randint(0, 127) )
			time.wait(250)

	time.wait(3000)


	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

