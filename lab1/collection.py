class Collection(object):
	def __init__(self, entries):
		self.entries = entries

	def add(self, entry):
		self.entries.append(entry)

	def remove(self, entry):
		if not entry: return False
		if not (entry in self.entries): return False
		self.entries.remove(entry)
		return True


	def find(self, key, attr):
		for entry in self.entries:
			if getattr(entry, key) == attr:
				return entry
		return None

	def findAll(self, key, attr):
		entries = []
		for entry in self.entries:
			if getattr(entry, key) == attr:
				entries.append(entry)
		return entries

	def empty(self):
		return self.entries == []

	def size(self):
		return len(self.entries)

	def clear(self):
		self.entries = []