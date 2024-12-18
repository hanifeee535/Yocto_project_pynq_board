Summary: Universal Boot Loader for embedded devices
Name: u-boot-digilent
Version: 2016.07
Release: r0
Epoch: 1
License: GPLv2+
Group: bootloaders
Packager: Poky <poky@yoctoproject.org>
URL: http://www.denx.de/wiki/U-Boot/WebHome
BuildRequires: bc-native
BuildRequires: dtc-native
BuildRequires: openssl-native
BuildRequires: virtual/arm-poky-linux-gnueabi-compilerlibs
BuildRequires: virtual/arm-poky-linux-gnueabi-gcc
BuildRequires: virtual/libc

%description
Universal Boot Loader for embedded devices.

%package -n u-boot-digilent-dbg
Summary: Universal Boot Loader for embedded devices - Debugging files
Group: devel

%description -n u-boot-digilent-dbg
Universal Boot Loader for embedded devices.  This package contains ELF
symbols and related sources for debugging purposes.

%package -n u-boot-digilent-staticdev
Summary: Universal Boot Loader for embedded devices - Development files (Static Libraries)
Group: devel
Requires: u-boot-digilent-dev = 1:2016.07-r0

%description -n u-boot-digilent-staticdev
Universal Boot Loader for embedded devices.  This package contains static
libraries for software development.

%package -n u-boot-digilent-dev
Summary: Universal Boot Loader for embedded devices - Development files
Group: devel
Requires: u-boot-digilent = 1:2016.07-r0

%description -n u-boot-digilent-dev
Universal Boot Loader for embedded devices.  This package contains symbolic
links, header files, and related items necessary for software development.

%package -n u-boot-digilent-doc
Summary: Universal Boot Loader for embedded devices - Documentation files
Group: doc

%description -n u-boot-digilent-doc
Universal Boot Loader for embedded devices.  This package contains
documentation.

%package -n u-boot-digilent-locale
Summary: Universal Boot Loader for embedded devices
Group: bootloaders

%description -n u-boot-digilent-locale
Universal Boot Loader for embedded devices.

%files
%defattr(-,-,-,-)
%dir "/boot"
"/boot/boot.bin-pynq-2016.07-r0"
"/boot/u-boot-pynq-2016.07-r0.elf"
"/boot/boot.bin"
"/boot/u-boot.elf"
"/boot/u-boot.img"
"/boot/u-boot-pynq-2016.07-r0.img"

%files -n u-boot-digilent-dbg
%defattr(-,-,-,-)

%files -n u-boot-digilent-dev
%defattr(-,-,-,-)

