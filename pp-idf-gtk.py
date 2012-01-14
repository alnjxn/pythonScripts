import pygtk
pygtk.require('2.0')

import gtk

# Check for new pygtk: this is new class in PyGtk 2.4
if gtk.pygtk_version < (2,3,90):
   print "PyGtk 2.3.90 or later required for this example"
   raise SystemExit

# What string are we looking for?
searchString = "$$ReplaceThis$$"
# What do we want to replace it with?
angles = range(0, 360)

def idfReplace(inFile):
	# For every replacement value in list of values:
	for thisAngle in angles:
	    # Open the input file
	    #inFile = open(simulationinFile)
	    idfFile = open(inFile)
	    # Open the output file
	    outFileName = "/home/alan/Desktop/out/output-" + str(thisAngle) + "-degree-rotation.idf";
	    outFile = open(outFileName,'w')
	    print "Now writing file:", outFileName    
	 
	    # For every line in the input file:
	    for line in idfFile:
	        # If searchString is found, replace it with thisAngle
	        #newLine = line.replace(searchString, thisAngle)
	        newLine = line.replace(searchString, str(thisAngle))
	        # Write the line to the output file
	        outFile.write(newLine)
	    outFile.close()
	    print "Finished writing!" 
	idfFile.close()
	print "Finished the whole script!"

dialog = gtk.FileChooserDialog("Open..", None, 
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
    simulationinFile = dialog.get_filename()
    idfReplace(simulationinFile)
elif response == gtk.RESPONSE_CANCEL:
    print 'Closed, no files selected'
dialog.destroy()
