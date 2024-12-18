Summary: Tiny versions of many common UNIX utilities in a single small executable
Name: busybox
Version: 1.24.1
Release: r0
License: GPLv2 & bzip2
Group: base
Packager: Poky <poky@yoctoproject.org>
URL: http://www.busybox.net
BuildRequires: initscripts
BuildRequires: kern-tools-native
BuildRequires: update-rc.d
BuildRequires: virtual/arm-poky-linux-gnueabi-compilerlibs
BuildRequires: virtual/arm-poky-linux-gnueabi-gcc
BuildRequires: virtual/libc
BuildRequires: virtual/update-alternatives
Requires: libc.so.6
Requires: libc.so.6(GLIBC_2.4)
Requires: libc6 >= 2.26
Requires: libm.so.6
Requires: libm.so.6(GLIBC_2.4)
Requires: rtld(GNU_HASH)
Requires: update-alternatives-opkg
Requires(post): libc.so.6
Requires(post): libc.so.6(GLIBC_2.4)
Requires(post): libc6 >= 2.26
Requires(post): libm.so.6
Requires(post): libm.so.6(GLIBC_2.4)
Requires(post): rtld(GNU_HASH)
Requires(post): update-alternatives-opkg
Requires(preun): libc.so.6
Requires(preun): libc.so.6(GLIBC_2.4)
Requires(preun): libc6 >= 2.26
Requires(preun): libm.so.6
Requires(preun): libm.so.6(GLIBC_2.4)
Requires(preun): rtld(GNU_HASH)
Requires(preun): update-alternatives-opkg
Requires(postun): libc.so.6
Requires(postun): libc.so.6(GLIBC_2.4)
Requires(postun): libc6 >= 2.26
Requires(postun): libm.so.6
Requires(postun): libm.so.6(GLIBC_2.4)
Requires(postun): rtld(GNU_HASH)
Requires(postun): update-alternatives-opkg
Recommends: busybox-syslog
Recommends: busybox-udhcpc
Provides: /bin/ash
Provides: /bin/cat
Provides: /bin/chattr
Provides: /bin/chgrp
Provides: /bin/chmod
Provides: /bin/chown
Provides: /bin/cp
Provides: /bin/cpio
Provides: /bin/date
Provides: /bin/dd
Provides: /bin/df
Provides: /bin/dmesg
Provides: /bin/dnsdomainname
Provides: /bin/dumpkmap
Provides: /bin/echo
Provides: /bin/egrep
Provides: /bin/false
Provides: /bin/fgrep
Provides: /bin/getopt
Provides: /bin/grep
Provides: /bin/gunzip
Provides: /bin/gzip
Provides: /bin/hostname
Provides: /bin/kill
Provides: /bin/ln
Provides: /bin/login
Provides: /bin/ls
Provides: /bin/mkdir
Provides: /bin/mknod
Provides: /bin/mktemp
Provides: /bin/more
Provides: /bin/mount
Provides: /bin/mv
Provides: /bin/netstat
Provides: /bin/pidof
Provides: /bin/ping
Provides: /bin/ping6
Provides: /bin/ps
Provides: /bin/pwd
Provides: /bin/rm
Provides: /bin/rmdir
Provides: /bin/run-parts
Provides: /bin/sed
Provides: /bin/sh
Provides: /bin/sleep
Provides: /bin/stat
Provides: /bin/stty
Provides: /bin/su
Provides: /bin/sync
Provides: /bin/tar
Provides: /bin/touch
Provides: /bin/true
Provides: /bin/umount
Provides: /bin/uname
Provides: /bin/usleep
Provides: /bin/vi
Provides: /bin/watch
Provides: /bin/zcat
Provides: /sbin/blkid
Provides: /sbin/depmod
Provides: /sbin/fdisk
Provides: /sbin/fsck
Provides: /sbin/fstrim
Provides: /sbin/getty
Provides: /sbin/halt
Provides: /sbin/hwclock
Provides: /sbin/ifconfig
Provides: /sbin/ifdown
Provides: /sbin/ifup
Provides: /sbin/insmod
Provides: /sbin/ip
Provides: /sbin/klogd
Provides: /sbin/loadkmap
Provides: /sbin/logread
Provides: /sbin/losetup
Provides: /sbin/lsmod
Provides: /sbin/mkswap
Provides: /sbin/modinfo
Provides: /sbin/modprobe
Provides: /sbin/pivot_root
Provides: /sbin/poweroff
Provides: /sbin/reboot
Provides: /sbin/rmmod
Provides: /sbin/route
Provides: /sbin/setconsole
Provides: /sbin/start-stop-daemon
Provides: /sbin/sulogin
Provides: /sbin/swapoff
Provides: /sbin/swapon
Provides: /sbin/switch_root
Provides: /sbin/sysctl
Provides: /sbin/syslogd
Provides: /sbin/udhcpc
Provides: /usr/bin/[
Provides: /usr/bin/[[
Provides: /usr/bin/awk
Provides: /usr/bin/basename
Provides: /usr/bin/bunzip2
Provides: /usr/bin/bzcat
Provides: /usr/bin/chrt
Provides: /usr/bin/chvt
Provides: /usr/bin/clear
Provides: /usr/bin/cmp
Provides: /usr/bin/cut
Provides: /usr/bin/dc
Provides: /usr/bin/deallocvt
Provides: /usr/bin/diff
Provides: /usr/bin/dirname
Provides: /usr/bin/du
Provides: /usr/bin/dumpleases
Provides: /usr/bin/env
Provides: /usr/bin/expr
Provides: /usr/bin/find
Provides: /usr/bin/flock
Provides: /usr/bin/free
Provides: /usr/bin/fuser
Provides: /usr/bin/groups
Provides: /usr/bin/head
Provides: /usr/bin/hexdump
Provides: /usr/bin/id
Provides: /usr/bin/killall
Provides: /usr/bin/less
Provides: /usr/bin/logger
Provides: /usr/bin/logname
Provides: /usr/bin/md5sum
Provides: /usr/bin/mesg
Provides: /usr/bin/microcom
Provides: /usr/bin/mkfifo
Provides: /usr/bin/nc
Provides: /usr/bin/nohup
Provides: /usr/bin/nslookup
Provides: /usr/bin/od
Provides: /usr/bin/openvt
Provides: /usr/bin/passwd
Provides: /usr/bin/patch
Provides: /usr/bin/printf
Provides: /usr/bin/readlink
Provides: /usr/bin/realpath
Provides: /usr/bin/renice
Provides: /usr/bin/reset
Provides: /usr/bin/resize
Provides: /usr/bin/seq
Provides: /usr/bin/sha1sum
Provides: /usr/bin/sha256sum
Provides: /usr/bin/shuf
Provides: /usr/bin/sort
Provides: /usr/bin/strings
Provides: /usr/bin/tail
Provides: /usr/bin/tee
Provides: /usr/bin/telnet
Provides: /usr/bin/test
Provides: /usr/bin/tftp
Provides: /usr/bin/time
Provides: /usr/bin/top
Provides: /usr/bin/tr
Provides: /usr/bin/traceroute
Provides: /usr/bin/tty
Provides: /usr/bin/uniq
Provides: /usr/bin/unlink
Provides: /usr/bin/unzip
Provides: /usr/bin/uptime
Provides: /usr/bin/users
Provides: /usr/bin/vlock
Provides: /usr/bin/wc
Provides: /usr/bin/wget
Provides: /usr/bin/which
Provides: /usr/bin/who
Provides: /usr/bin/whoami
Provides: /usr/bin/xargs
Provides: /usr/bin/yes
Provides: /usr/sbin/addgroup
Provides: /usr/sbin/adduser
Provides: /usr/sbin/chroot
Provides: /usr/sbin/delgroup
Provides: /usr/sbin/deluser
Provides: /usr/sbin/fbset
Provides: /usr/sbin/loadfont
Provides: /usr/sbin/rdate
Provides: /usr/sbin/rfkill
Provides: /usr/sbin/udhcpd

%description
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.

%package -n busybox-ptest
Summary: Tiny versions of many common UNIX utilities in a single small executable - Package test files
Group: devel
Requires: /bin/sh
Requires: busybox
Recommends: ptest-runner

%description -n busybox-ptest
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.  This package contains a test directory /usr/lib/busybox/ptest for
package test purposes.

%package -n busybox-httpd
Summary: Tiny versions of many common UNIX utilities in a single small executable
Group: base
Recommends: update-rc.d

%description -n busybox-httpd
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.

%package -n busybox-udhcpd
Summary: Tiny versions of many common UNIX utilities in a single small executable
Group: base
Requires: /bin/sh
Requires(pre): /bin/sh
Requires(post): /bin/sh
Requires(preun): /bin/sh
Requires(postun): /bin/sh
Recommends: update-rc.d

%description -n busybox-udhcpd
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.

%package -n busybox-udhcpc
Summary: Tiny versions of many common UNIX utilities in a single small executable
Group: base
Requires: /bin/sh

%description -n busybox-udhcpc
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.

%package -n busybox-syslog
Summary: Tiny versions of many common UNIX utilities in a single small executable
Group: base
Requires: /bin/sh
Requires(pre): /bin/sh
Requires(post): /bin/sh
Requires(preun): /bin/sh
Requires(postun): /bin/sh
Recommends: update-rc.d
Conflicts: rsyslog
Conflicts: sysklogd
Conflicts: syslog-ng

%description -n busybox-syslog
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.

%package -n busybox-mdev
Summary: Tiny versions of many common UNIX utilities in a single small executable
Group: base
Recommends: update-rc.d

%description -n busybox-mdev
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.

%package -n busybox-hwclock
Summary: Tiny versions of many common UNIX utilities in a single small executable
Group: base
Requires: /bin/sh
Requires(pre): /bin/sh
Requires(post): /bin/sh
Requires(preun): /bin/sh
Requires(postun): /bin/sh
Recommends: update-rc.d

%description -n busybox-hwclock
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.

%package -n busybox-dbg
Summary: Tiny versions of many common UNIX utilities in a single small executable - Debugging files
Group: devel
Recommends: libc6-dbg

%description -n busybox-dbg
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.  This package contains ELF symbols and related sources for
debugging purposes.

%package -n busybox-staticdev
Summary: Tiny versions of many common UNIX utilities in a single small executable - Development files (Static Libraries)
Group: devel
Requires: busybox-dev = 1.24.1-r0

%description -n busybox-staticdev
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.  This package contains static libraries for software development.

%package -n busybox-dev
Summary: Tiny versions of many common UNIX utilities in a single small executable - Development files
Group: devel
Requires: busybox = 1.24.1-r0
Recommends: initscripts-dev
Recommends: libc6-dev
Recommends: update-alternatives-opkg-dev
Recommends: update-rc.d-dev

%description -n busybox-dev
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.  This package contains symbolic links, header files, and related
items necessary for software development.

%package -n busybox-doc
Summary: Tiny versions of many common UNIX utilities in a single small executable - Documentation files
Group: doc

%description -n busybox-doc
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.  This package contains documentation.

%package -n busybox-locale
Summary: Tiny versions of many common UNIX utilities in a single small executable
Group: base

%description -n busybox-locale
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. It provides minimalist replacements for most of the
utilities you usually find in GNU fileutils, shellutils, etc. The utilities
in BusyBox generally have fewer options than their full-featured GNU
cousins; however, the options that are included provide the expected
functionality and behave very much like their GNU counterparts. BusyBox
provides a fairly complete POSIX environment for any small or embedded
system.

%post
# busybox - postinst
	# This part of code is dedicated to the on target upgrade problem.
	# It's known that if we don't make appropriate symlinks before update-alternatives calls,
	# there will be errors indicating missing commands such as 'sed'.
	# These symlinks will later be updated by update-alternatives calls.
	test -n 2 > /dev/null || alias test='busybox test'
	if test "x$D" = "x"; then
		# Remove busybox.nosuid if it's a symlink, because this situation indicates
		# that we're installing or upgrading to a one-binary busybox.
		if test -h /bin/busybox.nosuid; then
			rm -f /bin/busybox.nosuid
		fi
		for suffix in "" ".nosuid" ".suid"; do
			if test -e /etc/busybox.links$suffix; then
				while read link; do
					if test ! -e "$link"; then
						# we can use busybox here because even if we are using splitted busybox
						# we've made a symlink from /bin/busybox to /bin/busybox.nosuid.
						busybox rm -f $link
						busybox ln -s "/bin/busybox$suffix" $link
					fi
				done < /etc/busybox.links$suffix
			fi
		done
	fi
	if grep -q "^/bin/bash$" $D/etc/busybox.links*; then
		grep -q "^/bin/bash$" $D/etc/shells || echo /bin/bash >> $D/etc/shells
	fi
	update-alternatives --install /bin/gunzip gunzip /bin/busybox.nosuid 50
	update-alternatives --install /bin/zcat zcat /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/bunzip2 bunzip2 /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/bzcat bzcat /bin/busybox.nosuid 50
	update-alternatives --install /bin/cpio cpio /bin/busybox.nosuid 50
	update-alternatives --install /bin/gzip gzip /bin/busybox.nosuid 50
	update-alternatives --install /bin/tar tar /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/unzip unzip /bin/busybox.nosuid 50
	update-alternatives --install /bin/date date /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/groups groups /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/id id /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/shuf shuf /bin/busybox.nosuid 50
	update-alternatives --install /bin/sync sync /bin/busybox.nosuid 50
	update-alternatives --install /bin/touch touch /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/unlink unlink /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/users users /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/who who /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/awk awk /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/cmp cmp /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/diff diff /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/patch patch /bin/busybox.nosuid 50
	update-alternatives --install /bin/sed sed /bin/busybox.nosuid 50
	update-alternatives --install /bin/vi vi /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/find find /bin/busybox.nosuid 50
	update-alternatives --install /bin/grep grep /bin/busybox.nosuid 50
	update-alternatives --install /bin/egrep egrep /bin/busybox.nosuid 50
	update-alternatives --install /bin/fgrep fgrep /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/xargs xargs /bin/busybox.nosuid 50
	update-alternatives --install /sbin/halt halt /bin/busybox.nosuid 50
	update-alternatives --install /sbin/poweroff poweroff /bin/busybox.nosuid 50
	update-alternatives --install /sbin/reboot reboot /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/mesg mesg /bin/busybox.nosuid 50
	update-alternatives --install /usr/sbin/rfkill rfkill /bin/busybox.nosuid 50
	update-alternatives --install /sbin/depmod depmod /bin/busybox.nosuid 50
	update-alternatives --install /sbin/insmod insmod /bin/busybox.nosuid 50
	update-alternatives --install /sbin/lsmod lsmod /bin/busybox.nosuid 50
	update-alternatives --install /sbin/modinfo modinfo /bin/busybox.nosuid 50
	update-alternatives --install /sbin/modprobe modprobe /bin/busybox.nosuid 50
	update-alternatives --install /sbin/rmmod rmmod /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/wget wget /bin/busybox.nosuid 50
	update-alternatives --install /bin/ash ash /bin/busybox.nosuid 50
	update-alternatives --install /bin/sh sh /bin/busybox.nosuid 50
	update-alternatives --install /sbin/fstrim fstrim /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/[ lbracket /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/[[ [[ /bin/busybox.nosuid 50
	update-alternatives --install /usr/sbin/addgroup addgroup /bin/busybox.nosuid 50
	update-alternatives --install /usr/sbin/adduser adduser /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/basename basename /bin/busybox.nosuid 50
	update-alternatives --install /sbin/blkid blkid /bin/busybox.nosuid 50
	update-alternatives --install /bin/cat cat /bin/busybox.nosuid 50
	update-alternatives --install /bin/chattr chattr /bin/busybox.nosuid 50
	update-alternatives --install /bin/chgrp chgrp /bin/busybox.nosuid 50
	update-alternatives --install /bin/chmod chmod /bin/busybox.nosuid 50
	update-alternatives --install /bin/chown chown /bin/busybox.nosuid 50
	update-alternatives --install /usr/sbin/chroot chroot /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/chrt chrt /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/chvt chvt /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/clear clear /bin/busybox.nosuid 50
	update-alternatives --install /bin/cp cp /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/cut cut /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/dc dc /bin/busybox.nosuid 50
	update-alternatives --install /bin/dd dd /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/deallocvt deallocvt /bin/busybox.nosuid 50
	update-alternatives --install /usr/sbin/delgroup delgroup /bin/busybox.nosuid 50
	update-alternatives --install /usr/sbin/deluser deluser /bin/busybox.nosuid 50
	update-alternatives --install /bin/df df /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/dirname dirname /bin/busybox.nosuid 50
	update-alternatives --install /bin/dmesg dmesg /bin/busybox.nosuid 50
	update-alternatives --install /bin/dnsdomainname dnsdomainname /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/du du /bin/busybox.nosuid 50
	update-alternatives --install /bin/dumpkmap dumpkmap /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/dumpleases dumpleases /bin/busybox.nosuid 50
	update-alternatives --install /bin/echo echo /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/env env /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/expr expr /bin/busybox.nosuid 50
	update-alternatives --install /bin/false false /bin/busybox.nosuid 50
	update-alternatives --install /usr/sbin/fbset fbset /bin/busybox.nosuid 50
	update-alternatives --install /sbin/fdisk fdisk /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/flock flock /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/free free /bin/busybox.nosuid 50
	update-alternatives --install /sbin/fsck fsck /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/fuser fuser /bin/busybox.nosuid 50
	update-alternatives --install /bin/getopt getopt /bin/busybox.nosuid 50
	update-alternatives --install /sbin/getty getty /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/head head /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/hexdump hexdump /bin/busybox.nosuid 50
	update-alternatives --install /bin/hostname hostname /bin/busybox.nosuid 50
	update-alternatives --install /sbin/hwclock hwclock /bin/busybox.nosuid 50
	update-alternatives --install /sbin/ifconfig ifconfig /bin/busybox.nosuid 50
	update-alternatives --install /sbin/ifdown ifdown /bin/busybox.nosuid 50
	update-alternatives --install /sbin/ifup ifup /bin/busybox.nosuid 50
	update-alternatives --install /sbin/ip ip /bin/busybox.nosuid 50
	update-alternatives --install /bin/kill kill /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/killall killall /bin/busybox.nosuid 50
	update-alternatives --install /sbin/klogd klogd /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/less less /bin/busybox.nosuid 50
	update-alternatives --install /bin/ln ln /bin/busybox.nosuid 50
	update-alternatives --install /usr/sbin/loadfont loadfont /bin/busybox.nosuid 50
	update-alternatives --install /sbin/loadkmap loadkmap /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/logger logger /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/logname logname /bin/busybox.nosuid 50
	update-alternatives --install /sbin/logread logread /bin/busybox.nosuid 50
	update-alternatives --install /sbin/losetup losetup /bin/busybox.nosuid 50
	update-alternatives --install /bin/ls ls /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/md5sum md5sum /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/microcom microcom /bin/busybox.nosuid 50
	update-alternatives --install /bin/mkdir mkdir /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/mkfifo mkfifo /bin/busybox.nosuid 50
	update-alternatives --install /bin/mknod mknod /bin/busybox.nosuid 50
	update-alternatives --install /sbin/mkswap mkswap /bin/busybox.nosuid 50
	update-alternatives --install /bin/mktemp mktemp /bin/busybox.nosuid 50
	update-alternatives --install /bin/more more /bin/busybox.nosuid 50
	update-alternatives --install /bin/mount mount /bin/busybox.nosuid 50
	update-alternatives --install /bin/mv mv /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/nc nc /bin/busybox.nosuid 50
	update-alternatives --install /bin/netstat netstat /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/nohup nohup /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/nslookup nslookup /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/od od /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/openvt openvt /bin/busybox.nosuid 50
	update-alternatives --install /bin/pidof pidof /bin/busybox.nosuid 50
	update-alternatives --install /sbin/pivot_root pivot_root /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/printf printf /bin/busybox.nosuid 50
	update-alternatives --install /bin/ps ps /bin/busybox.nosuid 50
	update-alternatives --install /bin/pwd pwd /bin/busybox.nosuid 50
	update-alternatives --install /usr/sbin/rdate rdate /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/readlink readlink /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/realpath realpath /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/renice renice /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/reset reset /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/resize resize /bin/busybox.nosuid 50
	update-alternatives --install /bin/rm rm /bin/busybox.nosuid 50
	update-alternatives --install /bin/rmdir rmdir /bin/busybox.nosuid 50
	update-alternatives --install /sbin/route route /bin/busybox.nosuid 50
	update-alternatives --install /bin/run-parts run-parts /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/seq seq /bin/busybox.nosuid 50
	update-alternatives --install /sbin/setconsole setconsole /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/sha1sum sha1sum /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/sha256sum sha256sum /bin/busybox.nosuid 50
	update-alternatives --install /bin/sleep sleep /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/sort sort /bin/busybox.nosuid 50
	update-alternatives --install /sbin/start-stop-daemon start-stop-daemon /bin/busybox.nosuid 50
	update-alternatives --install /bin/stat stat /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/strings strings /bin/busybox.nosuid 50
	update-alternatives --install /bin/stty stty /bin/busybox.nosuid 50
	update-alternatives --install /sbin/sulogin sulogin /bin/busybox.nosuid 50
	update-alternatives --install /sbin/swapoff swapoff /bin/busybox.nosuid 50
	update-alternatives --install /sbin/swapon swapon /bin/busybox.nosuid 50
	update-alternatives --install /sbin/switch_root switch_root /bin/busybox.nosuid 50
	update-alternatives --install /sbin/sysctl sysctl /bin/busybox.nosuid 50
	update-alternatives --install /sbin/syslogd syslogd /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/tail tail /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/tee tee /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/telnet telnet /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/test test /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/tftp tftp /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/time time /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/top top /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/tr tr /bin/busybox.nosuid 50
	update-alternatives --install /bin/true true /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/tty tty /bin/busybox.nosuid 50
	update-alternatives --install /sbin/udhcpc udhcpc /bin/busybox.nosuid 50
	update-alternatives --install /usr/sbin/udhcpd udhcpd /bin/busybox.nosuid 50
	update-alternatives --install /bin/umount umount /bin/busybox.nosuid 50
	update-alternatives --install /bin/uname uname /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/uniq uniq /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/uptime uptime /bin/busybox.nosuid 50
	update-alternatives --install /bin/usleep usleep /bin/busybox.nosuid 50
	update-alternatives --install /bin/watch watch /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/wc wc /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/which which /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/whoami whoami /bin/busybox.nosuid 50
	update-alternatives --install /usr/bin/yes yes /bin/busybox.nosuid 50
	update-alternatives --install /bin/ping ping /bin/busybox.suid 50
	update-alternatives --install /bin/ping6 ping6 /bin/busybox.suid 50
	update-alternatives --install /bin/login login /bin/busybox.suid 50
	update-alternatives --install /usr/bin/passwd passwd /bin/busybox.suid 50
	update-alternatives --install /bin/su su /bin/busybox.suid 50
	update-alternatives --install /usr/bin/traceroute traceroute /bin/busybox.suid 50
	update-alternatives --install /usr/bin/vlock vlock /bin/busybox.suid 50


%preun
# busybox - prerm
if [ "$1" = "0" ] ; then
# This is so you can make busybox commit suicide - removing busybox with no other packages
	# providing its files, this will make update-alternatives work, but the update-rc.d part
	# for syslog, httpd and/or udhcpd will fail if there is no other package providing sh
	tmpdir=`mktemp -d /tmp/busyboxrm-XXXXXX`
	ln -s /bin/busybox $tmpdir/[
	ln -s /bin/busybox $tmpdir/test
	ln -s /bin/busybox $tmpdir/head
	ln -s /bin/busybox $tmpdir/sh
	ln -s /bin/busybox $tmpdir/basename
	ln -s /bin/busybox $tmpdir/echo
	ln -s /bin/busybox $tmpdir/mv
	ln -s /bin/busybox $tmpdir/ln
	ln -s /bin/busybox $tmpdir/dirname
	ln -s /bin/busybox $tmpdir/rm
	ln -s /bin/busybox $tmpdir/sed
	ln -s /bin/busybox $tmpdir/sort
	ln -s /bin/busybox $tmpdir/grep
	ln -s /bin/busybox $tmpdir/tail
	export PATH=$PATH:$tmpdir
	update-alternatives --remove  gunzip /bin/busybox.nosuid
	update-alternatives --remove  zcat /bin/busybox.nosuid
	update-alternatives --remove  bunzip2 /bin/busybox.nosuid
	update-alternatives --remove  bzcat /bin/busybox.nosuid
	update-alternatives --remove  cpio /bin/busybox.nosuid
	update-alternatives --remove  gzip /bin/busybox.nosuid
	update-alternatives --remove  tar /bin/busybox.nosuid
	update-alternatives --remove  unzip /bin/busybox.nosuid
	update-alternatives --remove  date /bin/busybox.nosuid
	update-alternatives --remove  groups /bin/busybox.nosuid
	update-alternatives --remove  id /bin/busybox.nosuid
	update-alternatives --remove  shuf /bin/busybox.nosuid
	update-alternatives --remove  sync /bin/busybox.nosuid
	update-alternatives --remove  touch /bin/busybox.nosuid
	update-alternatives --remove  unlink /bin/busybox.nosuid
	update-alternatives --remove  users /bin/busybox.nosuid
	update-alternatives --remove  who /bin/busybox.nosuid
	update-alternatives --remove  awk /bin/busybox.nosuid
	update-alternatives --remove  cmp /bin/busybox.nosuid
	update-alternatives --remove  diff /bin/busybox.nosuid
	update-alternatives --remove  patch /bin/busybox.nosuid
	update-alternatives --remove  sed /bin/busybox.nosuid
	update-alternatives --remove  vi /bin/busybox.nosuid
	update-alternatives --remove  find /bin/busybox.nosuid
	update-alternatives --remove  grep /bin/busybox.nosuid
	update-alternatives --remove  egrep /bin/busybox.nosuid
	update-alternatives --remove  fgrep /bin/busybox.nosuid
	update-alternatives --remove  xargs /bin/busybox.nosuid
	update-alternatives --remove  halt /bin/busybox.nosuid
	update-alternatives --remove  poweroff /bin/busybox.nosuid
	update-alternatives --remove  reboot /bin/busybox.nosuid
	update-alternatives --remove  mesg /bin/busybox.nosuid
	update-alternatives --remove  rfkill /bin/busybox.nosuid
	update-alternatives --remove  depmod /bin/busybox.nosuid
	update-alternatives --remove  insmod /bin/busybox.nosuid
	update-alternatives --remove  lsmod /bin/busybox.nosuid
	update-alternatives --remove  modinfo /bin/busybox.nosuid
	update-alternatives --remove  modprobe /bin/busybox.nosuid
	update-alternatives --remove  rmmod /bin/busybox.nosuid
	update-alternatives --remove  wget /bin/busybox.nosuid
	update-alternatives --remove  ash /bin/busybox.nosuid
	update-alternatives --remove  sh /bin/busybox.nosuid
	update-alternatives --remove  fstrim /bin/busybox.nosuid
	update-alternatives --remove  lbracket /bin/busybox.nosuid
	update-alternatives --remove  [[ /bin/busybox.nosuid
	update-alternatives --remove  addgroup /bin/busybox.nosuid
	update-alternatives --remove  adduser /bin/busybox.nosuid
	update-alternatives --remove  basename /bin/busybox.nosuid
	update-alternatives --remove  blkid /bin/busybox.nosuid
	update-alternatives --remove  cat /bin/busybox.nosuid
	update-alternatives --remove  chattr /bin/busybox.nosuid
	update-alternatives --remove  chgrp /bin/busybox.nosuid
	update-alternatives --remove  chmod /bin/busybox.nosuid
	update-alternatives --remove  chown /bin/busybox.nosuid
	update-alternatives --remove  chroot /bin/busybox.nosuid
	update-alternatives --remove  chrt /bin/busybox.nosuid
	update-alternatives --remove  chvt /bin/busybox.nosuid
	update-alternatives --remove  clear /bin/busybox.nosuid
	update-alternatives --remove  cp /bin/busybox.nosuid
	update-alternatives --remove  cut /bin/busybox.nosuid
	update-alternatives --remove  dc /bin/busybox.nosuid
	update-alternatives --remove  dd /bin/busybox.nosuid
	update-alternatives --remove  deallocvt /bin/busybox.nosuid
	update-alternatives --remove  delgroup /bin/busybox.nosuid
	update-alternatives --remove  deluser /bin/busybox.nosuid
	update-alternatives --remove  df /bin/busybox.nosuid
	update-alternatives --remove  dirname /bin/busybox.nosuid
	update-alternatives --remove  dmesg /bin/busybox.nosuid
	update-alternatives --remove  dnsdomainname /bin/busybox.nosuid
	update-alternatives --remove  du /bin/busybox.nosuid
	update-alternatives --remove  dumpkmap /bin/busybox.nosuid
	update-alternatives --remove  dumpleases /bin/busybox.nosuid
	update-alternatives --remove  echo /bin/busybox.nosuid
	update-alternatives --remove  env /bin/busybox.nosuid
	update-alternatives --remove  expr /bin/busybox.nosuid
	update-alternatives --remove  false /bin/busybox.nosuid
	update-alternatives --remove  fbset /bin/busybox.nosuid
	update-alternatives --remove  fdisk /bin/busybox.nosuid
	update-alternatives --remove  flock /bin/busybox.nosuid
	update-alternatives --remove  free /bin/busybox.nosuid
	update-alternatives --remove  fsck /bin/busybox.nosuid
	update-alternatives --remove  fuser /bin/busybox.nosuid
	update-alternatives --remove  getopt /bin/busybox.nosuid
	update-alternatives --remove  getty /bin/busybox.nosuid
	update-alternatives --remove  head /bin/busybox.nosuid
	update-alternatives --remove  hexdump /bin/busybox.nosuid
	update-alternatives --remove  hostname /bin/busybox.nosuid
	update-alternatives --remove  hwclock /bin/busybox.nosuid
	update-alternatives --remove  ifconfig /bin/busybox.nosuid
	update-alternatives --remove  ifdown /bin/busybox.nosuid
	update-alternatives --remove  ifup /bin/busybox.nosuid
	update-alternatives --remove  ip /bin/busybox.nosuid
	update-alternatives --remove  kill /bin/busybox.nosuid
	update-alternatives --remove  killall /bin/busybox.nosuid
	update-alternatives --remove  klogd /bin/busybox.nosuid
	update-alternatives --remove  less /bin/busybox.nosuid
	update-alternatives --remove  ln /bin/busybox.nosuid
	update-alternatives --remove  loadfont /bin/busybox.nosuid
	update-alternatives --remove  loadkmap /bin/busybox.nosuid
	update-alternatives --remove  logger /bin/busybox.nosuid
	update-alternatives --remove  logname /bin/busybox.nosuid
	update-alternatives --remove  logread /bin/busybox.nosuid
	update-alternatives --remove  losetup /bin/busybox.nosuid
	update-alternatives --remove  ls /bin/busybox.nosuid
	update-alternatives --remove  md5sum /bin/busybox.nosuid
	update-alternatives --remove  microcom /bin/busybox.nosuid
	update-alternatives --remove  mkdir /bin/busybox.nosuid
	update-alternatives --remove  mkfifo /bin/busybox.nosuid
	update-alternatives --remove  mknod /bin/busybox.nosuid
	update-alternatives --remove  mkswap /bin/busybox.nosuid
	update-alternatives --remove  mktemp /bin/busybox.nosuid
	update-alternatives --remove  more /bin/busybox.nosuid
	update-alternatives --remove  mount /bin/busybox.nosuid
	update-alternatives --remove  mv /bin/busybox.nosuid
	update-alternatives --remove  nc /bin/busybox.nosuid
	update-alternatives --remove  netstat /bin/busybox.nosuid
	update-alternatives --remove  nohup /bin/busybox.nosuid
	update-alternatives --remove  nslookup /bin/busybox.nosuid
	update-alternatives --remove  od /bin/busybox.nosuid
	update-alternatives --remove  openvt /bin/busybox.nosuid
	update-alternatives --remove  pidof /bin/busybox.nosuid
	update-alternatives --remove  pivot_root /bin/busybox.nosuid
	update-alternatives --remove  printf /bin/busybox.nosuid
	update-alternatives --remove  ps /bin/busybox.nosuid
	update-alternatives --remove  pwd /bin/busybox.nosuid
	update-alternatives --remove  rdate /bin/busybox.nosuid
	update-alternatives --remove  readlink /bin/busybox.nosuid
	update-alternatives --remove  realpath /bin/busybox.nosuid
	update-alternatives --remove  renice /bin/busybox.nosuid
	update-alternatives --remove  reset /bin/busybox.nosuid
	update-alternatives --remove  resize /bin/busybox.nosuid
	update-alternatives --remove  rm /bin/busybox.nosuid
	update-alternatives --remove  rmdir /bin/busybox.nosuid
	update-alternatives --remove  route /bin/busybox.nosuid
	update-alternatives --remove  run-parts /bin/busybox.nosuid
	update-alternatives --remove  seq /bin/busybox.nosuid
	update-alternatives --remove  setconsole /bin/busybox.nosuid
	update-alternatives --remove  sha1sum /bin/busybox.nosuid
	update-alternatives --remove  sha256sum /bin/busybox.nosuid
	update-alternatives --remove  sleep /bin/busybox.nosuid
	update-alternatives --remove  sort /bin/busybox.nosuid
	update-alternatives --remove  start-stop-daemon /bin/busybox.nosuid
	update-alternatives --remove  stat /bin/busybox.nosuid
	update-alternatives --remove  strings /bin/busybox.nosuid
	update-alternatives --remove  stty /bin/busybox.nosuid
	update-alternatives --remove  sulogin /bin/busybox.nosuid
	update-alternatives --remove  swapoff /bin/busybox.nosuid
	update-alternatives --remove  swapon /bin/busybox.nosuid
	update-alternatives --remove  switch_root /bin/busybox.nosuid
	update-alternatives --remove  sysctl /bin/busybox.nosuid
	update-alternatives --remove  syslogd /bin/busybox.nosuid
	update-alternatives --remove  tail /bin/busybox.nosuid
	update-alternatives --remove  tee /bin/busybox.nosuid
	update-alternatives --remove  telnet /bin/busybox.nosuid
	update-alternatives --remove  test /bin/busybox.nosuid
	update-alternatives --remove  tftp /bin/busybox.nosuid
	update-alternatives --remove  time /bin/busybox.nosuid
	update-alternatives --remove  top /bin/busybox.nosuid
	update-alternatives --remove  tr /bin/busybox.nosuid
	update-alternatives --remove  true /bin/busybox.nosuid
	update-alternatives --remove  tty /bin/busybox.nosuid
	update-alternatives --remove  udhcpc /bin/busybox.nosuid
	update-alternatives --remove  udhcpd /bin/busybox.nosuid
	update-alternatives --remove  umount /bin/busybox.nosuid
	update-alternatives --remove  uname /bin/busybox.nosuid
	update-alternatives --remove  uniq /bin/busybox.nosuid
	update-alternatives --remove  uptime /bin/busybox.nosuid
	update-alternatives --remove  usleep /bin/busybox.nosuid
	update-alternatives --remove  watch /bin/busybox.nosuid
	update-alternatives --remove  wc /bin/busybox.nosuid
	update-alternatives --remove  which /bin/busybox.nosuid
	update-alternatives --remove  whoami /bin/busybox.nosuid
	update-alternatives --remove  yes /bin/busybox.nosuid
	update-alternatives --remove  ping /bin/busybox.suid
	update-alternatives --remove  ping6 /bin/busybox.suid
	update-alternatives --remove  login /bin/busybox.suid
	update-alternatives --remove  passwd /bin/busybox.suid
	update-alternatives --remove  su /bin/busybox.suid
	update-alternatives --remove  traceroute /bin/busybox.suid
	update-alternatives --remove  vlock /bin/busybox.suid
fi

%postun
# busybox - postrm
if [ "$1" = "0" ] ; then
if grep -q "^/bin/bash$" $D/etc/busybox.links* && [ ! -e $D/bin/bash ]; then
		printf "$(grep -v "^/bin/bash$" $D/etc/shells)\n" > $D/etc/shells
	fi
fi

%pre -n busybox-httpd
# busybox-httpd - preinst
#!/bin/sh
if true && [ -z "$D" -a -f "/etc/init.d/busybox-httpd" ]; then
	/etc/init.d/busybox-httpd stop || :
fi
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-f -r $D"
	else
		OPT="-f"
	fi
	update-rc.d $OPT busybox-httpd remove
fi


%post -n busybox-httpd
# busybox-httpd - postinst
#!/bin/sh
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-r $D"
	else
		OPT="-s"
	fi
	update-rc.d $OPT busybox-httpd defaults
fi


%preun -n busybox-httpd
# busybox-httpd - prerm
#!/bin/sh
if [ "$1" = "0" ] ; then
if true && [ -z "$D" -a -x "/etc/init.d/busybox-httpd" ]; then
	/etc/init.d/busybox-httpd stop || :
fi
fi

%postun -n busybox-httpd
# busybox-httpd - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-f -r $D"
	else
		OPT="-f"
	fi
	update-rc.d $OPT busybox-httpd remove
fi
fi

%pre -n busybox-udhcpd
# busybox-udhcpd - preinst
#!/bin/sh
if true && [ -z "$D" -a -f "/etc/init.d/busybox-udhcpd" ]; then
	/etc/init.d/busybox-udhcpd stop || :
fi
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-f -r $D"
	else
		OPT="-f"
	fi
	update-rc.d $OPT busybox-udhcpd remove
fi


%post -n busybox-udhcpd
# busybox-udhcpd - postinst
#!/bin/sh
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-r $D"
	else
		OPT="-s"
	fi
	update-rc.d $OPT busybox-udhcpd defaults
fi


%preun -n busybox-udhcpd
# busybox-udhcpd - prerm
#!/bin/sh
if [ "$1" = "0" ] ; then
if true && [ -z "$D" -a -x "/etc/init.d/busybox-udhcpd" ]; then
	/etc/init.d/busybox-udhcpd stop || :
fi
fi

%postun -n busybox-udhcpd
# busybox-udhcpd - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-f -r $D"
	else
		OPT="-f"
	fi
	update-rc.d $OPT busybox-udhcpd remove
fi
fi

%pre -n busybox-syslog
# busybox-syslog - preinst
#!/bin/sh
if true && [ -z "$D" -a -f "/etc/init.d/syslog" ]; then
	/etc/init.d/syslog stop || :
fi
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-f -r $D"
	else
		OPT="-f"
	fi
	update-rc.d $OPT syslog remove
fi


%post -n busybox-syslog
# busybox-syslog - postinst
#!/bin/sh
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-r $D"
	else
		OPT="-s"
	fi
	update-rc.d $OPT syslog defaults
fi


%preun -n busybox-syslog
# busybox-syslog - prerm
if [ "$1" = "0" ] ; then
# remove syslog
	if test "x$D" = "x"; then
		if test "$1" = "upgrade" -o "$1" = "remove"; then
			/etc/init.d/syslog stop || :
		fi
	fi
if true && [ -z "$D" -a -x "/etc/init.d/syslog" ]; then
	/etc/init.d/syslog stop || :
fi
fi

%postun -n busybox-syslog
# busybox-syslog - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-f -r $D"
	else
		OPT="-f"
	fi
	update-rc.d $OPT syslog remove
fi
fi

%pre -n busybox-mdev
# busybox-mdev - preinst
#!/bin/sh
if true && [ -z "$D" -a -f "/etc/init.d/mdev" ]; then
	/etc/init.d/mdev stop || :
fi
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-f -r $D"
	else
		OPT="-f"
	fi
	update-rc.d $OPT mdev remove
fi


%post -n busybox-mdev
# busybox-mdev - postinst
#!/bin/sh
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-r $D"
	else
		OPT="-s"
	fi
	update-rc.d $OPT mdev start 04 S .
fi


%preun -n busybox-mdev
# busybox-mdev - prerm
#!/bin/sh
if [ "$1" = "0" ] ; then
if true && [ -z "$D" -a -x "/etc/init.d/mdev" ]; then
	/etc/init.d/mdev stop || :
fi
fi

%postun -n busybox-mdev
# busybox-mdev - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-f -r $D"
	else
		OPT="-f"
	fi
	update-rc.d $OPT mdev remove
fi
fi

%pre -n busybox-hwclock
# busybox-hwclock - preinst
#!/bin/sh
if true && [ -z "$D" -a -f "/etc/init.d/hwclock.sh" ]; then
	/etc/init.d/hwclock.sh stop || :
fi
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-f -r $D"
	else
		OPT="-f"
	fi
	update-rc.d $OPT hwclock.sh remove
fi


%post -n busybox-hwclock
# busybox-hwclock - postinst
#!/bin/sh
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-r $D"
	else
		OPT="-s"
	fi
	update-rc.d $OPT hwclock.sh defaults
fi


%preun -n busybox-hwclock
# busybox-hwclock - prerm
#!/bin/sh
if [ "$1" = "0" ] ; then
if true && [ -z "$D" -a -x "/etc/init.d/hwclock.sh" ]; then
	/etc/init.d/hwclock.sh stop || :
fi
fi

%postun -n busybox-hwclock
# busybox-hwclock - postrm
#!/bin/sh
if [ "$1" = "0" ] ; then
if true && type update-rc.d >/dev/null 2>/dev/null; then
	if [ -n "$D" ]; then
		OPT="-f -r $D"
	else
		OPT="-f"
	fi
	update-rc.d $OPT hwclock.sh remove
fi
fi

%files
%defattr(-,-,-,-)
%dir "/bin"
%dir "/etc"
"/bin/sh"
"/bin/busybox"
"/bin/busybox.suid"
"/bin/busybox.nosuid"
"/etc/busybox.links.suid"
"/etc/busybox.links.nosuid"

%files -n busybox-ptest
%defattr(-,-,-,-)
%dir "/usr"
%dir "/usr/lib"
%dir "/usr/lib/busybox"
%dir "/usr/lib/busybox/ptest"
%dir "/usr/lib/busybox/ptest/testsuite"
"/usr/lib/busybox/ptest/busybox"
"/usr/lib/busybox/ptest/run-ptest"
"/usr/lib/busybox/ptest/.config"
%dir "/usr/lib/busybox/ptest/testsuite/cp"
%dir "/usr/lib/busybox/ptest/testsuite/bunzip2"
%dir "/usr/lib/busybox/ptest/testsuite/pwd"
%dir "/usr/lib/busybox/ptest/testsuite/find"
%dir "/usr/lib/busybox/ptest/testsuite/md5sum"
%dir "/usr/lib/busybox/ptest/testsuite/false"
%dir "/usr/lib/busybox/ptest/testsuite/strings"
%dir "/usr/lib/busybox/ptest/testsuite/unexpand"
%dir "/usr/lib/busybox/ptest/testsuite/rmdir"
%dir "/usr/lib/busybox/ptest/testsuite/xargs"
%dir "/usr/lib/busybox/ptest/testsuite/id"
%dir "/usr/lib/busybox/ptest/testsuite/uptime"
%dir "/usr/lib/busybox/ptest/testsuite/hostname"
%dir "/usr/lib/busybox/ptest/testsuite/which"
%dir "/usr/lib/busybox/ptest/testsuite/mkdir"
%dir "/usr/lib/busybox/ptest/testsuite/date"
%dir "/usr/lib/busybox/ptest/testsuite/echo"
%dir "/usr/lib/busybox/ptest/testsuite/msh"
%dir "/usr/lib/busybox/ptest/testsuite/wget"
%dir "/usr/lib/busybox/ptest/testsuite/wc"
%dir "/usr/lib/busybox/ptest/testsuite/ln"
%dir "/usr/lib/busybox/ptest/testsuite/head"
%dir "/usr/lib/busybox/ptest/testsuite/tail"
%dir "/usr/lib/busybox/ptest/testsuite/rm"
%dir "/usr/lib/busybox/ptest/testsuite/hostid"
%dir "/usr/lib/busybox/ptest/testsuite/ls"
%dir "/usr/lib/busybox/ptest/testsuite/du"
%dir "/usr/lib/busybox/ptest/testsuite/dirname"
%dir "/usr/lib/busybox/ptest/testsuite/touch"
%dir "/usr/lib/busybox/ptest/testsuite/cut"
%dir "/usr/lib/busybox/ptest/testsuite/gunzip"
%dir "/usr/lib/busybox/ptest/testsuite/tar"
%dir "/usr/lib/busybox/ptest/testsuite/true"
%dir "/usr/lib/busybox/ptest/testsuite/tr"
%dir "/usr/lib/busybox/ptest/testsuite/expand"
%dir "/usr/lib/busybox/ptest/testsuite/expr"
%dir "/usr/lib/busybox/ptest/testsuite/gzip"
%dir "/usr/lib/busybox/ptest/testsuite/basename"
%dir "/usr/lib/busybox/ptest/testsuite/cmp"
%dir "/usr/lib/busybox/ptest/testsuite/tee"
%dir "/usr/lib/busybox/ptest/testsuite/dd"
%dir "/usr/lib/busybox/ptest/testsuite/mv"
%dir "/usr/lib/busybox/ptest/testsuite/cat"
"/usr/lib/busybox/ptest/testsuite/xargs.tests"
"/usr/lib/busybox/ptest/testsuite/mount.tests"
"/usr/lib/busybox/ptest/testsuite/grep.tests"
"/usr/lib/busybox/ptest/testsuite/README"
"/usr/lib/busybox/ptest/testsuite/uniq.tests"
"/usr/lib/busybox/ptest/testsuite/find.tests"
"/usr/lib/busybox/ptest/testsuite/busybox.tests"
"/usr/lib/busybox/ptest/testsuite/ar.tests"
"/usr/lib/busybox/ptest/testsuite/start-stop-daemon.tests"
"/usr/lib/busybox/ptest/testsuite/seq.tests"
"/usr/lib/busybox/ptest/testsuite/patch.tests"
"/usr/lib/busybox/ptest/testsuite/od.tests"
"/usr/lib/busybox/ptest/testsuite/pidof.tests"
"/usr/lib/busybox/ptest/testsuite/cal.tests"
"/usr/lib/busybox/ptest/testsuite/fold.tests"
"/usr/lib/busybox/ptest/testsuite/sha256sum.tests"
"/usr/lib/busybox/ptest/testsuite/makedevs.tests"
"/usr/lib/busybox/ptest/testsuite/umlwrapper.sh"
"/usr/lib/busybox/ptest/testsuite/awk_t1.tar.bz2"
"/usr/lib/busybox/ptest/testsuite/uuencode.tests"
"/usr/lib/busybox/ptest/testsuite/sha1sum.tests"
"/usr/lib/busybox/ptest/testsuite/sort.tests"
"/usr/lib/busybox/ptest/testsuite/tar.tests"
"/usr/lib/busybox/ptest/testsuite/mdev.tests"
"/usr/lib/busybox/ptest/testsuite/rx.tests"
"/usr/lib/busybox/ptest/testsuite/cpio.tests"
"/usr/lib/busybox/ptest/testsuite/sha512sum.tests"
"/usr/lib/busybox/ptest/testsuite/cut.tests"
"/usr/lib/busybox/ptest/testsuite/unexpand.tests"
"/usr/lib/busybox/ptest/testsuite/sum.tests"
"/usr/lib/busybox/ptest/testsuite/runtest"
"/usr/lib/busybox/ptest/testsuite/unzip.tests"
"/usr/lib/busybox/ptest/testsuite/gunzip.tests"
"/usr/lib/busybox/ptest/testsuite/readlink.tests"
"/usr/lib/busybox/ptest/testsuite/all_sourcecode.tests"
"/usr/lib/busybox/ptest/testsuite/makedevs.device_table.txt"
"/usr/lib/busybox/ptest/testsuite/mount.testroot"
"/usr/lib/busybox/ptest/testsuite/bzcat.tests"
"/usr/lib/busybox/ptest/testsuite/tail.tests"
"/usr/lib/busybox/ptest/testsuite/parse.tests"
"/usr/lib/busybox/ptest/testsuite/awk.tests"
"/usr/lib/busybox/ptest/testsuite/dc.tests"
"/usr/lib/busybox/ptest/testsuite/comm.tests"
"/usr/lib/busybox/ptest/testsuite/tr.tests"
"/usr/lib/busybox/ptest/testsuite/expand.tests"
"/usr/lib/busybox/ptest/testsuite/test.tests"
"/usr/lib/busybox/ptest/testsuite/md5sum.tests"
"/usr/lib/busybox/ptest/testsuite/ls.mk_uni_tests"
"/usr/lib/busybox/ptest/testsuite/ash.tests"
"/usr/lib/busybox/ptest/testsuite/sed.tests"
"/usr/lib/busybox/ptest/testsuite/diff.tests"
"/usr/lib/busybox/ptest/testsuite/cp.tests"
"/usr/lib/busybox/ptest/testsuite/taskset.tests"
"/usr/lib/busybox/ptest/testsuite/printf.tests"
"/usr/lib/busybox/ptest/testsuite/mkfs.minix.tests"
"/usr/lib/busybox/ptest/testsuite/uncompress.tests"
"/usr/lib/busybox/ptest/testsuite/sha3sum.tests"
"/usr/lib/busybox/ptest/testsuite/TODO"
"/usr/lib/busybox/ptest/testsuite/testing.sh"
"/usr/lib/busybox/ptest/testsuite/bunzip2.tests"
"/usr/lib/busybox/ptest/testsuite/ls.tests"
"/usr/lib/busybox/ptest/testsuite/cp/cp-copies-large-file"
"/usr/lib/busybox/ptest/testsuite/cp/cp-files-to-dir"
"/usr/lib/busybox/ptest/testsuite/cp/cp-a-preserves-links"
"/usr/lib/busybox/ptest/testsuite/cp/cp-dev-file"
"/usr/lib/busybox/ptest/testsuite/cp/cp-preserves-links"
"/usr/lib/busybox/ptest/testsuite/cp/cp-copies-empty-file"
"/usr/lib/busybox/ptest/testsuite/cp/cp-RHL-does_not_preserve-links"
"/usr/lib/busybox/ptest/testsuite/cp/cp-copies-small-file"
"/usr/lib/busybox/ptest/testsuite/cp/cp-parents"
"/usr/lib/busybox/ptest/testsuite/cp/cp-preserves-source-file"
"/usr/lib/busybox/ptest/testsuite/cp/cp-dir-existing-dir"
"/usr/lib/busybox/ptest/testsuite/cp/cp-preserves-hard-links"
"/usr/lib/busybox/ptest/testsuite/cp/cp-follows-links"
"/usr/lib/busybox/ptest/testsuite/cp/cp-dir-create-dir"
"/usr/lib/busybox/ptest/testsuite/cp/cp-does-not-copy-unreadable-file"
"/usr/lib/busybox/ptest/testsuite/cp/cp-a-files-to-dir"
"/usr/lib/busybox/ptest/testsuite/cp/cp-d-files-to-dir"
"/usr/lib/busybox/ptest/testsuite/bunzip2/bunzip2-removes-compressed-file"
"/usr/lib/busybox/ptest/testsuite/bunzip2/bunzip2-reads-from-standard-input"
"/usr/lib/busybox/ptest/testsuite/bunzip2/bzcat-does-not-remove-compressed-file"
"/usr/lib/busybox/ptest/testsuite/pwd/pwd-prints-working-directory"
"/usr/lib/busybox/ptest/testsuite/find/find-supports-minus-xdev"
"/usr/lib/busybox/ptest/testsuite/md5sum/md5sum-verifies-non-binary-file"
"/usr/lib/busybox/ptest/testsuite/false/false-is-silent"
"/usr/lib/busybox/ptest/testsuite/false/false-returns-failure"
"/usr/lib/busybox/ptest/testsuite/strings/strings-works-like-GNU"
"/usr/lib/busybox/ptest/testsuite/unexpand/unexpand-works-like-GNU"
"/usr/lib/busybox/ptest/testsuite/rmdir/rmdir-removes-parent-directories"
"/usr/lib/busybox/ptest/testsuite/xargs/xargs-works"
"/usr/lib/busybox/ptest/testsuite/id/id-ur-works"
"/usr/lib/busybox/ptest/testsuite/id/id-g-works"
"/usr/lib/busybox/ptest/testsuite/id/id-u-works"
"/usr/lib/busybox/ptest/testsuite/id/id-un-works"
"/usr/lib/busybox/ptest/testsuite/uptime/uptime-works"
"/usr/lib/busybox/ptest/testsuite/hostname/hostname-s-works"
"/usr/lib/busybox/ptest/testsuite/hostname/hostname-i-works"
"/usr/lib/busybox/ptest/testsuite/hostname/hostname-works"
"/usr/lib/busybox/ptest/testsuite/hostname/hostname-d-works"
"/usr/lib/busybox/ptest/testsuite/which/which-uses-default-path"
"/usr/lib/busybox/ptest/testsuite/mkdir/mkdir-makes-parent-directories"
"/usr/lib/busybox/ptest/testsuite/mkdir/mkdir-makes-a-directory"
"/usr/lib/busybox/ptest/testsuite/date/date-@-works"
"/usr/lib/busybox/ptest/testsuite/date/date-works-1"
"/usr/lib/busybox/ptest/testsuite/date/date-format-works"
"/usr/lib/busybox/ptest/testsuite/date/date-R-works"
"/usr/lib/busybox/ptest/testsuite/date/date-works"
"/usr/lib/busybox/ptest/testsuite/date/date-u-works"
"/usr/lib/busybox/ptest/testsuite/echo/echo-prints-newline"
"/usr/lib/busybox/ptest/testsuite/echo/echo-does-not-print-newline"
"/usr/lib/busybox/ptest/testsuite/echo/echo-prints-slash_00041"
"/usr/lib/busybox/ptest/testsuite/echo/echo-prints-slash-zero"
"/usr/lib/busybox/ptest/testsuite/echo/echo-prints-argument"
"/usr/lib/busybox/ptest/testsuite/echo/echo-prints-non-opts"
"/usr/lib/busybox/ptest/testsuite/echo/echo-prints-slash_0041"
"/usr/lib/busybox/ptest/testsuite/echo/echo-prints-arguments"
"/usr/lib/busybox/ptest/testsuite/echo/echo-prints-slash_41"
"/usr/lib/busybox/ptest/testsuite/echo/echo-prints-slash_041"
"/usr/lib/busybox/ptest/testsuite/echo/echo-prints-dash"
"/usr/lib/busybox/ptest/testsuite/msh/msh-supports-underscores-in-variable-names"
"/usr/lib/busybox/ptest/testsuite/wget/wget-retrieves-google-index"
"/usr/lib/busybox/ptest/testsuite/wget/wget-handles-empty-path"
"/usr/lib/busybox/ptest/testsuite/wget/wget--O-overrides--P"
"/usr/lib/busybox/ptest/testsuite/wget/wget-supports--P"
"/usr/lib/busybox/ptest/testsuite/wc/wc-counts-all"
"/usr/lib/busybox/ptest/testsuite/wc/wc-counts-lines"
"/usr/lib/busybox/ptest/testsuite/wc/wc-prints-longest-line-length"
"/usr/lib/busybox/ptest/testsuite/wc/wc-counts-words"
"/usr/lib/busybox/ptest/testsuite/wc/wc-counts-characters"
"/usr/lib/busybox/ptest/testsuite/ln/ln-force-creates-soft-links"
"/usr/lib/busybox/ptest/testsuite/ln/ln-preserves-hard-links"
"/usr/lib/busybox/ptest/testsuite/ln/ln-creates-hard-links"
"/usr/lib/busybox/ptest/testsuite/ln/ln-force-creates-hard-links"
"/usr/lib/busybox/ptest/testsuite/ln/ln-preserves-soft-links"
"/usr/lib/busybox/ptest/testsuite/ln/ln-creates-soft-links"
"/usr/lib/busybox/ptest/testsuite/head/head-works"
"/usr/lib/busybox/ptest/testsuite/head/head-n-works"
"/usr/lib/busybox/ptest/testsuite/tail/tail-n-works"
"/usr/lib/busybox/ptest/testsuite/tail/tail-works"
"/usr/lib/busybox/ptest/testsuite/rm/rm-removes-file"
"/usr/lib/busybox/ptest/testsuite/hostid/hostid-works"
"/usr/lib/busybox/ptest/testsuite/ls/ls-s-works"
"/usr/lib/busybox/ptest/testsuite/ls/ls-h-works"
"/usr/lib/busybox/ptest/testsuite/ls/ls-l-works"
"/usr/lib/busybox/ptest/testsuite/ls/ls-1-works"
"/usr/lib/busybox/ptest/testsuite/du/du-s-works"
"/usr/lib/busybox/ptest/testsuite/du/du-l-works"
"/usr/lib/busybox/ptest/testsuite/du/du-h-works"
"/usr/lib/busybox/ptest/testsuite/du/du-m-works"
"/usr/lib/busybox/ptest/testsuite/du/du-k-works"
"/usr/lib/busybox/ptest/testsuite/du/du-works"
"/usr/lib/busybox/ptest/testsuite/dirname/dirname-works"
"/usr/lib/busybox/ptest/testsuite/dirname/dirname-handles-absolute-path"
"/usr/lib/busybox/ptest/testsuite/dirname/dirname-handles-relative-path"
"/usr/lib/busybox/ptest/testsuite/dirname/dirname-handles-empty-path"
"/usr/lib/busybox/ptest/testsuite/dirname/dirname-handles-root"
"/usr/lib/busybox/ptest/testsuite/dirname/dirname-handles-single-component"
"/usr/lib/busybox/ptest/testsuite/dirname/dirname-handles-multiple-slashes"
"/usr/lib/busybox/ptest/testsuite/touch/touch-does-not-create-file"
"/usr/lib/busybox/ptest/testsuite/touch/touch-creates-file"
"/usr/lib/busybox/ptest/testsuite/touch/touch-touches-files-after-non-existent-file"
"/usr/lib/busybox/ptest/testsuite/cut/cut-cuts-an-unclosed-range"
"/usr/lib/busybox/ptest/testsuite/cut/cut-cuts-an-open-range"
"/usr/lib/busybox/ptest/testsuite/cut/cut-cuts-a-character"
"/usr/lib/busybox/ptest/testsuite/cut/cut-cuts-a-closed-range"
"/usr/lib/busybox/ptest/testsuite/cut/cut-cuts-a-field"
"/usr/lib/busybox/ptest/testsuite/gunzip/gunzip-reads-from-standard-input"
"/usr/lib/busybox/ptest/testsuite/tar/tar-extracts-file"
"/usr/lib/busybox/ptest/testsuite/tar/tar-archives-multiple-files"
"/usr/lib/busybox/ptest/testsuite/tar/tar-extracts-all-subdirs"
"/usr/lib/busybox/ptest/testsuite/tar/tar-demands-at-least-one-ctx"
"/usr/lib/busybox/ptest/testsuite/tar/tar-extracts-multiple-files"
"/usr/lib/busybox/ptest/testsuite/tar/tar-demands-at-most-one-ctx"
"/usr/lib/busybox/ptest/testsuite/tar/tar-complains-about-missing-file"
"/usr/lib/busybox/ptest/testsuite/tar/tar-handles-empty-include-and-non-empty-exclude-list"
"/usr/lib/busybox/ptest/testsuite/tar/tar-handles-exclude-and-extract-lists"
"/usr/lib/busybox/ptest/testsuite/tar/tar_with_link_with_size"
"/usr/lib/busybox/ptest/testsuite/tar/tar-extracts-to-standard-output"
"/usr/lib/busybox/ptest/testsuite/tar/tar-handles-multiple-X-options"
"/usr/lib/busybox/ptest/testsuite/tar/tar_with_prefix_fields"
"/usr/lib/busybox/ptest/testsuite/tar/tar-handles-cz-options"
"/usr/lib/busybox/ptest/testsuite/tar/tar-extracts-from-standard-input"
"/usr/lib/busybox/ptest/testsuite/tar/tar-handles-nested-exclude"
"/usr/lib/busybox/ptest/testsuite/true/true-is-silent"
"/usr/lib/busybox/ptest/testsuite/true/true-returns-success"
"/usr/lib/busybox/ptest/testsuite/tr/tr-d-alnum-works"
"/usr/lib/busybox/ptest/testsuite/tr/tr-rejects-wrong-class"
"/usr/lib/busybox/ptest/testsuite/tr/tr-works"
"/usr/lib/busybox/ptest/testsuite/tr/tr-non-gnu"
"/usr/lib/busybox/ptest/testsuite/tr/tr-d-works"
"/usr/lib/busybox/ptest/testsuite/expand/expand-works-like-GNU"
"/usr/lib/busybox/ptest/testsuite/expr/expr-works"
"/usr/lib/busybox/ptest/testsuite/expr/expr-big"
"/usr/lib/busybox/ptest/testsuite/gzip/gzip-accepts-single-minus"
"/usr/lib/busybox/ptest/testsuite/gzip/gzip-removes-original-file"
"/usr/lib/busybox/ptest/testsuite/gzip/gzip-accepts-multiple-files"
"/usr/lib/busybox/ptest/testsuite/basename/basename-does-not-remove-identical-extension"
"/usr/lib/busybox/ptest/testsuite/basename/basename-works"
"/usr/lib/busybox/ptest/testsuite/cmp/cmp-detects-difference"
"/usr/lib/busybox/ptest/testsuite/tee/tee-appends-input"
"/usr/lib/busybox/ptest/testsuite/tee/tee-tees-input"
"/usr/lib/busybox/ptest/testsuite/dd/dd-prints-count-to-standard-error"
"/usr/lib/busybox/ptest/testsuite/dd/dd-reports-write-errors"
"/usr/lib/busybox/ptest/testsuite/dd/dd-accepts-if"
"/usr/lib/busybox/ptest/testsuite/dd/dd-accepts-of"
"/usr/lib/busybox/ptest/testsuite/dd/dd-copies-from-standard-input-to-standard-output"
"/usr/lib/busybox/ptest/testsuite/mv/mv-refuses-mv-dir-to-subdir"
"/usr/lib/busybox/ptest/testsuite/mv/mv-files-to-dir"
"/usr/lib/busybox/ptest/testsuite/mv/mv-moves-symlinks"
"/usr/lib/busybox/ptest/testsuite/mv/mv-moves-empty-file"
"/usr/lib/busybox/ptest/testsuite/mv/mv-follows-links"
"/usr/lib/busybox/ptest/testsuite/mv/mv-moves-unreadable-files"
"/usr/lib/busybox/ptest/testsuite/mv/mv-preserves-hard-links"
"/usr/lib/busybox/ptest/testsuite/mv/mv-moves-small-file"
"/usr/lib/busybox/ptest/testsuite/mv/mv-preserves-links"
"/usr/lib/busybox/ptest/testsuite/mv/mv-moves-file"
"/usr/lib/busybox/ptest/testsuite/mv/mv-removes-source-file"
"/usr/lib/busybox/ptest/testsuite/mv/mv-moves-large-file"
"/usr/lib/busybox/ptest/testsuite/mv/mv-moves-hardlinks"
"/usr/lib/busybox/ptest/testsuite/cat/cat-prints-a-file-and-standard-input"
"/usr/lib/busybox/ptest/testsuite/cat/cat-prints-a-file"

%files -n busybox-udhcpd
%defattr(-,-,-,-)
%dir "/etc"
%dir "/etc/init.d"
"/etc/init.d/busybox-udhcpd"

%files -n busybox-udhcpc
%defattr(-,-,-,-)
%dir "/usr"
%dir "/etc"
%dir "/usr/share"
%dir "/usr/share/udhcpc"
"/usr/share/udhcpc/default.script"
%dir "/etc/udhcpc.d"
"/etc/udhcpc.d/50default"

%files -n busybox-syslog
%defattr(-,-,-,-)
%dir "/etc"
%dir "/etc/init.d"
%config "/etc/syslog-startup.conf"
"/etc/syslog.conf"
"/etc/init.d/syslog"

%files -n busybox-hwclock
%defattr(-,-,-,-)
%dir "/etc"
%dir "/etc/init.d"
"/etc/init.d/hwclock.sh"

%files -n busybox-dbg
%defattr(-,-,-,-)
%dir "/usr"
%dir "/bin"
%dir "/usr/src"
%dir "/usr/src/debug"
%dir "/usr/src/debug/busybox"
%dir "/usr/src/debug/busybox/1.24.1-r0"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/sysklogd"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/procps"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/editors"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/findutils"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/e2fsprogs"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/console-tools"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libpwdgrp"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/loginutils"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/shell"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/init"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/modutils"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/debianutils"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/miscutils"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/sysklogd/klogd.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/sysklogd/logger.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/sysklogd/logread.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/sysklogd/syslogd.c"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/hostname.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/ifupdown.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/wget.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/nslookup.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/ip.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/nc.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/ifconfig.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/traceroute.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/telnet.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/ping.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/tftp.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/netstat.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/interface.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/route.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/ip_common.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/rtm_map.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/ll_map.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/ip_parse_common_args.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/rt_names.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/ll_types.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/rtm_map.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/utils.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/ll_addr.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/utils.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/rt_names.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/ipaddress.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/iproute.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/libnetlink.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/iptunnel.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/iplink.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/libnetlink.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/libiproute/ll_map.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/static_leases.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/signalpipe.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/arpping.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/common.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/dumpleases.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/dhcpc.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/leases.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/socket.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/dhcpd.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/files.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/packet.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/common.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/dhcpd.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/networking/udhcp/dhcpc.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/procps/top.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/procps/free.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/procps/fuser.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/procps/ps.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/procps/pidof.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/procps/watch.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/procps/kill.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/procps/uptime.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/procps/sysctl.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/procps/renice.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/editors/diff.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/editors/patch.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/editors/vi.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/editors/awk.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/editors/cmp.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/editors/sed.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/findutils/find.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/findutils/grep.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/findutils/xargs.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/rtc.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/isdirectory.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/recursive_action.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/get_line_from_file.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/concat_path_file.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/get_last_path_component.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/find_root_device.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/executable.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/herror_msg.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/inode_hash.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/change_identity.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/xregcomp.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/utmp.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/replace.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/lineedit_ptr_hack.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/safe_strncpy.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/read.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/printable.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/xfuncs_printf.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/uuencode.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/xfunc_die.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/xatonum.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/bb_do_delay.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/percent_decode.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/makedev.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/get_shell_name.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/procps.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/find_pid_by_name.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/print_flags.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/make_directory.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/copyfd.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/device_open.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/mode_string.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/default_error_retval.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/verror_msg.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/pw_encrypt_des.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/xgethostbyname.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/systemd_support.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/signals.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/crc32.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/simplify_path.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/lineedit.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/speed_table.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/get_console.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/read_printf.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/xrealloc_vector.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/get_volsize.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/copy_file.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/inet_common.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/human_readable.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/str_tolower.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/ask_confirmation.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/dump.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/auto_string.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/strrstr.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/correct_password.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/xatonum_template.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/chomp.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/remove_file.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/fflush_stdout_and_exit.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/bb_pwd.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/bb_strtonum.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/perror_msg.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/fgets_str.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/xreadlink.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/kernel_version.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/find_mount_point.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/skip_whitespace.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/pw_encrypt.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/time.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/xconnect.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/appletlib.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/single_argv.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/progress.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/update_passwd.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/wfopen_input.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/u_signal_names.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/parse_config.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/hash_md5_sha.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/safe_write.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/llist.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/messages.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/bb_askpass.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/loop.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/bb_bswap_64.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/match_fstype.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/full_write.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/info_msg.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/read_key.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/xfuncs.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/vfork_daemon_rexec.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/setup_environment.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/compare_string_array.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/concat_subpath_file.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/ptr_to_globals.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/endofname.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/pidfile.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/process_escape_sequence.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/safe_poll.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/parse_mode.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/perror_nomsg_and_die.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/in_ether.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/safe_gethostname.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/inet_cksum.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/last_char_is.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/run_shell.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/wfopen.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/xgetcwd.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/perror_nomsg.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/sysconf.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/pw_encrypt_md5.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/nuke_str.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/udp_io.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/bb_qsort.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/login.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/getopt32.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/fclose_nonstdin.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libbb/printable_string.c"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/libcoreutils"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/test.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/date.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/true.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/sleep.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/dd.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/shuf.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/yes.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/whoami.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/wc.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/head.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/stty.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/tail.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/chgrp.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/unlink.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/rmdir.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/tr.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/sort.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/touch.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/realpath.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/readlink.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/chown.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/sync.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/ls.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/stat.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/mkdir.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/false.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/chmod.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/logname.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/uniq.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/od.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/who.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/printf.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/rm.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/uname.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/ln.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/tty.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/id.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/test_ptr_hack.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/du.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/basename.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/dirname.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/pwd.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/md5_sha1_sum.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/tee.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/expr.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/nohup.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/cut.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/mknod.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/mkfifo.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/mv.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/env.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/chroot.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/cp.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/seq.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/usleep.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/cat.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/echo.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/df.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/libcoreutils/getopt_mk_fifo_nod.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/libcoreutils/coreutils.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/coreutils/libcoreutils/cp_mv_stat.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/e2fsprogs/fsck.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/e2fsprogs/e2fs_lib.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/e2fsprogs/chattr.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/e2fsprogs/e2fs_lib.h"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/bbunzip.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/unzip.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/gzip.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/tar.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/cpio.c"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/unxz"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/filter_accept_all.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/unsafe_prefix.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/decompress_bunzip2.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/header_skip.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/filter_accept_list.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/header_verbose_list.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/header_list.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/decompress_unxz.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/decompress_unlzma.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/decompress_uncompress.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/get_header_tar.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/decompress_gunzip.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/get_header_cpio.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/seek_by_jump.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/filter_accept_reject_list.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/find_list_entry.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/data_align.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/open_transformer.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/data_extract_all.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/data_skip.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/data_extract_to_stdout.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/init_handle.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/seek_by_read.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/unxz/xz.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/unxz/xz_lzma2.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/unxz/xz_dec_lzma2.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/unxz/xz_stream.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/archival/libarchive/unxz/xz_dec_stream.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/inet_common.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/busybox.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/dump.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/bb_archive.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/xregex.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/applet_tables.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/unicode.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/rtc_.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/libbb.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/xatonum.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/bb_e2fs_defs.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/volume_id.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/platform.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/include/applet_metadata.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/console-tools/openvt.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/console-tools/loadfont.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/console-tools/chvt.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/console-tools/clear.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/console-tools/resize.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/console-tools/dumpkmap.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/console-tools/reset.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/console-tools/deallocvt.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/console-tools/loadkmap.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/console-tools/setconsole.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/libpwdgrp/uidgid_get.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/loginutils/sulogin.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/loginutils/adduser.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/loginutils/su.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/loginutils/getty.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/loginutils/deluser.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/loginutils/vlock.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/loginutils/passwd.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/loginutils/login.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/loginutils/addgroup.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/shell/ash_ptr_hack.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/shell/shell_common.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/shell/math.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/shell/math.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/shell/ash.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/shell/shell_common.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/init/halt.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/init/mesg.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/modutils/lsmod.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/modutils/modprobe.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/modutils/depmod.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/modutils/modutils.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/modutils/rmmod.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/modutils/modutils.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/modutils/modinfo.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/modutils/insmod.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/debianutils/mktemp.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/debianutils/run_parts.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/debianutils/which.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/debianutils/start_stop_daemon.c"
%dir "/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/volume_id"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/swaponoff.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/losetup.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/getopt.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/hwclock.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/switch_root.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/more.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/pivot_root.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/flock.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/mount.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/dmesg.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/mkswap.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/hexdump.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/rdate.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/blkid.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/fdisk.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/fstrim.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/fbset.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/umount.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/volume_id/ext.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/volume_id/fat.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/volume_id/f2fs.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/volume_id/volume_id.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/volume_id/util.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/volume_id/squashfs.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/volume_id/get_devname.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/volume_id/volume_id_internal.h"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/util-linux/volume_id/btrfs.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/miscutils/strings.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/miscutils/less.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/miscutils/chrt.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/miscutils/time.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/miscutils/dc.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/miscutils/rfkill.c"
"/usr/src/debug/busybox/1.24.1-r0/busybox-1.24.1/miscutils/microcom.c"
%dir "/bin/.debug"
"/bin/.debug/busybox.suid"
"/bin/.debug/busybox.nosuid"

%files -n busybox-dev
%defattr(-,-,-,-)

