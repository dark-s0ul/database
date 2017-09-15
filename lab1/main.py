from pc import PC
from gpu import GPU
from collection import Collection 
import menu
import db

def main():
	pcs = Collection(db.load("PCs.pickle"))
	gpus = Collection(db.load("GPUs.pickle"))

	while True:
		menu.clear()
		menu.show()

		num = menu.get()
		menu.clear()

		if num == 1:
			if not pcs.empty():
				print "%-15s %-15s | %-15s %-15s %-15s" % ("PC id", "PC name", "GPU id", "GPU vendor", "GPU model")
				for pc in pcs.entries:
					gpu = gpus.find("id", pc.gid)
					print "%-15s %-15s | %-15s %-15s %-15s" % (pc.id, pc.name, gpu.id, gpu.vendor, gpu.model)
			else: print "Database is empty"
		elif num == 2:
			id = raw_input ("Enter unique id for PC: ")
			if pcs.find("id", id):
				print "Id '%s' is already used by PC" % id
			elif gpus.find("id", id): 
				print "Id '%s' is already used by GPU" % id
			else:
				name = raw_input ("Enter PC name: ")

				gid = raw_input ("Enter GPU id for PC: ")
				while pcs.find("id", gid) or gid == id: 
					gid = raw_input ("Id '%s' is already used by PC\nRe-enter: " % id)

				if not gpus.find("id", gid):
					vendor = raw_input("Enter GPU vendor: ")
					model = raw_input("Enter GPU model: ")
					gpus.add(GPU(gid, vendor, model))
				pcs.add(PC(id, name, gid))
		elif num == 3:
			id = raw_input ("Enter entry id: ")
			if not pcs.remove(pcs.find("id", id)):
				gpu = gpus.find("id", id)

				if not gpu: print "Entry with id '%s' doesnt exist" % id
				else:
					entries = pcs.findAll("gid", id)
					if entries == []: gpus.remove(gpu)
					elif raw_input("Delete %d PCs from database (Y/N)[default = 'N']: " % len(entries)).upper() == "Y":
						for pc in entries: pcs.remove(pc)
						gpus.remove(gpu)
		elif num == 4:
			pcs.clear()
			gpus.clear()
			print "Database is cleared"
		elif num == 5:
			id = raw_input ("Enter entry id: ")
			pc = pcs.find("id", id)
			if pc:
				pc.name = raw_input ("Enter PC name[default = %s]: " % pc.name) or pc.name
				gid = raw_input ("Enter GPU id for PC[default = %s]: " % pc.gid) or pc.gid
				while not gpus.find("id", gid) or gid == id:
					gid = raw_input ("GPU with id '%s' doesn't exist or already used by PC\nRe-enter[default = %s]: " % (gid, pc.gid)) or pc.gid
				pc.gid = gid
			else:
				gpu = gpus.find("id", id)
				if gpu:
					gpu.vendor = raw_input ("Enter new vendor for GPU[default = %s]: " % gpu.vendor) or gpu.vendor
					gpu.model = raw_input ("Enter new model for GPU[default = %s]: " % gpu.model) or gpu.model
				else: print "Entry with id '%s' doesnt exist" % id
		elif num == 6:
			id = raw_input ("Enter id: ")
			entries = pcs.findAll("id", id)
			if entries == []: entries = pcs.findAll("gid", id)
			if entries == []: print "Search result is empty"
			else:
				print "%-15s %-15s | %-15s %-15s %-15s" % ("PC id", "PC name", "GPU id", "GPU vendor", "GPU model")
				for pc in entries:
					gpu = gpus.find("gid", id)
					print "%-15s %-15s | %-15s %-15s %-15s" % (pc.id, pc.name, id, gpu.vendor, gpu.model)
		elif num == 7: break
		elif num == 8: return
		menu.pause()
	db.save(pcs.entries, "PCs.pickle")
	db.save(gpus.entries, "GPUs.pickle")

if __name__ == "__main__":
    main()