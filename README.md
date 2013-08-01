launchpad.py
============

A Novation Launchpad control suite.

    http://www.askrproject.net

---
## Launchpad class methods overview

### Device control functions

    Open()
    Close()
    Reset()


### Utility functions

    ListAll()

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
## Detailed description

### Open()

    Opens the first available Launchpad and initializes it.

      PARAMS: -
      RETURN: -

### Close()

    Not required and not needed. No function in there (yet).

      PARAMS:
      RETURN:

### ListAll()

    Debug function.
    Can be called any time and does not even require Open().
    Prints a list of all detected MIDI equipment and addresses.

      PARAMS:
      RETURN:

### Reset()

    Resets the Launchpad and (quickly) turns off al LEDs.

      PARAMS:
      RETURN:

### LedGetColor( red, green )

    Returns a the special Launchpad color coding format, calculated
      from a red and green intensity value.

      PARAMS: <red>    red   LED intensity 0..3
              <green>  green LED intensity 0..3
      RETURN: number; Launchpad color code

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
## Button and LED codes

### RAW mode

    +---+---+---+---+---+---+---+---+ 
    |200|201|202|203|204|205|206|207| < AUTO
    +---+---+---+---+---+---+---+---+   Or u

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

Have fun  
FMMT666(ASkr)  

