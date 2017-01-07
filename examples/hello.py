#!/usr/bin/python
#
# Quick usage of "launchpad.py", LEDs and buttons.
# Works with all Launchpads: Mk1, Mk2, S/Mini and Pro.
# 
#
# ASkr 7/2013..1/2017
# www.askrprojects.net
#

import sys

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading lauchpad.py")

import random
from pygame import time


def main():

	mode = None

	# create an instance
	lp = launchpad.Launchpad();

	# check what we have here and override lp if necessary
	if lp.Check( 0, "pro" ):
		lp = launchpad.LaunchpadPro()
		if lp.Open(0,"pRo"):
			print("Launchpad Pro")
			mode = "Pro"
			
	elif lp.Check( 0, "mK2" ):
		lp = launchpad.LaunchpadMk2()
		if lp.Open( 0, "Mk2" ):
			print("Launchpad Mk2")
			mode = "Mk2"
			
	else:
		if lp.Open():
			print("Launchpad Mk1/S/Mini")
			mode = "Mk1"

	if mode is None:
		print("meh...")
		return


	# scroll "HELLO" from right to left
	if mode == "Mk1":
		lp.LedCtrlString( "HELLO ", 0, 3, -1 )
	else:
		lp.LedCtrlString( "HELLO ", 0, 63, 0, -1 )


	# random output until button "arm" (lower right) is pressed
	print("---\nRandom madness. Stop by creating 10 button events.")

	# Clear the buffer because the Launchpad remembers everything :-)
	while lp.ButtonStateRaw() != []:
		pass

	# Lightshow
	butHit = 0
	while 1:
		if mode == "Mk1":
			lp.LedCtrlRaw( random.randint(0,127), random.randint(0,3), random.randint(0,3) )
		else:
			lp.LedCtrlRaw( random.randint(0,127), random.randint(0,63), random.randint(0,63), random.randint(0,63) )
		
		time.wait( 5 )
		
		but = lp.ButtonStateRaw()
		if but != []:
			butHit += 1
			print( butHit, " button: ", but )
			if butHit > 10:
				break

	# now crash it :-)
	print("\nNow let's crash PyGame...")
	print("Don't worry, that's just a bug in PyGame's MIDI implementation.")

	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

