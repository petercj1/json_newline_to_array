import sys

try:
    inputfile = sys.argv[1]
except:
    raise Exception ("Input file must be specified as arg 1")

try:
    x = open(inputfile,"rb")
    x.close()
except:
    raise Exception("Could not read input file {0}".format(inputfile))

try:
    outputfile = sys.argv[2]
except:
    raise Exception("Output file must be specified as arg 2")

try:
    x = open(outputfile,"wb")
    x.close()
except:
    raise Exception("Could not open writable output file {0}".format(outputfile))

with open(outputfile,"wb") as o:
     o.write("[")
     with open(inputfile,"rb") as i:
             x=i.readlines()
             for l in range(len(x)-1):
                     o.write(x[l].rstrip())
                     o.write(",")
             o.write(x[-1])
     o.write("]")
