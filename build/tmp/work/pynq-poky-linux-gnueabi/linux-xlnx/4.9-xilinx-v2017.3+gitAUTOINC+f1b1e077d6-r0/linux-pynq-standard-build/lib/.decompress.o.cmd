cmd_lib/decompress.o := arm-poky-linux-gnueabi-gcc  -mno-thumb-interwork -marm -fuse-ld=bfd -ffile-prefix-map=/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source=/kernel-source/  -Wp,-MD,lib/.decompress.o.d  -nostdinc -isystem /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/linux-xlnx/4.9-xilinx-v2017.3+gitAUTOINC+f1b1e077d6-r0/recipe-sysroot-native/usr/bin/arm-poky-linux-gnueabi/../../lib/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/7.3.0/include -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include -I./arch/arm/include/generated/uapi -I./arch/arm/include/generated  -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include -I./include -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include/uapi -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi -I./include/generated/uapi -include /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/kconfig.h -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/lib -Ilib -D__KERNEL__ -mlittle-endian -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -Werror-implicit-function-declaration -Wno-format-security -std=gnu89 -fno-PIE -fno-dwarf2-cfi-asm -fno-ipa-sra -mabi=aapcs-linux -mno-thumb-interwork -mfpu=vfp -funwind-tables -marm -D__LINUX_ARM_ARCH__=7 -march=armv7-a -msoft-float -Uarm -fno-delete-null-pointer-checks -Wno-frame-address -Os -Wno-maybe-uninitialized --param=allow-store-data-races=0 -Wframe-larger-than=1024 -fno-stack-protector -Wno-unused-but-set-variable -Wno-unused-const-variable -fomit-frame-pointer -fno-var-tracking-assignments -Wdeclaration-after-statement -Wno-pointer-sign -fno-strict-overflow -fconserve-stack -Werror=implicit-int -Werror=strict-prototypes -Werror=date-time -Werror=incompatible-pointer-types -DCC_HAVE_ASM_GOTO    -DKBUILD_BASENAME='"decompress"'  -DKBUILD_MODNAME='"decompress"' -c -o lib/.tmp_decompress.o /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/lib/decompress.c

source_lib/decompress.o := /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/lib/decompress.c

deps_lib/decompress.o := \
    $(wildcard include/config/decompress/gzip.h) \
    $(wildcard include/config/decompress/bzip2.h) \
    $(wildcard include/config/decompress/lzma.h) \
    $(wildcard include/config/decompress/xz.h) \
    $(wildcard include/config/decompress/lzo.h) \
    $(wildcard include/config/decompress/lz4.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/decompress/generic.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/decompress/bunzip2.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/decompress/unlzma.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/decompress/unxz.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/decompress/inflate.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/decompress/unlzo.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/decompress/unlz4.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/types.h \
    $(wildcard include/config/have/uid16.h) \
    $(wildcard include/config/uid16.h) \
    $(wildcard include/config/lbdaf.h) \
    $(wildcard include/config/arch/dma/addr/t/64bit.h) \
    $(wildcard include/config/phys/addr/t/64bit.h) \
    $(wildcard include/config/64bit.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/linux/types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include/asm/types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/asm-generic/int-ll64.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/asm-generic/int-ll64.h \
  arch/arm/include/generated/asm/bitsperlong.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/asm-generic/bitsperlong.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/asm-generic/bitsperlong.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/linux/posix_types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/stddef.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/linux/stddef.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/compiler.h \
    $(wildcard include/config/sparse/rcu/pointer.h) \
    $(wildcard include/config/trace/branch/profiling.h) \
    $(wildcard include/config/profile/all/branches.h) \
    $(wildcard include/config/kasan.h) \
    $(wildcard include/config/enable/must/check.h) \
    $(wildcard include/config/enable/warn/deprecated.h) \
    $(wildcard include/config/kprobes.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/compiler-gcc.h \
    $(wildcard include/config/arch/supports/optimized/inlining.h) \
    $(wildcard include/config/optimize/inlining.h) \
    $(wildcard include/config/gcov/kernel.h) \
    $(wildcard include/config/arch/use/builtin/bswap.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include/uapi/asm/posix_types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/asm-generic/posix_types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/string.h \
    $(wildcard include/config/binary/printf.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/linux-xlnx/4.9-xilinx-v2017.3+gitAUTOINC+f1b1e077d6-r0/recipe-sysroot-native/usr/lib/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/7.3.0/include/stdarg.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/linux/string.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include/asm/string.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/init.h \
    $(wildcard include/config/debug/rodata.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/printk.h \
    $(wildcard include/config/message/loglevel/default.h) \
    $(wildcard include/config/early/printk.h) \
    $(wildcard include/config/printk/nmi.h) \
    $(wildcard include/config/printk.h) \
    $(wildcard include/config/dynamic/debug.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/kern_levels.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/linkage.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/stringify.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/export.h \
    $(wildcard include/config/have/underscore/symbol/prefix.h) \
    $(wildcard include/config/modules.h) \
    $(wildcard include/config/modversions.h) \
    $(wildcard include/config/trim/unused/ksyms.h) \
    $(wildcard include/config/unused/symbols.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include/asm/linkage.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/cache.h \
    $(wildcard include/config/smp.h) \
    $(wildcard include/config/arch/has/cache/line/size.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/linux/kernel.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/linux/sysinfo.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include/asm/cache.h \
    $(wildcard include/config/arm/l1/cache/shift.h) \
    $(wildcard include/config/aeabi.h) \

lib/decompress.o: $(deps_lib/decompress.o)

$(deps_lib/decompress.o):