import os
import sys
import re
import pandas as pd


# This is defined function to get miRNA quantification from filtered small RNA-Seq data associated in QA2RNA-Seq.py
# /homes/ganeshpanzade27/biotools/mirdeep2-master/bin/mapper.pl $configr -d -e -h -j -m -p $bindex -s cel_reads.fa -t cel_reads_vs_genome.arf -v -o 4

def miRqt(genome, prec, mature, proc):
    if os.path.isfile("reads_config.txt"):
        gt = re.sub(".fa|.fasta|.Fa|.FASTA","", genome)
        print(gt+"\t"+proc)
        if os.path.exists(gt+".1.ebwt"):
            print("Index file is present")
        else:
            print("Index is creating now")
            os.system("bowtie-build "+genome+" "+gt)
        os.system("mapper.pl reads_config.txt -d -c -j -m -p "+gt+" -s genome_mapped_collapse.fa -t genome_mapped.arf -v -o "+proc +" 2>mapper_log")
        os.system("quantifier.pl -c reads_config.txt -p "+prec+" -m "+mature+" -r genome_mapped_collapse.fa -y all_miRs -d -g 2 -e 4 -f 4 -T "+proc+" 2>quantifier_log")
    else:
        print("Read config file is not present, please provide correct file.")


#miRqt(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])