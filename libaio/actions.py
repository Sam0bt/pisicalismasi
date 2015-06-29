#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools,pisitools

# if pisi can't find source directory, see /var/pisi/libaio/work/ and:
# WorkDir="libaio-"+ get.srcVERSION() +"/sub_project_dir/"

#def setup():
    #shelltools.export("CFLAGS","CFLAGS=echo $CFLAGS ")
    #shelltools.system( sed -e 's/-fstack-protector//' && CXXFLAGS="$CFLAGS")
    #autotools.configure("--prefix=/usr")

#def build():
     #shelltools.cd("src")
     #shelltools.system("sudo make prefix=/usr install")

     #shelltools.system("install -D -m 644 libaio.h /usr/include/libaio.h")

def install():
    shelltools.system("sudo make prefix=/usr install")
    shelltools.system("sudo ln -sf libaio.so.1.0.1 /usr/lib/libaio.so.1")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.makedirs("%s/usr/include")
    shelltools.unlink(get.workDIR() + '/' + get.srcDIR() + "libaio.h")
    #pisitools.remove("/usr/include/libaio.h")
# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("libaio")

# You can use these as variables, they will replace GUI values before build.
# Package Name : libaio
# Version : 0.3.109
# Summary : hbn

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
