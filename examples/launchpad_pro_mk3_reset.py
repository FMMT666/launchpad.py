#!/usr/bin/env python
#
# Resets the Pro Mk3 (into Live mode)
# 
#
# FMMT666(ASkr) 7/2013..8/2020
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


def main():

	if launchpad.LaunchpadProMk3().Check( 0 ):
		lp = launchpad.LaunchpadProMk3()
		if lp.Open( 0 ):
			print("Launchpad Pro Mk3 found")
			lp.Close()
	else:
		print("Meh, did not find a Launchpad Pro Mk3")


	
if __name__ == '__main__':
	main()

