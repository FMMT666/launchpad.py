
#
# Quick demo of using multiple Launchpads with "launchpad.py"
#
# ASkr 2/2015
# www.askrprojects.net
#


import random
import launchpad
from pygame import time


def main():

	# create two Launchpad instances
	lp1 = launchpad.Launchpad()
	lp2 = launchpad.Launchpad()

	# open them
	lp1.Open(0)
	lp2.Open(1)


	while 1:
	
		# random light show
		lp1.LedCtrlRaw( random.randint(0,127), random.randint(0,3), random.randint(0,3) )
		lp2.LedCtrlRaw( random.randint(0,127), random.randint(0,3), random.randint(0,3) )
		
		# some extra time to give the button events a chance to come through...
		time.wait( 5 )

		# wait until the arm button (lower right) is hit
		but = lp1.ButtonStateRaw()
		if but != []:
			print( but )
			if but[0] == 120:
				break


	# No exit code in here yet :(
	# The PyGame MIDI implementation has bugs, so a proper
	# shutdown would not make any sense. Usually, that "bad pointer"
	# error always appears...


	
if __name__ == '__main__':
	main()

