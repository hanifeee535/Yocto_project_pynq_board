cmd_libbb/perror_nomsg_and_die.o := arm-poky-linux-gnueabi-gcc  -march=armv7-a -marm -mfpu=neon -mfloat-abi=hard -mcpu=cortex-a9 --sysroot=/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot -Wp,-MD,libbb/.perror_nomsg_and_die.o.d   -std=gnu99 -Iinclude -Ilibbb  -include include/autoconf.h -D_GNU_SOURCE -DNDEBUG -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -D"BB_VER=KBUILD_STR(1.24.1)" -DBB_BT=AUTOCONF_TIMESTAMP  -Wall -Wshadow -Wwrite-strings -Wundef -Wstrict-prototypes -Wunused -Wunused-parameter -Wunused-function -Wunused-value -Wmissing-prototypes -Wmissing-declarations -Wno-format-security -Wdeclaration-after-statement -Wold-style-definition -fno-builtin-strlen -finline-limit=0 -fomit-frame-pointer -ffunction-sections -fdata-sections -fno-guess-branch-probability -funsigned-char -static-libgcc -falign-functions=1 -falign-jumps=1 -falign-labels=1 -falign-loops=1 -fno-unwind-tables -fno-asynchronous-unwind-tables -fno-builtin-printf -Os -O2 -pipe -g -feliminate-unused-debug-types -march=armv7-a -marm -mfpu=neon -mfloat-abi=hard -mcpu=cortex-a9  -O2 -pipe -g -feliminate-unused-debug-types -fdebug-prefix-map=/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0=/usr/src/debug/busybox/1.24.1-r0 -fdebug-prefix-map=/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot-native= -fdebug-prefix-map=/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot=    -D"KBUILD_STR(s)=\#s" -D"KBUILD_BASENAME=KBUILD_STR(perror_nomsg_and_die)"  -D"KBUILD_MODNAME=KBUILD_STR(perror_nomsg_and_die)" -c -o libbb/perror_nomsg_and_die.o libbb/perror_nomsg_and_die.c

deps_libbb/perror_nomsg_and_die.o := \
  libbb/perror_nomsg_and_die.c \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/stdc-predef.h \
  include/platform.h \
    $(wildcard include/config/werror.h) \
    $(wildcard include/config/big/endian.h) \
    $(wildcard include/config/little/endian.h) \
    $(wildcard include/config/nommu.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot-native/usr/lib/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/7.3.0/include-fixed/limits.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot-native/usr/lib/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/7.3.0/include-fixed/syslimits.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/limits.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/libc-header-start.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/features.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/sys/cdefs.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/wordsize.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/wordsize-32.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/long-double.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/long-double-32.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/gnu/stubs.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/gnu/stubs-32.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/gnu/stubs-hard.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/posix1_lim.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/local_lim.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/local_lim-32.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/linux/limits.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/posix2_lim.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/xopen_lim.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/uio_lim.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/byteswap.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/byteswap.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/typesizes.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/typesizes-32.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/byteswap-16.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/endian.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/endian.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/endian-32.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/uintn-identity.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot-native/usr/lib/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/7.3.0/include/stdint.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/stdint.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/wchar.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/stdint-intn.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/stdint-uintn.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot-native/usr/lib/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/7.3.0/include/stdbool.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/unistd.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/posix_opt.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/environments.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot-native/usr/lib/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/7.3.0/include/stddef.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/confname.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/getopt_posix.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/cortexa9hf-neon-poky-linux-gnueabi/busybox/1.24.1-r0/recipe-sysroot/usr/include/bits/getopt_core.h \

libbb/perror_nomsg_and_die.o: $(deps_libbb/perror_nomsg_and_die.o)

$(deps_libbb/perror_nomsg_and_die.o):
