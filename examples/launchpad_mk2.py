#!/usr/bin/env python
#
# Launchpad Mk2 tests
# 
#
# FMMT666(ASkr) 7/2013..2/2018
# www.askrprojects.net
#

import sys

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("ERROR: loading launchpad.py failed")

import random
import pygame
from pygame import time


def CountdownPrint( n ):
	for i in range(n,0,-1):
		sys.stdout.write( str(i) + " ")
		sys.stdout.flush()
		time.wait(500)


def main():

	# some basic info
	print( "\nRunning..." )
	print( " - Python " + str( sys.version.split()[0] ) )
	print( " - PyGame " + str( pygame.ver ) )

	# create an instance
	lp = launchpad.LaunchpadMk2();

	# open the first Launchpad Mk2
	if lp.Open( 0, "mk2" ):
		print( " - Launchpad Mk2: OK" )
	else:
		print( " - Launchpad Mk2: ERROR" )
		return

	# Clear the buffer because the Launchpad remembers everything
	lp.ButtonFlush()

	# List the class's methods
	print( " - Available methods:" )
	for mName in sorted( dir( lp ) ):
		if mName.find( "__") >= 0:
			continue
		if callable( getattr( lp, mName ) ):
			print( "     " + str( mName ) + "()" )

	# LedAllOn() test
	print( " - Testing LedAllOn()" )
	for i in [ 5, 21, 79, 3]:
		lp.LedAllOn( i )
		time.wait(500)
	lp.LedAllOn( 0 )

	# LedCtrlXY() test
	# -> LedCtrlRaw()
	#    -> midi.RawWriteSysEx()
	#       -> devOut.write_sys_ex()
	print( " - Testing LedCtrlXY()" )
	colors = [ [63,0,0],[0,63,0],[0,0,63],[63,63,0],[63,0,63],[0,63,63],[63,63,63] ]
	for i in range(4):
		for y in range( i + 1, 8 - i + 1 ):
			for x in range( i, 8 - i ):
				lp.LedCtrlXY( x, y, colors[i][0], colors[i][1], colors[i][2])
		time.wait(500)

	# turn all LEDs off
	print( " - Testing Reset()" )
	lp.Reset()

	# close this instance
	print( " - More to come, goodbye...\n" )
	lp.Close()

	
if __name__ == '__main__':
	main()

