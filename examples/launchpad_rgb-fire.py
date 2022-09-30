#!/usr/bin/env python
"""Launchpad Fire Demo for Mk2, Mini Mk3, Pro, X, Pro Mk3"""
# FMMT666(ASkr) 7/2013..8/2020
# www.askrprojects.net
#

import sys

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        # noinspection PyPackageRequirements
        import launchpad
    except ImportError:
        sys.exit("ERROR: loading launchpad.py failed")

# import pygame
import random
from pygame import time


def limit(num, mini, maxi):
    """
    Get the number passed in, and return it if it is within the
    limits, otherwise return the closest limit
    """
    return max(min(maxi, num), mini)


def limit1(n):
    """
    Get the number passed in, and return it if it is within 0 and
    1, otherwise return the closest limit
    """
    return limit(n, 0.0, 1.0)


class Fire:
    """
    The Fire Matrix

    NO ERROR CHECKS. YOU HAVE BEEN WARNED!

    Args:  
    `xSize` (int): x size of the matrix  
    `ySize` (int): y size of the matrix  

    Returns:  
        `Fire`: a class Fire object if everything went fine  
        `None`: None if an error occured  
    """
    def __init__(self, xSize=8, ySize=8):
        """Returns an x/y value of the last button change as a list"""
        # The usage of floats might seem a bit rad here, but I wanted to
        # reuse this for sth else.
        # 0 -> minimum and 1.0 -> maximum intensity
        self.sizeX = xSize
        self.sizeY = ySize
        self.matrix = None  # becomes a 2D list of floats (yep,
        # no array.array due to mth)

        self.MatrixFill(0.0)  # fills self.Matrix

    def MatrixPrintDebug(self):
        """
        Prints the contents of the Fire matrix on the console; DEBUG ONLY

        The matrix is printed upsidedown, [0] bottom [sizeY] top, for
        better visibility.

        Returns:  
        Noting  
        """
        self.matrix.reverse()  # lol ;-)
        print("---")
        for yrow in self.matrix:
            for x in yrow:
                # Python 2
                sys.stdout.write("%5.1f" % x)
                sys.stdout.flush()
            # Python 3
            # print( '{:5.1f}'.format(x), end = "" )
            print("")
        self.matrix.reverse()

    def MatrixFill(self, value=None):
        """ Fills, aka completely creates a new matrix.

        Args:  
            `value` (float): update all matrix element with value of `value`  
            `value` (None):  fill matrix with random elements in 0.1 steps (
            0.0, 0.1 .. 1.0)

        Returns:  
            nothing  
        """
        if value is None:
            self.matrix = [
                [random.randint(0, 10) / 10.0 for _ in range(self.sizeX)] for _
                in range(self.sizeY)]
        else:
            self.matrix = [[limit1(float(value))] * self.sizeX for _ in
                           range(self.sizeY)]

    def MatrixSet(self, xyv):
        """ Sets elements of the matrix to a specific value.

        Args:  
            `xyv` (tuple): a tuple containing (x, y, v); x/y postition (int)
            and value (float)
            `xyv` (list):  a list of tuples  
        
        Returns:  
            `value` (int): Number of values written
        """
        if type(xyv) is tuple:
            xyv = [xyv]
        if type(xyv) is not list:
            return 0

        retVal = 0

        for tup in xyv:
            (x, y, v) = tup

            if x < 0 or x > self.sizeX - 1:
                return retVal
            if y < 0 or y > self.sizeY - 1:
                return retVal

            self.matrix[y][x] = limit1(float(v))
            retVal += 1

        return retVal

    def MatrixGetRow(self, y):
        """Get a list of the values of LEDs in a coloumn"""
        # TODO: return None instead of list w/ zeros?
        if y < 0 or y > self.sizeY - 1:
            return [0.0 for _ in range(self.sizeX)]

        return self.matrix[y]

    def MatrixGetValAtXY(self, x, y):
        """Get the value of an LED at the coordinates given"""
        if x < 0 or x > self.sizeX - 1:
            return 0.0
        if y < 0 or y > self.sizeY - 1:
            return 0.0

        return self.matrix[y][x]

    def MatrixGet3ValBelowXY(self, x, y):
        """
        Get the values for the LED at the coordinates specified and two below
        it
        """
        if y < 1 or y > self.sizeY:
            return None

        lstVal = []
        for i in range(3):
            lstVal.append(self.MatrixGetValAtXY(x - 1 + i, y - 1))

        return lstVal

    def MatrixEvolveAtXY(self, x, y):
        """Updates the Fire matrix at a single x/y position"""
        # self.MatrixSet( ( x, y, ( self.MatrixGetValAtXY( x, y ) + sum (
        # self.MatrixGet3ValBelowXY( x, y ) ) ) / 3.0 ) )

        valOwn = self.MatrixGetValAtXY(x, y)
        valBelow = sum(self.MatrixGet3ValBelowXY(x, y)) / 3.0 - 0.07 - (
                0.02 * random.random())
        # valYFac  = 1.0 - ( y / self.sizeY )
        valYFac = 1.0
        valRFac = 0.0

        valNew = valYFac * (valOwn + valBelow + valRFac) / 2.0

        self.MatrixSet((x, y, valNew))


    def MatrixEvolveRow(self, y):
        """Updates the Fire matrix for one row (y)"""
        for x in range(self.sizeX):
            self.MatrixEvolveAtXY(x, y)

    def MatrixEvolveAll(self):
        """Updates the complete Fire matrix, bottom to top"""
        for y in range(self.sizeY):
            self.MatrixEvolveRow(y + 1)


    def SeedSetAtX(self, x, value):
        """Sets the seed values (row 0)"""
        value = limit1(value)
        if x < 0 or x > self.sizeX - 1:
            return

        self.matrix[0][x] = value


    def SeedAddAtX(self, x, value):
        """Adds a value to the seed at position x"""
        if x < 0 or x > self.sizeX - 1:
            return

        self.matrix[0][x] = limit1(self.matrix[0][x] + value)

    def SeedSetRow(self, value):
        """Sets all seed values to one value"""
        value = limit1(value)

        for x in range(self.sizeX):
            self.matrix[0][x] = value

    def SeedRandom(self, min_=0.2, max_=0.8):
        """Sets all seeds to random values"""
        for x in range(self.sizeX):
            self.SeedSetAtX(x, limit(random.random(), min_, max_))

    def SeedAddFlickering(self, maxRandom):
        """Lets the seeds flicker"""
        for i in range(self.sizeX):
            self.SeedAddAtX(i, (0.5 - random.random()) * maxRandom)


class LpDisplay:
    """
    The Launchpad Display
    """

    def __init__(self):

        # remember the Launchpad type to adjust the mapping of the buttons
        self.mode = None

        # create an instance
        lp = launchpad.Launchpad()

        # try the first Mk2
        if lp.Check(name="mk2"):
            lp = launchpad.LaunchpadMk2()
            if lp.Open(name="mk2"):
                print(" - Launchpad Mk2: OK")
                self.mode = "mk2"
            else:
                print(" - Launchpad Mk2: ERROR")
                return

        # try the first Mini Mk3
        elif lp.Check(1, "minimk3"):
            lp = launchpad.LaunchpadMiniMk3()
            if lp.Open(1, "minimk3"):
                print(" - Launchpad Mini Mk3: OK")
                self.mode = "mk3"
            else:
                print(" - Launchpad Mini Mk3: ERROR")
                return

        # try the first Pro
        elif lp.Check(name="pad pro"):
            lp = launchpad.LaunchpadPro()
            if lp.Open(name="pad pro"):
                print(" - Launchpad Pro: OK")
                self.mode = "pro"
            else:
                print(" - Launchpad Pro: ERROR")
                return

        # try the first Pro Mk3
        elif lp.Check(name="mk3"):
            lp = launchpad.LaunchpadProMk3()
            if lp.Open():
                print(" - Launchpad Pro Mk3: OK")
                self.mode = "promk3"
            else:
                print(" - Launchpad Pro Mk3: ERROR")
                return

        # try the first X
        # Notice that this is already built-in in the LPX class' methods
        # Check() and Open,
        # but we're using the one from above!
        elif lp.Check(1, "Launchpad X") or lp.Check(1, "LPX"):
            lp = launchpad.LaunchpadLPX()
            # Open() includes looking for "LPX" and "Launchpad X"
            if lp.Open(1):
                print(" - Launchpad X: OK")
                self.mode = "lpx"
            else:
                print(" - Launchpad X: ERROR")
                return

        # nope
        else:
            raise Exception(
                "No compatible Launchpad found. Only for Mk2, Mk3, Pro")

        self.lp = lp

    def LiveMode(self):
        """Set the Launchpad to live mode"""
        if self.mode == "promk3":
            self.lp.LedSetMode(0)

    def Clear(self):
        """Reset the Launchpad"""
        self.lp.Reset()

    def Close(self):
        """Close the connection"""
        self.lp.Close()

    @staticmethod
    def CalcColorGradient(value):
        """ Returns a Launchpad RGB color value of a black-red-yellow-white
        color gradient

        Args:  
            `value`: float from 0.0 to 1.0  
        
        Returns:  
            `(R,G,B)`: a tuple with color information
        """
        value = limit1(value)

        # 63 max per channel -> 189 max, but - "a bit less" makes the
        # maximum color a bit more yellowish...
        rgbGradient = 150 * value
        r = limit1(rgbGradient / 63.0)
        rgbGradient -= r * 63
        g = limit1(rgbGradient / 63.0)
        rgbGradient -= g * 63
        b = limit1(rgbGradient / 63.0)
        rgbGradient -= b * 63

        # TODO: right now, this only returns a red...
        return int(r * 63.0), int(g * 63.0), int(b * 63.0)

    def UpdateRow(self, y, values):
        """Update a row of LEDs"""
        # WARNING: No error checks! (size)
        for i in range(8):
            (r, g, b) = self.CalcColorGradient(values[i])
            self.lp.LedCtrlXY(i, y, r, g, b)

    def ButtonGet(self):
        """Get if a button was pressed"""
        if self.mode == "pro" or self.mode == "promk3":
            return self.lp.ButtonStateXY()
        elif self.mode == "mk3" or self.mode == "lpx":
            return self.lp.ButtonStateXY()
        elif self.mode == "mk2":
            return self.lp.ButtonStateXY()

        return []

    def ButtonFlush(self):
        """Clear the button buffer"""
        self.lp.ButtonFlush()


if __name__ == '__main__':

    a = Fire()

    lpDis = LpDisplay()
    lpDis.Clear()

    a.SeedRandom()

    print("\nButtons (right column beside the 8x8 matrix):")

    print("  - upper right button -> EXIT")
    print("  - lower right button -> TURBO")

    while True:
        # calculate the next matrix state
        a.MatrixEvolveAll()

        # update the Launchpad's display
        for row in range(8):
            lpDis.UpdateRow(8 - row, a.MatrixGetRow(row))

        # add some flickering to the seeds
        a.SeedAddFlickering(0.2)
        # time.delay(20)

        # buttons
        buts = lpDis.ButtonGet()
        if buts:
            # print(buts)
            # --- turbo fire pressed
            #            if buts[0:2] == [ 0, 8 ] and buts[2]:
            if buts[0:2] == [8, 8] and buts[2]:
                a.SeedSetRow(0.8)
            # --- turbo fire released
            #            if buts[0:2] == [ 0, 8 ] and not buts[2]:
            if buts[0:2] == [8, 8] and not buts[2]:
                a.SeedSetRow(0.0)
            # --- matrix button
            # TODO:
            # That does not workj for the X (always spits out this message)
            if 0 < buts[0] < 9 and 0 < buts[1] < 9 and not buts[2]:
                print(
                    "Don't push the matrix buttons. Might create a lag ("
                    "pressure events).")
            # --- quit
            #            elif buts[0:2] == [ 0, 1 ]:
            elif buts[0:2] == [8, 1]:
                break

    lpDis.Clear()
    lpDis.LiveMode()
    lpDis.Close()
