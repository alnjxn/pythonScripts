from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory
from tkSimpleDialog import askstring
import tkMessageBox

root = Tk()

# What do we want to replace it with?
angles = (0, 90, 180, 270)

# Provide user with dialog box to select the IDF file to process
def userDialog():
	global getfile
	filename = askopenfilename(
		filetypes=[("All Files","*"),("IDF Files","*.idf")], 
		initialdir=["C:\\"], 
		title="Select IDF File to Process..")
	if filename == "":
		tkMessageBox.showinfo("Info", "User Cancelled")
	else:
		getfile = filename
		userEntry()

# Have user select the search string to be replaced
def userEntry():
	global searchstring
	searchstring = askstring(
		title="Search String",
		prompt="Enter Search String to be Replaced",
		initialvalue="$$ReplaceThis$$")
	if searchstring == None:
		tkMessageBox.showinfo("Info", "User Cancelled")
		quit()
	elif searchstring == "":
		tkMessageBox.showinfo("Info", "Invalid String")
		quit()
	else:
		userSave()

# Provide user with dialog box to select folder where processed
# files should be placed
def userSave():
	global getsave
	foldername = askdirectory(
		initialdir=["C:\\"],
		title="Select Output Directory...")

	if foldername == "":
		tkMessageBox.showinfo("Info", "User Cancelled")
		quit()
	else:
		getsave = foldername + "/"
		idfReplace(getfile)


def idfReplace(infile):
	# For every replacement value in list of values:
	for thisAngle in angles:
	    # Open the input file
	    idfFile = open(infile)
	    # Open the output file
	    outFileName = str(getsave) + "output-" + str(thisAngle) + "-degree-rotation.idf";
	    outFile = open(outFileName,'w')
	    print "Now writing file:", outFileName    
	 
	    # For every line in the input file:
	    for line in idfFile:
	        # If searchstring is found, replace it with thisAngle
	        newLine = line.replace(searchstring, str(thisAngle))
	        # Write the line to the output file
	        outFile.write(newLine)
	    outFile.close()
	    print "Finished writing!" 
	idfFile.close()
	print "Finished the whole script!"

	
# def main():
# 	gtk.main()
# 	return 0

if __name__ == "__main__":
    userDialog()

