__author__ = 'AivanF'
__copyright__ = 'Copyright 2018, AivanF'
__contact__ = 'aivanf@mail.ru'
__version__ = '1.0.0'
__license__ = """License:
 This software is provided 'as-is', without any express or implied warranty.
 You may not hold the author liable.

 Permission is granted to anyone to use this software for any purpose,
 including commercial applications, and to alter it and redistribute it freely,
 subject to the following restrictions:

 The origin of this software must not be misrepresented. You must not claim
 that you wrote the original software. When use the software, you must give
 appropriate credit, provide a link to the original file, and indicate if changes were made.
 This notice may not be removed or altered from any source distribution.

 If you have any questions, feel free to write: """

class MDI:
	def __init__(self, tocheck, autoreset=True, label_index='_index', label_total='_total'):
		self.tocheck = tocheck
		self.label_index = label_index
		self.label_total = label_total
		self.autoreset = autoreset
		
		self.index = 0
		self.inds = {}
		self.lens = {}
		self.keys = []
		for key in self.tocheck:
			self.keys.append(key)
			self.inds[key] = 0
			self.lens[key] = len(self.tocheck[key])
		self.keycnt = len(self.keys)
		self.total = 1
		for key in self.lens:
			self.total *= self.lens[key]

	def reset(self):
		self.index = 0
		self.inds = {}
		for key in self.keys:
			self.inds[key] = 0

	def calc(self, task, since=0, to=-1, reset=None):
		# Reset indices if needed
		if reset is None:
			reset = self.autoreset
		if reset:
			self.reset()
		completed = False

		while not completed:
			# Finish if reached upper bound
			if to > 0 and self.index >= to:
				break
			
			# Calculate if lower bound was skipped
			if self.index >= since:
				values = {}
				for key in self.keys:
					values[key] = self.tocheck[key][self.inds[key]]
				if self.label_index is not None:
					values[self.label_index] = self.index
				if self.label_total is not None:
					values[self.label_total] = self.total
				res = task(values)
				# Break if False was returned
				if res is not None and res == False:
					break
			self.index += 1

			# Update indices
			completed = True
			for i in range(self.keycnt):
				key = self.keys[i]
				self.inds[key] += 1
				if self.inds[key] >= len(self.tocheck[key]):
					self.inds[key] = 0
					continue
				else:
					completed = False
					break
