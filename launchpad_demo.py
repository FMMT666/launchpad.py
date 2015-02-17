
#
# Quick usage of "launchpad.py"
# For more info, see the "launchpad.py" file itself...
#
# ASkr 7/2013
# www.askrprojects.net
#


import random
import launchpad
from pygame import time



def main():

	LP = launchpad.Launchpad()  # creates a Launchpad instance (first Launchpad found)
	LP.Open()                   # start it


	LP.LedCtrlString( 'HELLO ', 0, 3, -1 )  # scroll "HELLO" from right to left

	# random output until button "arm" (lower right) is pressed
	print("---\nRandom madness. Stop by hitting the ARM button (lower right)")
	print("Remember the PyGame MIDI bug:")
	print("If the ARM button has no effect, hit an automap button (top row)")
	print("and try again...")

	while 1:
		LP.LedCtrlRaw( random.randint(0,127), random.randint(0,3), random.randint(0,3) )
		
		# some extra time to give the button events a chance to come through...
		time.wait( 5 )
		
		but = LP.ButtonStateRaw()
		if but != []:
			print( but )
			if but[0] == 120:
				break


	LP.Reset() # turn all LEDs off
	LP.Close() # close the Launchpad

	
if __name__ == '__main__':
	main()

