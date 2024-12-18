cmd_lib/crc16.o := arm-poky-linux-gnueabi-gcc  --sysroot=/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/recipe-sysroot -Wp,-MD,lib/.crc16.o.d  -nostdinc -isystem /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/recipe-sysroot-native/usr/bin/arm-poky-linux-gnueabi/../../lib/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/7.3.0/include -Iinclude  -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include  -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/include -include /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/linux/kconfig.h  -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/lib -Ilib -D__KERNEL__ -D__UBOOT__ -Wall -Wstrict-prototypes -Wno-format-security -fno-builtin -ffreestanding -Os -fno-stack-protector -fno-delete-null-pointer-checks -g -fstack-usage -Wno-format-nonliteral -Werror=date-time -D__ARM__ -marm -mno-thumb-interwork -mabi=aapcs-linux -mword-relocations -fno-pic -mno-unaligned-access -ffunction-sections -fdata-sections -fno-common -ffixed-r9 -msoft-float -pipe -march=armv7-a   -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/mach-zynq/include    -D"KBUILD_STR(s)=\#s" -D"KBUILD_BASENAME=KBUILD_STR(crc16)"  -D"KBUILD_MODNAME=KBUILD_STR(crc16)" -c -o lib/crc16.o /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/lib/crc16.c

source_lib/crc16.o := /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/lib/crc16.c

deps_lib/crc16.o := \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/crc.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/linux/types.h \
    $(wildcard include/config/uid16.h) \
    $(wildcard include/config/use/stdint.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/linux/posix_types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/linux/stddef.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/include/asm/posix_types.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/include/asm/types.h \
    $(wildcard include/config/arm64.h) \
    $(wildcard include/config/phys/64bit.h) \
    $(wildcard include/config/dma/addr/t/64bit.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/recipe-sysroot-native/usr/lib/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/7.3.0/include/stdbool.h \

lib/crc16.o: $(deps_lib/crc16.o)

$(deps_lib/crc16.o):
