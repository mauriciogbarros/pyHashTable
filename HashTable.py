class HashTable:
	def __init__(self):
		self.collection = {}

	def hash(self, key) -> int:
		ascii_total = 0
		for char in key:
			ascii_total += ord(char)
		return ascii_total

	def add(self, key, value) -> None:
		hash_key = self.hash(key)
		if hash_key in self.collection:
			self.collection[hash_key].update({key: value})
		else:
			self.collection[hash_key] = {key: value}

	def remove(self, key) -> None:
		hash_key = self.hash(key)
		if hash_key in self.collection and key in self.collection[hash_key]:
			del self.collection[hash_key][key]
					
	def lookup(self, key):
		hash_key = self.hash(key)
		if hash_key in self.collection:
			return self.collection[hash_key].get(key)
