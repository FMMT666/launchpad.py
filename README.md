launchpad.py
============

A [Novation Launchpad][1] control suite for [Python][2].

If you ever dreamed of using your Launchpad for completely other stuff than music: Welcome !-)

Compatible with most [tm] single board computers.

Watch a 6s video [here][7].  
Or take a look at [that one][8].  
What about the brand new Launchpad Pro support? [Right][9]!

Older Launchpads might be documented [here][10].

---
## NEWS

### CHANGES 2016/01/17:

    - Support for Launchpad Pro now build in (only a few functions, so far).
      Please notice the new class for the Pro:
        lp_pro = LaunchpadPro()
    - added method Check(); Checks whether a device is attached.
    - added demo code for Pro (including automatic device recognition)
    - added RGB LED control
    - added X/Y LED control for RGB and color code mode

### CHANGES 2016/01/10:

    - The current version does not work with Mac OS X.
      Regarding that, as well as the fact that PyGame somehow reached its
      end of life, I am currently looking for other Midi libraries or implementations.
    - I bought a Launchpad Pro. Time to implement this, although I am not sure
      what will come first, building a new Midi system or implementing the Pro.

### CHANGES 2015/02/21:

    - Support for multiple Launchpads now finally built in. Use 'em all:
        lp1 = launchpad.Launchpad()
        lp2 = launchpad.Launchpad()
        lp1.Open(0)
        lp2.Open(1)

### CHANGES 2015/02/18:
  
    - Added option to select a Launchpad if more than one is attached.
      Also supports search for a device string, e.g. "Mini".
    - Added optional parameters <number> and <name> to Open()


---
## Package
The "distribution" consists of:

  - launchpad.py
  - launchpad_charset.py
  - launchpad_demo.py

You only need the first two files.
"launchpad.py" as well as "launchpad_demo.py" contain demo code.


---
## License

[CC BY 4.0, Attribution 4.0 International][6]

You are free to:

Share — copy and redistribute the material in any medium or format  
Adapt — remix, transform, and build upon the material for any purpose, even commercially.
  
The licensor cannot revoke these freedoms as long as you follow the license terms.


---
## Requirements

  - [Python][2]
  - [Pygame][3] v1.9.1

Launchpad.py was tested under

  - Linux, 32 bit, 64 bit
  - Windows XP, 32 bit
  - Windows 7, 32 bit, 64 bit
  - [Raspberry-Pi 1/2][4] (Look out for my [Minecraft][5] controller here: [www.askrprojects.net][6])
  - Beagle Bone (Black)
  - Banana Pi (Pro/M2/R1)
  - pcDuino V3
  - ...

It does _not_ (yet) work with

  - Mac OS X
  
because PyGame's Mac implementation was built without any Midi functionality.


Supported and tested red/green LED Launchpad devices, here referred  to as "Classic":

  - Launchpad (the original, old "MK1")
  - Launchpad S
  - Launchpad Mini (MK1)
  
Supported and tested full RGB Launchpad devices:
  
  - Launchpad Pro

Notice that Novation now (1/2016) sells an RGB Launchpad under the same
name it once shipped the first red/green LED with!


---
## Notes (from the source)

### For Launchpad Pro users

      MAKE SURE THE LAUNCHPAD PRO IS IN LIVE MODE!
      To enter live mode, hold the SETUP bottom on the top left and
      push the top left matrix button ('green' in setup-mode ).
      
      IT WON'T WORK IN OTHER MODES (Note, Fader, Drums or Programming).

### For Windows users

      MIDI implementation in PyGame 1.9.2+ is broken and running this will
      bring up an 'insufficient memory' error ( pygame.midi.Input() ).

      SOLUTION: use v1.9.1

### For Linux and especially Raspberry-Pi users:

      Due to some bugs in PyGame's MIDI implementation, the buttons of the Launchpad
      won't work after you restarted a program (LEDs are not affected).

      WORKAROUND #2: Simply hit one of the AUTOMAP keys (the topmost 8 buttons).
                     For whatever reason, this makes the MIDI button events
                     appearing again...

      WORKAROUND #1: Pull the Launchpad's plug out and restart... (annoying).


---
## Common Launchpad class methods overview (valid for all devices)

### Device control functions

    Open( [name], [number] )
    Close()
    Reset()


### Utility functions

    ListAll()
    
    
---
## Launchpad "Classic" class methods overview (valid for green/red LED devices)

### LED functions

    LedGetColor( red, green )
    LedCtrlRaw( number, red, green )
    LedCtrlXY( x, y, red, green )
    LedCtrlRawRapid( allLeds )
    LedCtrlAutomap( number, red, green )
    LedAllOn()
    LedCtrlChar( char, red, green, offsx = 0, offsy = 0 )
    LedCtrlString( str, red, green, dir = 0 )

### Button functions

    ButtonChanged()
    ButtonStateRaw()
    ButtonStateXY()


---
## Launchpad "Pro" class methods overview (valid for RGB LED devices)

### LED functions

    LedGetColorByName( name )
    LedCtrlRaw( number, red, gree, [blue] )
    LedCtrlRawByCode( number, [colorcode] )
    LedCtrlXY( x, y, red, green, [blue] )
    LedCtrlXYByCode( x, y, colorcode )
    LedAllOn( [colorcode] )
    
    work in progress...

### Button functions

    work in progress...


---
## Detailed description of common Launchpad methods

### Open( [number], [name] )

    Opens the a Launchpad and initializes it.  
    Please notice that some devices have up to six MIDI entries!.
    A dump by ListAll(), with a "Pro" and a MK1 "Mini" might look like:
    
        ('ALSA', 'Midi Through Port-0', 0, 1, 0)
        ('ALSA', 'Midi Through Port-0', 1, 0, 0)
        ('ALSA', 'Launchpad Pro MIDI 1', 0, 1, 1)
        ('ALSA', 'Launchpad Pro MIDI 1', 1, 0, 1)
        ('ALSA', 'Launchpad Pro MIDI 2', 0, 1, 0)
        ('ALSA', 'Launchpad Pro MIDI 2', 1, 0, 0)
        ('ALSA', 'Launchpad Pro MIDI 3', 0, 1, 0)
        ('ALSA', 'Launchpad Pro MIDI 3', 1, 0, 0)
        ('ALSA', 'Launchpad Mini MIDI 1', 0, 1, 0)
        ('ALSA', 'Launchpad Mini MIDI 1', 1, 0, 0)
    
    You'll (usually) only need the first entry of each device.
    
    
      PARAMS: <number> OPTIONAL, number of Launchpad to open.
                       1st device = 0, 2nd device = 1, ...
                       Defaults to 0, the 1st device, if not given.
              <name>   OPTIONAL, only consider devices whose names contain
                       the string <name>. Defaults to "Launchpad".
                       It is sufficient to search for a part of the string, e.g.
                       "chpad S" will find a device named "Launchpad S" or even
                       "Novation Launchpad S"

      RETURN: True     success
              False    error

      EXAMPLES:
              # Open the first device attached:
              lp.Open()
              
              # Open the 2nd Launchpad:
              lp.Open( 1 )
              
              # Open the 3rd Launchpad Mini:
              lp.Open( 2, "Launchpad Mini")
              
              # alternative:
              lp.Open( name = "Launchpad Mini", number = 0)


### Check( [number], [name] )

    Checks if a device is attached.
    Uses exactly the same notation as Open(), but only returns True or False,
    without opening anything.
    
      PARAMS: see Open()
      
      RETURN: True     device exists
              False    device does not exist

              

### Close()

    Bug in PyGame. Don't call it (yet)...

      PARAMS:
      RETURN:


### ListAll()

    Debug function.
    Can be called any time and does not even require Open().
    Prints a list of all detected MIDI devices and addresses.

      PARAMS:
      RETURN:


---
## Detailed description of Launchpad "Classic" only methods


### Reset()

    Resets the Launchpad and (quickly) turns off all LEDs.

      PARAMS:
      RETURN:


### LedGetColor( red, green )

    Returns a the special Launchpad color coding format, calculated
    from a red and green intensity value.

      PARAMS: <red>    red   LED intensity 0..3
              <green>  green LED intensity 0..3
      RETURN: number   Launchpad color code


### LedCtrlRaw( number, red, green )

    Controls an LED via its number (see table somewhere below)

      PARAMS: <number> number of the LED to control
              <red>    red   LED intensity 0..3
              <green>  green LED intensity 0..3
      RETURN:


### LedCtrlXY( x, y, red, green )

    Controls an LED via its coordinates.

      PARAMS: <x>      x coordinate of the LED to control
              <y>      y coordinate of the LED to control
              <red>    red   LED intensity 0..3
              <green>  green LED intensity 0..3
      RETURN:


### LedCtrlRawRapid( allLeds )

    Sends a table of consecutive, special color values to the Launchpad.
    Requires (less than) half of the commands to update all buttons:
    [ LED1, LED2, LED3, ... LED80 ]
    First, the 8x8 matrix is updated, left to right, top to bottom.
    Afterwards, the algorithm continues with the rightmost buttons and
    the top "automap" buttons.

    LEDn color format: 00gg00rr <- 2 bits green, 2 bits red (0..3)
    Function LedGetColor() will do the coding for you...

    Notice that the amount of LEDs needs to be even.
    If an odd number of values is sent, the next, following LED is
    turned off!

      PARAMS: <allLeds> A table of up to 80 Launchpad color codes.
      RETURN:


### LedCtrlAutomap( number, red, green )

    Control one of the "automap" buttons (top row).
    Legacy function, provided for compatibility.

      PARAMS: <number> number of the LED to control
              <red>    red   LED intensity 0..3
              <green>  green LED intensity 0..3

### LedAllOn()

    Turns on all LEDs.

      PARAMS: 
      RETURN:

		
### LedCtrlChar( char, red, green, offsx = 0, offsy = 0 )

    Sends character <char> in colors <red/green> (0..3 each) and
    lateral offset <offsx> (-8..8) to the Launchpad.
    <offsy> does not have yet any function

      PARAMS: <char>   one field string to display; e.g.: 'A'
              <red>    red   LED intensity 0..3
              <green>  green LED intensity 0..3
              <offsx>  x offset of the character on the main, 8x8 matrix (-8..8)
                       Negative is left and positive right.
              <offsy>  no function
      RETURN:


### LedCtrlString( str, red, green, dir = 0 )

    Scrolls a string <str> across the Launchpad's main, 8x8 matrix.
    Red and green specify the color and intensity (0..3 each).
    <dir> determines the direction of scrolling.


      PARAMS: <str>    a string to display; e.g.: 'Hello'
              <red>    red   LED intensity 0..3
              <green>  green LED intensity 0..3
              <dir>    -1 -> scroll right to left
                        0 -> do not scroll, just show the character
                        1 -> scroll left to right
      RETURN:


### ButtonChanged()

    Returns True if a button event occured. False otherwise.

      PARAMS:
      RETURN: True/False
		

### ButtonStateRaw()

    Returns the state of the last occured button event in the queue in RAW mode.

      PARAMS:
      RETURN: [ <button>, <True/False> ] A table with two fields:
              <button> is the RAW button number, the second field determines
              if the button was pressed <True> or released <False>.


### ButtonStateXY()

    Returns the state of the last occured button event in the queue in X/Y mode.

      PARAMS:
      RETURN: [ <x>, <y>, <True/False> ] A table with three fields:
              <x> is the x coordinate of the button, <y>, guess what, the
              y coordinate. The third field reveals if the button was pressed
              <True> or released <False>.


---
## Detailed description of Launchpad "Pro" only methods

### LedGetColorByName( name )

    WORK IN PROGRESS! ONLY A FEW COLORS, SO FAR!

    Returns a color in the special Launchpad Pro color code format, derived
    from a color name, in the string <name>.
    [...]

      PARAMS: <name>   a name of a color in lower caps, "red", "green"...
      RETURN: number   Launchpad Pro color code

      EXAMPLES:
              colorRed = LP.LedGetColorByName( "red" )
    
    Supported, so far:
      off, black, white, red, green


### LedCtrlRaw( number, red, green, [blue] )

    Controls an LED via its number and red, green and blue intensity values.
    
    This method uses system-exclusive MIDI messages, which require 10 bytes to
    be sent for each message. For a faster version, hence less comfortable version,
    see LedCtrlRawByCode() below (though even sending 10 bytes is pretty fast on the Pro).
    
    If <blue> is omitted, this method runs in "Classic" compatibility mode, which only
    had red/green LEDs and intensities ranging from 0..3. In that mode, the input
    arguments are multiplied by 21, to map 0..3 to 0..63.

      PARAMS: <number>    number of the LED to control
              <red>       a number from 0..63
              <green>     a number from 0..63
              <blue>      OPTIONAL, a number from 0..63
      RETURN:


### LedCtrlRawByCode( number, [colorcode] )

    Controls an LED via its number and colorcode.
    If <colorcode> is omitted, 'white' is used.
    This is about three times faster than the comfortable RGB method LedCtrlRaw().

      PARAMS: <number>     number of the LED to control
              <colorcode>  OPTIONAL, a number from 0..127
      RETURN:


### LedCtrlXY( x, y, red, green, [blue], [mode] )

    Controls an LED via its x/y coordinates and red, green or blue intensity values.
    An additional <mode> parameter determines the origin of the x-axis.
    
    If <blue> is omitted, this method operates in "Classic" compatibility mode.
    The classic Launchpad only had 2 bit intensity values (0..3). In compatibility
    mode, these values are now multiplied by 21, to extend the range to 0..63.
    That way, old, existing code, written for the classic Launchpads does not
    need to be changed.
    
    By default, if <mode> is omitted, the origin of the x axis is the left side of
    the 8x8 matrix, like in "Classic" mode (those devices had no round buttons on
    the left).
    If <mode> is set to "pro" (string), x=0 will light up the round buttons on the
    left side. Please also see the table for X/Y modes somewhere at the end of this
    document.

    This method uses system-exclusive MIDI messages, which require 10 bytes to
    be sent for each message. For a faster version, hence less comfortable version,
    see LedCtrlXYBaCode() below.
    
      PARAMS: <x>      x coordinate of the LED to control
              <y>      y coordinate of the LED to control
              <red>    red   LED intensity 0..63 (or 0..3 in "Classic" mode)
              <green>  green LED intensity 0..63 (or 0..3 in "Classic" mode)
              <blue>   blue  LED intensity 0..63 (omit  for  "Classic" mode)
      RETURN:


### LedCtrlXYByCode( x, y, colorcode, [mode] )

    Controls an LED via its x/y coordinates and a color from the color palette.
    
    Except for the color code, this function does the same as LedCtrlXY() does,
    but about 3 times faster.
    
      PARAMS: <x>          x coordinate of the LED to control
              <y>          y coordinate of the LED to control
              <colorcode>  a number from 0..127
      RETURN:


### LedAllOn( [colorcode] )

    Quickly sets all LEDs to the color code given by <colorcode>.
    If <colorcode> is omitted, 'white' is used.

      PARAMS: <colorcode>   OPTIONAL, a number from 0..127
      RETURN:


---
## Button and LED codes, Launchpad "Classic" (red/green LEDs)

### RAW mode

    +---+---+---+---+---+---+---+---+ 
    |200|201|202|203|204|205|206|207| < or 0..7 with LedCtrlAutomap()
    +---+---+---+---+---+---+---+---+   

    +---+---+---+---+---+---+---+---+  +---+
    |  0|...|   |   |   |   |   |  7|  |  8|
    +---+---+---+---+---+---+---+---+  +---+
    | 16|...|   |   |   |   |   | 23|  | 24|
    +---+---+---+---+---+---+---+---+  +---+
    | 32|...|   |   |   |   |   | 39|  | 40|
    +---+---+---+---+---+---+---+---+  +---+
    | 48|...|   |   |   |   |   | 55|  | 56|
    +---+---+---+---+---+---+---+---+  +---+
    | 64|...|   |   |   |   |   | 71|  | 72|
    +---+---+---+---+---+---+---+---+  +---+
    | 80|...|   |   |   |   |   | 87|  | 88|
    +---+---+---+---+---+---+---+---+  +---+
    | 96|...|   |   |   |   |   |103|  |104|
    +---+---+---+---+---+---+---+---+  +---+
    |112|...|   |   |   |   |   |119|  |120|
    +---+---+---+---+---+---+---+---+  +---+

### X/Y mode

      0   1   2   3   4   5   6   7      8   
    +---+---+---+---+---+---+---+---+ 
    |   |1/0|   |   |   |   |   |   |         0
    +---+---+---+---+---+---+---+---+ 

    +---+---+---+---+---+---+---+---+  +---+
    |0/1|   |   |   |   |   |   |   |  |   |  1
    +---+---+---+---+---+---+---+---+  +---+
    |   |   |   |   |   |   |   |   |  |   |  2
    +---+---+---+---+---+---+---+---+  +---+
    |   |   |   |   |   |5/3|   |   |  |   |  3
    +---+---+---+---+---+---+---+---+  +---+
    |   |   |   |   |   |   |   |   |  |   |  4
    +---+---+---+---+---+---+---+---+  +---+
    |   |   |   |   |   |   |   |   |  |   |  5
    +---+---+---+---+---+---+---+---+  +---+
    |   |   |   |   |4/6|   |   |   |  |   |  6
    +---+---+---+---+---+---+---+---+  +---+
    |   |   |   |   |   |   |   |   |  |   |  7
    +---+---+---+---+---+---+---+---+  +---+
    |   |   |   |   |   |   |   |   |  |8/8|  8
    +---+---+---+---+---+---+---+---+  +---+


---
## Button and LED codes, Launchpad "Pro" (RGB LEDs)

### RAW mode

           +---+---+---+---+---+---+---+---+ 
           | 91|   |   |   |   |   |   | 98|
           +---+---+---+---+---+---+---+---+ 
    
    +---+  +---+---+---+---+---+---+---+---+  +---+
    | 80|  | 81|   |   |   |   |   |   |   |  | 89|
    +---+  +---+---+---+---+---+---+---+---+  +---+
    | 70|  |   |   |   |   |   |   |   |   |  | 79|
    +---+  +---+---+---+---+---+---+---+---+  +---+
    | 60|  |   |   |   |   |   |   | 67|   |  | 69|
    +---+  +---+---+---+---+---+---+---+---+  +---+
    | 50|  |   |   |   |   |   |   |   |   |  | 59|
    +---+  +---+---+---+---+---+---+---+---+  +---+
    | 40|  |   |   |   |   |   |   |   |   |  | 49|
    +---+  +---+---+---+---+---+---+---+---+  +---+
    | 30|  |   |   |   |   |   |   |   |   |  | 39|
    +---+  +---+---+---+---+---+---+---+---+  +---+
    | 20|  |   |   | 23|   |   |   |   |   |  | 29|
    +---+  +---+---+---+---+---+---+---+---+  +---+
    | 10|  |   |   |   |   |   |   |   |   |  | 19|
    +---+  +---+---+---+---+---+---+---+---+  +---+
    
           +---+---+---+---+---+---+---+---+ 
           |  1|  2|   |   |   |   |   |  8|
           +---+---+---+---+---+---+---+---+ 

### X/Y "Classic" mode

      9      0   1   2   3   4   5   6   7      8   
           +---+---+---+---+---+---+---+---+ 
           |0/0|   |2/0|   |   |   |   |   |         0
           +---+---+---+---+---+---+---+---+ 
            
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |   |  |0/1|   |   |   |   |   |   |   |  |   |  1
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |9/2|  |   |   |   |   |   |   |   |   |  |   |  2
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |   |  |   |   |   |   |   |5/3|   |   |  |   |  3
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |   |  |   |   |   |   |   |   |   |   |  |   |  4
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |   |  |   |   |   |   |   |   |   |   |  |   |  5
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |   |  |   |   |   |   |4/6|   |   |   |  |   |  6
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |   |  |   |   |   |   |   |   |   |   |  |   |  7
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |9/8|  |   |   |   |   |   |   |   |   |  |8/8|  8
    +---+  +---+---+---+---+---+---+---+---+  +---+
          
           +---+---+---+---+---+---+---+---+ 
           |   |1/9|   |   |   |   |   |   |         9
           +---+---+---+---+---+---+---+---+ 

### X/Y "Pro" mode

      0      1   2   3   4   5   6   7   8      9
           +---+---+---+---+---+---+---+---+ 
           |1/0|   |3/0|   |   |   |   |   |         0
           +---+---+---+---+---+---+---+---+ 
            
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |   |  |1/1|   |   |   |   |   |   |   |  |   |  1
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |0/2|  |   |   |   |   |   |   |   |   |  |   |  2
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |   |  |   |   |   |   |   |6/3|   |   |  |   |  3
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |   |  |   |   |   |   |   |   |   |   |  |   |  4
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |   |  |   |   |   |   |   |   |   |   |  |   |  5
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |   |  |   |   |   |   |5/6|   |   |   |  |   |  6
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |   |  |   |   |   |   |   |   |   |   |  |   |  7
    +---+  +---+---+---+---+---+---+---+---+  +---+
    |0/8|  |   |   |   |   |   |   |   |   |  |9/8|  8
    +---+  +---+---+---+---+---+---+---+---+  +---+
          
           +---+---+---+---+---+---+---+---+ 
           |   |2/9|   |   |   |   |   |   |         9
           +---+---+---+---+---+---+---+---+ 







---
Have fun  
FMMT666(ASkr)  



[1]: https://global.novationmusic.com/launch/launchpad
[2]: http://www.python.org
[3]: http://www.pygame.org
[4]: http://www.raspberrypi.org
[5]: http://pi.minecraft.net/
[6]: http://www.askrproject.net
[7]: https://mtc.cdn.vine.co/r/videos/5B6AFA722E1181009294682988544_30ec8c83a82.1.5.18230528301682594589.mp4
[8]: https://mtc.cdn.vine.co/r/videos/B02C20F7301181005332596555776_3da8b2c29ec.1.5.3791810774169827111.mp4
[9]: https://mtc.cdn.vine.co/r/videos/EFB02602EF1300276501647966208_4cce4117438.5.1.10016548273760817556.mp4
[10]: https://novationmusic.de/launch/launchpad-mk1
