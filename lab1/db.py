import pickle

def load(path):
	try:
		file = open(path, "rb")
		database = pickle.load(file)
		file.close()
		return database
	except Exception:
		return []

def save(database, path):
	file = open(path, "wb")
	pickle.dump(database, file)
	file.close()