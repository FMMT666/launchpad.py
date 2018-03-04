#!/usr/bin/env python
#
# Launchpad Pro Fire Demo
# 
#
# FMMT666(ASkr) 7/2013..3/2018
# www.askrprojects.net
#

import sys


try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("ERROR: loading launchpad.py failed")

# import pygame
import random
from pygame import time



limit  = lambda n, minVal, maxVal: max( min( maxVal, n ), minVal )
limit1 = lambda n: limit( n, 0.0, 1.0 )


########################################################################################
### CLASS Fire
###
### *burp*
########################################################################################
class Fire:
	""" The Fire Matrix

		NO ERROR CHECKS. YOU HAVE BEEN WARNED!

		 Args:  
			`xSize` (int): x size of the matrix  
			`ySize` (int): y size of the matrix  

		 Returns:  
			`Fire`: a class Fire object if everything went fine  
			`None`: None if an error occured  
	"""

	#-------------------------------------------------------------------------------------
	#-- Returns an x/y value of the last button change as a list:
	#--
	#-------------------------------------------------------------------------------------
	def __init__( self, xSize = 8, ySize = 8 ):
		# The usage of floats might seem a bit rad here, but I wanted to reuse this for sth else.
		# 0 -> minimum and 1.0 -> maximum intensity
		self.sizeX = xSize
		self.sizeY = ySize
		self.matrix = None      # becomes a 2D list of floats (yep, no array.array due to fck mth)

		self.MatrixFill( 0.0 )  # fills self.Matrix

	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	def MatrixPrintDebug( self ):
		""" Prints the contents of the Fire matrix on the console; DEBUG ONLY

		The matrix is printed upsidedown, [0] bottom [sizeY] top, for
		better visibility.

		Args:  
			Nothing  

		Returns:  
			Noting  
		"""
		self.matrix.reverse() # lol ;-)
		print("---")
		for yrow in self.matrix:
			for x in yrow:
				# Python 2
				sys.stdout.write( "%5.1f" % x )
				sys.stdout.flush()
				# Python 3
				# print( '{:5.1f}'.format(x), end = "" )
			print("")
		self.matrix.reverse() 

	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	def MatrixFill( self, value = None ):
		""" Fills, aka completely creates a new matrix.

		Args:  
			`value` (float): update all matrix element with value of `value`  
			`value` (None):  fill matrix with random elements in 0.1 steps (0.0, 0.1 .. 1.0)  

		Returns:  
			nothing  
		"""
		if value is None:
			self.matrix = [ [ random.randint(0,10)/10.0 for i in range( self.sizeX ) ] for y in range( self.sizeY ) ]
		else:
			self.matrix = [ [ limit1(float(value)) ] * self.sizeX for y in range( self.sizeY ) ]

	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	def MatrixSet( self, xyv ):
		""" Sets elements of the matrix to a specific value.

		Args:  
			`xyv` (tuple): a tuple containing (x, y, v); x/y postition (int) and value (float)  
			`xyv` (list):  a list of tuples  
		
		Returns:  
			`value` (int): Number of values written
		"""
		if type( xyv ) is tuple:
			xyv = [ xyv ]
		if type( xyv ) is not list:
			return 0

		retVal = 0

		for tup in xyv:
			( x, y, v ) = tup

			if x < 0 or x > self.sizeX - 1:
				return retVal
			if y < 0 or y > self.sizeY - 1:
				return retVal

			self.matrix[y][x] = limit1( float(v) )
			retVal += 1

		return retVal

	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	def MatrixGetRow( self, y ):
 		# TODO: return None instead of list w/ zeros?		
		if y < 0 or y > self.sizeY - 1:
			return [ 0.0 for i  in range(self.sizeX) ]
		
		return self.matrix[y]

	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	def MatrixGetValAtXY( self, x, y ):
		if x < 0 or x > self.sizeX - 1:
			return 0.0
		if y < 0 or y > self.sizeY - 1:
			return 0.0
		
		return self.matrix[y][x]

	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	def MatrixGet3ValBelowXY( self, x, y ):
		if y < 1 or y > self.sizeY:
			return None

		lstVal = []
		for i in range(3):
			lstVal.append( self.MatrixGetValAtXY( x-1+i, y-1 ) )

		return lstVal

	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	""" Updates the Fire matrix at a single x/y position

	"""
	def MatrixEvolveAtXY( self, x, y ):
		# self.MatrixSet( ( x, y, ( self.MatrixGetValAtXY( x, y ) + sum ( self.MatrixGet3ValBelowXY( x, y ) ) ) / 3.0 ) )

		valOwn   = self.MatrixGetValAtXY( x, y ) 
		valBelow = sum( self.MatrixGet3ValBelowXY( x, y ) ) / 3.0  - 0.07 - (0.02*random.random())
		# valYFac  = 1.0 - ( y / self.sizeY )
		valYFac  = 1.0
		valRFac  = 0.0

		valNew   = valYFac * ( valOwn + valBelow + valRFac ) / 2.0 
		
		self.MatrixSet( ( x, y, valNew ) )


	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	""" Updates the Fire matrix for one row (y)

	"""
	def MatrixEvolveRow( self, y ):
		for x in range( self.sizeX ):
			self.MatrixEvolveAtXY( x, y )


	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	""" Updates the complete Fire matrix, bottom to top

	"""
	def MatrixEvolveAll( self ):
		for y in range( self.sizeY ):
			self.MatrixEvolveRow( y + 1 )


	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	""" Sets the seed values (row 0)

	"""
	def SeedSetAtX( self, x, value ):
		value = limit1( value )
		if x < 0 or x > self.sizeX - 1:
			return

		self.matrix[0][x] = value 


	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	""" Adds a value to the seed at position x

	"""
	def SeedAddAtX( self, x, value ):
		if x < 0 or x > self.sizeX - 1:
			return

		self.matrix[0][x] = limit1( self.matrix[0][x] + value )


	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	""" Sets all seed values to one value

	"""
	def SeedSetRow( self, value ):
		value = limit1( value )

		for x in range( self.sizeX ):
			self.matrix[0][x] = value


	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	""" Sets all seeds to random values

	"""
	def SeedRandom( self, min = 0.2, max = 0.8 ):

		for x in range( self.sizeX ):
			self.SeedSetAtX( x, limit( random.random(), min, max ) )


	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	""" Lets the seeds flicker

	"""
	def SeedAddFlickering( self, maxRandom ):

		for i in range( self.sizeX ):
			self.SeedAddAtX( i, (0.5 - random.random())*maxRandom )


########################################################################################
### CLASS LpDisplay
###
### The Launchpad Display
########################################################################################
class LpDisplay():
	""" Well, well, well, well, well...

	"""
	
	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	def __init__( self, name ):

		self.lp = launchpad.LaunchpadPro();

		if not self.lp.Open( 0, name ):
			raise Exception("No Launchpad Pro was found")

	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	def Clear( self ):
		self.lp.Reset()

	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	def CalcColorGradient( self, value ):
		""" Returns an Launchpad RGB color value of an black-red-yellow-white color gradient

		Args:  
			`value`: float from 0.0 to 1.0  
		
		Returns:  
			`(R,G,B)`: a tuple with color information
		"""
		value = limit1( value )

		# 63 max per channel -> 189 max, but - "a bit less" makes the
		# maximum color a bit more yellowish...
		rgbGradient = 150 * value
		r = limit1( rgbGradient / 63.0 )
		rgbGradient -= r * 63
		g = limit1( rgbGradient / 63.0 )
		rgbGradient -= g * 63
		b = limit1( rgbGradient / 63.0 )
		rgbGradient -= b * 63

		# TODO: right now, this only returns a red...
		return ( int( r*63.0) , int( g*63.0), int( b*63.0) )


	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	def UpdateRow( self, y, values ):
		# WARNING: No error checks! (size)
		for i in range(8):
			(r, g, b) = self.CalcColorGradient( values[i] )
			self.lp.LedCtrlXY( i, y, r, g, b )


	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	def ButtonGet( self ):
		return self.lp.ButtonStateXY( mode = "pro" )


	#-------------------------------------------------------------------------------------
	#-- 
	#-------------------------------------------------------------------------------------
	def ButtonFlush( self ):
		self.lp.ButtonFlush()


########################################################################################
###
########################################################################################
if __name__ == '__main__':

	a = Fire()

	lpDis = LpDisplay( "pro" )
	lpDis.Clear()

	a.SeedRandom()

	print("\nButtons:")
	print("  - upper left ('Shift') -> EXIT")
	print("  - lower left ('O')     -> TURBO")

	while True:
		# calculate the next matrix state
		a.MatrixEvolveAll()

		# update the Launchpad's display
		for row in range(8):
			lpDis.UpdateRow( 8-row, a.MatrixGetRow( row ) )

		# add some flickering to the seeds
		a.SeedAddFlickering( 0.2 )
		# time.delay(20)

		# buttons
		buts = lpDis.ButtonGet()
		if buts != []:
			# print(buts)
			# --- turbo fire pressed
			if buts[0:2] == [ 0, 8 ] and buts[2]:
				a.SeedSetRow( 0.8 )
			# --- turbo fire released
			if buts[0:2] == [ 0, 8 ] and not buts[2]:
				a.SeedSetRow( 0.0 )
			# --- matrix button
			if 0 < buts[0] < 9 and  0 < buts[1] < 9 and not buts[2]:
				print("Don't push the matrix buttons. Might create a lag (pressure events).")
			# --- quit
			elif buts[0:2] == [ 0, 1 ]:
				break

	lpDis.Clear()
