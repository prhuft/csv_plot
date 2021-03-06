""" CSV Plot

	Preston Huft, January 2018
"""

#### Libraries 

import csv
from matplotlib import pyplot as plt

#### Classes

class CSV(object):

	def __init__(self,filename,skiplines):
		self.file = filename
		self.reader = self.get_reader()
		self.rows = self.get_rows(skiplines,1)
		self.cols = self.get_cols()
		self.header = self.get_header()
	
	def get_reader(self):
		f = open(self.file, 'r')
		return csv.reader(f)
		
	def get_rows(self,skip=None,debug=None):
		"""Returns a list of the rows of the csv file stored in self.reader."""
		rows = []
		iter = 0
		for row in self.reader:
			if skip is not None:
				if iter not in skip:
					rows.append(row)
			else:
				rows.append(row)
			iter = iter + 1
		if debug is not None:
			print(rows)
		return rows

	def get_cols(self,debug=None):
		"""Returns a list of the columns of the csv file stored in self.reader.
		Note that this method must be called after get_rows has be called."""
		cols = []
		try:
			for i in range(0, len(self.rows[0])):
				col = []
				for row in self.rows:
					col.append(row[i])
				cols.append(col)
			if debug is not None:
				print(cols)
			return cols
		except:
			print("The list of rows might be empty.")
		
	def get_header(self,debug=None):
		"""Returns the first row of the csv, without discerning whether the first
		row contains column titles. Note that this method must be called after
		get_rows has been called."""
		h = None
		for row in self.rows:
			h = row
			break
		if debug is not None:
			print(h)
		return h
			
#### Miscellaneous functions

def plot_cols(x,y,labels=None):
	"""For ``x`` a list of scalar reals and ``y`` a list of lists of scalar
	reals, returns a plot of the lists in ``y`` versus ``x``. ``labels`` should
	be left as None unless all data items have a label as the first element."""
	
	plt.plot(x,y)
				
#### Test it
skips = range(0,1)
n = CSV('ppl.csv', skips)


	