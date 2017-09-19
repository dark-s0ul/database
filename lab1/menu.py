import os

items = [
	"Show the database",
	"Add entry to the database",
	"Remove entry from the database",
	"Clear the database",
	"Modify entry in the database",
	"Filter database",
	"Save & Exit",
	"Exit without Save"
]

def clear():
	os.system("clear")

def show():
	i = 1
	for item in items:
		print "%i. %s" % (i, item)
		i += 1

def get():
	num = read("Input the number you would like to choose: ")
	while (num < 1) or (num > len(items)):
		num = read("Re-enter number: ")
	return num

def pause():
	raw_input("Press Enter to continue ...")

def read(text):
	try: return input(text)
	except Exception: return 0
