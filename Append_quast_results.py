import sys
import os
a=os.listdir("#")
print (a)
for ln in a: 
          print(ln)
          ln1=ln.rstrip()
          cmd = 'python quast.py '  +ln1+  ' -r reference.fasta'
          print(cmd)
          os.system(cmd)
