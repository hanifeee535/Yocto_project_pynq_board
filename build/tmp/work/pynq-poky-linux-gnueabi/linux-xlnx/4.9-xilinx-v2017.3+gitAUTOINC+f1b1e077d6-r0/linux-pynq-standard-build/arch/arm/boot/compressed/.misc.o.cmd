cmd_arch/arm/boot/compressed/misc.o := arm-poky-linux-gnueabi-gcc  -mno-thumb-interwork -marm -fuse-ld=bfd -ffile-prefix-map=/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source=/kernel-source/  -Wp,-MD,arch/arm/boot/compressed/.misc.o.d  -nostdinc -isystem /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/linux-xlnx/4.9-xilinx-v2017.3+gitAUTOINC+f1b1e077d6-r0/recipe-sysroot-native/usr/bin/arm-poky-linux-gnueabi/../../lib/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/7.3.0/include -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include -I./arch/arm/include/generated/uapi -I./arch/arm/include/generated  -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include -I./include -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include/uapi -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi -I./include/generated/uapi -include /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/kconfig.h -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/boot/compressed -Iarch/arm/boot/compressed -D__KERNEL__ -mlittle-endian -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -Werror-implicit-function-declaration -Wno-format-security -std=gnu89 -fno-PIE -fno-dwarf2-cfi-asm -fno-ipa-sra -mabi=aapcs-linux -mno-thumb-interwork -mfpu=vfp -funwind-tables -marm -D__LINUX_ARM_ARCH__=7 -march=armv7-a -msoft-float -Uarm -fno-delete-null-pointer-checks -Wno-frame-address -Os -Wno-maybe-uninitialized --param=allow-store-data-races=0 -Wframe-larger-than=1024 -fno-stack-protector -Wno-unused-but-set-variable -Wno-unused-const-variable -fomit-frame-pointer -fno-var-tracking-assignments -Wdeclaration-after-statement -Wno-pointer-sign -fno-strict-overflow -fconserve-stack -Werror=implicit-int -Werror=strict-prototypes -Werror=date-time -Werror=incompatible-pointer-types -DCC_HAVE_ASM_GOTO -DDISABLE_BRANCH_PROFILING -fpic -mno-single-pic-base -fno-builtin  -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/boot/compressed    -DKBUILD_BASENAME='"misc"'  -DKBUILD_MODNAME='"misc"' -c -o arch/arm/boot/compressed/.tmp_misc.o /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/boot/compressed/misc.c

source_arch/arm/boot/compressed/misc.o := /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/boot/compressed/misc.c

deps_arch/arm/boot/compressed/misc.o := \
    $(wildcard include/config/uncompress/include.h) \
    $(wildcard include/config/debug/icedcc.h) \
    $(wildcard include/config/cpu/v6.h) \
    $(wildcard include/config/cpu/v6k.h) \
    $(wildcard include/config/cpu/v7.h) \
    $(wildcard include/config/cpu/xscale.h) \
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
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/linux/types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include/asm/types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/asm-generic/int-ll64.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/asm-generic/int-ll64.h \
  arch/arm/include/generated/asm/bitsperlong.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/asm-generic/bitsperlong.h \
    $(wildcard include/config/64bit.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/asm-generic/bitsperlong.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/linux/posix_types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/stddef.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/linux/stddef.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include/uapi/asm/posix_types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/uapi/asm-generic/posix_types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/types.h \
    $(wildcard include/config/have/uid16.h) \
    $(wildcard include/config/uid16.h) \
    $(wildcard include/config/lbdaf.h) \
    $(wildcard include/config/arch/dma/addr/t/64bit.h) \
    $(wildcard include/config/phys/addr/t/64bit.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/linkage.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/stringify.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/include/linux/export.h \
    $(wildcard include/config/have/underscore/symbol/prefix.h) \
    $(wildcard include/config/modules.h) \
    $(wildcard include/config/modversions.h) \
    $(wildcard include/config/trim/unused/ksyms.h) \
    $(wildcard include/config/unused/symbols.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include/asm/linkage.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work-shared/pynq/kernel-source/arch/arm/include/debug/uncompress.h \
    $(wildcard include/config/debug/uncompress.h) \

arch/arm/boot/compressed/misc.o: $(deps_arch/arm/boot/compressed/misc.o)

$(deps_arch/arm/boot/compressed/misc.o):
