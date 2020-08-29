#!/usr/bin/env python
#
# Quick button test.
# Works with these Launchpads: Mk1, Mk2, Mini Mk3, S/Mini, Pro, Pro Mk3
# And these:                   Midi Figther 64
# 
#
# FMMT666(ASkr) 7/2013..8/2020
# www.askrprojects.net
#

import sys
import time


try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading launchpad.py")


def main():

	mode = None

	if launchpad.LaunchpadPro().Check( 0 ):
		lp = launchpad.LaunchpadPro()
		if lp.Open( 0 ):
			print("Launchpad Pro")
			mode = "Pro"

	elif launchpad.LaunchpadProMk3().Check( 0 ):
		lp = launchpad.LaunchpadProMk3()
		if lp.Open( 0 ):
			print("Launchpad Pro Mk3")
			mode = "ProMk3"

	elif launchpad.LaunchpadMiniMk3().Check( 1 ):
		lp = launchpad.LaunchpadMiniMk3()
		if lp.Open( 1 ):
			print("Launchpad Mini Mk3")
			mode = "MiniMk3"

	elif launchpad.LaunchpadLPX().Check( 1 ):
		lp = launchpad.LaunchpadLPX()
		if lp.Open( 1 ):
			print("Launchpad X")
			mode = "LPX"
			
	elif launchpad.LaunchpadMk2().Check( 0 ):
		lp = launchpad.LaunchpadMk2()
		if lp.Open( 0 ):
			print("Launchpad Mk2")
			mode = "Mk2"

	# elif launchpad.LaunchControlXL().Check( 0 ):
	# 	lp = launchpad.LaunchControlXL()
	# 	if lp.Open( 0 ):
	# 		print("Launch Control XL")
	# 		mode = "XL"
			
	# elif launchpad.LaunchKeyMini().Check( 0 ):
	# 	lp = launchpad.LaunchKeyMini()
	# 	if lp.Open( 0 ):
	# 		print("LaunchKey (Mini)")
	# 		mode = "LKM"

	elif launchpad.Dicer().Check( 0 ):
		lp = launchpad.Dicer()
		if lp.Open( 0 ):
			print("Dicer")
			mode = "Dcr"

	elif launchpad.MidiFighter64().Check( 0 ):
		lp = launchpad.MidiFighter64()
		if lp.Open( 0 ):
			print("Midi Fighter 64")
			mode = "F64"

	elif launchpad.Launchpad().Check( 0 ):
		lp = launchpad.Launchpad()
		if lp.Open( 0 ):
			print("Launchpad Mk1/S/Mini")
			mode = "Mk1"

	if mode is None:
		print("Did not find any Launchpads, meh...")
		return

	print("QUIT: Push a single button for longer than 3s and release it.")

	lastBut = (-99,-99)
	tStart = time.time()
	while True:
		if mode == 'Pro' or mode == 'ProMk3':
			buts = lp.ButtonStateXY( mode = 'pro')
		else:
			buts = lp.ButtonStateXY()

		if buts != []:
			print( buts[0], buts[1], buts[2] )

			# quit?
			if buts[2] > 0:
				lastBut = ( buts[0], buts[1] )
				tStart = time.time()
			else:
				if lastBut == ( buts[0], buts[1] ) and (time.time() - tStart) > 2:
					break


	print("bye ...")

	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

