import sys

inputfile = open(sys.argv[1],"r")
outputfile = open(sys.argv[2],"w")

lines = inputfile.readlines() ## Take whole file as an array of strings
for line in lines:
    words = line.rstrip("\n").split(sep=",") ## Strip away newline then split into array
    name = words[0] ## First word in line is the name
    for word in words:
        if (word and word != name): ## Exclude empty words and the name
            outputfile.write(name + "," + word + "\n") ## Write to .csv format

inputfile.close()
outputfile.close()
