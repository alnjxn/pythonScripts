import pygtk
pygtk.require('2.0')

import gtk

# Check for new pygtk: this is new class in PyGtk 2.4
if gtk.pygtk_version < (2,3,90):
   print "PyGtk 2.3.90 or later required for this example"
   raise SystemExit

# Find the simulation input file
#simulationInputFile = "/home/alan/Desktop/test.idf"
# What string are we looking for?
searchString = "$$ReplaceThis$$"
# What do we want to replace it with?
#angles = "0","90","180","270"
angles = range(0, 360)

dialog = gtk.FileChooserDialog("Open..",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
dialog.set_default_response(gtk.RESPONSE_OK)

filter = gtk.FileFilter()
filter.set_name("Text files")
filter.add_pattern("*.txt")
dialog.add_filter(filter)

response = dialog.run()

if response == gtk.RESPONSE_OK:
    #print dialog.get_filename(), 'selected'
    simulationInputFile = dialog.get_filename()
elif response == gtk.RESPONSE_CANCEL:
    print 'Closed, no files selected'
dialog.destroy()

#simulationInputFile = chooser.get_filename()

# For every replacement value in list of values:
for thisAngle in angles:
    # Open the input file
    inputFile = open(simulationInputFile)
    # Open the output file
    outputFileName = "/home/alan/Desktop/out/output-" + str(thisAngle) + "-degree-rotation.idf";
    outputFile = open(outputFileName,'w')
    print "Now writing file:", outputFileName    
 
    # For every line in the input file:
    for line in inputFile:
        # If searchString is found, replace it with thisAngle
        #newLine = line.replace(searchString, thisAngle)
        newLine = line.replace(searchString, str(thisAngle))
        # Write the line to the output file
        outputFile.write(newLine)
    outputFile.close()
    print "Finished writing!"
 
inputFile.close()
print "Finished the whole script!"
