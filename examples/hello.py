#!/usr/bin/env python
#
# Quick usage of "launchpad.py", LEDs and buttons.
# Works with all Launchpads: Mk1, Mk2, S/Mini, Pro, XL and LaunchKey
# 
#
# FMMT666(ASkr) 7/2013..2/2020
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
	if lp.Check( 0, "pro" ):
		lp = launchpad.LaunchpadPro()
		if lp.Open(0,"pro"):
			print("Launchpad Pro")
			mode = "Pro"

	# experimental MK3 implementation
	# The MK3 has two MIDI instances per device; we need the 2nd one.
	# If you have two MK3s attached, its "1" for the first and "3" for the 2nd device
	elif lp.Check( 1, "mk3" ):
		lp = launchpad.LaunchpadMk3()
		if lp.Open( 1, "mk3" ):
			print("Launchpad Mk3")
			mode = "Pro"

	# experimental LPX implementation
	# Like the Mk3, the LPX also has two MIDI instances per device; we need the 2nd one.
	# If you have two LPXs attached, its "1" for the first and "3" for the 2nd device
	elif lp.Check( 1, "lpx" ):
		lp = launchpad.LaunchpadLPX()
		if lp.Open( 1, "lpx" ):
			print("Launchpad X")
			mode = "Pro"
	
	# experimental ProMk3 implementation
	# ProMk3 has three MIDI instances per device; we need the 1st one.
	# If you have two ProMk3s attached, its "0" for the first and "3" for the 2nd device
	elif lp.Check( 0, "promk3" ):
		lp = launchpad.LaunchpadProMk3()
		if lp.Open( 0, "promk3" ):
			print("Launchpad ProMk3")
			mode = "Pro"
			
	elif lp.Check( 0, "mk2" ):
		lp = launchpad.LaunchpadMk2()
		if lp.Open( 0, "mk2" ):
			print("Launchpad Mk2")
			mode = "Mk2"

	elif lp.Check( 0, "control xl" ):
		lp = launchpad.LaunchControlXL()
		if lp.Open( 0, "control xl" ):
			print("Launch Control XL")
			mode = "XL"
			
	elif lp.Check( 0, "launchkey" ):
		lp = launchpad.LaunchKeyMini()
		if lp.Open( 0, "launchkey" ):
			print("LaunchKey (Mini)")
			mode = "LKM"

	elif lp.Check( 0, "dicer" ):
		lp = launchpad.Dicer()
		if lp.Open( 0, "dicer" ):
			print("Dicer")
			mode = "Dcr"
			
	else:
		if lp.Open():
			print("Launchpad Mk1/S/Mini")
			mode = "Mk1"

	if mode is None:
		print("Did not find any Launchpads, meh...")
		return


	# scroll "HELLO" from right to left
	if mode == "Mk1":
		lp.LedCtrlString( "HELLO ", 0, 3, -1 )
	# for all others except the XL and the LaunchKey
	elif mode != "XL" and mode != "LKM" and mode != "Dcr":
		lp.LedCtrlString( "HELLO ", 0, 63, 0, -1 )


	# random output
	if mode == "LKM":
		print("The LaunchKey(Mini) does not (yet) support LED activation, but you")
		print("can push some buttons or rotate some knobes now...")
		print("Auto exit if first number reaches 0")
	else:
		print("---\nRandom madness. Create some events. Stops after reaching 0 (first number)")
		print("Notice that sometimes, old Mk1 units don't recognize any button")
		print("events before you press one of the (top) automap buttons")
		print("(or power-cycle the unit...).")

	# Clear the buffer because the Launchpad remembers everything :-)
	lp.ButtonFlush()

	# Lightshow
	if mode == "XL" or mode == "LKM":
		butHit = 100
	elif mode == "Dcr":
		butHit = 30
	else:
		butHit = 10
		
	while 1:
		if mode == "Mk1" or mode == "XL":
			lp.LedCtrlRaw( random.randint(0,127), random.randint(0,3), random.randint(0,3) )
		elif mode == "Dcr":
			lp.LedCtrlRaw( random.randint(0,130), random.randint(0,7), random.randint(0,15) )
		elif mode != "LKM":
			lp.LedCtrlRaw( random.randint(0,127), random.randint(0,63), random.randint(0,63), random.randint(0,63) )
		
		time.wait( 5 )
		
		if mode == "XL" or mode == "LKM":
			but = lp.InputStateRaw()
		else:
			but = lp.ButtonStateRaw()

		if but != []:
			butHit -= 1
			if butHit < 1:
				break
			print( butHit, " event: ", but )

	# now quit...
	print("Quitting might raise a 'Bad Pointer' error (~almost~ nothing to worry about...:).\n\n")

	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

