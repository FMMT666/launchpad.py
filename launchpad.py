
#!/usr/bin/python

#
# Novation Launchpad Python V0.8a
# 7/2013, 2/2015, 1/2016 ASkr(FMMT666)
# www.askrprojects.net
#
#
# 2016/01/XX:
#  - basic Launchpad Pro support now built in; working on more...
#  - added RGB LED control
#  - added X/Y LED control (RGB and colorcode)
#  - added a lot more stuff for "Pro"
#  - added "Mk2" support (new class)
#
# 2016/01/16:
#  - preparations for Launchpad Pro support (new base class)
#
# 2015/02/21:
#  - multiple Launchpad support now built-in
#
# 2015/02/10:
#  - Tagged stuff for refactoring with REFAC2015. The original code was
#    quickly hacked together within a weekend. Looks like a lot of this
#    badly needs some changes :)
#  - The S/Mini variants, escpecially in conjunction with a fast PC
#    are waaaays faster that the original Launchpad.
#    While this is quite nice for the real-time behaviour of all the
#    buttons and LEDs, the character drawing functions now need a
#    timer.
#    -> temporarily "fixed" with a delay :)
#
# 
# This provides complete Python enabled control over a Novation Launchpad.
#
#
# TODO/NEXT:
#  - bad pointer (midi) on close
#  - defines for buttons
#  - docstrings
#  - ...
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
#  - Linux 64 bit (Python 2.7.x, Pygame 1.9.1)
#  - several others
#  - does _not_ work on Mac OS X (for now)
#
#
# ANYTHING MISSING?
#  - Regarding Launchpad's functionality, it's pretty complete.
#  - Lot of stuff missing in the code (exception handling, error andling, etc...)
#
#
# KNOWN ISSUES
#  - The Launchpad.Close() function does not work (bad pointer) and will
#    crash the application upon calling it.
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
#
#
#
#  >>>
#  >>> NOTICE FOR SPACE USERS:
#  >>>
#  >>>  Yep, this one uses tabs. Tabs everywhere.
#  >>>  Deal with it :-)
#  >>>
#

import string
import random
import sys

from pygame import midi
from pygame import time

from launchpad_charset import *


MIDI_BUFFER_OUT = 128  # intended for real-time behaviour, but does not have any effect
MIDI_BUFFER_IN  = 16   # same here...
#MIDI_BUFFER_OUT = 1   # TESTING S/MINI
#MIDI_BUFFER_IN  = 1   # TESTING S/MINI



##########################################################################################
### CLASS Midi
### Midi singleton wrapper
##########################################################################################
class Midi:

	# instance created 
	instanceMidi = None;

	#---------------------------------------------------------------------------------------
	#-- init
	#-- Allow only one instance to be created
	#---------------------------------------------------------------------------------------
	def __init__( self ):
		if Midi.instanceMidi is None:
			try:
				Midi.instanceMidi = Midi.__Midi()
			except:
				print("unable to initialize MIDI")
				Midi.instanceMidi = None

		self.devIn  = None
		self.devOut = None


	#---------------------------------------------------------------------------------------
	#-- getattr
	#-- Pass all unknown method calls to the inner Midi class __Midi()
	#---------------------------------------------------------------------------------------
	def __getattr__( self, name ):
		return getattr( self.instanceMidi, name )
	

	#-------------------------------------------------------------------------------------
	#--
	#-------------------------------------------------------------------------------------
	def OpenOutput( self, midi_id ):
		if self.devOut is None:
			try:
				self.devOut = midi.Output( midi_id, 0, MIDI_BUFFER_OUT )
			except:
				self.devOut = None
				return False
		return True


	#-------------------------------------------------------------------------------------
	#--
	#-------------------------------------------------------------------------------------
	def CloseOutput( self ):
		if self.devOut is not None:
			self.devOut.close()
			self.devOut = None


	#-------------------------------------------------------------------------------------
	#--
	#-------------------------------------------------------------------------------------
	def OpenInput( self, midi_id ):
		if self.devIn is None:
			try:
				self.devIn = midi.Input( midi_id, MIDI_BUFFER_IN )
			except:
				self.devIn = None
				return False
		return True


	#-------------------------------------------------------------------------------------
	#--
	#-------------------------------------------------------------------------------------
	def CloseInput( self ):
		if self.devIn is not None:
			self.devIn.close()
			self.devIn = None


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
	#-- Sends a list of messages. If timestamp is 0, it is ignored.
	#-- Amount of <dat> bytes is arbitrary.
	#-- [ [ [stat, <dat1>, <dat2>, <dat3>], timestamp ],  [...], ... ]
	#-- <datN> fields are optional
	#-------------------------------------------------------------------------------------
	def RawWriteMulti( self, lstMessages ):
		self.devOut.write( lstMessages )

	
	#-------------------------------------------------------------------------------------
	#-- Sends a single system-exclusive message, given by list <lstMessage>
	#-- The start (0xF0) and end bytes (0xF7) are added automatically.
	#-- [ <dat1>, <dat2>, ..., <datN> ]
	#-- Timestamp is not supported and will be sent as '0' (for now)
	#-------------------------------------------------------------------------------------
	def RawWriteSysEx( self, lstMessage, timeStamp = 0 ):
		self.devOut.write_sys_ex( timeStamp, [0xf0] + lstMessage + [0xf7] )


	########################################################################################
	### CLASS __Midi
	### The rest of the Midi class, non Midi-device specific.
	########################################################################################
	class __Midi:

		#-------------------------------------------------------------------------------------
		#-- init
		#-------------------------------------------------------------------------------------
		def __init__( self ):
			# exception handling moved up to Midi()
			midi.init()
			# but I can't remember why I put this one in here...
			midi.get_count()

				
		#-------------------------------------------------------------------------------------
		#-- del
		#-- This will never be executed, because no one knows, how many Launchpad instances
		#-- exist(ed) until we start to count them...
		#-------------------------------------------------------------------------------------
		def __del__( self ):
			midi.quit()


		#-------------------------------------------------------------------------------------
		#-- Returns a list of devices that matches the string 'name' and has in- or outputs.
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
		#-- Returns the first device that matches the string 'name'.
		#-- NEW2015/02: added number argument to pick from several devices (if available)
		#-------------------------------------------------------------------------------------
		def SearchDevice( self, name, output = True, input = True, number = 0 ):
			ret = self.SearchDevices( name, output, input )
			
			if number < 0 or number >= len( ret ):
				return None

			return ret[number]


		#-------------------------------------------------------------------------------------
		#-- Return MIDI time
		#-------------------------------------------------------------------------------------
		def GetTime( self ):
			return midi.time()
		
	


########################################################################################
### CLASS LaunchpadBase
###
### Todo: Could be abstract, but "abc" and "ABCMeta" are somehow a PITA...
########################################################################################
class LaunchpadBase( object ):

	def __init__( self ):
		self.midi   = Midi() # midi interface instance (singleton)
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
	#-- Opens one of the attached Launchpad MIDI devices.
	#-------------------------------------------------------------------------------------
	def Open( self, number = 0, name = "Launchpad" ):
		self.idOut = self.midi.SearchDevice( name, True, False, number = number )
		self.idIn  = self.midi.SearchDevice( name, False, True, number = number )
		
		if self.idOut is None or self.idIn is None:
			return False

		if self.midi.OpenOutput( self.idOut ) == False:
			return False
		
		return self.midi.OpenInput( self.idIn )


	#-------------------------------------------------------------------------------------
	#-- Checks if a device exists, but does not open it.
	#-- Does not check whether a device is in use or other, strange things...
	#-------------------------------------------------------------------------------------
	def Check( self, number = 0, name = "Launchpad" ):
		self.idOut = self.midi.SearchDevice( name, True, False, number = number )
		self.idIn  = self.midi.SearchDevice( name, False, True, number = number )
		
		if self.idOut is None or self.idIn is None:
			return False
		
		return True


	#-------------------------------------------------------------------------------------
	#-- Closes this device
	#-------------------------------------------------------------------------------------
	def Close( self ):
		self.midi.CloseInput()
		self.midi.CloseOutput()
	

	#-------------------------------------------------------------------------------------
	#-- prints a list of all devices to the console (for debug)
	#-------------------------------------------------------------------------------------
	def ListAll( self ):
		self.midi.SearchDevices( "*", True, True, False )



########################################################################################
### CLASS Launchpad
###
### For 2-color Launchpads with 8x8 matrix and 2x8 top/right rows
########################################################################################
class Launchpad( LaunchpadBase ):

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


	#-------------------------------------------------------------------------------------
	#-- reset the Launchpad
	#-- Turns off all LEDs
	#-------------------------------------------------------------------------------------
	def Reset( self ):
		self.midi.RawWrite( 176, 0, 0 )


	#-------------------------------------------------------------------------------------
	#-- Returns a Launchpad compatible "color code byte"
	#-- NOTE: In here, number is 0..7 (left..right)
	#-- REFAC2015: Probably device specific.
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
	#-- REFAC2015: Device specific.
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
	#-- Sends a list of consecutive, special color values to the Launchpad.
	#-- Only requires (less than) half of the commands to update all buttons.
	#-- [ LED1, LED2, LED3, ... LED80 ]
	#-- First, the 8x8 matrix is updated, left to right, top to bottom.
	#-- Afterwards, the algorithm continues with the rightmost buttons and the
	#-- top "automap" buttons.
	#-- LEDn color format: 00gg00rr <- 2 bits green, 2 bits red (0..3)
	#-- Function LedGetColor() will do the coding for you...
	#-- Notice that the amount of LEDs needs to be even.
	#-- If an odd number of values is sent, the next, following LED is turned off!
	#-- REFAC2015: Device specific.
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
	#-- REFAC2015: Device specific.
	#-------------------------------------------------------------------------------------
	def LedCtrlAutomap( self, number, red, green ):

		number = min( int(number), 7 ) # make int and limit to <=7
		number = max( number, 0 )      # minimum is 104
		
		led = self.LedGetColor( red, green )
		
		self.midi.RawWrite( 176, 104 + number, led )


	#-------------------------------------------------------------------------------------
	#-- all LEDs on
	#-- <colorcode> is here for backwards compatibility with the newer "Mk2" and "Pro"
	#-- classes. If it's "0", all LEDs are turned off and on otherwise.
	#-------------------------------------------------------------------------------------
	def LedAllOn( self, colorcode = None ):
		if colorcode == 0:
			self.midi.RawWrite( 176, 0, 127 )
		else:
			self.Reset()

		
	#-------------------------------------------------------------------------------------
	#-- Sends character <char> in colors <red/green> and lateral offset <offsx> (-8..8)
	#-- to the Launchpad. <offsy> does not have yet any function
	#-------------------------------------------------------------------------------------
	def LedCtrlChar( self, char, red, green, offsx = 0, offsy = 0 ):
		char = ord( char )
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
	#-- Scroll <string>, in colors specified by <red/green>, as fast as we can.
	#-- <direction> specifies: -1 to left, 0 no scroll, 1 to right
	#--
	#-- The "no scroll" characters are sent 8 times to have a comparable speed.
	#-- ^^^ WTF?
	#-------------------------------------------------------------------------------------
	def LedCtrlString( self, string, red, green, direction = 0, waitms = 150 ):

		# TODO: The delay was a dirty hack.
		#       It won't go :-/

		if direction == -1:
			for i in string:
				for offsx in range(5,-8,-1):
					self.LedCtrlChar(i, red, green, offsx = offsx)
					# TESTING ONLY (slowdown for S/Mini)
					time.wait(waitms);
		elif direction == 0:
			for i in string:
				for offsx in range(4):
					self.LedCtrlChar(i, red, green)
					# TESTING ONLY (slowdown for S/Mini)
					time.wait(waitms);
		elif direction == 1:
			for i in string:
				for offsx in range(-5,8):
					self.LedCtrlChar(i, red, green, offsx = offsx)
					# TESTING ONLY (slowdown for S/Mini)
					time.wait(waitms);
					

					
	#-------------------------------------------------------------------------------------
	#-- Returns True if a button event was received.
	#-------------------------------------------------------------------------------------
	def ButtonChanged( self ):
		return self.midi.ReadCheck();

		
	#-------------------------------------------------------------------------------------
	#-- Returns the raw value of the last button change as a list:
	#-- [ <button>, <True/False> ]
	#-- REFAC2015: Device specific.
	#-------------------------------------------------------------------------------------
	def ButtonStateRaw( self ):
		if self.midi.ReadCheck():
			a = self.midi.ReadRaw()
			return [ a[0][0][1] if a[0][0][0] == 144 else a[0][0][1] + 96, True if a[0][0][2] > 0 else False ]
		else:
			return []


	#-------------------------------------------------------------------------------------
	#-- Returns an x/y value of the last button change as a list:
	#-- [ <x>, <y>, <True/False> ]
	#-- REFAC2015: Device specific.
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
### CLASS LaunchpadPro
###
### For 3-color "Pro" Launchpads with 8x8 matrix and 4x8 left/right/top/bottom rows
########################################################################################

class LaunchpadPro( LaunchpadBase ):

	# LED AND BUTTON NUMBERS IN RAW MODE (DEC)
	# WITH LAUNCHPAD IN "LIVE MODE" (PRESS SETUP, top-left GREEN).
	#
	# Notice that the fine manual doesn't know that mode.
	# According to what's written there, the numbering used
	# refers to the "PROGRAMMING MODE", which actually does
	# not react to any of those notes (or numbers).
	#
	#        +---+---+---+---+---+---+---+---+ 
	#        | 91|   |   |   |   |   |   | 98|
	#        +---+---+---+---+---+---+---+---+ 
	#         
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# | 80|  | 81|   |   |   |   |   |   |   |  | 89|
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# | 70|  |   |   |   |   |   |   |   |   |  | 79|
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# | 60|  |   |   |   |   |   |   | 67|   |  | 69|
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# | 50|  |   |   |   |   |   |   |   |   |  | 59|
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# | 40|  |   |   |   |   |   |   |   |   |  | 49|
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# | 30|  |   |   |   |   |   |   |   |   |  | 39|
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# | 20|  |   |   | 23|   |   |   |   |   |  | 29|
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# | 10|  |   |   |   |   |   |   |   |   |  | 19|
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	#       
	#        +---+---+---+---+---+---+---+---+ 
	#        |  1|  2|   |   |   |   |   |  8|
	#        +---+---+---+---+---+---+---+---+ 
	#
	#
	# LED AND BUTTON NUMBERS IN XY CLASSIC MODE (X/Y)
	#
	#   9      0   1   2   3   4   5   6   7      8   
	#        +---+---+---+---+---+---+---+---+ 
	#        |0/0|   |2/0|   |   |   |   |   |         0
	#        +---+---+---+---+---+---+---+---+ 
	#         
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |   |  |0/1|   |   |   |   |   |   |   |  |   |  1
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |9/2|  |   |   |   |   |   |   |   |   |  |   |  2
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |   |  |   |   |   |   |   |5/3|   |   |  |   |  3
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |   |  |   |   |   |   |   |   |   |   |  |   |  4
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |   |  |   |   |   |   |   |   |   |   |  |   |  5
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |   |  |   |   |   |   |4/6|   |   |   |  |   |  6
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |   |  |   |   |   |   |   |   |   |   |  |   |  7
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |9/8|  |   |   |   |   |   |   |   |   |  |8/8|  8
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	#       
	#        +---+---+---+---+---+---+---+---+ 
	#        |   |1/9|   |   |   |   |   |   |         9
	#        +---+---+---+---+---+---+---+---+ 
	#
	#
	# LED AND BUTTON NUMBERS IN XY PRO MODE (X/Y)
	#
	#   0      1   2   3   4   5   6   7   8      9
	#        +---+---+---+---+---+---+---+---+ 
	#        |1/0|   |3/0|   |   |   |   |   |         0
	#        +---+---+---+---+---+---+---+---+ 
	#         
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |   |  |1/1|   |   |   |   |   |   |   |  |   |  1
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |0/2|  |   |   |   |   |   |   |   |   |  |   |  2
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |   |  |   |   |   |   |   |6/3|   |   |  |   |  3
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |   |  |   |   |   |   |   |   |   |   |  |   |  4
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |   |  |   |   |   |   |   |   |   |   |  |   |  5
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |   |  |   |   |   |   |5/6|   |   |   |  |   |  6
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |   |  |   |   |   |   |   |   |   |   |  |   |  7
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	# |0/8|  |   |   |   |   |   |   |   |   |  |9/8|  8
	# +---+  +---+---+---+---+---+---+---+---+  +---+
	#       
	#        +---+---+---+---+---+---+---+---+ 
	#        |   |2/9|   |   |   |   |   |   |         9
	#        +---+---+---+---+---+---+---+---+ 
	#
	
	COLORS = {'black':0, 'off':0, 'white':3, 'red':5, 'green':17 }

	#-------------------------------------------------------------------------------------
	#-- Opens one of the attached Launchpad MIDI devices.
	#-- Uses search string "Pro", by default.
	#-------------------------------------------------------------------------------------
	# Overrides "LaunchpadBase" method
	def Open( self, number = 0, name = "Pro" ):
		retval = super( LaunchpadPro, self ).Open( number = number, name = name )
		if retval == True:
			self.LedSetMode( 0 )

		return retval


	#-------------------------------------------------------------------------------------
	#-- Checks if a device exists, but does not open it.
	#-- Does not check whether a device is in use or other, strange things...
	#-- Uses search string "Pro", by default.
	#-------------------------------------------------------------------------------------
	# Overrides "LaunchpadBase" method
	def Check( self, number = 0, name = "Pro" ):
		return super( LaunchpadPro, self ).Check( number = number, name = name )


	#-------------------------------------------------------------------------------------
	#-- Sets the button layout (and codes) to the set, specified by <mode>.
	#-- Valid options:
	#--  00 - Session, 01 - Drum Rack, 02 - Chromatic Note, 03 - User (Drum)
	#--  04 - Audio, 05 -Fader, 06 - Record Arm, 07 - Track Select, 08 - Mute
	#--  09 - Solo, 0A - Volume 
	#-- Until now, we'll need the "Session" (0x00) settings.
	#-------------------------------------------------------------------------------------
	# TODO: ASkr, Undocumented!
	def LedSetLayout( self, mode ):
		mode = min( mode, 0x0A )
		mode = max( mode, 0 )
		
		self.midi.RawWriteSysEx( [ 240, 0, 32, 41, 2, 16, 34, mode ] )


	#-------------------------------------------------------------------------------------
	#-- Selects the Pro's mode.
	#-- <mode> -> 0 -> "Ableton Live mode"  (what we need)
	#--           1 -> "Standalone mode"    (power up default)
	#-------------------------------------------------------------------------------------
	def LedSetMode( self, mode ):
		if mode < 0 or mode > 1:
			return
			
		self.midi.RawWriteSysEx( [ 240, 0, 32, 41, 2, 16, 33, mode ] )


	#-------------------------------------------------------------------------------------
	#-- Sets the button layout to "Session" mode.
	#-------------------------------------------------------------------------------------
	# TODO: ASkr, Undocumented!
	def LedSetButtonLayoutSession( self ):
		self.LedSetLayout( 0 )


	#-------------------------------------------------------------------------------------
	#-- Returns an RGB colorcode by trying to find a color of a name given by string <name>.
	#-- If nothing was found, Code 'black' (off) is returned.
	#-------------------------------------------------------------------------------------
	def LedGetColorByName( self, name ):
		# should not be required
		#if type( name ) is not str:
		#	return 0;
		if name in LaunchpadPro.COLORS:
			return LaunchpadPro.COLORS[name]
		else:
			return LaunchpadPro.COLORS['black']


	#-------------------------------------------------------------------------------------
	#-- Controls a grid LED by its position <number> and a color, specified by
	#-- <red>, <green> and <blue> intensities, with can each be an integer between 0..63.
	#-- If <blue> is omitted, this methos runs in "Classic" compatibility mode and the
	#-- intensities, which were within 0..3 in that mode, are multiplied by 21 (0..63)
	#-- to emulate the old brightness feeling :)
	#-- Notice that each message requires 10 bytes to be sent. For a faster, but
	#-- unfortunately "not-RGB" method, see "LedCtrlRawByCode()"
	#-------------------------------------------------------------------------------------
	def LedCtrlRaw( self, number, red, green, blue = None ):

		number = min( number, 99 )
		number = max( number, 0 )

		if blue is None:
			blue   = 0
			red   *= 21
			green *= 21
			
		red = min( red, 63 )
		red = max( red, 0 )
		green = min( green, 63 )
		green = max( green, 0 )
		blue = min( blue, 63 )
		blue = max( blue, 0 )

		self.midi.RawWriteSysEx( [ 240, 0, 32, 41, 2, 16, 11, number, red, green, blue ] )


	#-------------------------------------------------------------------------------------
	#-- Controls a grid LED by its position <number> and a color code <colorcode>
	#-- from the Launchpad's color palette.
	#-- If <colorcode> is omitted, 'white' is used.
	#-- This method should be ~3 times faster that the RGB version "LedCtrlRaw()", which
	#-- uses 10 byte, system-exclusive MIDI messages.
	#-------------------------------------------------------------------------------------
	def LedCtrlRawByCode( self, number, colorcode = None ):

		number = min( number, 99 )
		number = max( number, 0 )

		if colorcode is None:
			colorcode = LaunchpadPro.COLORS['white']

		self.midi.RawWrite( 144, number, colorcode )


	#-------------------------------------------------------------------------------------
	#-- Controls a grid LED by its coordinates <x>, <y> and <reg>, <green> and <blue>
	#-- intensity values. By default, the old and compatible "Classic" mode is used
	#-- (8x8 matrix left has x=0). If <mode> is set to "pro", x=0 will light up the round
	#-- buttons on the left of the Launchpad Pro (not available on other models).
	#-- This method internally uses "LedCtrlRaw()". Please also notice the comments
	#-- in that one.
	#-------------------------------------------------------------------------------------
	def LedCtrlXY( self, x, y, red, green, blue = None, mode = "classic" ):
		x = min( x, 9 )
		x = max( x, 0 )
		y = min( y, 9 )
		y = max( y, 0 )
		
		# rotate matrix to the right, column 9 overflows from right to left, same row
		if mode != "pro":
			x = ( x + 1 ) % 10
			
		# swap y
		led = 90-(10*y) + x
		
		self.LedCtrlRaw( led, red, green, blue )
	

	#-------------------------------------------------------------------------------------
	#-- Controls a grid LED by its coordinates <x>, <y> and its <colorcode>.
	#-- By default, the old and compatible "Classic" mode is used (8x8 matrix left has x=0).
	#-- If <mode> is set to "pro", x=0 will light up the round buttons on the left of the
	#-- Launchpad Pro (not available on other models).
	#-------------------------------------------------------------------------------------
	def LedCtrlXYByCode( self, x, y, colorcode, mode = "classic" ):
		x = min( x, 9 )
		x = max( x, 0 )
		y = min( y, 9 )
		y = max( y, 0 )
		
		# rotate matrix to the right, column 9 overflows from right to left, same row
		if mode != "pro":
			x = ( x + 1 ) % 10
			
		# swap y
		led = 90-(10*y) + x
		
		self.LedCtrlRawByCode( led, colorcode )


	#-------------------------------------------------------------------------------------
	#-- EXPERIMENTAL
	#-- New approach to color arguments.
	#-- <lstColor> list of length 3 with RGB color information, [<r>,<g>,<b>]
	#-------------------------------------------------------------------------------------
	# TODO: ASkr, Undocumented!
	def LedCtrlXYByRGB( self, x, y, lstColor, mode = "classic" ):
		if type( lstColor ) is not list:
			return
			
		x = min( x, 9 )
		x = max( x, 0 )
		y = min( y, 9 )
		y = max( y, 0 )
		
		# rotate matrix to the right, column 9 overflows from right to left, same row
		if mode != "pro":
			x = ( x + 1 ) % 10
			
		# swap y
		led = 90-(10*y) + x
	
		self.LedCtrlRaw( led, lstColor[0], lstColor[1], lstColor[2] )


	#-------------------------------------------------------------------------------------
	#-- Sends character <char> in colors <red/green/blue> and lateral offset <offsx> (-8..8)
	#-- to the Launchpad. <offsy> does not have yet any function.
	#-- If <blue> is omitted, this method runs in "Classic" compatibility mode and the
	#-- old 0..3 <red/green> values are multiplied with 21, to match the "Pro" 0..63 range.
	#-------------------------------------------------------------------------------------
	def LedCtrlChar( self, char, red, green, blue = None, offsx = 0, offsy = 0 ):
		char = ord( char )
		char = min( char, 255)
		char = max( char, 0) * 8

		# compatibility mode
		if blue is None:
			red   *= 21
			green *= 21
			blue   =  0

		min( red, 63 )
		max( red,  0 )
		min( green, 63 )
		max( green,  0 )
		min( blue, 63 )
		max( blue,  0 )

		for i in range(81, 1, -10):
			for j in range(8):
				sum = i + j + offsx
				if sum >= i and sum < i + 8:
					if CHARTAB[char]  &  0x80 >> j:
						self.LedCtrlRaw( sum, red, green, blue )
					else:
						self.LedCtrlRaw( sum, 0, 0, 0 )
			char += 1


	#-------------------------------------------------------------------------------------
	#-- Scroll <string>, with color specified by <red/green/blue>, as fast as we can.
	#-- <direction> specifies: -1 to left, 0 no scroll, 1 to right
	#-- If <blue> is omitted, "Classic" compatibility mode is turned on and the old
	#-- 0..3 color intensity range is streched by 21 to 0..63.
	#--
	#-- The "no scroll" characters are sent 8 times to have a comparable speed.
	#-- ^^^ WAT?
	#-------------------------------------------------------------------------------------
	def LedCtrlString( self, string, red, green, blue = None, direction = 0, waitms = 150 ):

		# TODO: The delay was a dirty hack.
		#       It won't go :-/

		# compatibility mode
		if blue is None:
			red   *= 21
			green *= 21
			blue   =  0

		min( red, 63 )
		max( red,  0 )
		min( green, 63 )
		max( green,  0 )
		min( blue, 63 )
		max( blue,  0 )

		if direction == -1:
			for i in string:
				for offsx in range(5,-8,-1):
					self.LedCtrlChar(i, red, green, blue, offsx = offsx)
					# TESTING ONLY (slowdown for S/Mini)
					time.wait(waitms);
		elif direction == 0:
			for i in string:
				for offsx in range(4):
					self.LedCtrlChar(i, red, green, blue)
					# TESTING ONLY (slowdown for S/Mini)
					time.wait(waitms);
		elif direction == 1:
			for i in string:
				for offsx in range(-5,8):
					self.LedCtrlChar(i, red, green, blue, offsx = offsx)
					# TESTING ONLY (slowdown for S/Mini)
					time.wait(waitms);

		

	#-------------------------------------------------------------------------------------
	#-- Quickly sets all all LEDs to the same color, given by <colorcode>.
	#-- If <colorcode> is omitted, "white" is used.
	#-------------------------------------------------------------------------------------
	def LedAllOn( self, colorcode = None ):
		if colorcode is None:
			colorcode = LaunchpadPro.COLORS['white']
		else:
			colorcode = min( colorcode, 127 )
			colorcode = max( colorcode, 0 )
		
		self.midi.RawWriteSysEx( [ 240, 0, 32, 41, 2, 16, 14, colorcode ] )



########################################################################################
### CLASS LaunchpadMk2
###
### For 3-color "Mk2" Launchpads with 8x8 matrix and 2x8 right/top rows
########################################################################################

class LaunchpadMk2( LaunchpadPro ):

	# LED AND BUTTON NUMBERS IN RAW MODE (DEC)
	# WITH LAUNCHPAD IN "LIVE MODE" (PRESS SETUP, top-left GREEN).
	#
	# Notice that the fine manual doesn't know that mode.
	# According to what's written there, the numbering used
	# refers to the "PROGRAMMING MODE", which actually does
	# not react to any of those notes (or numbers).
	#
	#        +---+---+---+---+---+---+---+---+ 
	#        |104|   |106|   |   |   |   |111|
	#        +---+---+---+---+---+---+---+---+ 
	#         
	#        +---+---+---+---+---+---+---+---+  +---+
	#        | 81|   |   |   |   |   |   |   |  | 89|
	#        +---+---+---+---+---+---+---+---+  +---+
	#        | 71|   |   |   |   |   |   |   |  | 79|
	#        +---+---+---+---+---+---+---+---+  +---+
	#        | 61|   |   |   |   |   | 67|   |  | 69|
	#        +---+---+---+---+---+---+---+---+  +---+
	#        | 51|   |   |   |   |   |   |   |  | 59|
	#        +---+---+---+---+---+---+---+---+  +---+
	#        | 41|   |   |   |   |   |   |   |  | 49|
	#        +---+---+---+---+---+---+---+---+  +---+
	#        | 31|   |   |   |   |   |   |   |  | 39|
	#        +---+---+---+---+---+---+---+---+  +---+
	#        | 21|   | 23|   |   |   |   |   |  | 29|
	#        +---+---+---+---+---+---+---+---+  +---+
	#        | 11|   |   |   |   |   |   |   |  | 19|
	#        +---+---+---+---+---+---+---+---+  +---+
	#       
	#
	#
	# LED AND BUTTON NUMBERS IN XY MODE (X/Y)
	#
	#          0   1   2   3   4   5   6   7      8   
	#        +---+---+---+---+---+---+---+---+ 
	#        |0/0|   |2/0|   |   |   |   |   |         0
	#        +---+---+---+---+---+---+---+---+ 
	#         
	#        +---+---+---+---+---+---+---+---+  +---+
	#        |0/1|   |   |   |   |   |   |   |  |   |  1
	#        +---+---+---+---+---+---+---+---+  +---+
	#        |   |   |   |   |   |   |   |   |  |   |  2
	#        +---+---+---+---+---+---+---+---+  +---+
	#        |   |   |   |   |   |5/3|   |   |  |   |  3
	#        +---+---+---+---+---+---+---+---+  +---+
	#        |   |   |   |   |   |   |   |   |  |   |  4
	#        +---+---+---+---+---+---+---+---+  +---+
	#        |   |   |   |   |   |   |   |   |  |   |  5
	#        +---+---+---+---+---+---+---+---+  +---+
	#        |   |   |   |   |4/6|   |   |   |  |   |  6
	#        +---+---+---+---+---+---+---+---+  +---+
	#        |   |   |   |   |   |   |   |   |  |   |  7
	#        +---+---+---+---+---+---+---+---+  +---+
	#        |   |   |   |   |   |   |   |   |  |8/8|  8
	#        +---+---+---+---+---+---+---+---+  +---+
	#       


	#-------------------------------------------------------------------------------------
	#-- Opens one of the attached Launchpad MIDI devices.
	#-- Uses search string "MK2", by default.
	#-------------------------------------------------------------------------------------
	# Overrides "LaunchpadPro" method
	def Open( self, number = 0, name = "MK2" ):
		return super( LaunchpadMk2, self ).Open( number = number, name = name );


	#-------------------------------------------------------------------------------------
	#-- Checks if a device exists, but does not open it.
	#-- Does not check whether a device is in use or other, strange things...
	#-- Uses search string "MK2", by default.
	#-------------------------------------------------------------------------------------
	# Overrides "LaunchpadPro" method
	def Check( self, number = 0, name = "MK2" ):
		return super( LaunchpadMk2, self ).Check( number = number, name = name );
	

	#-------------------------------------------------------------------------------------
	#-- Controls a grid LED by its position <number> and a color, specified by
	#-- <red>, <green> and <blue> intensities, with can each be an integer between 0..63.
	#-- If <blue> is omitted, this methos runs in "Classic" compatibility mode and the
	#-- intensities, which were within 0..3 in that mode, are multiplied by 21 (0..63)
	#-- to emulate the old brightness feeling :)
	#-- Notice that each message requires 10 bytes to be sent. For a faster, but
	#-- unfortunately "not-RGB" method, see "LedCtrlRawByCode()"
	#-------------------------------------------------------------------------------------
	# Overrides "LaunchpadPro" method
	def LedCtrlRaw( self, number, red, green, blue = None ):

		number = min( number, 111 )
		number = max( number, 0 )

		if number > 89 and number < 104:
			return

		if blue is None:
			blue   = 0
			red   *= 21
			green *= 21
			
		red = min( red, 63 )
		red = max( red, 0 )
		green = min( green, 63 )
		green = max( green, 0 )
		blue = min( blue, 63 )
		blue = max( blue, 0 )

		self.midi.RawWriteSysEx( [ 240, 0, 32, 41, 2, 16, 11, number, red, green, blue ] )


	#-------------------------------------------------------------------------------------
	#-- Controls a grid LED by its coordinates <x>, <y> and <reg>, <green> and <blue>
	#-- intensity values.
	#-- This method internally uses "LedCtrlRaw()".
	#-- Please also notice the comments in that one.
	#-------------------------------------------------------------------------------------
	# Overrides "LaunchpadPro" method
	def LedCtrlXY( self, x, y, red, green, blue = None ):
		x = min( x, 8 )
		x = max( x, 0 )
		y = min( y, 8 )
		y = max( y, 0 )

		# top row (round buttons)
		if y == 0:
			led = 104 + x
		else:
			# swap y
			led = 91-(10*y) + x
		
		self.LedCtrlRaw( led, red, green, blue )



########################################################################################
########################################################################################
########################################################################################
def main():

	# THIS SHOULD ALL BE REWRITTEN...

	LP = Launchpad()

	print("--------------------------------------------------")
	LP.ListAll()
	
	# Check if there's a Pro attached.
	# If yes, just loop in here and never return...
	if LP.Check( 0, "Pro" ) or LP.Check( 0, "MK2" ):
		# lol :-)
		if LP.Check( 0, "Pro" ):
			print("--------------------------------------------------")
			print("Launchpad Pro found")
			print(">>> Make sure the device is in 'LIVE' mode!")
			print(">>> Push 'Setup' + top left matrix button.")
			lp = LaunchpadPro()
			lp.Open(0,"Pro")
		else:
			print("--------------------------------------------------")
			print("Launchpad Mk2 found")
			lp = LaunchpadMk2()
			lp.Open(0,"MK2")
		
		lp.LedCtrlString( '*burp*', 63, 0, 63, direction = -1, waitms = 50 )
		
		color = 0
		led = 0
		while( True ):
			lp.LedCtrlRawByCode( led, color )
			color+=1
			led+=1
			if color > 128:
				color = 0
			if led > 111:
				led = 1
			

	print("--------------------------------------------------")
	
	# "Classic" demo code ahead...
	if LP.Check() == False:
		print("No standard Launchpad found.")
		return

	print("Launchpad Classic found")

	# open the first "Classic" Launchpad
	LP.Open()


	# the latter of these two messages might not finish (MIDI buffer too large,
	# MIDI speed too low...)
	print("HELLO")
	LP.LedCtrlString( 'HELLO', 3, 0, direction = 0 ) # display HELLO in red
	print("USER")
	LP.LedCtrlString( 'USER', 0, 3, direction = -1 ) # scroll USER in green, from right to left
	
	# try to give it some extra time:
	# TESTING S/MINI
#	time.wait( 5000 )

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
	print("---\nFast update via color list.")
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


