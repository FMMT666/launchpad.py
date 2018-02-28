#!/usr/bin/env python
#
# Launchpad Pro tests
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
	lp = launchpad.LaunchpadPro();

	# open the first Launchpad Pro
	if lp.Open( 0, "pro" ):
		print( " - Launchpad Pro: OK" )
	else:
		print( " - Launchpad Pro: ERROR" )
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

	# LedCtrlXY() test
	# -> LedCtrlRaw()
	#    -> midi.RawWriteSysEx()
	#       -> devOut.write_sys_ex()
	print( " - Testing LedCtrlXY(), Pro Mode" )
	colors = [ [63,0,0],[0,63,0],[0,0,63],[63,63,0],[63,0,63],[0,63,63],[63,63,63] ]
	for i in range(5):
		for y in range( i, 10 - i ):
			for x in range( i, 10 - i ):
				lp.LedCtrlXY( x, y, colors[i][0], colors[i][1], colors[i][2], mode = "pro" )
		time.wait(500)

	print( " - Testing LedCtrlXY(), Classic Mode" )
	for i in range(4,-1,-1):
		for y in range( i, 10 - i ):
			for x in range( i, 10 - i ):
				if x == 0:
					x = 10
				lp.LedCtrlXY( x-1, y, colors[3-i+2][0], colors[4-i+2][1], colors[4-i+2][2] )
		time.wait(500)
		
	i = 1
	for y in range( i, 10 - i ):
		for x in range( i, 10 - i ):
			lp.LedCtrlXY( x, y, 0, 0, 0, mode = "pro" )
	time.wait(100)

	# ledCtrlChar() test
	# -> LedCtrlChar( char, red, green, [blue], [offsx], [offsy] )
	print( " - Testing LedCtrlChar()" )
	for i in range( -7, 7, 1):
		lp.LedCtrlChar( 'A', 63, 0, 0, i, 0 )
		if   i == -6:
			print( "   - left edge" )
			time.wait(2000)
		elif i ==  6:
			print( "   - right edge" )
			time.wait(2000)
		else:
			time.wait(250)

	# turn all LEDs off
	print( " - Testing Reset()" )
	lp.Reset()

	# close this instance
	print( " - More to come, goodbye...\n" )
	lp.Close()

	
if __name__ == '__main__':
	main()

