import sys
workingDirectory = sys.path[0] + "\\" ## Get path to the directory the code was called from
inputPath = workingDirectory + sys.argv[1]
outputPath = workingDirectory + sys.argv[2]
sepChar = "," ## TODO: take sys.argv[3] and use it as the separator character, "," if undefined

if (inputPath != outputPath):
    try:
        inputfile = open(inputPath,"r")
        outputfile = open(outputPath,"w")

        lines = inputfile.readlines() ## Take whole file as an array of strings
        for line in lines:
            words = line.rstrip("\n").split(sep=sepChar) ## Strip away newline then split into array
            name = words[0] ## First word in line is the name
            for word in words:
                if (word and word != name): ## Exclude empty words and the name
                    outputfile.write(name + sepChar + word + "\n") ## Write to .csv format                    
    finally:
        inputfile.close()
        outputfile.close()
