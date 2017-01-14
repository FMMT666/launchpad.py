
import rtmidi2


print(rtmidi2.get_in_ports())
print(rtmidi2.get_out_ports())




midi_out = rtmidi2.MidiOut()
midi_in = rtmidi2.MidiIn()


# open the first available port
midi_out.open_port(0) 

# send C3 with vel. 100 on channel 1
midi_out.send_noteon(0, 48, 100)


midi_in.open_port(0)

while True:
	# will block until a message is available
	message = midi_in.get_message()  

	if message is not None:
		print( message )
		
		midi_out.akki()

		# live mode
		midi_out.send_sysex( 240, 0, 32, 41, 2, 16, 33, 0  )
		
		midi_out.send_sysex( 240, 0, 32, 41, 2, 16, 11, message[1], 63, 0, 0 )
#		midi_out.send_message( 240, 0, 32, 41, 2, 16, 11, 50, 63, 0, 0 )

		



