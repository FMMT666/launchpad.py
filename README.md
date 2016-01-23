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
## STATUS 2016/01/22:

What's hot, what's not?

    Launchpad Mk1   - class "Launchpad()"     all features; LEDs and buttons
    Launchpad/S     - class "Launchpad()"     all features; LEDs and buttons
    Launchpad Mini  - class "Launchpad()"     all features; LEDs and buttons

    Launchpad Mk2   - class "LaunchpadMk2()"  alpha;        LEDs

    Launchpad Pro   - class "LaunchpadPro()"  in work;      LEDs


---
## NEWS

### CHANGES 2016/01/XX:

    - Support for Launchpad Pro now built in (only a few functions, so far).
      Please notice the new class for the Pro:
        lp_pro = LaunchpadPro()
      Except for a few, low level functions (e.g. "LedCtrlRaw()"), this and
      probably all future classes will remain compatible to the good, old
      "Classic" Launchpad (MK1).
    - added method Check(); Checks whether a device is attached.
    - added demo code for Pro (including automatic device recognition)
    - added Pro RGB LED control
    - added Pro X/Y LED control for RGB and color code mode
    - added Pro character display incl. left/right shift
    - added Pro string scrolling
    - Support for Launchpad Mk2 now built in
      Please notice the new class for the Mk2:
        lp_pro = LaunchpadMk2()
    - classes for "Pro" and "Mk2" now with default names for Open() and Check();
    - "Pro" now automatically put in "Ableton Live mode" after opening it.
      No need to push "Setup - Live" button anymore.


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
## Upcoming attractions, notes and thoughts

  - missing "Pro" functions, buttons, etc...
  - missing "Mk2" functions, check compatibility
  - maybe "Mk2" should be the base class for the "Pro" and not the other way round?
  - device search string should be case insensitive
  - better event system
  - custom bitmaps and graphics
  - better custom font support
  - Why the **** didn't I use [r,g,b] lists for colors, instead single args??? (*sigh*)
  - background color in char and string methods
  - string scroll: screen update bug if rightmost column is filled (not deleted)
  - ...


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
  - Launchpad Mk2

Notice that Novation now (1/2016) sells an RGB Launchpad under the same
name it once shipped the first red/green LED with!


---
## Notes (from the source)

### For Launchpad Mk1 users (the original "Classic" Launchpad):

      USE CLASS "Launchpad":
      
        lp = launchpad.Launchpad()

### For Launchpad Pro users

      USE CLASS "LaunchpadPro":
      
        lp = launchpad.LaunchpadPro()

      MAKE SURE THE LAUNCHPAD PRO IS IN LIVE MODE!
      To enter live mode, hold the SETUP bottom on the top left and
      push the top left matrix button ('green' in setup-mode ).
      
      IT WON'T WORK IN OTHER MODES (Note, Fader, Drums or Programming).

      That will soon be automated...

### For Launchpad Mk2 users

      USE CLASS "LaunchpadMk2":
      
        lp = launchpad.LaunchpadMk2()

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
## Common Launchpad Mk1 ("Classic") class methods overview (valid for all devices)

### Device control functions

    Open( [name], [number] )
    Close()
    Reset()


### Utility functions

    ListAll()
    
    
---
## Launchpad Mk1 "Classic" class methods overview (valid for green/red LED devices)

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
## Launchpad "Mk2" and "Pro" class methods overview (valid for RGB LED devices)

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

### Color codes

All RGB Launchpads have a 128 color palette built-in.  
Controlling LEDs with colors from the palette is about three times faster than
using the, indeed much more comfortable, RGB notation.

![RGB color palette](/images/lppro_colorcodes.png)

---
## Detailed description of common Launchpad methods

### Open( [number], [name] )

    Opens the a Launchpad and initializes it.  
    Please notice that some devices have up to six MIDI entries!.
    A dump by ListAll(), with a "Pro", a MK1 "Mini" and a "MK2" might look like:
    
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
        ('ALSA', 'Launchpad MK2 MIDI 1', 0, 1, 0)
        ('ALSA', 'Launchpad MK2 MIDI 1', 1, 0, 0)

    You'll only need to count the entries if you have two or more identical Launchpads attached.
    
      PARAMS: <number> OPTIONAL, number of Launchpad to open.
                       1st device = 0, 2nd device = 1, ...
                       Defaults to 0, the 1st device, if not given.
              <name>   OPTIONAL, only consider devices whose names contain
                       the string <name>. The default names for the classes are:
                         Launchpad()     -> "Launchpad"
                         LaunchpadMk2()  -> "MK2"
                         LaunchpadPro()  -> "Pro"
                       It is sufficient to search for a part of the string, e.g.
                       "chpad S" will find a device named "Launchpad S" or even
                       "Novation Launchpad S"

      RETURN: True     success
              False    error

    Notice that the default name for the class Launchpad(), the "Mk1" or "Classic" Launchpads,
    will also react to an attached "Pro" or "Mk2" model. In that case, it's required to either
    enter the complete name (as shown by "ListAll()").


      EXAMPLES:
              # Open the first device attached:
              lp.Open()
              
              # Open the 2nd Launchpad:
              lp.Open( 1 )
              
              # Open the 3rd Launchpad Mini:
              lp.Open( 2, "Launchpad Mini")
              
              # alternative:
              lp.Open( name = "Launchpad Mini", number = 0)
              
              # open the 1st "Mk2"
              lp = launchpad.LaunchpadMk2()  # notice the "Mk2" class!
              lp.Open()                      # equals Open( 0, "MK2" )
              
              # open the 1st "Pro"
              lp = launchpad.LaunchpadPro()  # notice the "Pro" class!
              lp.Open()                      # equals Open( 0, "Pro" )


### Check( [number], [name] )

    Checks if a device is attached.
    Uses exactly the same notation as Open(), but only returns True or False,
    without opening anything.
    
    Like Open(), this method uses different default names for the different classes:
      Launchpad()     -> "Launchpad"
      LaunchpadMk2()  -> "MK2"
      LaunchpadPro()  -> "Pro"
      
    Notice that it's absolutely safe to query for an "Pro" or "Mk2" from all classes, e.g.:
    
      lp = lauchpad.Launchpad()        # Launchpad "Mk1" or "Classic" class
      if lp.Check( 0, "Pro" ):         # check for "Pro"
		lp = launchpad.LaunchpadPro()  # "reload" the new class for the "Pro"
		lp.Open()                      # equals lp.Open( 0, "Pro" )
      
    
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
## Detailed description of Launchpad Mk1 "Classic" only methods


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

    Sends a list of consecutive, special color values to the Launchpad.
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

      PARAMS: <allLeds> A list of up to 80 Launchpad color codes.
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
    <offsy> does not have yet any function.
    
    It is highly recommended to use <offsx> and <offsy> as
    named parameters, for compatible code with the RGB Launchpads, e.g.:
    
      lp.LedCtrlChar( 'a', 3, 2, offsx = xvar )

      PARAMS: <char>   one field string to display; e.g.: 'A'
              <red>    red   LED intensity 0..3
              <green>  green LED intensity 0..3
              <offsx>  x offset of the character on the main, 8x8 matrix (-8..8)
                       Negative is left and positive right.
              <offsy>  no function
      RETURN:

      EXAMPLES:
              # scroll a red 'A' from left to right
              for x in range( -8, 9 ):
			    lp.LedCtrlChar( 'A', 3, 0, offsx = x )
			    time.wait( 100 )
		

### LedCtrlString( string, red, green, direction = 0, waitms = 150 )

    Scrolls <string> across the Launchpad's main, 8x8 matrix.
    <red/green> specify the color and intensity (0..3 each).
    <direction> determines the direction of scrolling.
    Dirty hack: <waitms>, by default 150, delays the scrolling speed.
    
    For future compatibility, it is highly recommended to use
    <direction> and <waitms> as a named arguments, e.g.:
    
      lp.LedCtrlString( "Hello", 3,1, direction = -1, waitms = 100 )


      PARAMS: <string>     a string to display; e.g.: 'Hello'
              <red>        red   LED intensity 0..3
              <green>      green LED intensity 0..3
              <direction> -1 -> scroll right to left
                           0 -> do not scroll, just show the character
                           1 -> scroll left to right
              <waitms>     OPTIONAL: delay for scrolling speed, default 150
      RETURN:


### ButtonChanged()

    Returns True if a button event occured. False otherwise.

      PARAMS:
      RETURN: True/False
		

### ButtonStateRaw()

    Returns the state of the last occured button event in the queue in RAW mode.

      PARAMS:
      RETURN: [ <button>, <True/False> ] A list with two fields:
              <button> is the RAW button number, the second field determines
              if the button was pressed <True> or released <False>.


### ButtonStateXY()

    Returns the state of the last occured button event in the queue in X/Y mode.

      PARAMS:
      RETURN: [ <x>, <y>, <True/False> ] A list with three fields:
              <x> is the x coordinate of the button, <y>, guess what, the
              y coordinate. The third field reveals if the button was pressed
              <True> or released <False>.


---
## Detailed description of Launchpad "Pro" or "Mk2" only methods

### LedSetMode( mode ) *>>> PRO ONLY <<<*

    Sets the Launchpad's mode.
    For proper operation with launchpad.py, the "Pro" must be set to "Ableton Live" mode.
    There is no need to call this method as it is automatically executed within Open().

      PARAMS: <mode>   0 selects "Ableton Live mode" (what we need)
                       1 selects "Standalone mode"   (power-up default)
      RETURN:


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
    
    Notice that the "Pro" and "Mk2" have different LED number layouts.
    Please see tables, somewhere below.

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
    
    For "Pro" only:
      By default, if <mode> is omitted, the origin of the x axis is the left side
      of the 8x8 matrix, like in "Classic" mode (those devices had no round buttons
      on the left).
      If <mode> is set to "pro" (string), x=0 will light up the round buttons on the
      left side. Please also see the table for X/Y modes somewhere at the end of this
      document.

    This method uses system-exclusive MIDI messages, which require 10 bytes to
    be sent for each message. For a faster version, hence less comfortable version,
    see LedCtrlXYByCode() below.
    
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


### LedCtrlChar( char, red, green, [blue], offsx = 0, offsy = 0 )

    Sends character <char> in colors <red/green/blue> (0..63 each) and
    lateral offset <offsx> (-8..8) to the Launchpad.
    <offsy> does not have yet any function.
    
    It is highly recommended to use <offsx> and <offsy> as
    named parameters, for compatible code with the RGB Launchpads, e.g.:
    
      lp.LedCtrlChar( 'a', 3, 2, offsx = xvar )
      
    If <blue> is ommited, this methods runs in "Classic" compatibility
    mode and multiplies the <red> and <green> intensity values with 21, to
    adapt the old 0..3 range to the new 0..63 one of the "Pro" mode.
    That way, it is compatible to old, existing "Classic" code.

      PARAMS: <char>   one field string to display; e.g.: 'A'
              <red>    red   LED intensity 0..63 (or 0..3 in "Classic" mode)
              <green>  green LED intensity 0..63 (or 0..3 in "Classic" mode)
              <blue>   blue  LED intensity 0..63 (omit  for  "Classic" mode)
              <offsx>  x offset of the character on the main, 8x8 matrix (-8..8)
                       Negative is left and positive right.
              <offsy>  no function
      RETURN:

      EXAMPLES:
              # scroll a purple 'A' from left to right
              for x in range( -8, 9 ):
			    lp.LedCtrlChar( 'A', 63, 0, 63, offsx = x )
			    time.wait( 100 )


### LedCtrlString( string, red, green, blue = None, direction = 0, waitms = 150 )

    Scrolls a string <str> across the Launchpad's main, 8x8 matrix.
    <red/green/blue> specify the color and intensity (0..63 each).
    <direction> determines the direction of scrolling.
    Dirty hack: <waitms>, by default 150, delays the scrolling speed.
    
    If <blue> is omitted, "Classic" compatibility mode is turned on and the old
    0..3 <red/green> intensity values are strechted to 0..63.
    
    For future compatibility, it is highly recommended to use
    <direction> and <waitms> as a named arguments, e.g.:
    
      lp.LedCtrlString( "Hello", 3,1, direction = -1, waitms = 100 )


      PARAMS: <string>     a string to display; e.g.: 'Hello'
              <red>        red   LED intensity 0..63 (or 0..3 in "Classic" mode)
              <green>      green LED intensity 0..63 (or 0..3 in "Classic" mode)
              <blue>       green LED intensity 0..63 (omit  for  "Classic" mode)
              <direction> -1 -> scroll right to left
                           0 -> do not scroll, just show the character
                           1 -> scroll left to right
              <waitms>     OPTIONAL: delay for scrolling speed, default 150
      RETURN:


### LedAllOn( [colorcode] )

    Quickly sets all LEDs to the color code given by <colorcode>.
    If <colorcode> is omitted, 'white' is used.

      PARAMS: <colorcode>   OPTIONAL, a number from 0..127
      RETURN:


---
## Button and LED codes, Launchpad Mk1 "Classic" (red/green LEDs)

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
    |0/0|1/0|   |   |   |   |   |   |         0
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
## Button and LED codes, Launchpad "Mk2" (RGB LEDs)

### RAW mode

    +---+---+---+---+---+---+---+---+ 
    |104|   |106|   |   |   |   |111|
    +---+---+---+---+---+---+---+---+ 
    
    +---+---+---+---+---+---+---+---+  +---+
    | 81|   |   |   |   |   |   |   |  | 89|
    +---+---+---+---+---+---+---+---+  +---+
    | 71|   |   |   |   |   |   |   |  | 79|
    +---+---+---+---+---+---+---+---+  +---+
    | 61|   |   |   |   |   | 67|   |  | 69|
    +---+---+---+---+---+---+---+---+  +---+
    | 51|   |   |   |   |   |   |   |  | 59|
    +---+---+---+---+---+---+---+---+  +---+
    | 41|   |   |   |   |   |   |   |  | 49|
    +---+---+---+---+---+---+---+---+  +---+
    | 31|   |   |   |   |   |   |   |  | 39|
    +---+---+---+---+---+---+---+---+  +---+
    | 21|   | 23|   |   |   |   |   |  | 29|
    +---+---+---+---+---+---+---+---+  +---+
    | 11|   |   |   |   |   |   |   |  | 19|
    +---+---+---+---+---+---+---+---+  +---+
    

### X/Y mode

      0   1   2   3   4   5   6   7      8   
    +---+---+---+---+---+---+---+---+ 
    |0/0|   |2/0|   |   |   |   |   |         0
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
