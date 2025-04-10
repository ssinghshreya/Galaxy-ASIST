import subprocess
import os
import sys
if not os.path.exists("./out"):
  os.mkdir("out")

OUT_FOLDER = "out"

COMMAND_ARR = ["quast.py"]

COMMAND_ARR.extend(sys.argv[1:-1])

COMMAND_ARR.extend([ "-r" , sys.argv[-1] , "-o" , OUT_FOLDER])

subprocess.run(COMMAND_ARR)
