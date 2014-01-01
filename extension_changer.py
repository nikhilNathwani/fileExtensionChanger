import os.path
import os
import sys


def extension_changer(folder,old_ext,new_ext):
	os.chdir(folder)
	for f in os.listdir("."):
		name,ext= os.path.splitext(f)
		if ext=="."+old_ext:
			os.rename(f,name+"."+new_ext)	


if __name__ == "__main__":
	if len(sys.argv)==4:
		extension_changer(sys.argv[1],sys.argv[2],sys.argv[3])
		for f in os.listdir("."):
			print f
		print "Done!"
	else: 
		folder= raw_input('Enter desired folder path: ')
		old_ext= raw_input('Extension to be replaced? (don\'t need a \'.\'): ')
		new_ext= raw_input('Extension to be substituted in? (don\'t need a \'.\'): ')
		extension_changer(folder,old_ext,new_ext)
		for f in os.listdir("."):
			print f
		print "Done!"