import re
import StringIO

def main():
    f = open("/Users/ajackson/Desktop/epfile.idf")
    o = open("/Users/ajackson/Desktop/out.txt", "w")
    out = StringIO.StringIO()
    out.write(trnCon(f, o))
    out.write(trnMat(f, o))
    #print >>o, out.getvalue()
    print out.getvalue()
    f.close()

def trnCon(f, o): 
    output = StringIO.StringIO()
    line = f.readline()
    x = []
    while line:
        str1 = "Construction,"
        str2 = ";"
        str3 = ","
        if re.search(str1, line):
            line = f.readline()
            cName = line.split(str3)[0].strip()
            line = f.readline()
            
            while (not re.search(str2, line)):
                x.append(line.split(str3)[0].strip())
                line = f.readline()
            x.append(line.split(str2)[0].strip())

            cLayers = cName + ' Layers'
            output.write('"' + cName + '"' + " = CONSTRUCTION\n")
            output.write('\tTYPE\t\t= LAYERS\n')
            output.write('\tLAYERS\t\t= "' + cLayers + '"\n')
            output.write('\t..\n\n')
            output.write('"' + cLayers + '" = LAYERS\n')
            output.write('\tMATERIAL\t\t= ( ')

            cnt = len(x)
            for item in x:
                if (cnt > 1):
                    output.write('"' + item + '", ')
                else:
                    output.write('"' + item + '" ')
                cnt = cnt - 1
            del x[:]

            output.write(')\n')
            output.write('\t..\n\n')

        else:
            line = f.readline()
    f.seek(0)
    return output.getvalue()

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
            mThck = float(mThck) * 3.28
            line = f.readline()
            mCond = line.split(str3)[0].strip()
            line = f.readline()
            mDens = line.split(str3)[0].strip()
            line = f.readline()
            mSphe = line.split(str2)[0].strip()

            output.write('"' + mName + '" = MATERIAL\n')
            output.write('\tTYPE\t\t\t= PROPERTIES\n')
            output.write('\tTHICKNESS\t\t= ' + str(mThck) + '\n')
            output.write('\tCONDUCTIVITY\t= ' + mCond + '\n')
            output.write('\tDENSITY\t\t\t= ' + mDens + '\n')
            output.write('\tSPECIFIC-HEAT\t= ' + mSphe + '\n')
            output.write('\t..\n\n')
        else:
            line = f.readline()
    
    return output.getvalue()

if __name__ == '__main__':
    main()