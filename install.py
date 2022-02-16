import os
import sys
import platform
import re

osname=platform.linux_distribution()[0]
arch = platform.machine()
#print(osname)
#print(arch)

if re.search("ubuntu|Ubuntu|Debian|debian|UBUNTU", osname):
    print(osname)
    if "x86_64" in arch:
        print(arch)
    else:
        print("32 bits")
elif re.search("centos|CENTOS|CentOS|centos", osname):
    print(osname)
    if "x86_64" in arch:
        print(arch)
    else:
        print("32 bits")
elif re.search("macos|MACOS|MAC", osname):
    print(osname)
    if "x86_64" in arch:
        print(arch)
        os.system("bash tools/X86_64_Linux/Miniconda3-latest-MacOSX-x86_64.sh")


    else:
        print("32 bits")
elif re.search("win|WIN|WINDOWS", osname):
    print(osname)
    if "x86_64" in arch:
        print(arch)
    else:
        print("32 bits")
else:
    print("Can't find it!")
