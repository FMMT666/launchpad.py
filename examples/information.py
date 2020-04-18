#!/usr/bin/env python
#
# Just shows some infos about the system and attached devices.
# 
#
# FMMT666(ASkr) 7/2013..4/2020
# www.askrprojects.net
#

import sys
import os
import platform

try:
	import pygame
except ImportError:
	sys.exit("error loading PyGame")


try:
	import launchpad_py as launchpad
except ImportError:
	print("no system-wide installation of Launchpad.py found")
	try:
		import launchpad
	except ImportError:
		print("no system-wide installation of Launchpad.py found")
		sys.exit("error loading launchpad.py")



def main():

	# create an instance
	lp = launchpad.Launchpad()

	# some basic info
	print( "\nRunning..." )
	print( " - OS      : " + str( os.name ) )
	print( " - Platform: " + str( platform.system() ) )
	print( " - Release : " + str( platform.release() ) )
	print( " - Python  : " + str( sys.version.split()[0] ) )
	print( " - PyGame  : " + str( pygame.ver ) )

	# print list of attached MIDI devices
	print( "\nAvailable MIDI devices:" )
	lp.ListAll()

	# print list of attached MIDI devices
	print( "\n\ngoodbye ..." )



if __name__ == '__main__':
	main()

