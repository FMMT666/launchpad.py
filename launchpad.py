#!/usr/bin/python

#
# Novation Launchpad Python V0.7
# 7/2013 ASkr(FMMT666)
# www.askrprojects.net
#
# 
# This provides complete Python enabled control over a Novation Launchpad.
#
#
# TODO:
#  - docstrings 
#
#
# REQUIREMENTS:
#  - Python >= v2.7
#  - Pygame v1.9.1 (newer versions come with a broken MIDI implementation)
#
#
# TESTSUITES:
#  - Windows XP, 32 bit (Python 2.7.x, Pygame 1.9.1 (read below))
#  - Raspberry-Pi, Wheezy (standard installation, Python 2.7.3 + Pygame 1.9.1)
#
#
# ANYTHING MISSING?
#  - It's pretty complete, except for this "dual, hidden, shadow" display.
#
#
# KNOWN ISSUES
#  - A lot of traffic (e.g. using the provided text-scrolling feature)
#    will lead to an extreme lag with big buffer sizes.
#    Unfortunately, the Pygame MIDI implementation does not allow to reduce
#    the buffer size on mist systems...
#
#
#  >>>
#  >>> NOTICE FOR WINDOWS USERS:
#  >>>
#  >>>  MIDI implementation in PyGame 1.9.2+ is broken and running this will
#  >>>  bring up an 'insufficient memory' error ( pygame.midi.Input() ).
#  >>>
#  >>>  SOLUTION: use v1.9.1
#  >>>
#
#
#
#  >>>
#  >>> NOTICE FOR RASPBERRY-PI USERS:
#  >>>
#  >>>  Due to some bugs in PyGame's MIDI implementation, the buttons of the Launchpad
#  >>>  won't work after you restarted a program (LEDs are not affected).
#  >>>
#  >>>  WORKAROUND #2: Simply hit one of the AUTOMAP keys (the topmost 8 buttons)
#  >>>                 For whatever reason, this makes the MIDI button  events
#  >>>                 appearing again...
#  >>>
#  >>>  WORKAROUND #1: Pull the Launchpad's plug out and restart... (annoying).
#  >>>
#  >>>
#
# Code does not yet contain any docstrings.
# Browse manually...
#
#

import string
import random
import sys

from pygame import midi
from pygame import time

from launchpad_charset import *




MIDI_BUFFER_OUT = 128  # intended for real-time behaviour, but does not have any effect
MIDI_BUFFER_IN  = 16   # same here...



########################################################################################
### CLASS Midi
### Mini HAL for MIDI
########################################################################################
class Midi:

	#-------------------------------------------------------------------------------------
	#-- init
	#-------------------------------------------------------------------------------------
	def __init__( self ):

		self.devIn  = None
		self.devOut = None

		midi.init()

		# TODO: this sucks...
		try:
			midi.get_count()
		except:
			print("ERROR: MIDI not available...")


	#-------------------------------------------------------------------------------------
	#-- returns a list of devices that matches the string 'name' and has in- or outputs
	#-------------------------------------------------------------------------------------
	def SearchDevices( self, name, output = True, input = True, quiet = True ):
		ret = []
		i = 0
		for n in range( midi.get_count() ):
			md = midi.get_device_info( n )
			if quiet == False:
				print(md)
				sys.stdout.flush()
			if string.find( md[1], name ) >= 0:
				if output == True and md[3] > 0:
					ret.append( i )
				if input == True and md[2] > 0:
					ret.append( i )
			i += 1

		return ret

		
	#-------------------------------------------------------------------------------------
	#-- returns a list of devices that matches the string 'name' and has in- or outputs
	#-------------------------------------------------------------------------------------
	def SearchDevice( self, name, output = True, input = True ):
		ret = self.SearchDevices( name, output, input )
		if len(ret) > 0:
			return ret[0]
		else:
			return None

		
	#-------------------------------------------------------------------------------------
	#--
	#-------------------------------------------------------------------------------------
	def OpenOutput( self, midi_id ):
		if self.devOut is None:
			self.devOut = midi.Output( midi_id, 0, MIDI_BUFFER_OUT )


	#-------------------------------------------------------------------------------------
	#--
	#-------------------------------------------------------------------------------------
	def CloseOutput( self ):
		if self.devOut is not None:
			self.Output.close( self.devOut )
			self.devOut = None


	#-------------------------------------------------------------------------------------
	#--
	#-------------------------------------------------------------------------------------
	def OpenInput( self, midi_id ):
		if self.devIn is None:
			self.devIn = midi.Input( midi_id, MIDI_BUFFER_IN )


	#-------------------------------------------------------------------------------------
	#--
	#-------------------------------------------------------------------------------------
	def CloseInput( self ):
	  if self.devIn is not None:
	    midi.Input.close( self.devIn )
	    self.devIn = None


	#-------------------------------------------------------------------------------------
	#-- Return MIDI time
	#-------------------------------------------------------------------------------------
	def GetTime( self ):
		return midi.time()

			
	#-------------------------------------------------------------------------------------
	#--
	#-------------------------------------------------------------------------------------
	def ReadCheck( self ):
		return self.devIn.poll()

		
	#-------------------------------------------------------------------------------------
	#--
	#-------------------------------------------------------------------------------------
	def ReadRaw( self ):
		return self.devIn.read( 1 )


	#-------------------------------------------------------------------------------------
	#-- sends a single, short message
	#-------------------------------------------------------------------------------------
	def RawWrite( self, stat, dat1, dat2 ):
		self.devOut.write_short( stat, dat1, dat2 )

		
	#-------------------------------------------------------------------------------------
	#-- Sends a table of messages. If timestamp is 0, it is ignored.
	#-- Amount of <dat> bytes is arbitrary.
	#-- [ [ [stat, <dat1>, <dat2>, <dat3>], timestamp ],  [...], ... ]
	#-- <datN> fields are optional
	#-------------------------------------------------------------------------------------
	def RawWriteMulti( self, msgTable ):
		self.devOut.write( msgTable )
	
	


########################################################################################
### CLASS Launchpad
###
########################################################################################
class Launchpad:

	# LED AND BUTTON NUMBERS IN RAW MODE (DEC):
	#
	# +---+---+---+---+---+---+---+---+ 
	# |200|201|202|203|204|205|206|207| < AUTOMAP BUTTON CODES;
	# +---+---+---+---+---+---+---+---+   Or use LedCtrlAutomap() for LEDs (alt. args)
	# 
	# +---+---+---+---+---+---+---+---+  +---+
	# |  0|...|   |   |   |   |   |  7|  |  8|
	# +---+---+---+---+---+---+---+---+  +---+
	# | 16|...|   |   |   |   |   | 23|  | 24|
	# +---+---+---+---+---+---+---+---+  +---+
	# | 32|...|   |   |   |   |   | 39|  | 40|
	# +---+---+---+---+---+---+---+---+  +---+
	# | 48|...|   |   |   |   |   | 55|  | 56|
	# +---+---+---+---+---+---+---+---+  +---+
	# | 64|...|   |   |   |   |   | 71|  | 72|
	# +---+---+---+---+---+---+---+---+  +---+
	# | 80|...|   |   |   |   |   | 87|  | 88|
	# +---+---+---+---+---+---+---+---+  +---+
	# | 96|...|   |   |   |   |   |103|  |104| 
	# +---+---+---+---+---+---+---+---+  +---+
	# |112|...|   |   |   |   |   |119|  |120|
	# +---+---+---+---+---+---+---+---+  +---+
	# 
	#
	# LED AND BUTTON NUMBERS IN XY MODE (X/Y)
	#
	#   0   1   2   3   4   5   6   7      8   
	# +---+---+---+---+---+---+---+---+ 
	# |   |1/0|   |   |   |   |   |   |         0
	# +---+---+---+---+---+---+---+---+ 
	# 
	# +---+---+---+---+---+---+---+---+  +---+
	# |0/1|   |   |   |   |   |   |   |  |   |  1
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |   |   |   |   |  |   |  2
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |   |5/3|   |   |  |   |  3
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |   |   |   |   |  |   |  4
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |   |   |   |   |  |   |  5
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |4/6|   |   |   |  |   |  6
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |   |   |   |   |  |   |  7
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |   |   |   |   |  |8/8|  8
	# +---+---+---+---+---+---+---+---+  +---+
	#
	
	def __init__( self ):
		self.midi   = Midi() # midi interface class
		self.idOut  = None   # midi id for output
		self.idIn   = None   # midi id for input

		# just in case someone likes "defines" ;)
		SCROLL_NONE  =  0
		SCROLL_LEFT  = -1
		SCROLL_RIGHT =  1
		# same for LED brightness
		LED_OFF      =  0
		LED_LOW      =  1
		LED_MED      =  2
		LED_HIGH     =  3


	def __delete__( self ):
		self.Close();
		

	#-------------------------------------------------------------------------------------
	#-- opens the first-found Launchpad MIDI devices (one in, one out)
	#-------------------------------------------------------------------------------------
	def Open( self ):
		self.idOut = self.midi.SearchDevice("Launchpad", True, False )
		self.idIn  = self.midi.SearchDevice("Launchpad", False, True )
		
		if self.idOut is None or self.idIn is None:
			return False

		self.midi.OpenOutput( self.idOut )
		self.midi.OpenInput( self.idIn )

		return True


	#-------------------------------------------------------------------------------------
	#-- Closes everything
	#-------------------------------------------------------------------------------------
	def Close( self ):
		None
	

	#-------------------------------------------------------------------------------------
	#-- prints a list of all devices to the console (for debug)
	#-------------------------------------------------------------------------------------
	def ListAll( self ):
		self.midi.SearchDevices("*", True, True, False )


	#-------------------------------------------------------------------------------------
	#-- reset the Launchpad
	#-------------------------------------------------------------------------------------
	def Reset( self ):
		self.midi.RawWrite( 176, 0, 0 )


	#-------------------------------------------------------------------------------------
	#-- Returns a Launchpad compatible "color code byte"
	#-- NOTE: In here, number is 0..7 (left..right)
	#-------------------------------------------------------------------------------------
	def LedGetColor( self, red, green ):
		led = 0
		
		red = min( int(red), 3 ) # make int and limit to <=3
		red = max( red, 0 )      # no negative numbers

		green = min( int(green), 3 ) # make int and limit to <=3
		green = max( green, 0 )      # no negative numbers

		led |= red
		led |= green << 4 
		
		return led

		
	#-------------------------------------------------------------------------------------
	#-- Controls a grid LED by its raw <number>; with <green/red> brightness: 0..3
	#-- For LED numbers, see grid description on top of class.
	#-------------------------------------------------------------------------------------
	def LedCtrlRaw( self, number, red, green ):

		if number > 199:
			self.LedCtrlAutomap( number - 200, red, green )

		else:
			number = min( int(number), 120 ) # make int and limit to <=127
			number = max( number, 0 )        # no negative numbers
				
			led = self.LedGetColor( red, green )
			
			self.midi.RawWrite( 144, number, led )


	#-------------------------------------------------------------------------------------
	#-- Controls a grid LED by its coordinates <x> and <y>  with <green/red> brightness 0..3
	#-------------------------------------------------------------------------------------
	def LedCtrlXY( self, x, y, red, green ):

		if x < 0 or y > 8 or y < 0 or y > 8:
			return

		if y == 0:
			self.LedCtrlAutomap( x, red, green )
		
		else:
			self.LedCtrlRaw( ( (y-1) << 4) | x, red, green )


	#-------------------------------------------------------------------------------------
	#-- Sends a table of consecutive, special color values to the Launchpad.
	#-- Only requires (less than) half of the commands to update all buttons.
	#-- [ LED1, LED2, LED3, ... LED80 ]
	#-- First, the 8x8 matrix is updated, left to right, top to bottom.
	#-- Afterwards, the algorithm continues with the rightmost buttons and the
	#-- top "automap" buttons.
	#-- LEDn color format: 00gg00rr <- 2 bits green, 2 bits red (0..3)
	#-- Function LedGetColor() will do the coding for you...
	#-- Notice that the amount of LEDs needs to be even.
	#.. If an odd number of values is sent, the next, following LED is turned off!
	#-------------------------------------------------------------------------------------
	def LedCtrlRawRapid( self, allLeds ):
		le = len( allLeds )

		for i in range( 0, le, 2 ):
			self.midi.RawWrite( 146, allLeds[i], allLeds[i+1] if i+1 < le else 0 )

#   This fast version does not work, because the Launchpad gets confused
#   by the timestamps...
#
#		tmsg= []
#		for i in range( 0, le, 2 ):
#			# create a message
#			msg = [ 146 ]
#			msg.append( allLeds[i] )
#			if i+1 < le:
#				msg.append( allLeds[i+1] )
#			# add it to the list
#			tmsg.append( msg )
#			# add a timestanp
#			tmsg.append( self.midi.GetTime() + i*10 )
#
#		self.midi.RawWriteMulti( [ tmsg ] )


	#-------------------------------------------------------------------------------------
	#-- Controls an automap LED <number>; with <green/red> brightness: 0..3
	#-- NOTE: In here, number is 0..7 (left..right)
	#-------------------------------------------------------------------------------------
	def LedCtrlAutomap( self, number, red, green ):

		number = min( int(number), 7 ) # make int and limit to <=7
		number = max( number, 0 )      # minimum is 104
		
		led = self.LedGetColor( red, green )
		
		self.midi.RawWrite( 176, 104 + number, led )


	#-------------------------------------------------------------------------------------
	#-- all LEDs on
	#-------------------------------------------------------------------------------------
	def LedAllOn( self ):
		self.midi.RawWrite( 176, 0, 127 )

		
	#-------------------------------------------------------------------------------------
	#-- Sends character <char> in colors <red/green> and lateral offset <offsx> (-8..8)
	#-- to the Launchpad. <offsy> does not have yet any function
	#-------------------------------------------------------------------------------------
	def LedCtrlChar( self, char, red, green, offsx = 0, offsy = 0 ):
		char = ord(char)
		char = min( char, 255)
		char = max( char, 0) * 8

		for i in range(0, 8*16, 16):
			for j in range(8):
				sum = i + j + offsx
				if sum >= i and sum < i + 8:
					if CHARTAB[char]  &  0x80 >> j:
						self.LedCtrlRaw( sum, red, green )
					else:
						self.LedCtrlRaw( sum, 0, 0 )
			char += 1
					

	#-------------------------------------------------------------------------------------
	#-- Scroll a string, as fast as we can, over the Launch pad.
	#-- Dir specifies: -1 to left, 0 no scroll, 1 to right
	#-- The "no scroll" characters are sent 8 times to have a comparable speed.
	#-------------------------------------------------------------------------------------
	def LedCtrlString( self, str, red, green, dir = 0 ):

		if dir == -1:
			for i in str:
				for off in range(5,-8,-1):
					self.LedCtrlChar(i, red, green, off)
		elif dir == 0:
			for i in str:
				for off in range(4):
					self.LedCtrlChar(i, red, green)
		elif dir == 1:
			for i in str:
				for off in range(-5,8):
					self.LedCtrlChar(i, red, green, off)

					
	#-------------------------------------------------------------------------------------
	#-- Returns True if a button event was received.
	#-------------------------------------------------------------------------------------
	def ButtonChanged( self ):
		return self.midi.ReadCheck();

		
	#-------------------------------------------------------------------------------------
	#-- Returns the raw value of the last button change as a table:
	#-- [ <button>, <True/False> ]
	#-------------------------------------------------------------------------------------
	def ButtonStateRaw( self ):
		if self.midi.ReadCheck():
			a = self.midi.ReadRaw()
			return [ a[0][0][1] if a[0][0][0] == 144 else a[0][0][1] + 96, True if a[0][0][2] > 0 else False ]
		else:
			return []


	#-------------------------------------------------------------------------------------
	#-- Returns an x/y value of the last button change as a table:
	#-- [ <x>, <y>, <True/False> ]
	#-------------------------------------------------------------------------------------
	def ButtonStateXY( self ):
		if self.midi.ReadCheck():
			a = self.midi.ReadRaw()

			if a[0][0][0] == 144:
				x = a[0][0][1] & 0x0f
				y = ( a[0][0][1] & 0xf0 ) >> 4
				
				return [ x, y+1, True if a[0][0][2] > 0 else False ]
				
			elif a[0][0][0] == 176:
				return [ a[0][0][1] - 104, 0, True if a[0][0][2] > 0 else False ]
				
		return []

		
########################################################################################
########################################################################################
########################################################################################
def main():

	# some demo code ahead...

	LP = Launchpad()  # create a Launchpad instance
	LP.Open()         # start it

	LP.ListAll()      # debug function: list all available MIDI devices

	# the latter of these two messages might not finish (MIDI buffer too large,
	# MIDI speed too low...)
	print("HELLO")
	LP.LedCtrlString( 'HELLO', 3, 0, 0 )  # display  H E L L O  in green
	print("USER")
	LP.LedCtrlString( 'USER   ', 0, 3, -1 )  # scroll  U S E R  from right to left
	# try to give it some extra time:
	time.wait( 5000 )

	print("---\nTurning on all LEDs.")
	LP.LedAllOn()
	time.wait( 3000 )


	# control of automap buttons and LEDs
	print("---\nAutomap buttons.")
	for n in range(3):
		for i in range(0,8):
			LP.LedCtrlAutomap( i, 3, 0 )
			time.wait(50)
		for i in range(0,8):
			LP.LedCtrlAutomap( i, 0, 3 )
			time.wait(50)
	for i in range(0,8):
		LP.LedCtrlAutomap( i, 0, 0 )


	# random output until button "arm" (lower right) is pressed
	print("---\nRandom madness. Stop by hitting the ARM button (lower right)")
	print("Remember the PyGame MIDI bug:")
	print("If the ARM button has no effect, hit an automap button (top row)")
	print("and try again...")
	while 1:
		LP.LedCtrlRaw( random.randint(0,127), random.randint(0,3), random.randint(0,3) )
		time.wait( 10 )
		but = LP.ButtonStateRaw()
		if but != []:
			print( but[0] )
			if but[0] == 120:
				break

	# fast update method
	print("---\nFast update via color table.")
	g = LP.LedGetColor( 0, 3 )
	r = LP.LedGetColor( 3, 0 )
	y = LP.LedGetColor( 3, 3 )
	ledTab = [ ]
	for i in range( 80 ):
		ledTab.append( r )
		ledTab.append( g )
		ledTab.append( y )
	LP.LedCtrlRawRapid( ledTab )

		
	# turn off every pressed key
	print("---\nPress some buttons. End by pushing ARM.")
	while 1:
		but = LP.ButtonStateRaw()
		if but != []:
			print( but )
			if but == [ 120, True ]:
				break
			LP.LedCtrlRaw( but[0], 3 if but[1] else 0, 0 )


	# query buttons via the "xy return strategy"
	print("---\nPress some buttons. End by pushing ARM.")
	while True:
		time.wait( 10 )
		but = LP.ButtonStateXY()
		if but != []:
			LP.LedCtrlXY( but[0], but[1], 3, 0 )
			print( but )
			if but == [ 8, 8, True ]:
				break

	print("---\nGoodbye...")

	LP.Reset()
			
	LP.Close()
	

	
if __name__ == '__main__':
	main()


