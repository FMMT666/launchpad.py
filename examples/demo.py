import launchpad_py

def main():

	# THIS SHOULD ALL BE REWRITTEN...

	LP = launchpad_py.Launchpad()

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
	LP.LedCtrlString( '*', 0, 3, direction = -1 ) # erase test
	LP.LedCtrlString( '*', 0, 3, direction =  1 ) # erase test
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

