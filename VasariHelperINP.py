import re
import pygtk
pygtk.require('2.0')

import gtk

# Check for new pygtk: this is new class in PyGtk 2.4
if gtk.pygtk_version < (2,3,90):
   print "PyGtk 2.3.90 or later required for this example"
   raise SystemExit

def main():
	openDialog()
	
readFile = None

# get file to process
def openDialog():
	dialog = gtk.FileChooserDialog("Select INP File to Process..", None, 
		gtk.FILE_CHOOSER_ACTION_OPEN, 
		(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, 
		gtk.STOCK_OPEN, gtk.RESPONSE_OK))
	dialog.set_default_response(gtk.RESPONSE_OK)
	
	filter = gtk.FileFilter()
	filter.set_name("INP files")
	filter.add_pattern("*.inp")
	dialog.add_filter(filter)
	
	response = dialog.run()
	
	if response == gtk.RESPONSE_OK:
	    readFile = dialog.get_filename()
	    print readFile
	    procINP(readFile)
	elif response == gtk.RESPONSE_CANCEL:
	    print 'Closed, no files selected'
	dialog.destroy()
	
# search file for instance of space definition
def procINP(openFile):
	
	searchStr = "= SPACE"	
	f = open(openFile)
	
	count = 0
	
	for line in f:
		count = count + 1
		if searchStr in line:
			print count
    
    
	
# return line of instance

# find space name on that line

# store the string from lines above

# replace with new string

if __name__ == "__main__":
    main()
