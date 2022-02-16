

# 09r1IP_S24_R1_001_barcode -> folder name
# 7-N2-r2_S37_R1_001_barcode_7-N2-r2.fastq.gz -> Filename

$filjoin;
@file=();
opendir(GP, "$ARGV[0]") || die;
while($files=readdir(GP))
{
chomp($files);
#print "$files\n";
@sp = split("_",$files);

$st=$sp[5];
$st=~s/.fastq.gz//g;
#print "$sp[0]\t$st\n";
if($sp[0] eq $st || $files =~/unassigned/ || $files =~/^$st/ && $files !~/\.\./ && $files !~/\.$|\.log/)
{
#print "$files\n";

#$filjoin.="$ARGV[0]/$files ";
#if($files =~/^$st/ || $files =)
#{
	$filjoin.="$ARGV[0]/$files ";
	#print "$files\n";
#}

$lfiles=`ls *_barcode/* | grep "$st\\." | grep -v "unassigned\|\$s" | grep -v "^$st" | tr '\n' ' '`;
#print "ls *_barcode/* | grep \"$st\\.\" \n";


chomp($lfiles);
#print "$lfiles\n";

if($lfiles !~/unassigned/)
{
$filjoin.="$lfiles \n";
}

=head
@Lfile=join("\t",$lfiles);
foreach $fl(@Lfile)
{
chomp($fl);
#print "$fl\t$sp[5]\n";
if($fl =~/$st/)
{
print "$st\t$fl\n";
}
last;
}
=cut
#last;
}

}

$mdir=$ARGV[0];
$outfile=$ARGV[0];
$outfile=~s/_barcode//g;
$mdir=~s/_barcode/_join/g;

$filjoin=~s/\n//g; 
chomp($filjoin);

print "$filjoin\n";

`mkdir -p $mdir`;
`cp $filjoin $mdir/`;
`zcat $filjoin | gzip > $mdir/$outfile\_splited.fastq.gz`;

