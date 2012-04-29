import re

def main():
	f = open("/Users/ajackson/Desktop/epfile.idf")
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
			print '"' + cName + '"' + " = CONSTRUCTION"
			print '\tTYPE\t\t= LAYERS'
			print '\tLAYERS\t\t= "' + cLayers + '"'
			print '\t..'
			print ''
			print '"' + cLayers + '" = LAYERS'
			print '\tMATERIAL\t\t= (',
			for item in x:
				print '"' + item + '",',
			print ')'
			print '\t..'
			print ''
		else:
			line = f.readline()

main()