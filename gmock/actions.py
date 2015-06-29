#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
# if pisi can't find source directory, see /var/pisi/gmock/work/ and:
# WorkDir="gmock-"+ get.srcVERSION() +"/sub_project_dir/"
#find -name \*.py -exec sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/env python2/' {} \;
shelltools.system("find -name \*.py -exec sed -i 's/root\/usr\/bin\/env python/root\/usr\/bin\/env python2/' {} \;;")
def setup():
    autotools.configure("--prefix=/usr \
                         --enable-external-gtest ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
   
# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("gmock")

# You can use these as variables, they will replace GUI values before build.
# Package Name : gmock
# Version : 1.6.0
# Summary : hj

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
