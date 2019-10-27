import sys
import fileinput

def usage():
    print("Usage: glu.py [file_name] [output_file] [variable_names]")

def error():
    print("Could not open the file. Exiting...")
    exit()

if len(sys.argv) < 4:
    usage()
else:
    glu_i = ""
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        error()
    
    filedata = f.read()
    for options in range(3, len(sys.argv)):
        filedata = filedata.replace(sys.argv[options], "glu" + glu_i)
        glu_i += "glu"
    
    new_f = open(sys.argv[2], "x")
    new_f.write(filedata)
    
    new_f.close()
    f.close()