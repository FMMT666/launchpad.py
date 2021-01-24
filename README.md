launchpad.py
============

A [Novation Launchpad][1] (and [Midi Fighter][25]) control suite for [Python][2].

If you ever dreamed of using your Launchpad for completely other stuff than music: Welcome !-)

Compatible with most [tm] single board computers.

Watch a 6s video [here][7].  
Or take a look at [that one][8].  
What about the brand new Launchpad Pro support? [Right][9]!

Hey - and the Mac? Yep, that finally works too. [Look][12] \o/  

Upcoming attraction: [Launch Control XL][15].

Oh, don't let us forget the [Dicer][16].

Older Launchpads might be documented [here][10].

Did we mention [Python 3][18] yet?

First [Mk3][21] and [X][22] Launchpad code snippets running now (4/2020).

Now with full [Midi Fighter 64][23] support (8/2020).

Finally! Hehe, say hello to the [Mk3 Pro][24] (8/2020)  

---
## STATUS 2021/01/xx:

### Devices

    Launchpad Mk1      - class "Launchpad()"        LEDs and buttons
    Launchpad/S        - class "Launchpad()"        LEDs and buttons
    Launchpad Mini     - class "Launchpad()"        LEDs and buttons

    Launchpad Mk2      - class "LaunchpadMk2()"     LEDs and buttons

    Launchpad Pro      - class "LaunchpadPro()"     LEDs and buttons (digitally only (yet))

    Launchpad Pro Mk3  - class "LaunchpadProMk3()"  EXPERIMENTAL+++ as in "should be really ok"

    Launchpad Mini Mk3 - class "LaunchpadMiniMk3()" LEDs and buttons  *** RENAMED 5/2020 ***

    Launchpad X        - class "LaunchpadLPX()"     EXPERIMENTAL+++ as in "should work really well"

    Launch Control     - class "LaunchControl()"    EXPERIMENTAL

    Launch Control XL  - class "LaunchControlXL()"  LEDs, buttons and potentiometers
    
    LaunchKey (Mini)   - class "LaunchKeyMini()"    Buttons, keys and potentiometers/sliders, no LEDs
    
    Dicer              - class "Dicer()"            LEDs and buttons

    Midi Fighter 64    - class "MidiFighter64"      LEDs and buttons


> PRO MK3 USERS:  
> You need to disable the Launchpad's "Transmit Clock" in the MIDI settings!  
> See section "For Launchpad Pro Mk3 users"  
>  
> The Pro Mk3 needs the latest Firmware to operate flawlessly. FW is only available  
> via a Novation account- and product registration.

Please notice that the class "LaunchpadMk3()" was renamed to "LaunchpadMiniMk3()" in 5/2020.  
This was necessary to avoid confusion with the device search string and the new "Pro-Mk3" Launchpad.  
The "Pro Mk3" now is in LaunchpadProMk3().

Please notice the changes in methods "Open()" and "Check()" for the Mini Mk3 and X.  
Also, see demo files "hello.py" or "launchpad_rgb.py" as a reference on how to use them.


### Python

Now with Python 3 support \o/


### OS

Now full functionality also on Windows 10 and macOS based systems.  
Successfully tested with Ubuntu 18.04-LTS+. Requires compiling your own PyGame though (which is actually very easy; see below...).


---
## NEWS

### CHANGES 2021/01/XX:
    - fix for Python 3.9
    - updated documentation for raw LED and button codes (top row had wrong values)
    - changed version and tag to v0.9.1
    - uploaded v0.9.1 to PyPI

### CHANGES 2020/12/XX:
    - changed version and tag to v0.9.0
    - uploaded v0.9.0 to PyPI (finally :)

### CHANGES 2020/09/XX:
    - fixed sending command to not ready Pro Mk3 
    - fixed MF64 LedCtrlString() to correctly work with the background color
    - updated hello.py demo file for Midi Fighter 64
    - updated demo files to new and recommended default device search strategy
    - added Pro Mk3 ButtonStateXY() pressure events
    - added demo file "launchpad_pressure_xy()" for new XY pressure events (Pro Mk3, so far)
    - fixed MF64 minor init flaw
    - added X ButtonStateXY() pressure events
    - updated pressure xy demo file for X and also fixed an error for the Pro Mk3
    - added Pro ButtonStateXY() pressure events
    - updated pressure xy demo file for the Pro


### CHANGES 2020/08/XX:
    - added support for pressure events via ButtonStateRaw() for the Pro and Pro Mk3
    - added support for pressure events via ButtonStateRaw() for the X
    - added demo file "launchpad_pressure.py" for pressure sensitivity
    - updated pressure demo to work with the X too
    - added multiple search names for the X
    - updated all rgb-demos to work with the X
    - changed ListAll() method to optionally accept a string to query specific devices only
    - added a general midi_events.py demo file for better debugging
    - added a class for the Midi Fighter 64, only (raw) buttons so far
    - added MF64 LedCtrlRaw(), ButtonStateXY(), LedAllOn()
    - added MF64 LedCtrlXY()
    - added support for the Launchpad Pro Mk3
    - updated some demos to work with the Pro Mk3
    - updated even some demos to work with the Pro Mk3
    - updated yet some more demos and eliminated some bug
    - updated pressure event handling in the Pro, Pro Mk3 and X's ButtonStateXY() methods
    - added a Pro Mk3 "reset to Live mode" demo file
    - updated ButtonStateXY() for the Pro Mk3, incl "classic" and "Pro" mode
    - added character and string scrolling for Midi Fighter 64
    - added stupid Midi Fighter text scrolling demo
    - added MF64 LED-mode settings: brightness, toggling, flashing and animation settings
    - updated MF64 LedCtrlRaw() to accept LED-mode settings
    - updated MF64 LedAllOn() to optionally accept LED-mode settings
    - updated MF64 LedCtrlXY() to optionally accept LED-mode settings
    - added MF64 "constants" for easier LED-mode settings
    - added MF64 LED-mode example file "midifighter_led_modes.py"


### CHANGES 2020/05/XX:

    - changed class name for the Mini MK3 to LaunchpadMiniMk3(); for compatibility w/ Pro-Mk3
    - changed default search string for the Mini-Mk3 to "MiniMK3", for compatibility with Pro-Mk3
    - changed default search string for the original Pro to "Launchpad Pro"; for compatibility w/ Pro-Mk3
    - updated all included example files to match the class name and search term changes

### CHANGES 2020/04/XX:

    - added Mk3 Launchpad pull request #48; most of the Mk3 functionality available
    - updated example launchpad_rgb.py (was "...mk2.py") for Mk2, Mk3 and Pro
    - added "information.py" example to output some system and devices infos
    - updated the "fire demo" to work with Mk2 and Mk3 too
    - updated the "pulse demo" to work with Mk2 and Mk3 too
    - added a class for the original Launch Control
    - added Launchpad X pull request #51; most of the X functionality available

### CHANGES 2020/03/XX:

    - added Mk3 Launchpad; just a few lines of code, so far; ** EXPERIMENTAL **
    - added LPX Launchpad; just a few lines of code, so far; ** EXPERIMENTAL **
    - updated "hello.py" demo with basic Mk3/LPX code

### CHANGES 2019/09/XX:

    - added Mk1 LedCtrlRawRapidHome(), return to home position for LedCtrlRawRapid()
    - updated build instructions

### CHANGES 2018/10/XX:

    - added PRO/Mk2 LedCtrlPulseByCode(), pulse LEDs by color code (RGB not supported)
    - added PRO/Mk2 LedCtrlFlashByCode(), LED dual color flash by color codes (RGB not supported)
    - added PRO/Mk2 LedCtrlBpm(), set pulsing/flashing rate
    - updated PyGame compilation instructions
    - added PRO/MK2 LedCtrlPulseXYByCode(), pulse LEDs by color code and X/Y position
    - added PRO/MK2 LedCtrlFlashXYByCode(), flash LEDs by color code and X/Y position
    - added PRO/MK2 flashing/pulsing example file
    - changed version and tag to v0.8.1
    - uploaded v0.8.1 to PyPI \o\\o//o/

### CHANGES 2018/06/XX:

    - added notes on how to compile your own PyGame (trouble solving)

### CHANGES 2018/02/XX:

    - added experimental (aka "seems quite good") support for Python 3
    - added Pro example/test file "launchpad_pro.py"
    - improving the doc, letter by letter
    - added Mk2 example/test file "launchpad_mk2.py"
    - removed the "Python 2 only" restriction from the setup file
    - changed the imports in __init__.py to work with Python 3
    - launchpad_py now ready for installations on Python 2 and 3
    - updated "launchpad_pro.py" example/test; LedCtrlChar() positioning
    - changed version and tag to v0.8.0
    - uploaded v0.8.0 to PyPI \o\\o//o/
    - added "launchpad_pro-fire.py" example; just a simple fire animation

### CHANGES 2017/09/XX:

    - added notes for Ubuntu 17.04 systems and /etc/alsa/alsa.conf issues
    - added experimental 'Bad Pointer' fix upon exiting (needs more testing (w/ multiple LPads))

### CHANGES 2017/08/XX:

    - changed DCR; renamed InputStateRaw() to ButtonStateRaw()
    - added DCR LedCtrlRaw()
    - added DCR Reset()
    - added DCR LedAllOff()
    - added DCR "shift-lock" support (holding down mode buttons for additional 3*5 button events (per Dicer)
    - added DCR ModeSet()
    - added DCR "one page mode" support for buttons and LEDs
    - added DCR support in hello.py demo

### CHANGES 2017/07/29:

    - added a class for the Dicer
    - added DCR InputStateRaw() with coolest button mapping ever <3
    - added DCR LedSetLightShow()

### CHANGES 2017/06/XX:

    - added support for the Launch Control XL pad
    - added XL LedCtrlXY()
    - added XL ButtonStateRaw(), later renamed to InputStateRaw()
    - added XL TemplateSet()
    - added XL potentiometer support (via InputStateRaw())
    - added XL InputChanged()
    - added XL InputFlush()
    - added XL docs
    - updated "hello.py" example to work with Control XL
    - added EventRaw() for all devices
    - added preliminary support for the LaunchKey (Mini)
    - changed XL InputStateRaw(); added 3rd "velocity" field [<number>, <True/False or value>, <velocity> ]
    - changed LaunchKey device search name from "Launchkey Mini" to just "Launchkey"
    - added LKM InputFlush() and InputChanged() for LaunchKey(Mini)
    - added LKM docs
    - added LKM to the hello.py test file
    
### CHANGES 2017/04/30:

    - launchpad.py is now available via PyPI, the Python Package Index.

### CHANGES 2017/04/09:

    - Windows 10 and macOS SysEx issues are fixed \o\ \o/ /o/

### CHANGES 2017/01/XX:

    - launchpad.py is now available as an [optionally] installable package;
    - fixed unintentional installs under Python 3 dist-packages
    - added ButtonFlush() method to empty the button buffer
    - added Pro LedAllOn() and Mk2 Reset()
    - added macOS notes
    - some minor tweaks for the Mk2

### CHANGES 2016/12/XX:

    - added "fireworks demo" note (device not recognized)
    - reworked string scrolling for Mk1 and Mk2 Launchpads:
      - characters now adjacent
      - no artifacts left on screen (right to left scrolling)
      - scrolling from left to right still has some issues ("quick hack drawback" :)
    - implemented same scrolling behaviour for the Pro Launchpad
    - Mk2 LedCtrlXY() now does nothing if x/y are out of range (were clamped to 0 or 8 before)
    - Mk2 LedCtrlXYByCode() now also exits if x/y values are out of range
    - added LedCtrlXYByRGB() for Mk2/Pro; pass color arguments as list [r,g,b]
    - tried to clarify "Mk1" color and x/y origin mode for Pro pads in the doc
    - added ButtonStateXY() for Mk2 and Pro
    - device name search patterns now are case insensitive

### CHANGES 2016/11/XX:

    - added notes about how to use it on macOS

### CHANGES 2016/01/XX:

    - Support for Launchpad Pro now built in (only a few functions, so far).
      Please notice the new class for the Pro:
        lp_pro = LaunchpadPro()
      Except for a few, low level functions (e.g. "LedCtrlRaw()"), this and
      probably all future classes will remain compatible to the good, old
      "Classic" Launchpad (Mk1).
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
    - added Mk2 LedCtrlRawByCode() and LedCtrlXYByCode()
    - added Pro ButtonStateRaw(); first *damn fast* button reads \o/

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

  - "PK3": the Pro Mk3 has some issues; needs to be fixed
  - "All": optionally avoid resetting the X and Pro Mk3 to Live mode in Close(); (bc LEDs turn on)
  - "FNT": fix character set; e.g. "!", "0", "N" and probably many more
  - "All": RGB to color code approximation (for flash/pulse and color code methods)
  - "All": either remove or add the (non-) optional \<colorcode\> argument to all methods
  - "DCR": query mode
  - "All": native scrolling for RGB pads
  - "All": split the doc in smaller, readable parts
  - "CXL": x/y support (if it makes sense...)
  - "All": LedCtrlChar() make y-offset work
  - "Pro": change ButtonStateXY() to return True/False + velocity, as in the LaunchKeyMini
  - "Pro": remove the "Mk1" compatibility from the "Pro" functions (blue LEDs and intensity values)
  - "All": [r,g,b] lists for colors, instead of single args (might affect compatibility)
  - "Pro": implement native text scrolling
  - "Pro": support full analog reads (button already pressed, but intensity changes)
  - "Doc": split installation and usage (and condense that a little)
  - "All": fix manual text scrolling
  - "All": replace MIDI cmd numbers with sth human readable (144->Note On; 176->Control Change, etc...)
  - "All": custom bitmaps and graphics
  - "All": event system
  - "All": better custom font support
  - "All": [r,g,b] lists for colors, instead of single args (might affect compatibility)
  - ...

## cancelled:

  - "M64": RGB to color code mapping *NOPE* This does not work.

---
## Installation/Usage

### Install as Python package

#### Via pip from PyPI

Please notice that the PyPI version is not always up to date!  
Simply execute

    pip install launchpad_py

or

    sudo pip install launchpad_py

(in case you need superuser rights) to install it.  
Notice that the required dependencies (see below) are not automatically resolved and you need to install PyGame separately.

Also make sure that you're using the right "pip", matching your Python 2 or 3 preference.  
Check with

    pip --version

Which should bring up somewthing like:

    pip 9.0.1 from /usr/lib/python2.7/dist-packages (python 2.7)

For explicitly installing this in an Python 3 environment, use

    pip3 install launchpad_py


#### From local file system

If you downloaded the Launchpad.py source package, simply execute the command

      python setup.py install

from the base directory or 

      sudo python setup.py install

if superuser access is required.

Load and use the module with

      import launchpad_py
      ...
      ...
      # Mk1 Launchpad:
      lp = launchpad_py.Launchpad()
      # Mk2 Launchpad:
      lp = launchpad_py.LaunchpadMk2()
      # Mk3 Launchpad:
      lp = launchpad_py.LaunchpadMk2()
      #  X  Launchpad:
      lp = launchpad_py.LaunchpadLPX()
      # Pro Launchpad:
      lp = launchpad_py.LaunchpadPro()
      # Pro Mk3 Launchpad:
      lp = launchpad_py.LaunchpadProMk3()
      # Control:
      lp = launchpad_py.LaunchControl()
      # Control XL:
      lp = launchpad_py.LaunchControlXL()
      # LaunchKey Mini:
      lp = launchpad_py.LaunchKeyMini()
      # Dicer:
      lp = launchpad_py.Dicer()

or if you dislike typing that much, use

      import launchpad_py as lppy
      ...
      ...
      lp = lppy.Launchpad()
      lp = lppy.LaunchpadMk2()
      lp = lppy.LaunchpadMiniMk3()
      lp = lppy.LaunchpadLPX()
      lp = lppy.LaunchpadPro()
      lp = lppy.LaunchpadProMk3()
      lp = lppy.LaunchControl()
      lp = lppy.LaunchControlXL()
      lp = lppy.LaunchKeyMini()
      lp = lppy.Dicer()

For compatibility with existing code, use

      import launchpad_py as launchpad


#### Install directly from Github

Instead of downloading the source distribution, you can directly install it from Github
by executing

      pip install git+https://github.com/FMMT666/launchpad.py


#### Via your system's package manager, e.g. on Raspbian

    ATTENTION Raspberry Pi Raspbian user. This is for you!

Some Linux distributions come with their own PyGame package.  
Check your manual :)

With "apt", for example, you could either try

    apt search pygame

or

    apt-cache search pygame
    apt-cache search pygame | grep pygame

Make sure to install the right PyGame version, matching your Python 2 or 3 prefewrence.  
Sample output from a Raspbian Jesse:

    python-pygame - SDL bindings for games development in Python (Python 2)
    python3-pygame - SDL bindings for games development in Python (Python 3)

An Ubuntu 17.0.1, which comes with Python 3 as default, outputs

    python-pygame - SDL bindings for games development in Python
    python-pygame-sdl2 - reimplementation of the Pygame API using SDL2

but this is only a Python 2 installation of PyGame.


### Direct usage

If you don't want to or cannot install the package on your system, simply
copy the two files

      launchpad.py
      charset.py

to your working directory.  
Use those files as described above, but without the "_py":

      import launchpad
      ...
      ...
      # Mk1 Launchpad:
      lp = launchpad.Launchpad()
      ...

or

      import launchpad as LP
      ...
      ...
      lp = LP.Launchpad()
      ...

### Universal loading template code

#### Checks for an installed version first, loads local one as the last resort

      import sys
      
      try:
        import launchpad_py as launchpad
      except ImportError:
        try:
          import launchpad
        except ImportError:
          sys.exit("error loading lauchpad.py")

#### Checks for a local version first (file in same folder), uses the installed one secondary

      import sys
      
      try:
        import launchpad as launchpad
      except ImportError:
        try:
          import launchpad_py
        except ImportError:
          sys.exit("error loading lauchpad.py")


---
## License

[CC BY 4.0, Attribution 4.0 International][11]

You are free to:

Share — copy and redistribute the material in any medium or format  
Adapt — remix, transform, and build upon the material for any purpose, even commercially.
  
The licensor cannot revoke these freedoms as long as you follow the license terms.


---
## Requirements

  - [Python][2] 2, 3
  - [Pygame][3] v1.9.1, (v1.9.2), v1.9.3, v1.9.4-XX, ...

Some Pygame versions do not work on some OSes (e.g. v1.9.2 might cause trouble
with Windows 7/10). I cannot tell you any more than just "try!".  
The latest fixes (4/2017) were tested with v1.9.3 (via pip from Python 2.7.13)
and Windows 10 (x64). That seems to work fine again...
  
As of 2/2018, launchpad.py comes with Python 3 support.  
Tested, so far:  

  - Windows 10, Python 3.6.4, PyGame 1.9.3 (via pip), MK2 Pad
  - macOS Sierra, Python 3.6 (Macports), PyGame 1.9.3 (via pip), Pro Pad
  - Raspbian Jessy, RPi3, Python 3.4.2, PyGame 1.9.2a0 (via apt), Mini Pad

Python 3 might not (yet and out-of-the-box) work for:  

  - stock Ubuntu 16.04.3-LTS (requires building PyGame from sources)
  - stock Ubuntu 17.04       (same)
  - stock Ubuntu 17.10       (same)
  - stock Ubuntu 18.04       (workaround available)

See below for instructions on how to compile PyGame on your own...


Previously, launchpad.py was tested under

  - Linux, 32 bit, 64 bit
  - Windows XP, 32 bit
  - Windows 7, 32 bit, 64 bit
  - Windows 10, 64 bit
  - macOS Sierra
  - [Raspberry-Pi 1/2/3][4]
  - Beagle Bone (Black)
  - Banana Pi (Pro/M2/R1)
  - pcDuino V3
  - ...

Supported and tested red/green LED Launchpad devices, here referred  to as "Classic" or "Mk1":

  - Launchpad (the original, old "Mk1")
  - Launchpad S
  - Launchpad Mini (Mk1)

Supported and tested full RGB Launchpad devices:
  
  - Launchpad Pro
  - Launchpad Pro Mk3
  - Launchpad Mk2
  - Launchpad Mini Mk3
  - Launchpad LPX

Supported completely different stuff:

  - Launch Control
  - Launch Control XL
  - LaunchKey (Mini)
  - Dicer
  - Midi Fighter 64

Notice that Novation now (1/2016) sells an RGB Launchpad under the same
name it once shipped the first red/green LED with!

---
## Compiling your own PyGame

 If you have problems with errors like "alsa.conf" or the ListAll() method
 not recognizing any attached Launchpads on newer systems, especially Ubuntu 17/18,
 you might consider compiling your own PyGame version.

 This explanation is for Ubuntu 18.04-LTS and Python 3, but it should work [tm] for most other systems too.

 Additional package requirements, install them with

    sudo apt-get install <package name>

 I recommend installing these one after another (for easy "debugging")

    git
    automake
    cmake
    libsdl1.2-dev        <--- for older PyGame versions
    libsdl2-dev          <--- for newer PyGame versions (ca. mid 2019+)
    libfreetype6-dev
    libportmidi-dev
    python3-setuptools   <--- for Python 3
    python3-dev          <--- same
    ...

### Compile via "setup.py"

 Find the complete compilation instructions [here][19].

 Download the PyGame source code.  
 Notice that this will create a sub-folder named "pygame":

    git clone https://github.com/pygame/pygame

 Enter that directory and type

     python3 setup.py build

 which results in something like:

    ...
    No package 'freetype2' found
    WARNING: "pkg-config freetype2" failed!
    SDL     : found 1.2.15
    FONT    : not found
    IMAGE   : not found
    MIXER   : not found
    PNG     : found
    JPEG    : not found
    SCRAP   : found
    PORTMIDI: found
    PORTTIME: found
    FREETYPE: not found
    
    Warning, some of the pygame dependencies were not found. Pygame can still
    compile and install, but games that depend on those missing dependencies
    will not run. Would you like to continue the configuration? [Y/n]

 If you need a fully working PyGame, with all features, I leave it up to you,
 to resolve the remaining "not found" issues, but they're not required by Launchpad.py

 Make sure PORTMIDI and PORTTIME are marked with "found", then continue the build process.
 After a hopfully error-free build, execute (Ubuntu example for superuser access)

    sudo python3 setup.py install

  After a short time, you now should have PyGame in the default path

    /usr/local/lib/python3.6/dist-packages/

 ...


### Compile via "configure" (old)

 Newer Python variants come with a fully functional setup.py (see above).  
 I just leave the old compiling instructions here...

 Download the PyGame source code.  
 Notice that this will create a sub-folder named "pygame":

    git clone https://github.com/pygame/pygame

 Enter that directory and type

     ./configure

 which results in something like:

    ...
    No package 'freetype2' found
    WARNING: "pkg-config freetype2" failed!
    SDL     : found 1.2.15
    FONT    : not found
    IMAGE   : not found
    MIXER   : not found
    PNG     : found
    JPEG    : not found
    SCRAP   : found
    PORTMIDI: found
    PORTTIME: found
    FREETYPE: not found

 If you need a fully working PyGame, with all features, I leave it up to you,
 to resolve the remaining "not found" issues, but they're not required by Launchpad.py

 Next, type

    make

 to create the build files, followed by a

    sudo python3 setup.py install

 After a short time, you now should have PyGame in the default path

    /usr/local/lib/python3.6/dist-packages/

 ...

 
---
## Random Notes

### Button, value and potentiometer polling

 Until now (6/2017), Launchpad.py does not have an event system built in. You need to poll the buttons' or
 potentiometer's values manually.  
 Notice that actually nothing will get lost, but every event you create will be buffered (until you run out
 or memory :). If you don't poll the buttons or potentiometers regulary, your might end up with thousands
 of old states and values, blocking the current input.  
 Especially rotating a potentiometer or pushing a slider, creates an event for each single value that
 was sampled. This can easily be hundreds of messages in a few seconds.

 So either poll regulary or use the ButtonFlush()/InputFlush() method to clear everything.

 Also notice that the buffer might be filled right after you started your application...
  

### For Launchpad Mk1 users (the original "Classic" Launchpad):

      USE CLASS "Launchpad":
      
        lp = launchpad.Launchpad()

### For Launchpad Pro users

      USE CLASS "LaunchpadPro":
      
        lp = launchpad.LaunchpadPro()
        
      As of 2016/01/24, the "Pro" is now automatically set to "Ableton Live mode",
      which is required for launchpad.py to work.

### For Launchpad Pro Mk3 users

      USE CLASS "LaunchpadProMk3":
      
        lp = launchpad.LaunchpadProMk3()
        
      You need to disable the "Transmit Clock" in the Launchpad settings!
      Hold "Setup" and disable the 2nd LED from the left (must be red).

![RGB color palette](/images/promk3_transmit.png)

      Otherwise the receive buffer will be spammed with messages.

### For Launchpad Mk2 users

      USE CLASS "LaunchpadMk2":
      
        lp = launchpad.LaunchpadMk2()

### For Launchpad Mini Mk3 users

      USE CLASS "LaunchpadMiniMk3":
      
        lp = launchpad.LaunchpadMiniMk3()

### For Launchpad X users

      USE CLASS "LaunchpadLPX":
      
        lp = launchpad.LaunchpadLPX()

### For Launch Control users

      USE CLASS "LaunchControl":
      
        lp = launchpad.LaunchControl()

### For Launch Control XL users

      USE CLASS "LaunchControlXL":
      
        lp = launchpad.LaunchControlXL()

### For LaunchKey (Mini) users

Even it is named "Mini", it also supports most of the bigger keyboards' functionalities.  
Notice that some of the button and key numbers collide and cannot be differed.

      USE CLASS "LaunchKeyMini":
      
        lp = launchpad.LaunchKeyMini()

### For Dicer users

      USE CLASS "Dicer":
      
        lp = launchpad.Dicer()

The Dicer uses "page" mode by default. The three small buttons "cue", "loop" and "auto loop"
select six different pages (per Dicer module) and each of those can be handled independently.

The first set of the six mode is enabled by simply pushing (and releasing) on of the three mode
buttons, the second set, "shift-mode" is activated by holding down one of the mode buttons while
pushing a number button.

So, if the "cue" page is active and you try to activate an LED in the "loop" page, that
will not be visible until you activate that page.


### For Midi Fighter 64 users

      USE CLASS "MidiFighter64":
      
        lp = launchpad.MidiFighter64()

The Midi Fighter needs to be set to MIDI channel 3 (factory default).
It does not matter which bank is selected, both are supported.

Switching the banks does currently make no difference in button numbers or events.
Drop me a note if it would make sense to change that ...


### alsa.conf issues

Several users reported errors because of a missing alsa.conf file, e.g.:

    ALSA lib conf.c:3009:(snd_config_update_r) Cannot access file /etc/alsa/alsa.conf
    ALSA lib seq.c:935:(snd_seq_open_noupdate) Unknown SEQ default

If /etc/alsa/alsa.conf does not exist, you can create a symbolic link to where it resides on
your system. Find it with:

    find /etc /usr -name "alsa.conf"

If that command can _not_ find "alsa.conf" (a common place is /usr/share/alsa/alsa.conf), you
probably don't have Alsa installed at all.

In all other cases, you can create a symbolic link from /etc/alsa/alsa.conf to the real, existing file
(assuming /usr/share/alsa/alsa.conf here).  
Warning: Double check whether /etc/alsa/alsa.conf _really_ does not exist first!

    sudo mkdir /etc/alsa
    sudo ln -s /usr/share/alsa/alsa.conf /etc/alsa/alsa.conf

After that, you still might experience that Launchpad.py cannot find any MIDI devices.  
The output from "lp.ListAll()" does not return anything and executing the "hello.py" example just shows
something like:

    Exception AttributeError: "'NoneType' object has no attribute 'quit'" in <bound method __Midi.__del__
    ... of <launchpad_py.launchpad.__Midi instance at 0x7f0860cb3128>> ignored

In this case, the default sequencer entries might be missing in your alsa.conf.  
You might wish to add this to your alsa.conf:

    #
    #  Sequencer interface
    #
    
    seq.default {
      type hw
      hint.description "Added by experts. Source: Internet \o/"
    }
    
    seq.hw {
    type hw
    }

Thanks to [MartinPaulEve][17] for pointing that out.  
Please notice that this "fix" won't work on all systems. While it does, for example,
work with Ubuntu 17.04, the same error usually just indicates that your system was not
built with a PyGame compatible ALSA (PortMidi) version.  
There is no easy fix for this (unless you wish to spend a lot of time completely recompiling your system...)


### For Mac users

#### Mac Python and Pygame

Good news, everybody. It now works with macOS Sierra \o/  
Best part: It even works with the stock "Apple Python".
      
Pygame can be installed via "pip". Just enter "pip" on the console
to see whether it is installed:
      
        pip
      
If it isn't, you can install it with:
      
        sudo easy_install pip
        
If pip is working, search for Pygame via pip (console command):
      
        sudo pip search pygame
      
Somewhere in the list, you should see something like
      
        Pygame (1.9.2b8)   - Python Game Development
        
Install that with:
      
        sudo pip install pygame

#### Hardware

Notice that the original Launchpad Mk1 requires an USB driver. Thanks, [Stewart!][13].  
Get it from [here][14] (Novation USB Driver-2.7.dmg).

As it seems, all newer Launchpads work right out of the box, no driver required.

### For Raspberry Pi users

Please notice that some the newer RGB LED Launchpads consume more current than a
Raspberry Pi can deliver. If you turn on a lot of LEDs, the Launchpad will just reset and show the fireworks demo.  
At least for the Launchpad Pro, you could use an external power supply adapter. For the Mk2, you
would need a an "USB-Y" cable, with the "power plug" connected to an external power supply (or other PC).

As written somewhere above, at least for Raspbian (Jesse), you should install Raspbian's PyGame version
via the package manager or apt. The PyPI version (installation via "pip") will not work due to some missing SDL components.  

Btw, you can check your Raspbian version with the console command

    cat /etc/os-release

Which outputs something comparable to

    PRETTY_NAME="Raspbian GNU/Linux 8 (jessie)"
    NAME="Raspbian GNU/Linux"
    VERSION_ID="8"
    VERSION="8 (jessie)"
    ...


### For Windows users

      MIDI implementation in PyGame 1.9.2+ is broken and running this might
      bring up an 'insufficient memory' error ( pygame.midi.Input() ).

      SOLUTION: use v1.9.1 or try v1.9.3

### For Linux and especially Raspberry-Pi users:

      Due to some bugs in PyGame's MIDI implementation, the buttons of the Launchpad Mk1
      won't work after you restarted a program (LEDs are not affected).

      WORKAROUND #2: Simply hit one of the AUTOMAP keys (the topmost 8 buttons).
                     For whatever reason, this makes the MIDI button events
                     appearing again...

      WORKAROUND #1: Pull the Launchpad's plug out and restart... (annoying).

### Other Notes

#### Launchpad (Pro) not recognized, playing fireworks demo

Just discovered another oddity...

I attached a Launchpad Pro to my Linux box, as many times before, to finally add the
button methods, but it refused to show up as an USB device. Instead of the "note mode",
indicated by a turquoise/pink colour pattern, it played that "fireworks animation" and
did nothing...

The first time I discovered that, I blamed it on an attached FTDI UART chip, but as it
turned out, that was not the reason it didn't work.

It simply was a power issue.

So, if your Launchpad Pro shows that firework demo, check your USB cable!  
Seriously. That thing draws a lot of current and most USB cables simply
do not conform to the USB standard (or your USB port isn't, e.g. Raspberry Pi).

On Linux, you can check that via the console command "dmesg".  
If the output contains hundreds of "urb status -32" errors, followed by

    ...
    [ 1414.983069] usb 1-1.5: urb status -32
    [ 1414.983232] usb 1-1.5: urb status -32
    [ 1414.983345] usb 1-1.5: urb status -32
    [ 1414.983456] usb 1-1.5: urb status -32
    [ 1414.983495] usb 1-1.5: USB disconnect, device number 8
    [ 1414.983568] usb 1-1.5: urb status -32
    [ 1414.983692] usb 1-1.5: urb status -32
    [ 1415.288539] usb 1-1.5: new full-speed USB device number 9 using dwc_otg
    [ 1415.445968] usb 1-1.5: New USB device found, idVendor=1235, idProduct=0051
    [ 1415.445984] usb 1-1.5: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [ 1415.445992] usb 1-1.5: Product: Launchpad Pro
    [ 1415.446000] usb 1-1.5: Manufacturer: Focusrite A.E. Ltd
    [ 1415.446009] usb 1-1.5: SerialNumber: Launchpad Pro
    ...

My USB cable "looked quite good" from the outside.  
With its ~5.5mm diameter, I assumed it had AWG 22 (~60mOhm/m) or better, but it in fact
has ~drumroll~ AWG 28 (~240mOhm/m) and two thick plastic strings to fill the gaps.

Well, we all know that companies try to save money wherever they can, but that's just
fraud...

Btw, the fireworks demo will play whenever the Launchpad cannot be enumerated (configured).  
[...]

---
## Common class methods overview (valid for all devices)

### Device control functions

    Open( [name], [number], [template (*1*)] )
    Close()
    Reset()
    ButtonFlush()
    
    (*1*) Control (XL) only
    

### Utility functions

    ListAll( [searchString] )
    EventRaw()
    
    
---
## Launchpad Mk1 "Classic" class methods overview (valid for green/red LED devices)

### LED functions

    LedGetColor( red, green )
    LedCtrlRaw( number, red, green )
    LedCtrlXY( x, y, red, green )
    LedCtrlRawRapid( allLeds )
    LedCtrlRawRapidHome()
    LedCtrlAutomap( number, red, green )
    LedAllOn()
    LedCtrlChar( char, red, green, offsx = 0, offsy = 0 )
    LedCtrlString( str, red, green, dir = 0 )

### Button functions

    ButtonChanged()
    ButtonStateRaw()
    ButtonStateXY()
    ButtonFlush()


---
## Launchpad "Mk2/3", "Pro", "Pro Mk3" and "X" class methods overview (valid for RGB LED devices)

Please notice that some devices do not yet have all of these or are implemented slightly different.  
Refer to the "detailed description of ..." section for each device.

### LED functions

    LedSetMode( mode )
    LedGetColorByName( name )
    LedCtrlRaw( number, red, green, [blue] )
    LedCtrlRawByCode( number, [colorcode] )
    LedCtrlPulseByCode( number, colorcode )
    LedCtrlPulseXYByCode( x, y, colorcode )
    LedCtrlFlashByCode( number, colorcode )
    LedCtrlFlashXYByCode( x, y, colorcode )
    LedCtrlBpm( bpm )
    LedCtrlXY( x, y, red, green, [blue] )
    LedCtrlXYByCode( x, y, colorcode )
    LedCtrlXYByRGB( x, y, colorlist )
    LedCtrlChar( char, red, green, [blue], [offsx], [offsy] )
    LedCtrlString( string, red, green, [blue], [direction], [waitms] )
    LedAllOn( [colorcode] )


### Button functions

    ButtonStateRaw( [returnPressure] )
    ButtonStateXY( [mode], [returnPressure] )
    ButtonFlush()


### Color codes

All RGB Launchpads have a 128 color palette built-in.  
Controlling LEDs with colors from the palette is about three times faster than
using the, indeed much more comfortable, RGB notation.

Functions requiring a color code have a "...ByCode" naming style.

![RGB color palette](/images/lppro_colorcodes.png)



---
## Launch Control or Control XL class methods overview

*WORK IN PROGESS*

### Device
    TemplateSet( template )


### LED functions

    LedGetColor( red, green )
    LedCtrlRaw( number, red, gree )
    LedCtrlXY( x, y, red, green )
    LedAllOn( [colorcode] )


### Input functions

    InputChanged()
    InputFlush()
    InputStateRaw()



---
## LaunchKey Mini class methods overview

*WORK IN PROGESS*

### LED functions

    TODO


### Input functions

    InputChanged()
    InputFlush()
    InputStateRaw()


---
## Dicer class methods overview

*WORK IN PROGESS*

### LED functions

    LedSetLightshow()
    LedCtrlRaw()
    LedAllOff()


### Button functions

    ButtonStateRaw()


---
## Midi Fighter 64 class methods overview

*WORK IN PROGESS*

### LED functions

    LedCtrlRaw( number, color, [mode] )
    LedCtrlRawMode( number, mode )
    LedCtrlXY( x, y, color )
    LedAllOn( [color] )
    LedCtrlChar( char, color, [offsx], [offsy], [coloroff] )
    LedCtrlString( string, color, [coloroff], [direction], [waitms] )


### Button functions

    ButtonStateRaw()
    ButtonStateXY()


### Color codes

The Midi Fighter 64 only supports a color table.  
There is no possibility to control the RGB LEDs individually.

![RGB color palette](/images/mf64_colorcodes.png)



---
## Detailed description of common Launchpad methods

### Open( [number], [name], [template (1)] )

    Opens the a Launchpad and initializes it.  
    Please notice that some devices have multiple and even up to six MIDI entries!

    To open the first Mini Mk3 or X device, "number" needs to be set to "1", not "0",
    as valid for (most) of the other Launchpads.
    
    Some Launchpads, e.g. the "Mk3 Pro" come with 3 MIDI devices. While the first device's
    number is "0", the 2nd device will require opening number "3" and not "1".
    
    (1) Notice that <template> is only valid for the Launch Control XL pad.
    A number of 1..8 selects and activates a user template (1 by default)
    or 9..16 a factory one.
    This corresponds to holding down one of the "Template buttons" and
    selecting the template number via the bottom button row.
    
    A dump by ListAll(), with a "Pro", a Mk1 "Mini" and a "Mk2" might look like:
    
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
        ('ALSA', 'Launch Control XL MIDI 1', 0, 1, 1)
        ('ALSA', 'Launch Control XL MIDI 1', 1, 0, 1)
    
    You'll only need to count the entries if you have two or more identical Launchpads attached.
    
      PARAMS: <number>   OPTIONAL, number of Launchpad to open.
                         1st device = 0, 2nd device = 1, ...
                         Defaults to 0, the 1st device, if not given.
              <name>     OPTIONAL, only consider devices whose names contain
                         the string <name>. The default names for the classes are:
                           Launchpad()        -> "Launchpad"
                           LaunchpadMk2()     -> "Mk2"
                           LaunchpadMiniMk3() -> "MiniMk3"
                           LaunchpadLPX()     -> "LPX" and "Launchpad X"
                           LaunchpadPro()     -> "Launchpad Pro"
                           LaunchpadProMk3()  -> "Launchpad Pro Mk3"
                           LaunchControl()    -> "Control MIDI"
                           LaunchControlXL()  -> "Control XL"
                           LaunchKeyMini()    -> "Launchkey" (should work for all variants)
                         It is sufficient to search for a part of the string, e.g.
                         "chpad S" will find a device named "Launchpad S" or even
                         "Novation Launchpad S"
              <template> OPTIONAL, ONLY FOR LAUNCH CONTROL (XL)
                         The Launch Control XL supports eight user and eight factory settings,
                         selectable via the two "Template" burrons on the top right.
                         By default, Launchpad.py uses the template "User 1".
                         Simply don't touch this and you're safe.
                         Notice that these values are internally remapped to 0..15, as they
                         appear in the Novation documentation. The buttons on the HW are labeled "1..8",
                         that is why Launchpad.py uses 1..16 rather than 0..15.
                         1.. 8 -> select user template    1..8
                         9..16 -> select factory template 1..8

      RETURN: True     success
              False    error

  As of 12/2016, the name search patterns are case insensitive, hence strings like "mk2", "pRo"
  or even "lAunCHpAd MiNI" are valid too.

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
              lp = launchpad.LaunchpadMk2()     # notice the "Mk2" class!
              lp.Open()                         # equals Open( 0, "Mk2" )

              # open the 1st "Mk3"
              #   NOTICE: Mk3 has two MIDI instances and we need the 2nd one.
              #   So, to open the first attached devices, use "Open(1)" and not "Open(0)". 
              lp = launchpad.LaunchpadMiniMk3() # notice the "MiniMk3" class!
              lp.Open()                         # THIS WILL NOT WORK!
              lp.Open(1)                        # this will open the first device
              lp.Open(3)                        # this would open the 2nd attached Launchpad

              # open the 1st "X"
              #   NOTICE: The X has two MIDI instances and we need the 2nd one.
              #   So, to open the first attached devices, use "Open(1)" and not "Open(0)". 
              lp = launchpad.LaunchpadLPX()     # notice the "LPX" class!
              lp.Open()                         # THIS WILL NOT WORK!
              lp.Open(1)                        # this will open the first device
              lp.Open(3)                        # this would open the 2nd attached Launchpad

              # open the 1st "Pro"
              lp = launchpad.LaunchpadPro()     # notice the "Pro" class!
              lp.Open()                         # equals Open( 0, "Launchpad Pro" )
              
              # open the 1st "XL" with user template 3
              lp = launchpad.LaunchControlXL( template = 3 )
              lp.Open()
              
              # open the 1st "XL" with factory template 2
              lp = launchpad.LaunchControlXL( template = 10 )
              lp.Open()



### Check( [number], [name] )

    Checks if a device is attached.
    Uses exactly the same notation as Open(), but only returns True or False,
    without opening anything.
    
    Like Open(), this method uses different default names for the different classes:
      Launchpad()        -> "Launchpad"
      LaunchpadMk2()     -> "Mk2"
      LaunchpadMiniMk3() -> "MiniMk3"
      LaunchpadLPX()     -> "LPX" and "Launchpad X"
      LaunchpadPro()     -> "Launchpad Pro"
      LaunchpadProMk3()  -> "ProMk3"
      LaunchControl()    -> "Control MIDI"
      LaunchControlXL()  -> "Control XL"
      LaunchKeyMini()    -> "Launchkey"

    Notice that the first Mk3 and the first X Launchpads need to be checked with "1", not "0".
      
    Notice that it's absolutely safe to query for an "Pro" or "Mk2" from all classes, e.g.:
    
      lp = lauchpad.Launchpad()             # Launchpad "Mk1" or "Classic" class
      if lp.Check( 0, "Pro" ):              # check for "Pro"
        lp = launchpad.LaunchpadPro()       # "reload" the new class for the "Pro"
        lp.Open()                           # equals lp.Open( 0, "Launchpad Pro" )

    As of 8/2020, the recommended way is to simply omit the name and trust the
    internal name search, though the above "name search variant" might be helpful in a pinch.

      if launchpad.LaunchpadPro.Check( 0 ): # check for "Pro"
        lp = launchpad.LaunchpadPro()       # "reload" the new class for the "Pro"
        lp.Open( 0 )                        # equals lp.Open( 0, "Launchpad Pro" )

    Search patterns are case insensitive.  
    
      PARAMS: see Open()
      
      RETURN: True     device exists
              False    device does not exist


### Close()

    No effect for most devices, except for the "Pro Mk3" and "X".
    Resets these Launchpads to Live mode.

      PARAMS:
      RETURN:


### ButtonFlush()

    Flushes the Launchpads button buffer.
    If you do not poll the buttons frequently or even if your software is not running,
    the Launchpad will store each button event in its buffer.
    This function can be used to clear all button events.

      PARAMS:
      RETURN:


### ListAll( searchString = '' )

    Debug function.
    Prints a list of all detected MIDI devices and addresses.
    Can be called any time and does not even require an opened device.
    The optional <searchString> parameter can be used to return a filtered set of
    device names only. By default, it is set to an empty string, which simply prints everything.

      PARAMS: <searchString>     [OPTIONAL] only devices containing this string will be considered
      RETURN:


### EventRaw()

    Debug function.
    Returns an unprocessed list of all MIDI events.


      PARAMS:
      RETURN: []  an empty list if nothing happened or this MIDI message:
              [[[ <cmd>, <data1>, <data2>, <res> ], <timestamp> ]] 


---
## Detailed description of Launchpad Mk1 "Classic" only methods


### Reset()

    Resets the Launchpad and (quickly) turns off all LEDs.
    Notice that only the Mk1 performs a 

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

    To return to the start position (LED1), issue an
    LedCtrlRawRapidHome() command. Thanks to "afandian" (issue #38).

      PARAMS: <allLeds> A list of up to 80 Launchpad color codes.
      RETURN:


### LedCtrlRawRapidHome()

    Resets the current LedCtrlRawRapid() position to LED1, aka. "homing".

      PARAMS:
      RETURN:

      EXAMPLE:
                LEDs = [ 0x03, 0x30, 0x33 ]  # LEDs 1..3: RGY
                lp.LedCtrlRawRapid( LEDs )
                time.wait(1000)

                lp.LedCtrlRawRapidHome()     # home position
                
                rgy = [ 0x30, 0x03, 0x33 ]   # LEDs 1..3; GRY
                lp.LedCtrlRawRapid( rgy )


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
    
    WARNING:
    Too short times will overflow the Launchpad's buffer and mess up
    the screen.
    
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

    Returns the state of the buttons in RAW mode.

      PARAMS:
      RETURN: [ ]                        An empty list if no event occured, otherwise...
              [ <button>, <True/False> ] ... a list with two fields:
              <button> is the RAW button number, the second field determines
              if the button was pressed <True> or released <False>.


### ButtonStateXY()

    Returns the state of buttons in X/Y mode.

      PARAMS:
      RETURN: [ ]                        An empty list if no event occured, otherwise...
              [ <x>, <y>, <True/False> ] ... a list with three fields:
              <x> is the x coordinate of the button, <y>, guess what, the
              y coordinate. The third field reveals if the button was pressed
              <True> or released <False>.


---
## Detailed description of RGB Launchpad only methods

 Applies to "Pro", "Pro Mk3", "Mk2", "Mini Mk3" and "LPX" unless otherwise noted.

### LedSetMode( mode ) *>>> PRO, MK3, LPX ONLY <<<*

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

    +++ NOTICE:
    +++   It is recommended to always call this with a "blue" parameter.
    +++   The compatibility mode will be removed soon. 
    
    Controls an LED via its number and red, green and blue intensity values.
    
    This method uses system-exclusive MIDI messages, which require 10 bytes to
    be sent for each message. For a faster version, hence less comfortable version,
    see LedCtrlRawByCode() below (though even sending 10 bytes is pretty fast on the Pro).
    
    If <blue> is omitted, this method runs in "Mk1" compatibility mode, which only
    had red/green LEDs and intensities ranging from 0..3. In that mode, the input
    arguments are multiplied by 21, to map 0..3 to 0..63.
    
    Notice that the "Pro" and "Mk2" have different LED number layouts.
    Please see tables, somewhere below.

    Notice that even though the Mk3 and the X support 0..127 intensities,
    only 0..63 can be used here. The values will be scaled up, resulting in the
    same intensity.
    Technically speaking, 0..63 is shifted left to match 0..127 with the LSB being omitted.

      PARAMS: <number>    number of the LED to control
              <red>       a number from 0..63
              <green>     a number from 0..63
              <blue>      OPTIONAL, a number from 0..63
      RETURN:


### LedCtrlRawByCode( number, [colorcode] )

    Controls an LED via its number and color code.
    If <colorcode> is omitted, 'white' is used.
    This is about three times faster than the comfortable RGB method LedCtrlRaw().

      PARAMS: <number>     number of the LED to control
              <colorcode>  a number from 0..127 (see image; white if omitted)
      RETURN:


### LedCtrlPulseByCode( number, colorcode )

    Controls an LED via its number and color code, as "LedCtrlRawByCode()" does,
    but pulsing the LED instead of just turning it on or off.
    If <colorcode> is omitted, 'white' is used.
    Pulsing can be turned off by simply sending another on/off command.
    The pulsing rate can be (roughly) set by LedCtrlBpm()
    
    Notice that there is no RGB control variant of this method (not supported by Launchpad).

      PARAMS: <number>     number of the LED to control
              <colorcode>  a number from 0..127 (see image)
      RETURN:


### LedCtrlPulseXYByCode( x, y, colorcode, [mode] )

    Pulses an LED via its x/y coordinates and color codes.
    An additional <mode> parameter determines the origin of the x-axis.
    
    For "Pro" only:
      By default, if <mode> is omitted, the origin of the x axis is the left side
      of the 8x8 matrix, like in the "Mk1" mode (those devices had no round buttons
      on the left).
      If <mode> is set to "pro" (string), x=0 will light up the round buttons on the
      left side. Please also see the table for X/Y modes somewhere at the end of this
      document.

      PARAMS: <x>          x coordinate of the LED to control
              <y>          y coordinate of the LED to control
              <colorcode>  a number from 0..127 (see image)
              <mode>       OPTIONAL: "pro" selects new x/y origin >>> PRO ONLY <<<
      RETURN:


### LedCtrlFlashByCode( number, colorcode )

    Flashes an LED between two colors or on/off.
    The first color can be set by any "LedCtrl...()" command, the second color and the
    activation of the flashing is then done by this method.
    Flashing can be turned off by simply sending another on/off/color command.
    The flashing rate can be (roughly) set by LedCtrlBpm()
    
    Notice that there is no RGB control variant of this method (not supported by Launchpad).

      PARAMS: <number>     number of the LED to control
              <colorcode>  a number from 0..127 (see image)
      RETURN:

      EXAMPLES:
              LP.LedCtrlRawByCode( 81, 16 )      # set top left LED (#81) to green ("16") (Mk2)
              LP.LedCtrlFlashByCode( 81, 6 )     # now set 2nd color to red ("6") and flash LED #81

              LP.LedCtrlXY( 0, 1, 63, 63, 63 )   # set top left LED to white (Mk2)
              LP.LedCtrlFlashByCode( 81, 6 )     # now set 2nd color to red ("6") and flash LED #81


### LedCtrlFlashXYByCode( x, y, colorcode, [mode] )

    Flashes an LED via its x/y coordinates and color codes.
    An additional <mode> parameter determines the origin of the x-axis.
    
    For "Pro" only:
      By default, if <mode> is omitted, the origin of the x axis is the left side
      of the 8x8 matrix, like in the "Mk1" mode (those devices had no round buttons
      on the left).
      If <mode> is set to "pro" (string), x=0 will light up the round buttons on the
      left side. Please also see the table for X/Y modes somewhere at the end of this
      document.

      PARAMS: <x>          x coordinate of the LED to control
              <y>          y coordinate of the LED to control
              <colorcode>  a number from 0..127 (see image)
              <mode>       OPTIONAL: "pro" selects new x/y origin >>> PRO ONLY <<<
      RETURN:


### LedCtrlBpm( bpm )

    EXPERIMENTAL/PRELIMINARY

    Sets the LED's pulsing or flashing frequency in beats per minute (bpm).
    By default, the Launchpads are set to 120 bpm.
    
    Notice that this comes with several restrictions (yet):

     - This function blocks for 67.5 / bpm seconds, e.g.:
          40 bpm - 1688 ms
         100 bpm -  675 ms
         240 bpm -  281 ms
        so it should only be called if absolutely necessary, preferably right in the beginning.

      - Due to the shortest time step of 1ms and the way the Launchpads handle the timing settings,
        the bpm values are restricted to:
        
          10 ms - 250 bpm     23 ms - 108 bpm     36 ms -  69 bpm     49 ms -  51 bpm
          11 ms - 227 bpm     24 ms - 104 bpm     37 ms -  67 bpm     50 ms -  50 bpm
          12 ms - 208 bpm     25 ms - 100 bpm     38 ms -  65 bpm     51 ms -  49 bpm
          13 ms - 192 bpm     26 ms -  96 bpm     39 ms -  64 bpm     52 ms -  48 bpm
          14 ms - 178 bpm     27 ms -  92 bpm     40 ms -  62 bpm     53 ms -  47 bpm
          15 ms - 166 bpm     28 ms -  89 bpm     41 ms -  60 bpm     54 ms -  46 bpm
          16 ms - 156 bpm     29 ms -  86 bpm     42 ms -  59 bpm     55 ms -  45 bpm
          17 ms - 147 bpm     30 ms -  83 bpm     43 ms -  58 bpm     56 ms -  44 bpm
          18 ms - 138 bpm     31 ms -  80 bpm     44 ms -  56 bpm     57 ms -  43 bpm
          19 ms - 131 bpm     32 ms -  78 bpm     45 ms -  55 bpm     58 ms -  43 bpm
          20 ms - 125 bpm     33 ms -  75 bpm     46 ms -  54 bpm     59 ms -  42 bpm
          21 ms - 119 bpm     34 ms -  73 bpm     47 ms -  53 bpm     60 ms -  41 bpm
          22 ms - 113 bpm     35 ms -  71 bpm     48 ms -  52 bpm     61 ms -  40 bpm

      PARAMS: <bpm>     beats per minute, 40..240
      RETURN:
      
      EXAMPLES:
              LP.LedCtrlBpm( 100 )      # set LED flashing/pulsing to ~100 beats per minute



### LedCtrlXY( x, y, red, green, [blue], [mode] )

    +++ NOTICE:
    +++   It is recommended to always call this with a "blue" parameter.
    +++   The compatibility mode will be removed soon. 
    
    Controls an LED via its x/y coordinates and red, green or blue intensity values.
    An additional <mode> parameter determines the origin of the x-axis.
    
    If <blue> is omitted, this method operates in "Mk1" compatibility mode.
    The Mk1 Launchpad only had 2 bit intensity values (0..3). In compatibility
    mode, these values are now multiplied by 21, to extend the range to 0..63.
    That way, old, existing code, written for the classic Launchpads does not
    need to be changed.
    
    For "Pro" only:
      By default, if <mode> is omitted, the origin of the x axis is the left side
      of the 8x8 matrix, like in the "Mk1" mode (those devices had no round buttons
      on the left).
      If <mode> is set to "pro" (string), x=0 will light up the round buttons on the
      left side. Please also see the table for X/Y modes somewhere at the end of this
      document.

    This method uses system-exclusive MIDI messages, which require 10 bytes to
    be sent for each message. For a faster version, hence less comfortable version,
    see LedCtrlXYByCode() below.

    Notice that even though the Mk3 and the X support 0..127 intensities,
    only 0..63 can be used here. The values will be scaled up, resulting in the
    same intensity.
    Technically speaking, 0..63 is shifted left to match 0..127 with the LSB being omitted.

      PARAMS: <x>      x coordinate of the LED to control
              <y>      y coordinate of the LED to control
              <red>    red   LED intensity 0..63 (or 0..3 in "Mk1" mode)
              <green>  green LED intensity 0..63 (or 0..3 in "Mk1" mode)
              <blue>   blue  LED intensity 0..63 (omit  for  "Mk1" mode)
              <mode>   OPTIONAL: "pro" selects new x/y origin >>> PRO ONLY <<<
      RETURN:


### LedCtrlXYByCode( x, y, colorcode, [mode] )

    Controls an LED via its x/y coordinates and a color from the color palette.
    
    Except for the color code, this function does the same as LedCtrlXY() does,
    but about 3 times faster.
    
      PARAMS: <x>          x coordinate of the LED to control
              <y>          y coordinate of the LED to control
              <colorcode>  a number from 0..127
              <mode>       OPTIONAL: "pro" selects new x/y origin >>> PRO ONLY <<<
      RETURN:


### LedCtrlXYByRGB( x, y, colorlist, [mode] )

    Controls an LED via its x/y coordinates and a list of colors in RGB format.
    
    This function does the same as LedCtrlXY() does, except that the color information
    is now passed in as list [R,G,B].
    
      PARAMS: <x>          x coordinate of the LED to control
              <y>          y coordinate of the LED to control
              <colorlist>  a list with [ R, G, B ] color codes; each from 0..63
              <mode>       OPTIONAL: "pro" selects new x/y origin >>> PRO ONLY <<<
      RETURN:
      
      EXAMPLES:
              LP.LedCtrlXYByRGB( 3, 7, [63, 42, 0] )


### LedCtrlChar( char, red, green, [blue], offsx = 0, offsy = 0 )

    +++ NOTICE:
    +++   It is recommended to always call this with a "blue" parameter.
    +++   The compatibility mode will be removed soon.
    
    Sends character <char> in colors <red/green/blue> (0..63 each) and
    lateral offset <offsx> (-8..8) to the Launchpad.
    <offsy> does not have yet any function.
    
    It is highly recommended to use <offsx> and <offsy> as
    named parameters, for compatible code with the RGB Launchpads, e.g.:
    
      lp.LedCtrlChar( 'a', 3, 2, offsx = xvar )
      
    If <blue> is ommited, this methods runs in "Mk1" compatibility
    mode and multiplies the <red> and <green> intensity values with 21, to
    adapt the old 0..3 range to the new 0..63 one of the "Pro" mode.
    That way, it is compatible to old, existing "Mk1" code.

    Notice that even though the Mk3 and the X support 0..127 intensities,
    only 0..63 can be used here. The values will be scaled up, resulting in the
    same intensity.
    Technically speaking, 0..63 is shifted left to match 0..127 with the LSB being omitted.

      PARAMS: <char>   one field string to display; e.g.: 'A'
              <red>    red   LED intensity 0..63 (or 0..3 in "Mk1" mode)
              <green>  green LED intensity 0..63 (or 0..3 in "Mk1" mode)
              <blue>   blue  LED intensity 0..63 (omit  for  "Mk1" mode)
              <offsx>  x offset of the character on the main, 8x8 matrix (-8..8)
                       Negative is left and positive right.
              <offsy>  no function
      RETURN:

      EXAMPLES:
              # scroll a purple 'A' from left to right
              for x in range( -8, 9 ):
                lp.LedCtrlChar( 'A', 63, 0, 63, offsx = x )
                time.wait( 100 )


### LedCtrlString( string, red, green, [blue], direction = 0, waitms = 150 )

    +++ NOTICE:
    +++   It is recommended to always call this with a "blue" parameter.
    +++   The compatibility mode will be removed soon (and the output on
    +++   Mk2 and Pro pads might be messed up).
    
    Notice that the Launchpad Pro has string scrolling capabilities built in, but
    this function provides the old, Mk1 compatible functionality. Advantages
    are custom fonts and symbols (in the future).

    Scrolls a string <str> across the Launchpad's main, 8x8 matrix.
    <red/green/blue> specify the color and intensity (0..63 each).
    <direction> determines the direction of scrolling.
    Dirty hack: <waitms>, by default 150, delays the scrolling speed.
    
    If <blue> is omitted, "Mk1" compatibility mode is turned on and the old
    0..3 <red/green> intensity values are strechted to 0..63.
    
    For future compatibility, it is highly recommended to use
    <direction> and <waitms> as a named arguments, e.g.:
    
      lp.LedCtrlString( "Hello", 3,1, direction = -1, waitms = 100 )

    Notice that even though the Mk3 and the X support 0..127 intensities,
    only 0..63 can be used here. The values will be scaled up, resulting in the
    same intensity.
    Technically speaking, 0..63 is shifted left to match 0..127 with the LSB being omitted.

      PARAMS: <string>     a string to display; e.g.: 'Hello'
              <red>        red   LED intensity 0..63 (or 0..3 in "Mk1" mode)
              <green>      green LED intensity 0..63 (or 0..3 in "Mk1" mode)
              <blue>       green LED intensity 0..63 (omit  for  "Mk1" mode)
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


### ButtonStateRaw( [returnPressure] )

    Returns the state of the buttons and pressure events in RAW mode.
    
    Notice that this is not directly compatible with the "Mk1" ButtonStateRaw()
    method, which returns [ <button>, <True/False> ].

    Only the Pro, X and Pro Mk3 support pressure events.
    They can be enables by passing "returnPressure=True" to the method call.
    Notice that the Pro and X behave differently:

    Pro and Pro Mk3:
      There is only one pressure value for all buttons together. If multiple buttons
      are pressed, the biggest value is returned. There is no possibility to determine
      which button caused it. To distinguish the pressure events from button events,
      a fake <button> number of "255" is returned in the list: [ 255, <value>].

    X:
      The X supports multiple pressure values. For a distinction between button events
      and pressure events, "255" is added to the button number:
       [ 255 + <button>, <pressure> ]

      PARAMS:
      RETURN: [ ]                    An empty list if no event occured, otherwise...
              [ <button>, <value> ]            ... a list with two fields:
                <button> is the button number (0..127), the second field, <value> determines
                the intensity (0..127) with which the button was pressed.
                0 means that the button was released.
              [ 255, <value> ]                 ... PRO: a list of pressure events with two fields:
                "255" as an indicator for a pressure event and <value> for the the intensity
                of the pressure (0..127).
              [ 255 + <button>, <value> ]      ... LPX: a list of pressure events with two fields:
                "255" + the button numbericator for a pressure event and <value> for the intensity
                of the pressure (0..127).


### ButtonStateXY( [mode], [returnPressure] )

    Returns the state of the buttons in X/Y mode and optionally the pressure value.
    
    Notice that this is not directly compatible with the "Mk1" ButtonStateRaw()
    method, which returns [ <button>, <True/False> ].

    Only the Pro, X and Pro Mk3 support pressure events.
    They can be enables by passing "returnPressure=True" to the method call.
    Notice that the Pro and X behave differently:

    Pro and Pro Mk3:
      There is only one pressure value for all buttons together. If multiple buttons
      are pressed, the biggest value is returned. There is no possibility to determine
      which button caused it. To distinguish the pressure events from button events,
      fake coordinates of "255" are returned in the list: [ 255, 255, <value>].

    X:
      The X supports multiple pressure values. For a distinction between button events
      and pressure events, "255" is added to the coordinate:
       [ <x> + 255, <y> + 255, <value> ]

      PARAMS: <mode>       OPTIONAL: "pro" selects new x/y origin >>> PRO ONLY <<<
      RETURN: [ ]                    An empty list if no event occured, otherwise...
              [ <x>, <y>, <value> ]  ... a list with three fields:
                <x> and <y> are the button's coordinates. The third field, <value> determines
                the intensity (0..127) with which the button was pressed.
                0 means that the button was released.
                Notice that "Mk2" Pads will only return either 0 or 127.
                They don't have the full analog mode like the "Pro" has.
              [ 255, 255, <value> ]             ... PRO: a list of pressure events with two fields:
                "255" as an indicator for a pressure event and <value> for the the intensity
                of the pressure (0..127).
              [ <x> + 255, <y> + 255, <value> ] ... LPX: a list of pressure events with two fields:
                "255" added to the <x> and <y> coordinates for a pressure event and <value> for the intensity
                of the pressure (0..127).



---
## Detailed description of Launch Control and Control XL specific methods

*WORK IN PROGRESS*


### TemplateSet( template )

    Activates one of the user or factory templates, as specified by <template>.
    Don't touch this, unless you know what you are doing. Settings other values
    than "1", the default, might have an impact on other functionality like LedAllOn().
    
      PARAMS: 1.. 8    activate user template    1..8
              9..16    activate factory template 1..8
      
      RETURN:


### Reset()

    Resets the Launchpad and (quickly) turns off all LEDs.
    Only resets the currently active template.

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


### InputChanged()

    Returns True if a button or potentiometer event occured. False otherwise.

      PARAMS:
      RETURN: True/False


### InputFlush()

    Flushes the Launch Control XL's input buffer.
    If you do not poll the buttons or potentiometer values frequently or even if your software
    is not running, the Launch Control XL will store each event in its buffer.
    This function can be used to clear all button and potentiometer events.

      PARAMS:
      RETURN:


### InputStateRaw()

    Returns the state of the buttons or the value of the last potentiometer change in RAW mode.

    In case the last event was caused by a button being pressed or released, this function
    returns the button number and either "True" or "False" or if a potentiometer was rotated
    or a slider moved, its value (0..127).

    Notice that this is different from other's Launchpad "ButtonStateRaw()" methods, as it
    forces you to check whether the 2nd field is a number or a boolean value.

    Notice that the Control XL buttons do not support an analog velocity value.
    For compatibility, either "0" or "127" are returned in the third list field, corresponding
    to "False" (0) or "True" (127).
  
      PARAMS:
      RETURN: [ ]                               An empty list if no event occured, otherwise either
              [ <button>, <True/False>, 0/127 ] the button number, True or False and the velocity
              [ <potnum>, <value>     , 0     ] the potentiometer number and its value 0..127
              <button> and <potnum> are the RAW button or potentiometer numbers, the second field
              either determines the state of the button ("True" if pressed, "False" if released) or
              returns the value of the potentiometer that was changed.
              
      EXAMPLES:
      
        xlEvent = lp.InputStateRaw()
        if xlEvent != []:
          if xlEvent[1] is True or xlEvent[1] is False:
            print( "Button        ", xlEvent[0], xlEvent[1] )
          else:
            print( "Potentiometer ", xlEvent[0], xlEvent[1] )


---
## Detailed description of LaunchKey (Mini) specific methods


### InputChanged()

    Returns True if a button, key or potentiometer event occured. False otherwise.

      PARAMS:
      RETURN: True/False


### InputFlush()

    Flushes the buffer of the LaunchKey (Mini)'s.
    If you do not poll the buttons, keys or potentiometer values frequently or even if your software
    is not running, the Launch Control XL will store each event in its buffer.
    This function can be used to clear all button and potentiometer events.

      PARAMS:
      RETURN:


### InputStateRaw()

    Returns the state of the buttons, keys or the value of the last potentiometer change in RAW mode.

    In case the last event was caused by a button being pressed or released, this function
    returns the button number and either "True" or "False" or if a potentiometer was rotated
    or a slider moved, its value (0..127).

    Notice that this is different from other's Launchpad "ButtonStateRaw()" methods, as it
    forces you to check whether the 2nd field is a number or a boolean value.

      PARAMS:
      RETURN: [ ]                                    An empty list if no event occured, otherwise either
              [ <button>, <True/False>, <velocity> ] the button number, True or False and the velocity
              [ <key>,    <True/False>, <velocity> ] the key number and its velocity 0..127
              [ <potnum>, <value>     , 0          ] the potentiometer number and its value 0..127
              <button>, <key> and <potnum> are the RAW button, key or potentiometer numbers, the second
              field either determines the state of the button or key ("True" if pressed, "False" if released)
              or returns the value of the potentiometer that was changed.
              
      EXAMPLES:
      
        lkEvent = lp.InputStateRaw()
        if lkEvent != []:
          if lkEvent[1] is True or lkEvent[1] is False:
            print( "Button/Key    ", lkEvent[0], lkEvent[1], lkEvent[2] )
          else:
            print( "Potentiometer ", lkEvent[0], lkEvent[1] )



---
## Detailed description of Dicer specific methods


### Reset()

    Resets the Dicer, (quickly) turns off all LEDs and restores the power-on defaults.
    Notice that an enabled light show will *not* be stopped.

      PARAMS:
      RETURN:


### ModeSet( device, mode )

    Enables on of the seven modes (or button and LED "pages") of the Dicer:
    
      0  cue
      1  cue + shift
      2  loop
      3  loop + shift
      4  auto loop 
      5  auto loop + shift
      6  one page mode
      
    See ButtonStateRaw(), LedCtrlRaw() or the Dicer's button and LED table at the end of this
    document to see how mode 0..5 work.
    
    If the "one page mode" is enabled, the mode buttons themselves do not select a bank anymore,
    but return a value instead.
    
      PARAMS: <device>     0 = master, 1 = slave
              <mode>       0..6 as specifies above
      RETURN:


### ButtonStateRaw()

    Returns the state of the buttons in (an already nicely mapped :) RAW mode.
    The returned numbers of the buttons equal the labels on the Dicer's buttons, with
    the following extension (also see the LED/button mapping ASCII drawing somewhere below):
    
    The three mode buttons "cue", "loop" and "auto loop" act as a modifier and add the following
    numbers to the button value.
    For "shift" operation, continue to hold down one of the three mode buttons while pressing a number.
    
      Master, "cue":        01 ..  05  +shift:  06 ..  10
      Master, "loop":       11 ..  15  +shift:  16 ..  20
      Master, "auto loop":  21 ..  25  +shift:  26 ..  30
    
      Slave,  "cue":       101 .. 105  +shift: 106 .. 110
      Slave,  "loop:       111 .. 115  +shift: 116 .. 120
      Slave,  "auto loop": 121 .. 115  +shift: 126 .. 130
      
    In "one page mode", the mode buttons do not have a special function but return a value upon being pressed:
    
      Master, "cue":         6
      Master, "loop":        7
      Master, "auto loop":   8

      Slave,  "cue":       106
      Slave,  "loop:       107
      Slave,  "auto loop": 108
    
    The mode can either be set by pushing/holding down the corresponding buttons
    or via ModeSet( <device>, <mode> ).
    
      PARAMS:
      RETURN: [ ]                                 An empty list if no event occured, otherwise
              [ <button>, <True/False>, <0/127> ] the button number, True or False and the velocity (only 0 or 127).
              


### LedSetLightshow( device, enable )

    Enables or disables the built-in LED light show of the Dicer.
    Notice that the dicer will do nothing (else) during the light show.

      PARAMS: <device>    0 selects master, 1 selects slave
              <enable>    True turns the light show on, False off
      RETURN:


### LedCtrlRaw( number, hue, intensity )

    Control an LED via its number, a hue and intensity information.
    The number of the LED to control corresponds to the button's labels 1..5,
    with the following modifiers:

      Master, "cue":        01 ..  05  +shift:  06 ..  10
      Master, "loop":       11 ..  15  +shift:  16 ..  20
      Master, "auto loop":  21 ..  25  +shift:  26 ..  30
    
      Slave,  "cue":       101 .. 105  +shift: 106 .. 110
      Slave,  "loop:       111 .. 115  +shift: 116 .. 120
      Slave,  "auto loop": 121 .. 115  +shift: 126 .. 130

    In "one page mode", the mode LEDs can be controlled via:
    
      Master, "cue":         6
      Master, "loop":        7
      Master, "auto loop":   8

      Slave,  "cue":       106
      Slave,  "loop:       107
      Slave,  "auto loop": 108

    The mode can either be set by pushing/holding down the corresponding buttons
    or via ModeSet( <device>, <mode> ).
    
    The color shade can be controlled with <hue>, avalue from 0..7:
    
      0  red
      1  red-orange
      2  orange
      3  orange-amber
      4  amber
      5  yellow
      6  yellow-green
      7  green

    I just leave that as it is. Complaints can be sent to Novation :'-)
        
    
      PARAMS: <number>     number of the LED (see Dicer mapping table somewhere below)
              <hue>        0..7 hue value (see text above)
              <intensity>  LED intensity value 0..15
      RETURN:


### LedAllOff()

    Quickly turns off all LEDs on all Dicers.
    No other settings are affected.


      PARAMS:
      RETURN:



---
## Detailed description of Midi Fighter specific methods

### Constants

#### LED Modes

    The following constants can be used instead of using integer values for the LED modes.

        MODE_BRIGHT[0..15]  instead of  18..33  for brightness
        MODE_TOGGLE[0..7]   instead of  34..41  for toggling
        MODE_PULSE[0..7]    instead of  42..49  for pulsing
        MODE_ANIM_SQUARE    instead of  50
        MODE_ANIM_CIRCLE    instead of  51
        MODE_ANIM_STAR      instead of  52
        MODE_ANIM_TRIANGLE  instead of  53

    Some examples:
      lp.LedAllOn( 5, 18 )  becomes lp.LedAllOn( 5, lp.MODE_BRIGHT[0] );  LED RED BUT OFF
      lp.LedAllOn( 5, 33 )  becomes lp.LedAllOn( 5, lp.MODE_BRIGHT[15] ); LED RED FULLY ON
      lp.LedAllOn( 5, 33 )  becomes lp.LedAllOn( 5, lp.MODE_BRIGHT[15] ); LED RED FULLY ON

    Accessing "out of bounds" list values will of course crash your app.


### ButtonStateRaw()

    Returns the state of the buttons in RAW mode.
    See table with button and LED numbers at the end of this document.

      PARAMS:
      RETURN: [ ]                        An empty list if no event occured, otherwise...
              [ <button>, <value> ]      ... a list with two fields:
                                         <button> is the RAW button number
                                         <value>  >0 = pressed; 0 = released


### ButtonStateXY()

    Returns the state of the buttons in X/Y mode.
    See table with coordinates at the end of this document.

      PARAMS:
      RETURN: [ ]                        An empty list if no event occured, otherwise...
              [ <x> , <y>, <value> ]     ... a list with three fields:
                                         <x>      0..7; x coordinate of button
                                         <y>      0..7; y coordinate of button
                                         <value>  >0 = pressed; 0 = released


### LedCtrlRaw( led, colorcode, [mode] )

    Controls an LED via its number <button> and <colorcode>.
    See table with button number at the end of this document.
    Color codes are somewhere above (see image).
    The optional <mode> parameter selects the brightness, toggling, flashing
    or animation setting of the LED.
    This also needs to be used to turn an LED comnpletely off.

      Values for mode:
        18..33: set brightness of the LED (0..15)
        34..41: set toggling speed from every 16 beats down to 1/8 beat
        42..49: set pulsing  speed from every 32 beats down to 1/8 beat (*)
        50:     animation set to square
        51:     animation set to circle
        52:     animation set to star
        53:     animation set to triangle

        (*) This might be an error in the manual, as it does not contain an 1/4 setting
            and starts at 1/32. Need to check ...

      As an alternative and instead of using the numbers above, these constants can be used.
      E.g. "LedAllOn( 5, lp.MODE_BRIGHT[5] )" for an intensity value of 5, from 0..15

        MODE_BRIGHT[0..15]
        MODE_TOGGLE[0..7]
        MODE_PULSE[0..7]
        MODE_ANIM_SQUARE
        MODE_ANIM_CIRCLE
        MODE_ANIM_STAR
        MODE_ANIM_TRIANGLE

      PARAMS: <led>         36..99; number of the LED to control
              <colorcode>   0..127; color code
              <mode>        [OPTIONAL] 18..53, see above
      RETURN:


### LedCtrlRawMode( led, mode )

    Controls the mode of an LED via its number <button> and <mode>.
    See table with button number at the end of this document.
    The <mode> parameter can be set to:

        18..33: set brightness of the LED (0..15)
        34..41: set toggling speed from every 16 beats down to 1/8 beat
        42..49: set pulsing  speed from every 32 beats down to 1/8 beat (*)
        50:     animation set to square
        51:     animation set to circle
        52:     animation set to star
        53:     animation set to triangle

        (*) This might be an error in the manual, as it does not contain an 1/4 setting
            and starts at 1/32. Need to check ...

      As an alternative and instead of using the numbers above, these constants can be used.
      E.g. "LedAllOn( 5, lp.MODE_BRIGHT[5] )" for an intensity value of 5, from 0..15

        MODE_BRIGHT[0..15]
        MODE_TOGGLE[0..7]
        MODE_PULSE[0..7]
        MODE_ANIM_SQUARE
        MODE_ANIM_CIRCLE
        MODE_ANIM_STAR
        MODE_ANIM_TRIANGLE

      PARAMS: <led>         36..99; number of the LED to control
              <mode>        18..53; see above
      RETURN:


### LedCtrlXY( x, y, colorcode )

    Controls an LED via its coordinates <x>/<y> and a <colorcode>.
    See table with coordinates at the end of this document.
    Color codes are somewhere above (see image).

      PARAMS: <x>           0..7; x coordinate
              <y>           0..7; y coordinate
              <colorcode>   0..127; color code
      RETURN:


### LedCtrlChar( char, color, [offsx = 0], [offsy = 0], [coloroff = 0] )

    Displays character <char> with a color of <color> and a
    lateral offset of <offsx> (-8..8) on the Midi Fighter.
    <offsy> does not have yet any function.
    The optional <coloroff> parameter specifies the background color.
    Notice that it is not possible to set this to "black" or off as the
    Midi Fighter doesn't support this.
    
    Also notice that this method is not compatible with the Launchpad "RGB-calls",
    because the Midi Fighter also lacks RGB support. For 500 bucks. Lol :-)
    
      lp.LedCtrlChar( 'a', 5, offsx = xvar, coloroff = 0 )

      PARAMS: <char>      one field string to display; e.g.: 'A'
              <color>     color of the character; see table and image somewhere above
              <offsx>     x offset of the character on the main, 8x8 matrix (-8..8)
                          Negative is left and positive right.
              <offsy>     no function
              <coloroff>  color of the background; see table and image somewhere above
      RETURN:

      EXAMPLES:
              # scroll a red 'A' from left to right
              for x in range( -8, 9 ):
                lp.LedCtrlChar( 'A', 3, 0, offsx = x )
                time.wait( 100 ) # from PyGame (from pygame import time)


### LedCtrlString( string, color, [coloroff = 0], [direction = 0], [waitms = 150] )

    Scrolls <string> across the Midi Fighter's 8x8 matrix.
    <color> specifies the color of the string and <coloroff> the background.
    <direction> determines the direction of scrolling.
    <waitms>, by default 150, delays the scrolling speed.
    
    For future compatibility, it is highly recommended to use
    <direction> and <waitms> as a named arguments, e.g.:
    
      lp.LedCtrlString( "Hello", 3,1, direction = -1, waitms = 100 )

      PARAMS: <string>     a string to display; e.g.: 'Hello'
              <color>      color of the character; see color table
              <coloroff>   color of the background; see color table
              <direction> -1 -> scroll right to left
                           0 -> do not scroll, just show the character
                           1 -> scroll left to right
              <waitms>     OPTIONAL: delay for scrolling speed, default 150
      RETURN:


### LedAllOn( [colorcode], [mode] )

    Quickly sets all LEDs to white or an optional color of <colorcode>
    and a mode setting of <mode>.
    To turn the LEDs off, set their brightness to "0" via the <mode> parameter:

        18..33: set brightness of the LED (0..15)
        34..41: set toggling speed from every 16 beats down to 1/8 beat
        42..49: set pulsing  speed from every 32 beats down to 1/8 beat (*)
        50:     animation set to square
        51:     animation set to circle
        52:     animation set to star
        53:     animation set to triangle

        (*) This might be an error in the manual, as it does not contain an 1/4 setting
            and starts at 1/32. Need to check ...

      As an alternative and instead of using the numbers above, these constants can be used.
      E.g. "LedAllOn( 5, lp.MODE_BRIGHT[5] )" for an intensity value of 5, from 0..15

        MODE_BRIGHT[0..15]
        MODE_TOGGLE[0..7]
        MODE_PULSE[0..7]
        MODE_ANIM_SQUARE
        MODE_ANIM_CIRCLE
        MODE_ANIM_STAR
        MODE_ANIM_TRIANGLE

      PARAMS: <colorcode>   0..127; color code
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
## Button and LED codes, Launchpad "Mk3" and "X" (RGB LEDs)

### RAW mode

    +---+---+---+---+---+---+---+---+  +---+
    | 91|   |   |   | 95|   |   | 98|  | 99|
    +---+---+---+---+---+---+---+---+  +---+
    
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
    +---+---+---+---+---+---+---+---+  +---+
    |0/0|   |2/0|   |   |   |   |   |  |2/8|  0
    +---+---+---+---+---+---+---+---+  +---+
     
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
## Button and LED codes, Launchpad "Pro Mk3" (RGB LEDs)

### LED and and button numbers in RAW mode

    +---+  +---+---+---+---+---+---+---+---+  +---+
    | 90|  | 91|   |   |   |   |   |   | 98|  | 99|
    +---+  +---+---+---+---+---+---+---+---+  +---+
            
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
           |101|102|   |   |   |   |   |108|
           +---+---+---+---+---+---+---+---+ 
           |  1|  2|   |   |   |   |   |  8|
           +---+---+---+---+---+---+---+---+ 


### LED and and button numbers in X/Y (classic) mode

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
           |/10|   |   |   |   |   |   |   |        10
           +---+---+---+---+---+---+---+---+ 

### LED and and button numbers in X/Y (pro) mode

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
           |   |2/9|   |   |   |   |   |8/9|         9
           +---+---+---+---+---+---+---+---+ 
           |   |   |   |   |   |   |   |/10|        10
           +---+---+---+---+---+---+---+---+ 



---
## Buttons, LED and potentiometer codes, Launch Control

Notice that the two "Templates" buttons on the top right cannot be controlled (NOP).


### RAW mode

          0   1   2   3   4   5   6   7      8    9
         
        +---+---+---+---+---+---+---+---+  +---++---+
     0  | 21| 22| 23| 24| 25| 26| 27| 28|  |NOP||NOP| 
        +---+---+---+---+---+---+---+---+  +---++---+
     1  | 41| 42| 43| 44| 45| 46| 47| 48|  |114||115| 
        +---+---+---+---+---+---+---+---+  +---++---+
        +---+---+---+---+---+---+---+---+  +---++---+
     2  |  9| 10| 11| 12| 25| 26| 27| 28|  |116||117| 
        +---+---+---+---+---+---+---+---+  +---++---+



### X/Y mode

*PRELIMINARY*

          0   1   2   3   4   5   6   7      8    9
         
        +---+---+---+---+---+---+---+---+  +---++---+
        | - | - | - | - | - | - | - | - |  |NOP||NOP| 
        +---+---+---+---+---+---+---+---+  +---++---+
     1  | - | - | - | - | - | - | - | - |  |8/1||9/1| 
        +---+---+---+---+---+---+---+---+  +---++---+
        +---+---+---+---+---+---+---+---+  +---++---+
     0  |0/0|   |   |   |   |   |   |7/0|  |8/0||9/0| 
        +---+---+---+---+---+---+---+---+  +---++---+


---
## Buttons, LED and potentiometer codes, Launch Control XL

Notice that the two "Templates" buttons on the top right cannot be controlled (NOP).


### RAW mode

        +---+---+---+---+---+---+---+---+  +---++---+
        | 13| 29| 45| 61| 77| 93|109|125|  |NOP||NOP| 
        +---+---+---+---+---+---+---+---+  +---++---+
        | 14| 30| 46| 62| 78| 94|110|126|  |104||105| 
        +---+---+---+---+---+---+---+---+  +---++---+
        | 15| 31| 47| 63| 79| 95|111|127|  |106||107| 
        +---+---+---+---+---+---+---+---+  +---++---+
        
        +---+---+---+---+---+---+---+---+     +---+
        |   |   |   |   |   |   |   |   |     |105| 
        |   |   |   |   |   |   |   |   |     +---+
        |   |   |   |   |   |   |   |   |     |106| 
        | 77| 78| 79| 80| 81| 82| 83| 84|     +---+
        |   |   |   |   |   |   |   |   |     |107| 
        |   |   |   |   |   |   |   |   |     +---+
        |   |   |   |   |   |   |   |   |     |108| 
        +---+---+---+---+---+---+---+---+     +---+
        
        +---+---+---+---+---+---+---+---+  
        | 41| 42| 43| 44| 57| 58| 59| 60| 
        +---+---+---+---+---+---+---+---+  
        | 73| 74| 75| 76| 89| 90| 91| 92| 
        +---+---+---+---+---+---+---+---+  


### X/Y mode

*PRELIMINARY*

          0   1   2   3   4   5   6   7      8    9
         
        +---+---+---+---+---+---+---+---+  +---++---+
     0  |0/1|   |   |   |   |   |   |   |  |NOP||NOP|  0
        +---+---+---+---+---+---+---+---+  +---++---+
     1  |   |   |   |   |   |   |   |   |  |   ||   |  1
        +---+---+---+---+---+---+---+---+  +---++---+
     2  |   |   |   |   |   |5/2|   |   |  |   ||   |  2
        +---+---+---+---+---+---+---+---+  +---++---+
                                               8/9
        +---+---+---+---+---+---+---+---+     +---+
        |   |   |   |   |   |   |   |   |     |   |    3(!)
        |   |   |   |   |   |   |   |   |     +---+
        |   |   |   |   |   |   |   |   |     |   |    4(!)
     3  |   |   |2/3|   |   |   |   |   |     +---+
        |   |   |   |   |   |   |   |   |     |   |    5(!)
        |   |   |   |   |   |   |   |   |     +---+
        |   |   |   |   |   |   |   |   |     |   |    6
        +---+---+---+---+---+---+---+---+     +---+
        
        +---+---+---+---+---+---+---+---+  
     4  |   |   |   |   |   |   |   |   |              4(!)
        +---+---+---+---+---+---+---+---+  
     5  |   |   |   |3/4|   |   |   |   |              5(!)
        +---+---+---+---+---+---+---+---+  



---
## Buttons, LED and potentiometer codes, LaunchKey Mini

Notice that the two "Octave" and the "INCONTROL" buttons cannot be controlled (NOP).
 
                   +---+---+---+---+---+---+---+---+
                   | 21| 22|...|   |   |   |   | 28|
     +---+---+---+ +---+---+---+---+---+---+---+---+ +---+  +---+
     |106|107|NOP| | 40| 41| 42| 43| 48| 49| 50| 51| |108|  |104| 
     +---+---+---+ +---+---+---+---+---+---+---+---+ +---+  +---+
     |NOP|NOP|     | 36| 37| 38| 39| 44| 45| 46| 47| |109|  |105| 
     +---+---+     +---+---+---+---+---+---+---+---+ +---+  +---+
     
     +--+-+-+-+--+--+-+-+-+-+-+--+--+-+-+-+--+--+-+-+-+-+-+--+---+
     |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |   |
     |  |4| |5|  |  | | | | | |  |  |6| | |  |  | | | | |7|  |   |
     |  |9| |1|  |  | | | | | |  |  |1| | |  |  | | | | |0|  |   |
     |  +-+ +-+  |  +-+ +-+ +-+  |  +-+ +-+  |  +-+ +-+ +-+  |   |
     | 48| 50| 52|   |   |   |   | 60|   |   |   |   |   | 71| 72|
     |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
     | C | D | E |...|   |   |   | C2| D2|...|   |   |   |   | C3|
     +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+


---
## Buttons and LED codes, Dicer

### Standard Mode

Button numbers equal the labels on the buttons, plus a number, 
as specified by the mode buttons.

For "shift-lock" operation, continue to hold down one of the
three mode buttons while pressing a number button.

    Master, "cue":        01 ..  05  +shift:  06 ..  10
    Master, "loop":       11 ..  15  +shift:  16 ..  20
    Master, "auto loop":  21 ..  25  +shift:  26 ..  30

    Slave,  "cue":       101 .. 105  +shift: 106 .. 110
    Slave,  "loop:       111 .. 115  +shift: 116 .. 120
    Slave,  "auto loop": 121 .. 115  +shift: 126 .. 130


              MASTER                            SLAVE
     +-----+  +-----+  +-----+        +-----+  +-----+  +-----+
     |#    |  |#    |  |     |        |#   #|  |#   #|  |    #|
     |  #  |  |     |  |  #  |        |  #  |  |     |  |  #  |
     |    #|  |    #|  |     |        |#   #|  |#   #|  |#    |
     +-----+  +-----+  +-----+        +-----+  +-----+  +-----+
      
     +-----+            +---+          +----+           +-----+
     |#   #|            | +0|          |  +0|           |    #|
     |     |            +---+          +----+           |     |
     |#   #|       +---+                    +----+      |#    |
     +-----+       |+10|                    |+110|      +-----+
                   +---+                    +----+
     +-----+  +---+                             +----+  +-----+
     |#   #|  |+20|                             |+100|  |     |
     |  #  |  +---+                             +----+  |  #  |
     |#   #|                                            |     |
     +-----+                                            +-----+


### One Page Mode

Button numbers equal the labels on the buttons.
The mode keys return:

    Master, "cue":         6
    Master, "loop":        7
    Master, "auto loop":   8

    Slave,  "cue":       106
    Slave,  "loop:       107
    Slave,  "auto loop": 108


              MASTER                            SLAVE
     +-----+  +-----+  +-----+        +-----+  +-----+  +-----+
     |#    |  |#    |  |     |        |#   #|  |#   #|  |    #|
     |  #  |  |     |  |  #  |        |  #  |  |     |  |  #  |
     |    #|  |    #|  |     |        |#   #|  |#   #|  |#    |
     +-----+  +-----+  +-----+        +-----+  +-----+  +-----+
      
     +-----+            +---+          +----+           +-----+
     |#   #|            | 6 |          | 108|           |    #|
     |     |            +---+          +----+           |     |
     |#   #|       +---+                    +----+      |#    |
     +-----+       | 7 |                    | 107|      +-----+
                   +---+                    +----+
     +-----+  +---+                             +----+  +-----+
     |#   #|  | 8 |                             | 106|  |     |
     |  #  |  +---+                             +----+  |  #  |
     |#   #|                                            |     |
     +-----+                                            +-----+


---
## (TODO) Led and Button codes, Midi Fighter 64

### RAW Mode

    +---+---+---+---+---+---+---+---+
    | 64|   |   | 67| 96|   |   | 99|
    +---+---+---+---+---+---+---+---+
    | 60|   |   | 63| 92|   |   | 95|
    +---+---+---+---+---+---+---+---+
    | 56|   |   | 59| 88|   |   | 91|
    +---+---+---+---+---+---+---+---+
    | 52|   |   | 55| 84|   |   | 87|
    +---+---+---+---+---+---+---+---+
    | 48|   |   | 51| 80|   |   | 83|
    +---+---+---+---+---+---+---+---+
    | 44|   |   | 47| 76|   |   | 79|
    +---+---+---+---+---+---+---+---+
    | 40|   |   | 43| 72|   |   | 75|
    +---+---+---+---+---+---+---+---+
    | 36|   |   | 39| 68|   |   | 71|
    +---+---+---+---+---+---+---+---+

### X/Y Mode

      0   1   2   3   4   5   6   7
    +---+---+---+---+---+---+---+---+
    |0/0|   |   |   |   |   |   |   | 0
    +---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   | 1
    +---+---+---+---+---+---+---+---+
    |   |   |   |   |   |5/2|   |   | 2
    +---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   | 3
    +---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   | 4
    +---+---+---+---+---+---+---+---+
    |   |   |   |   |4/5|   |   |   | 5
    +---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   | 6
    +---+---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |   | 7
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
[11]: https://creativecommons.org/licenses/by/4.0/
[12]: https://twitter.com/FMMT666/status/802869723910275072/video/1
[13]: https://github.com/FMMT666/launchpad.py/issues/9
[14]: https://novationmusic.de/support/product-downloads?product=Launchpad+MK1
[15]: https://twitter.com/FMMT666/status/871094540140240896
[16]: https://twitter.com/FMMT666/status/891077439023087618
[17]: https://github.com/FMMT666/launchpad.py/issues/24
[18]: https://twitter.com/FMMT666/status/967551405644025857
[19]: https://www.pygame.org/wiki/Compilation
[20]: https://github.com/FMMT666/launchpad.py/issues/38#issuecomment-519698406
[21]: https://twitter.com/FMMT666/status/1242950069923520519
[22]: https://twitter.com/FMMT666/status/1242978460454326272
[23]: https://twitter.com/FMMT666/status/1299842680533463043
[24]: https://twitter.com/FMMT666/status/1299478117497688073
[25]: https://www.midifighter.com/
