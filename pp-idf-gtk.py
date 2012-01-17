import pygtk
pygtk.require('2.0')

import gtk

# Check for new pygtk: this is new class in PyGtk 2.4
if gtk.pygtk_version < (2,3,90):
   print "PyGtk 2.3.90 or later required for this example"
   raise SystemExit

class userEntry:
    def enter_callback(self, widget, entry):
        entry_text = entry.get_text()
        searchString = entry_text
        print "Entry contents: %s\n" % entry_text

    def entry_toggle_editable(self, checkbutton, entry):
        entry.set_editable(checkbutton.get_active())

    def entry_toggle_visibility(self, checkbutton, entry):
        entry.set_visibility(checkbutton.get_active())

    def __init__(self):
        # create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(225, 100)
        window.set_title("Search String")
        window.connect("delete_event", lambda w,e: gtk.main_quit())

        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()
        
        label = gtk.Label(str="Enter Search String to be Replaced:")
        vbox.pack_start(label, True, True, 0)
        label.show()
        
        entry = gtk.Entry()
        entry.set_max_length(50)
        entry.connect("activate", self.enter_callback, entry)
        entry.set_text("$$ReplaceThis$$")
        entry.select_region(0, len(entry.get_text()))
        vbox.pack_start(entry, True, True, 0)
        entry.show()

        hbox = gtk.HBox(False, 0)
        vbox.add(hbox)
        hbox.show()
                                  
        button = gtk.Button(stock=gtk.STOCK_OK)
        button.connect("clicked", self.enter_callback, entry)
        vbox.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()
        window.show()

def userSave():
	saveDialog = gtk.FileChooserDialog("Select output directory..", None, 
	gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER, 
	(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, 
	gtk.STOCK_OPEN, gtk.RESPONSE_OK))
	
	saveDialog.set_default_response(gtk.RESPONSE_OK)
	response = saveDialog.run()

def idfReplace(inFile):
	# For every replacement value in list of values:
	for thisAngle in angles:
	    # Open the input file
	    idfFile = open(inFile)
	    # Open the output file
	    outFileName = "/home/alan/Desktop/out/output-" + str(thisAngle) + "-degree-rotation.idf";
	    outFile = open(outFileName,'w')
	    print "Now writing file:", outFileName    
	 
	    # For every line in the input file:
	    for line in idfFile:
	        # If searchString is found, replace it with thisAngle
	        newLine = line.replace(searchString, str(thisAngle))
	        # Write the line to the output file
	        outFile.write(newLine)
	    outFile.close()
	    print "Finished writing!" 
	idfFile.close()
	print "Finished the whole script!"

def userDialog():
	dialog = gtk.FileChooserDialog("Select IDF File..", None, 
		gtk.FILE_CHOOSER_ACTION_OPEN, 
		(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, 
		gtk.STOCK_OPEN, gtk.RESPONSE_OK))
	dialog.set_default_response(gtk.RESPONSE_OK)
	
	filter = gtk.FileFilter()
	filter.set_name("IDF files")
	filter.add_pattern("*.idf")
	dialog.add_filter(filter)
	
	response = dialog.run()
	
	if response == gtk.RESPONSE_OK:
	    #print dialog.get_filename(), 'selected'
	    getFile = dialog.get_filename()
	    userEntry()
	    userSave()
	    idfReplace(getFile)
	elif response == gtk.RESPONSE_CANCEL:
	    print 'Closed, no files selected'
	dialog.destroy()

# What do we want to replace it with?
angles = (0, 90, 180, 270)
	
def main():
	gtk.main()
	return 0

if __name__ == "__main__":
    print "hello"
    main()

