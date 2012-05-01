from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename
import tkMessageBox
import sys
import re
import StringIO

def main():
    try:
        f = open(userDialog())
        o = open(userSave(), 'w')
        out = StringIO.StringIO()
        out.write(trnMat(f, o))
        out.write(trnAir(f, o))
        out.write(trnCon(f, o))
        print >>o, out.getvalue()
        f.close()
        o.close()
    except (RuntimeError, TypeError, NameError):
        print "Unexpected error:", sys.exc_info()[0]
        raise

# Provide user with dialog box to select the IDF file to process
def userDialog():
    filename = askopenfilename(
        filetypes=[('All Files','*'),('IDF Files','*.idf')], 
        initialdir=['C:\\'], 
        title='Select IDF File to Process ...')
    if filename == "":
        tkMessageBox.showinfo('Info', 'User Cancelled')
    else:
        return filename

# Provide user with dialog box to select folder where processed
# files should be placed
def userSave():
    savename = asksaveasfilename(
        filetypes=[('All Files','*'),('INP Files','*.inp')],
        initialdir = ['C:\\'],
        title='Save Output INP As ...',
        )
    if savename == "":
        tkMessageBox.showinfo("Info", "User Cancelled")
    else:
        return savename

# Translate all Construction definitions
def trnCon(f, o): 
    output = StringIO.StringIO()
    line = f.readline()
    x = []
    while line:
        str1 = 'Construction,'
        str2 = ';'
        str3 = ','
        str4 = 'CostSource:'
        
        if re.search(str4, line):
            break 
        elif re.search(str1, line):
            line = f.readline()
            cName = line.split(str3)[0].strip()
            cLayers = cName + ' Layers'
            line = f.readline()
            
            while (not re.search(str2, line)):
                x.append(line.split(str3)[0].strip())
                line = f.readline()
            x.append(line.split(str2)[0].strip())
            
            output.write('"' + cLayers + '" = LAYERS\n')
            output.write('\tMATERIAL\t\t= ( ')

            cnt = len(x)
            for item in x:
                if (cnt > 1):
                    output.write('"' + item + '", \n\t\t')
                else:
                    output.write('"' + item + '" ')
                cnt = cnt - 1
            del x[:]

            output.write(')\n')
            output.write('\t..\n\n')

            output.write('"' + cName + '"' + ' = CONSTRUCTION\n')
            output.write('\tTYPE\t\t= LAYERS\n')
            output.write('\tLAYERS\t\t= "' + cLayers + '"\n')
            output.write('\t..\n\n')

        else:
            line = f.readline()
    f.seek(0)
    return output.getvalue()

# Translate all Material definitions
def trnMat(f, o):
    output = StringIO.StringIO()
    line = f.readline()
    x = []
    while line:
        str1 = "Material,"
        str2 = ";"
        str3 = ","
        if re.search(str1, line):
            line = f.readline()            
            mName = line.split(str3)[0].strip()
            line = f.readline() 
            mRuff = line.split(str3)[0].strip()
            line = f.readline()
            mThck = line.split(str3)[0].strip()
            mThck = float(mThck) * 3.280840
            line = f.readline()
            mCond = line.split(str3)[0].strip()
            mCond = float(mCond) * 0.577789
            line = f.readline()
            mDens = line.split(str3)[0].strip()
            mDens = float(mDens) * 0.062428
            line = f.readline()

            if not re.search(str2, line):
                mSphe = line.split(str3)[0].strip()
                mSphe = float(mSphe) * 0.000239
                line = f.readline()
                mAbsT = line.split(str3)[0].strip()
                line = f.readline()
                mAbsS = line.split(str3)[0].strip()
                line = f.readline()
                mAbsV = line.split(str2)[0].strip()
            else:
                mSphe = line.split(str2)[0].strip()
                mSphe = float(mSphe) * 0.000239

            output.write('"' + mName + '" = MATERIAL\n')
            output.write('\tTYPE\t\t\t= PROPERTIES\n')
            output.write('\tTHICKNESS\t\t= ' + str(mThck) + '\n')
            output.write('\tCONDUCTIVITY\t= ' + str(mCond) + '\n')
            output.write('\tDENSITY\t\t\t= ' + str(mDens) + '\n')
            output.write('\tSPECIFIC-HEAT\t= ' + str(mSphe) + '\n')
            output.write('\t..\n\n')
        else:
            line = f.readline()
    f.seek(0)
    return output.getvalue()

# Translate all AirGap definitions
def trnAir(f, o):
    output = StringIO.StringIO()
    line = f.readline()
    x = []
    while line:
        str1 = "Material:AirGap,"
        str2 = ";"
        str3 = ","
        if re.search(str1, line):
            line = f.readline()            
            aName = line.split(str3)[0].strip()
            line = f.readline() 
            aRes = line.split(str2)[0].strip()
            aRes = float(aRes) * 5.674467

            output.write('"' + aName + '" = MATERIAL\n')
            output.write('\tTYPE\t\t\t= RESISTANCE\n')
            output.write('\tRESISTANCE\t\t= ' + str(aRes) + '\n')
            output.write('\t..\n\n')
        else:
            line = f.readline()
    f.seek(0)   
    return output.getvalue()

if __name__ == '__main__':
    main()