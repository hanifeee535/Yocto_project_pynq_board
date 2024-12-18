Summary: Device Trees for BSPs
Name: device-tree
Version: 1.0
Release: r0
License: MIT & GPLv2
Group: bsp
Packager: Poky <poky@yoctoproject.org>
BuildRequires: dtc-native

%description
Device Tree generation and packaging for BSP Device Trees.

%package -n device-tree-dbg
Summary: Device Trees for BSPs - Debugging files
Group: devel

%description -n device-tree-dbg
Device Tree generation and packaging for BSP Device Trees.  This package
contains ELF symbols and related sources for debugging purposes.

%package -n device-tree-staticdev
Summary: Device Trees for BSPs - Development files (Static Libraries)
Group: devel
Requires: device-tree-dev = 1.0-r0

%description -n device-tree-staticdev
Device Tree generation and packaging for BSP Device Trees.  This package
contains static libraries for software development.

%package -n device-tree-dev
Summary: Device Trees for BSPs - Development files
Group: devel
Requires: device-tree = 1.0-r0

%description -n device-tree-dev
Device Tree generation and packaging for BSP Device Trees.  This package
contains symbolic links, header files, and related items necessary for
software development.

%package -n device-tree-doc
Summary: Device Trees for BSPs - Documentation files
Group: doc

%description -n device-tree-doc
Device Tree generation and packaging for BSP Device Trees.  This package
contains documentation.

%package -n device-tree-locale
Summary: Device Trees for BSPs
Group: bsp

%description -n device-tree-locale
Device Tree generation and packaging for BSP Device Trees.

%files
%defattr(-,-,-,-)
%dir "/boot"
%dir "/boot/devicetree"
"/boot/devicetree/devicetree.dtb"

%files -n device-tree-dbg
%defattr(-,-,-,-)

%files -n device-tree-dev
%defattr(-,-,-,-)

