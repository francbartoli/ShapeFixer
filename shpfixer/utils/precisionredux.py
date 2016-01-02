from shapely.geometry import *
from utils import geomerremovertools

class PrecisionRedux(object):
	"""Class PrecisionRedux for managing the precision of geometries

	"""
	def __init__(self, arg):
		super(PrecisionRedux, self).__init__()
		self.arg = arg
		
	def round():
		pass

class PrecisionReduxPoint(PrecisionRedux):
	"""Derived class for Point"""

	def round_point(input):
		if isinstance (Point,input):

		pass

class PrecisionReduxMultiPoint(PrecisionRedux):
	"""Derived class for MultiPoint"""

	def round_multipoint(input):
		if isinstance (Multipoint,input):

		pass

class PrecisionReduxLineString(PrecisionRedux):
	"""Derived class for LineString"""

	def round_linestring(input):
		if isinstance (Linestring,input):

		pass

class PrecisionReduxMultiLineString(PrecisionRedux):
	"""Derived class for MultiLineString"""

	def round_multilinestring(input):
		if isinstance (MultiLinestring,input):

		pass
