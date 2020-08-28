#!/usr/bin/env python
#
# Show MIDI events for a device.
#
# Some restrictions apply:
#  - This will only work if a device has an in- AND output, because the Launchpad
#    classes always open both directions.
#  - This will not work for devices which require an initialization, e.g. ProMk3, etc ...
#  - Picking the wrong device might result in no output.
#  - Quit with CTRL-C :)
#
#
# FMMT666(ASkr) 7/2013..8/2020
# www.askrprojects.net

import sys

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading launchpad.py")



def cmdInput( prompt ):
	if sys.version_info.major == 2:
		inName = str(raw_input( prompt ))
	elif sys.version_info.major == 3:
		inName = str(input( prompt ))
	else:
		print('Meh, please consider running this with either Python 2 or 3')
		sys.exit(-1)

	return inName


def main():

	lp = launchpad.Launchpad()

	print("===\nAvailable MIDI devices:")
	lp.ListAll(  )
	print("===")

	print("Enter a part of the device name, that shall be monitored.")
	print("The string needs to cover the in- and output channels of a device!")
	print("Otherwise, opening only one input or one output channel will result in an error.")
	print("The search string is case-insensitive.")

	inName = cmdInput( "  search string:" )

	while True:
		print("===")
		lp.ListAll( searchString = inName )
		print("===")
		
		inOk = cmdInput( "  ENTER to continue or new search string:" )
		if inOk == '':
			break
		else:
			inName = inOk

	try:
		lp.Open( 0, inName )
	except:
		print("error opening this device")
		sys.exit(-1)

	print("===")
	print("Now hit the keys, turn the knobs or push the buttons:")

	# DEBUG STUFF
	# lp.midi.RawWriteSysEx( [ 0, 32, 41, 2, 14, 14, 1 ] )  # Pro Mk3 programmer's mode ON
	# lp.midi.RawWriteSysEx( [ 0, 32, 41, 2, 14, 14, 0 ] )  # Pro Mk3 programmer's mode OFF (Live mode)

	while(True):
		events = lp.EventRaw()
		if events != []:
			print( events )

	
if __name__ == '__main__':
	main()
