import os
directory = '/home/shreya/resfinder/sample fasta sequences/sequences'
for filename in os.listdir(directory):
	print(filename)
	cmd='python3 run_resfinder.py -s Other -l 0.6 -t 0.8 --acquired -ifq ' + filename +  " -o output_" + filename
	print(cmd)
	os.system(cmd) 