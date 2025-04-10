from ast import arg
import py_compile
import quast 
import pandas as pd 
import sys
import subprocess
import abricate
#import asist_dynamic
#import clsi_profile

input = sys.argv[1]
#rg = sys.argv[2]
#input2 = sys.argv[2]


out = subprocess.run(['python','quast.py','input'], capture_output=True)
#out1 = subprocess.run(["abricate", "*"],capture_output=True)

#out3 = subprocess.run(["python","clsi_profile.py",input2],capture_output=True)

print(out)
