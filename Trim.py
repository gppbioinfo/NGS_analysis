import argparse
import subprocess
import os
import sys
import re
import pandas as pd

# Initiate the parser

# add long and short arguement


def trimm(fdir, adpseq, mis, qts, proc, scode):
    if os.path.exists(fdir):
        print("exists")
        for fl in os.listdir(fdir):
            if re.search("_splited.fastq.gz", fl, flags=re.IGNORECASE):
               if fl.endswith(".gz"):
                   ifastq = re.sub(".gz", "", fl)
                   print("File is compressed, decompressing now")
                   if os.path.isfile(fdir+"/"+ifastq):
                       continue
                   else:
                        os.system("gunzip -rk "+fdir+"/"+fl)
                   outdir = re.sub(".fastq.gz", "", fl)
                   os.system("mkdir "+outdir+"_filtered")
                   os.system("flexbar -r "+fdir+"/"+ifastq+" -a "+adpseq+" -ao "+mis+" -ae 0.1 -t "+outdir+"_filtered/"+outdir+" -n "+proc+" -j -x 1 -y 1 -qt "+qts+" --fasta-output")
                   os.system("cut -d ' ' -f 1 "+outdir+"_filtered/"+outdir+".fasta > "+outdir+"_filtered/"+outdir+"1.fasta")
                   if int(scode) < 10:
                       os.system("collapse_reads_md.pl "+outdir+"_filtered/"+outdir+".fasta S0"+str(scode)+" > "+outdir+"_filtered/"+outdir+"_collapse.fa")
                       os.system("echo "+outdir+"_filtered/"+outdir+"1.fasta\tS0"+str(scode)+" >> reads_config.txt")
                   else:
                       os.system("collapse_reads_md.pl "+outdir+"_filtered/"+outdirs+".fasta S"+str(scode)+" > "+outdir+"_filtered/"+outdir+"_collapse.fa")
                       os.system("echo "+outdir+"_filtered/"+outdir+"1.fasta\tS"+str(scode)+" >> reads_config.txt")
               elif fl.endswith(".fastq"):
                   print("file is in fastq format")
                   outdir = re.sub(".fastq", "", fl)
                   os.system("mkdir " + outdir + "_filtered")
                   os.system("flexbar -r "+fdir+"/"+fl+" -a "+adpseq+" -ao "+mis+" -ae 0.1 -t "+outdir+"_filtered/"+outdir+" -n "+proc+" -j -x 1 -y 1 -qt "+qts+" --fasta-output")
                   os.system("cut -d ' ' -f 1 " + outdir + "_filtered/" + outdir + ".fasta > " + outdir + "_filtered/" + outdir + "1.fasta")
                   if int(scode) < 10:
                       os.system("collapse_reads_md.pl "+outdir+ "_filtered/" + outdir + ".fasta S0"+str(scode)+" > "+outdir+"_filtered/"+outdir+"_collapse.fa")
                       os.system("echo "+outdir+"_filtered/"+outdir+"1.fasta\tS0"+str(scode)+" >> reads_config.txt")
                   else:
                        os.system("collapse_reads_md.pl "+outdir+ "_filtered/" + outdir + ".fasta S"+str(scode)+" > "+outdir+"_filtered/"+outdir+"_collapse.fa")
                        os.system("echo "+outdir+"_filtered/"+outdir+"1.fasta\tS"+str(scode)+" >> reads_config.txt")
    else:
            print("File not exists!")


'''
if args.folder:
    trimm(args.folder)
if args.adpseq:
    trimm(args.adpseq)
if args.mis:
    trimm(args.mis)
if args.qt:
    trimm(args.qt)
if args.proc:
    trimm(args.proc)
'''
