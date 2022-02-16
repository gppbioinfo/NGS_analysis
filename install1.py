import os
import sys
import platform
import re



ospl=platform.system()
osname=platform.linux_distribution()[0]
arch = platform.machine()
#print(osname)
#print(arch)

if re.search("Linux|linux|unix|Unix|LINUX", ospl): #and re.search("ubuntu|Ubuntu|Debian|debian|UBUNTU", osname):
    print(osname)
    if "x86_64" in arch:
        print(arch)
    else:
        print("32 bits")
#elif re.search("centos|CENTOS|CentOS|centos", osname):
#    print(osname)
#    if "x86_64" in arch:
#        print(arch)
#    else:
#        print("32 bits")
elif re.search("Darwin|darwin", ospl):# and re.search("macos|MACOS|MAC", osname):
    print(osname)
    if "x86_64" in arch:
        print(arch)
        cht = os.system("conda list &>/dev/null && echo $?")
        if cht == 0:
            print("Conda already installed!")
            os.system("conda config --add channels defaults && conda config --add channels bioconda && conda config --add channels conda-forge")
            os.system("brew tap homebrew/dupes; brew install grep")
            os.system("git clone https://github.com/rajewsky-lab/mirdeep2.git")
            os.system("cd mirdeep2 && perl install.pl")                 
            #os.system("exit")
            os.system("conda init bash")
            os.system("exit")            
            os.system("conda create -n training bwa bowtie bowtie2 hisat2 star")
            os.system("conda activate training")	
            os.system("/usr/bin/ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)")
            os.system("tap brewsci/bio && brew install seqan && brew install brewsci/science/flexbar")
            os.system("exit")
            os.system("conda activate training")
        else:
            os.system("bash tools/X86_64_Linux/Miniconda3-latest-MacOSX-x86_64.sh")
            os.system("conda config --add channels defaults && conda config --add channels  bioconda && conda config --add channels conda-forge")
            os.system("conda init bash")
            os.system("conda create -n training bwa bowtie bowtie2 hisat2 star")
            os.system("conda activate training")	
            os.system("/usr/bin/ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)")
            os.system("tap brewsci/bio && brew install seqan && brew install brewsci/science/flexbar")
            os.system("exit")
            os.system("conda activate training")
       
    else:
        print("32 bits")
elif re.search("win|WIN|WINDOWS", ospl):
    print(osname)
    if "x86_64" in arch:
        print(arch)
    else:
        print("32 bits")
else:
    print("Can't find it!")
