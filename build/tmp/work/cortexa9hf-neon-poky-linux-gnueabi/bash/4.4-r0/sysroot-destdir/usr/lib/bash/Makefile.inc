#
# Sample makefile for bash loadable builtin development
#
# Copyright (C) 2015 Free Software Foundation, Inc.     

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

PACKAGE = bash
VERSION = 4.4-release

PACKAGE_NAME = bash
PACKAGE_VERSION = 4.4-release

# Include some boilerplate Gnu makefile definitions.
prefix = /usr

exec_prefix = /usr
bindir = /usr/bin
libdir = /usr/lib
infodir = /usr/share/info
includedir = /usr/include

datarootdir = ${prefix}/share

loadablesdir = ${libdir}/bash
headersdir = /usr/include/bash

topdir = ../../../bash-4.4
BUILD_DIR = /bash/4.4-r0/build
srcdir = ../../../bash-4.4/examples/loadables
VPATH = ../../../bash-4.4/examples/loadables

# Support an alternate destination root directory for package building
DESTDIR =

INSTALL = install -c
INSTALL_PROGRAM = ${INSTALL}
INSTALL_SCRIPT = ${INSTALL}
INSTALL_DATA = ${INSTALL} -m 644
INSTALLMODE= -m 0755


CC = arm-poky-linux-gnueabi-gcc  -march=armv7-a -marm -mfpu=neon -mfloat-abi=hard -mcpu=cortex-a9 
RM = rm -f

SHELL = /bin/sh

host_os = linux-gnueabi
host_cpu = arm
host_vendor = poky

CFLAGS =  -O2 -pipe -g -feliminate-unused-debug-types  -DNON_INTERACTIVE_LOGIN_SHELLS -Wno-parentheses -Wno-format-security
LOCAL_CFLAGS = 
DEFS = -DHAVE_CONFIG_H
LOCAL_DEFS = -DSHELL

CPPFLAGS = 

BASHINCDIR = ${topdir}/include

SUPPORT_SRC = $(topdir)/support/

LIBBUILD = ${BUILD_DIR}/lib

INTL_LIBSRC = ${topdir}/lib/intl
INTL_BUILDDIR = ${LIBBUILD}/intl
INTL_INC = 
LIBINTL_H = 

CCFLAGS = $(DEFS) $(LOCAL_DEFS) $(LOCAL_CFLAGS) $(CFLAGS)

#
# These values are generated for configure by ${topdir}/support/shobj-conf.
# If your system is not supported by that script, but includes facilities for
# dynamic loading of shared objects, please update the script and send the
# changes to bash-maintainers@gnu.org.
#
SHOBJ_CC = arm-poky-linux-gnueabi-gcc -march=armv7-a -marm -mfpu=neon -mfloat-abi=hard -mcpu=cortex-a9 
SHOBJ_CFLAGS = -fPIC
SHOBJ_LD = ${CC}
SHOBJ_LDFLAGS = -shared -Wl,-soname,$@ -Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed
SHOBJ_XLDFLAGS = 
SHOBJ_LIBS = 
SHOBJ_STATUS = supported

INC = -I$(headersdir) -I$(headersdir)/include -I$(headersdir)/builtins

.c.o:
	$(SHOBJ_CC) $(SHOBJ_CFLAGS) $(CCFLAGS) $(INC) -c -o $@ $<

all:	example

example:	example.o
	$(SHOBJ_LD) $(SHOBJ_LDFLAGS) $(SHOBJ_XLDFLAGS) -o $@ example.o $(SHOBJ_LIBS)

example.o: example.c