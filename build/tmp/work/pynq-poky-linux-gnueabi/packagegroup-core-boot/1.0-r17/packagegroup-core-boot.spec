Summary: Minimal boot requirements
Name: packagegroup-core-boot
Version: 1.0
Release: r17
License: MIT
Group: base
Packager: Poky <poky@yoctoproject.org>
BuildRequires: virtual/arm-poky-linux-gnueabi-compilerlibs
BuildRequires: virtual/arm-poky-linux-gnueabi-gcc
BuildRequires: virtual/libc
Requires: base-files
Requires: base-passwd
Requires: busybox
Requires: device-tree
Requires: init-ifupdown
Requires: initscripts
Requires: modutils-initscripts
Requires: netbase
Requires: sysvinit
Requires: udev
Requires: update-alternatives-opkg

%description
The minimal set of packages required to boot the system

%package -n packagegroup-core-boot-dbg
Summary: Minimal boot requirements - Debugging files
Group: devel
Recommends: base-files-dbg
Recommends: base-passwd-dbg
Recommends: busybox-dbg
Recommends: device-tree-dbg
Recommends: init-ifupdown-dbg
Recommends: initscripts-dbg
Recommends: modutils-initscripts-dbg
Recommends: netbase-dbg
Recommends: sysvinit-dbg
Recommends: udev-dbg
Recommends: update-alternatives-opkg-dbg

%description -n packagegroup-core-boot-dbg
The minimal set of packages required to boot the system  This package
contains ELF symbols and related sources for debugging purposes.

%package -n packagegroup-core-boot-dev
Summary: Minimal boot requirements - Development files
Group: devel
Requires: packagegroup-core-boot = 1.0-r17
Recommends: base-files-dev
Recommends: base-passwd-dev
Recommends: busybox-dev
Recommends: device-tree-dev
Recommends: init-ifupdown-dev
Recommends: initscripts-dev
Recommends: modutils-initscripts-dev
Recommends: netbase-dev
Recommends: sysvinit-dev
Recommends: udev-dev
Recommends: update-alternatives-opkg-dev

%description -n packagegroup-core-boot-dev
The minimal set of packages required to boot the system  This package
contains symbolic links, header files, and related items necessary for
software development.

%package -n packagegroup-core-boot-ptest
Summary: Minimal boot requirements
Group: base

%description -n packagegroup-core-boot-ptest
The minimal set of packages required to boot the system

%files
%defattr(-,-,-,-)

%files -n packagegroup-core-boot-dbg
%defattr(-,-,-,-)

%files -n packagegroup-core-boot-dev
%defattr(-,-,-,-)

%files -n packagegroup-core-boot-ptest
%defattr(-,-,-,-)

