##importing required libraries

import os
import sys
import subprocess
import re

##To make list of file names (give path if files are running from different folder)
list1 = ['Prot_seq1.fasta', 'Prot_seq10.fasta']

for i in list1:
    ##To extract the number from filename
    j = i.split('seq')[1]
    j = j.split('.')[0]
    #print(i)
    #print(j)
    # To make another file with change
    #subprocess.call("sed '/^>/ s/$/ Seq"+j+"/' "+i+" >/mnt/d/Random/Prot_seq"+j+"_1.fasta", shell = True)
    # To append same file
    subprocess.call("sed -i '/^>/ s/$/ Seq"+j+"/' "+i, shell = True)