################################################################
# A wrapper script to perform NGS analysis for RNA-Seq, small RNA-Seq, etc.
# Under GNU open source license
################################################################

This program is designed to do NGS data analysis with minimal options. 


Description:

usage: QA2RNA-Seq.py [-h] [--seqType SEQTYPE] [--protocal PROTOCAL]
                     [--infile INFILE [INFILE ...]] [--barcode BARCODE]
                     [--barcodefile BARCODEFILE] [--adapter ADAPTER]
                     [--adapterfile ADAPTERFILE] [--qualityscore QUALITYSCORE]
                     [--mismatch MISMATCH] [--aligner ALIGNER]
                     [--aligner-path ALIGNER_PATH] [--genome GENOME]
                     [--transcriptome TRANSCRIPTOME] [--index INDEX]
                     [--gfffile GFFFILE] [--gtffile GTFFILE]
                     [--precursor PRECURSOR] [--mature MATURE]
                     [--quantification QUANTIFICATION] [--processor PROCESSOR]

optional arguments:
  -h, --help            show this help message and exit
  --seqType SEQTYPE, -sT SEQTYPE
                        Select read sequence protocal either RNA-Seq or
                        smallRNA-seq or WGS/Bisulfite/ChIP-Seq/CLIP/CLASH
  --protocal PROTOCAL, -p PROTOCAL
                        Select read type either Single end (SE) or Paired end
                        (PE)
  --infile INFILE [INFILE ...], -f INFILE [INFILE ...]
                        Examples: -f file1.fq file2.fq
  --barcode BARCODE, -b BARCODE
                        Barcode generated data answer in Yes/No
  --barcodefile BARCODEFILE, -bf BARCODEFILE
                        Provide barcode file in fasta format
  --adapter ADAPTER, -ad ADAPTER
                        Provide adapter sequence according to protocol in
                        fasta format
  --adapterfile ADAPTERFILE, -adf ADAPTERFILE
                        Provide adapter sequences file according to protocol
  --qualityscore QUALITYSCORE, -QS QUALITYSCORE
                        Quality score for read filtering
  --mismatch MISMATCH, -ms MISMATCH
                        Mismatch in adapter alignment
  --aligner ALIGNER, -al ALIGNER
                        Alignment program Tophat2/Hisat2/Bowtie2/BWA
  --aligner-path ALIGNER_PATH, -alpath ALIGNER_PATH
                        Please provide the executable path of
                        Tophat2/Hisat2/Bowtie2/BWA
  --genome GENOME, -g GENOME
                        Reference genome file
  --transcriptome TRANSCRIPTOME, -ts TRANSCRIPTOME
                        Reference transcriptome file for RSEM expression
                        analysis
  --index INDEX, -id INDEX
                        Genome index name. Tophat2/bowtie2 takes bowtie2 index
                        while others generated using their program
                        /Hisat2/Bowtie2/BWA
  --gfffile GFFFILE, -gff GFFFILE
                        Reference genome annotation file GFF3
  --gtffile GTFFILE, -gtf GTFFILE
                        Reference genome GTF file
  --precursor PRECURSOR, -prec PRECURSOR
                        Precursor miRNA sequence file in fasta format
  --mature MATURE, -mat MATURE
                        mature miRNA sequence file in fasta format
  --quantification QUANTIFICATION, -qt QUANTIFICATION
                        Quantification/assembly by Cufflink/HTseq count
                        utility/RSEM expression calculation
  --processor PROCESSOR, -n PROCESSOR
                        Number of processor
			


Example 1: for RNA-Seq expression calculation

python3 QA2RNA-Seq.py -sT RNA -QS 30 --infile N2-1_CGATGT_L002_R1_001.fastq uY38-1_GCCAAT_L002_R1_001.fastq -ms 3 -n 20 -adf Current-Adapters.fa -al Hisat2 -g /media/ganesh/RA1/KSU/WormBase/w269/ensembl/Caenorhabditis_elegans.WBcel235.dna.toplevel.fa -gtf /media/ganesh/RA1/KSU/WormBase/w269/ensembl/Caenorhabditis_elegans.WBcel235.95.gtf -gff /media/ganesh/RA1/KSU/WormBase/w269/ensembl/Caenorhabditis_elegans.WBcel235.95.gff3 -qt cufflink 

Example 2: for small RNA-Seq based miRNA quantification

python3 QA2RNA-Seq.py -sT smallRNA --infile 7-N2-r2_S37_R1_001.fastq 9-84-r2_S38_R1_001.fastq -n 20 --barcodefile barcode_ip.fa --adapterfile smRNA-adp.fa --mismatch 3 -QS 25 --genome /media/ganesh/RA1/KSU/WormBase/w269/ensembl/Caenorhabditis_elegans.WBcel235.dna.toplevel.fa --precursor /media/ganesh/RA1/KSU/WormBase/w269/ensembl/cel_precursor-DNA.fa --mature /media/ganesh/RA1/KSU/WormBase/w269/ensembl/cel_mature-DNA.fa 			
