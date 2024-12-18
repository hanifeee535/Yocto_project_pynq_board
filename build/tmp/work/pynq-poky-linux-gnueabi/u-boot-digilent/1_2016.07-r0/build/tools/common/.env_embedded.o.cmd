cmd_tools/common/env_embedded.o := gcc  -isystem/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/recipe-sysroot-native/usr/include -O2 -pipe -L/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/recipe-sysroot-native/usr/lib -L/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/recipe-sysroot-native/lib -Wl,-rpath-link,/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/recipe-sysroot-native/usr/lib -Wl,-rpath-link,/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/recipe-sysroot-native/lib -Wl,-rpath,/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/recipe-sysroot-native/usr/lib -Wl,-rpath,/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/recipe-sysroot-native/lib -Wl,-O1 -Wl,--allow-shlib-undefined -Wl,--dynamic-linker=/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/sysroots-uninative/x86_64-linux/lib/ld-linux-x86-64.so.2 -Wp,-MD,tools/common/.env_embedded.o.d -Itools -Wall -Wstrict-prototypes -O2 -fomit-frame-pointer -DCONFIG_FIT_SIGNATURE -include /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/libfdt_env.h -idirafterinclude -idirafter/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include -idirafter/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/include   -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/lib/libfdt   -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/tools -DCONFIG_SYS_TEXT_BASE=0x4000000 -DUSE_HOSTCC -D__KERNEL_STRICT_NAMES -D_GNU_SOURCE -c -o tools/common/env_embedded.o tools/common/env_embedded.c

source_tools/common/env_embedded.o := tools/common/env_embedded.c

deps_tools/common/env_embedded.o := \
  /usr/include/stdc-predef.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/libfdt_env.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/compiler.h \
    $(wildcard include/config/use/stdint.h) \
  /usr/lib/gcc/x86_64-linux-gnu/7/include/stddef.h \
  /usr/lib/gcc/x86_64-linux-gnu/7/include/stdint.h \
  /usr/include/stdint.h \
  /usr/include/x86_64-linux-gnu/bits/libc-header-start.h \
  /usr/include/features.h \
  /usr/include/x86_64-linux-gnu/sys/cdefs.h \
  /usr/include/x86_64-linux-gnu/bits/wordsize.h \
  /usr/include/x86_64-linux-gnu/bits/long-double.h \
  /usr/include/x86_64-linux-gnu/gnu/stubs.h \
  /usr/include/x86_64-linux-gnu/gnu/stubs-64.h \
  /usr/include/x86_64-linux-gnu/bits/types.h \
  /usr/include/x86_64-linux-gnu/bits/typesizes.h \
  /usr/include/x86_64-linux-gnu/bits/wchar.h \
  /usr/include/x86_64-linux-gnu/bits/stdint-intn.h \
  /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h \
  /usr/include/errno.h \
  /usr/include/x86_64-linux-gnu/bits/errno.h \
  /usr/include/linux/errno.h \
  /usr/include/x86_64-linux-gnu/asm/errno.h \
  /usr/include/asm-generic/errno.h \
  /usr/include/asm-generic/errno-base.h \
  /usr/include/stdlib.h \
  /usr/include/x86_64-linux-gnu/bits/waitflags.h \
  /usr/include/x86_64-linux-gnu/bits/waitstatus.h \
  /usr/include/x86_64-linux-gnu/bits/floatn.h \
  /usr/include/x86_64-linux-gnu/bits/floatn-common.h \
  /usr/include/x86_64-linux-gnu/bits/types/locale_t.h \
  /usr/include/x86_64-linux-gnu/bits/types/__locale_t.h \
  /usr/include/x86_64-linux-gnu/sys/types.h \
  /usr/include/x86_64-linux-gnu/bits/types/clock_t.h \
  /usr/include/x86_64-linux-gnu/bits/types/clockid_t.h \
  /usr/include/x86_64-linux-gnu/bits/types/time_t.h \
  /usr/include/x86_64-linux-gnu/bits/types/timer_t.h \
  /usr/include/endian.h \
  /usr/include/x86_64-linux-gnu/bits/endian.h \
  /usr/include/x86_64-linux-gnu/bits/byteswap.h \
  /usr/include/x86_64-linux-gnu/bits/byteswap-16.h \
  /usr/include/x86_64-linux-gnu/bits/uintn-identity.h \
  /usr/include/x86_64-linux-gnu/sys/select.h \
  /usr/include/x86_64-linux-gnu/bits/select.h \
  /usr/include/x86_64-linux-gnu/bits/types/sigset_t.h \
  /usr/include/x86_64-linux-gnu/bits/types/__sigset_t.h \
  /usr/include/x86_64-linux-gnu/bits/types/struct_timeval.h \
  /usr/include/x86_64-linux-gnu/bits/types/struct_timespec.h \
  /usr/include/x86_64-linux-gnu/bits/select2.h \
  /usr/include/x86_64-linux-gnu/sys/sysmacros.h \
  /usr/include/x86_64-linux-gnu/bits/sysmacros.h \
  /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h \
  /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h \
  /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h \
  /usr/include/alloca.h \
  /usr/include/x86_64-linux-gnu/bits/stdlib-bsearch.h \
  /usr/include/x86_64-linux-gnu/bits/stdlib-float.h \
  /usr/include/x86_64-linux-gnu/bits/stdlib.h \
  /usr/include/stdio.h \
  /usr/include/x86_64-linux-gnu/bits/types/__FILE.h \
  /usr/include/x86_64-linux-gnu/bits/types/FILE.h \
  /usr/include/x86_64-linux-gnu/bits/libio.h \
  /usr/include/x86_64-linux-gnu/bits/_G_config.h \
    $(wildcard include/config/h.h) \
  /usr/include/x86_64-linux-gnu/bits/types/__mbstate_t.h \
  /usr/lib/gcc/x86_64-linux-gnu/7/include/stdarg.h \
  /usr/include/x86_64-linux-gnu/bits/stdio_lim.h \
  /usr/include/x86_64-linux-gnu/bits/sys_errlist.h \
  /usr/include/x86_64-linux-gnu/bits/stdio.h \
  /usr/include/x86_64-linux-gnu/bits/stdio2.h \
  /usr/include/string.h \
  /usr/include/strings.h \
  /usr/include/x86_64-linux-gnu/bits/strings_fortified.h \
  /usr/include/x86_64-linux-gnu/bits/string_fortified.h \
  /usr/include/x86_64-linux-gnu/sys/mman.h \
  /usr/include/x86_64-linux-gnu/bits/mman.h \
  /usr/include/x86_64-linux-gnu/bits/mman-linux.h \
  /usr/include/x86_64-linux-gnu/bits/mman-shared.h \
  /usr/include/fcntl.h \
  /usr/include/x86_64-linux-gnu/bits/fcntl.h \
  /usr/include/x86_64-linux-gnu/bits/fcntl-linux.h \
  /usr/include/x86_64-linux-gnu/bits/types/struct_iovec.h \
  /usr/include/linux/falloc.h \
  /usr/include/x86_64-linux-gnu/bits/stat.h \
  /usr/include/x86_64-linux-gnu/bits/fcntl2.h \
  /usr/include/byteswap.h \
  /usr/include/time.h \
  /usr/include/x86_64-linux-gnu/bits/time.h \
  /usr/include/x86_64-linux-gnu/bits/timex.h \
  /usr/include/x86_64-linux-gnu/bits/types/struct_tm.h \
  /usr/include/x86_64-linux-gnu/bits/types/struct_itimerspec.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/linux/types.h \
    $(wildcard include/config/uid16.h) \
  /usr/include/linux/posix_types.h \
  /usr/include/linux/stddef.h \
  /usr/include/x86_64-linux-gnu/asm/posix_types.h \
  /usr/include/x86_64-linux-gnu/asm/posix_types_64.h \
  /usr/include/asm-generic/posix_types.h \
  /usr/include/x86_64-linux-gnu/asm/bitsperlong.h \
  /usr/include/asm-generic/bitsperlong.h \
    $(wildcard include/config/64bit.h) \
  /usr/include/x86_64-linux-gnu/asm/types.h \
  /usr/include/asm-generic/types.h \
  /usr/include/asm-generic/int-ll64.h \
  /usr/lib/gcc/x86_64-linux-gnu/7/include/stdbool.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/tools/../common/env_embedded.c \
    $(wildcard include/config/build/envcrc.h) \
    $(wildcard include/config/sys/use/ppcenv.h) \
    $(wildcard include/config/env/addr/redund.h) \
    $(wildcard include/config/env/offset.h) \
  include/config.h \
    $(wildcard include/config/boarddir.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/config_defaults.h \
    $(wildcard include/config/defaults/h/.h) \
    $(wildcard include/config/bootm/linux.h) \
    $(wildcard include/config/bootm/netbsd.h) \
    $(wildcard include/config/bootm/plan9.h) \
    $(wildcard include/config/bootm/rtems.h) \
    $(wildcard include/config/bootm/vxworks.h) \
    $(wildcard include/config/gzip.h) \
    $(wildcard include/config/zlib.h) \
    $(wildcard include/config/partitions.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/config_uncmd_spl.h \
    $(wildcard include/config/uncmd/spl/h//.h) \
    $(wildcard include/config/spl/build.h) \
    $(wildcard include/config/spl/dm.h) \
    $(wildcard include/config/dm/serial.h) \
    $(wildcard include/config/dm/gpio.h) \
    $(wildcard include/config/dm/i2c.h) \
    $(wildcard include/config/dm/spi.h) \
    $(wildcard include/config/dm/warn.h) \
    $(wildcard include/config/dm/stdio.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/configs/zynq_artyz7.h \
    $(wildcard include/config/zynq/artyz7/h.h) \
    $(wildcard include/config/sys/no/flash.h) \
    $(wildcard include/config/zynq/usb.h) \
    $(wildcard include/config/zynq/i2c0.h) \
    $(wildcard include/config/zynq/i2c1.h) \
    $(wildcard include/config/sys/i2c/eeprom/addr/len.h) \
    $(wildcard include/config/cmd/eeprom.h) \
    $(wildcard include/config/zynq/gem/eeprom/addr.h) \
    $(wildcard include/config/zynq/gem/i2c/mac/offset.h) \
    $(wildcard include/config/display.h) \
    $(wildcard include/config/i2c/edid.h) \
    $(wildcard include/config/zynq/gem/spi/mac/offset.h) \
    $(wildcard include/config/zynq/ps/clk/freq.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/configs/zynq-common.h \
    $(wildcard include/config/zynq/common/h.h) \
    $(wildcard include/config/cpu/freq/hz.h) \
    $(wildcard include/config/sys/cacheline/size.h) \
    $(wildcard include/config/sys/l2cache/off.h) \
    $(wildcard include/config/sys/l2/pl310.h) \
    $(wildcard include/config/sys/pl310/base.h) \
    $(wildcard include/config/sys/timerbase.h) \
    $(wildcard include/config/sys/timer/counts/down.h) \
    $(wildcard include/config/sys/timer/counter.h) \
    $(wildcard include/config/baudrate.h) \
    $(wildcard include/config/sys/baudrate/table.h) \
    $(wildcard include/config/arm/dcc.h) \
    $(wildcard include/config/zynq/serial.h) \
    $(wildcard include/config/zynq/gem.h) \
    $(wildcard include/config/mii.h) \
    $(wildcard include/config/sys/fault/echo/link/down.h) \
    $(wildcard include/config/phy/marvell.h) \
    $(wildcard include/config/phy/realtek.h) \
    $(wildcard include/config/phy/xilinx.h) \
    $(wildcard include/config/bootp/serverip.h) \
    $(wildcard include/config/bootp/bootpath.h) \
    $(wildcard include/config/bootp/gateway.h) \
    $(wildcard include/config/bootp/hostname.h) \
    $(wildcard include/config/bootp/may/fail.h) \
    $(wildcard include/config/zynq/spi.h) \
    $(wildcard include/config/zynq/qspi.h) \
    $(wildcard include/config/sf/default/speed.h) \
    $(wildcard include/config/spi/flash/issi.h) \
    $(wildcard include/config/sys/flash/base.h) \
    $(wildcard include/config/sys/flash/size.h) \
    $(wildcard include/config/sys/max/flash/banks.h) \
    $(wildcard include/config/sys/max/flash/sect.h) \
    $(wildcard include/config/sys/flash/erase/tout.h) \
    $(wildcard include/config/sys/flash/write/tout.h) \
    $(wildcard include/config/flash/show/progress.h) \
    $(wildcard include/config/sys/flash/cfi.h) \
    $(wildcard include/config/sys/flash/empty/info.h) \
    $(wildcard include/config/flash/cfi/driver.h) \
    $(wildcard include/config/sys/flash/protection.h) \
    $(wildcard include/config/sys/flash/use/buffer/write.h) \
    $(wildcard include/config/zynq/sdhci.h) \
    $(wildcard include/config/mmc.h) \
    $(wildcard include/config/generic/mmc.h) \
    $(wildcard include/config/sdhci.h) \
    $(wildcard include/config/zynq/sdhci/max/freq.h) \
    $(wildcard include/config/usb/ehci.h) \
    $(wildcard include/config/usb/storage.h) \
    $(wildcard include/config/usb/ehci/zynq.h) \
    $(wildcard include/config/ehci/is/tdi.h) \
    $(wildcard include/config/usb/max/controller/count.h) \
    $(wildcard include/config/sys/dfu/data/buf/size.h) \
    $(wildcard include/config/usb/function/dfu.h) \
    $(wildcard include/config/dfu/ram.h) \
    $(wildcard include/config/usb/cable/check.h) \
    $(wildcard include/config/cmd/thor/download.h) \
    $(wildcard include/config/thor/reset/off.h) \
    $(wildcard include/config/usb/function/thor.h) \
    $(wildcard include/config/dfu/mmc.h) \
    $(wildcard include/config/support/vfat.h) \
    $(wildcard include/config/fat/write.h) \
    $(wildcard include/config/dos/partition.h) \
    $(wildcard include/config/sys/i2c/zynq.h) \
    $(wildcard include/config/sys/i2c.h) \
    $(wildcard include/config/sys/i2c/zynq/speed.h) \
    $(wildcard include/config/sys/i2c/zynq/slave.h) \
    $(wildcard include/config/zynq/eeprom.h) \
    $(wildcard include/config/sys/i2c/eeprom/addr.h) \
    $(wildcard include/config/sys/eeprom/page/write/bits.h) \
    $(wildcard include/config/sys/eeprom/page/write/delay/ms.h) \
    $(wildcard include/config/sys/eeprom/size.h) \
    $(wildcard include/config/env/size.h) \
    $(wildcard include/config/env/overwrite.h) \
    $(wildcard include/config/env/is/nowhere.h) \
    $(wildcard include/config/env/is/in/flash.h) \
    $(wildcard include/config/env/is/in/spi/flash.h) \
    $(wildcard include/config/env/sect/size.h) \
    $(wildcard include/config/bootdelay.h) \
    $(wildcard include/config/preboot.h) \
    $(wildcard include/config/extra/env/settings.h) \
    $(wildcard include/config/bootcommand.h) \
    $(wildcard include/config/sys/load/addr.h) \
    $(wildcard include/config/cmdline/editing.h) \
    $(wildcard include/config/auto/complete.h) \
    $(wildcard include/config/board/late/init.h) \
    $(wildcard include/config/display/boardinfo.h) \
    $(wildcard include/config/sys/longhelp.h) \
    $(wildcard include/config/clocks.h) \
    $(wildcard include/config/cmd/clk.h) \
    $(wildcard include/config/sys/maxargs.h) \
    $(wildcard include/config/sys/cbsize.h) \
    $(wildcard include/config/sys/pbsize.h) \
    $(wildcard include/config/sys/prompt.h) \
    $(wildcard include/config/sys/text/base.h) \
    $(wildcard include/config/nr/dram/banks.h) \
    $(wildcard include/config/sys/memtest/start.h) \
    $(wildcard include/config/sys/memtest/end.h) \
    $(wildcard include/config/sys/malloc/len.h) \
    $(wildcard include/config/sys/init/ram/addr.h) \
    $(wildcard include/config/sys/init/ram/size.h) \
    $(wildcard include/config/sys/init/sp/addr.h) \
    $(wildcard include/config/fpga.h) \
    $(wildcard include/config/fpga/xilinx.h) \
    $(wildcard include/config/fpga/zynqpl.h) \
    $(wildcard include/config/cmd/fpga/loadmk.h) \
    $(wildcard include/config/cmd/fpga/loadp.h) \
    $(wildcard include/config/cmd/fpga/loadbp.h) \
    $(wildcard include/config/cmd/fpga/loadfs.h) \
    $(wildcard include/config/image/format/legacy.h) \
    $(wildcard include/config/display/boardinfo/late.h) \
    $(wildcard include/config/sys/bootm/len.h) \
    $(wildcard include/config/sys/mmc/max/device.h) \
    $(wildcard include/config/sys/ldscript.h) \
    $(wildcard include/config/cmd/spl.h) \
    $(wildcard include/config/spl/framework.h) \
    $(wildcard include/config/spl/libcommon/support.h) \
    $(wildcard include/config/spl/libgeneric/support.h) \
    $(wildcard include/config/spl/serial/support.h) \
    $(wildcard include/config/spl/board/init.h) \
    $(wildcard include/config/spl/ram/device.h) \
    $(wildcard include/config/spl/ldscript.h) \
    $(wildcard include/config/spl/fpga/support.h) \
    $(wildcard include/config/spl/fpga/load/addr.h) \
    $(wildcard include/config/spl/fpga/load/args/name.h) \
    $(wildcard include/config/spl/mmc/support.h) \
    $(wildcard include/config/sys/mmcsd/raw/mode/u/boot/sector.h) \
    $(wildcard include/config/sys/u/boot/max/size/sectors.h) \
    $(wildcard include/config/sys/mmcsd/fs/boot/partition.h) \
    $(wildcard include/config/spl/libdisk/support.h) \
    $(wildcard include/config/spl/fat/support.h) \
    $(wildcard include/config/spl/fs/load/payload/name.h) \
    $(wildcard include/config/sys/dcache/off.h) \
    $(wildcard include/config/sys/spl/args/addr.h) \
    $(wildcard include/config/spl/fs/load/args/name.h) \
    $(wildcard include/config/spl/fs/load/kernel/name.h) \
    $(wildcard include/config/sys/mmcsd/raw/mode/args/sector.h) \
    $(wildcard include/config/sys/mmcsd/raw/mode/args/sectors.h) \
    $(wildcard include/config/sys/mmcsd/raw/mode/kernel/sector.h) \
    $(wildcard include/config/spl/spi/support.h) \
    $(wildcard include/config/spl/spi/load.h) \
    $(wildcard include/config/spl/spi/flash/support.h) \
    $(wildcard include/config/sys/spi/u/boot/offs.h) \
    $(wildcard include/config/sys/spi/args/offs.h) \
    $(wildcard include/config/sys/spi/args/size.h) \
    $(wildcard include/config/sys/spi/kernel/offs.h) \
    $(wildcard include/config/spl/os/boot.h) \
    $(wildcard include/config/spl/text/base.h) \
    $(wildcard include/config/spl/max/size.h) \
    $(wildcard include/config/sys/spl/malloc/start.h) \
    $(wildcard include/config/sys/spl/malloc/size.h) \
    $(wildcard include/config/spl/stack.h) \
    $(wildcard include/config/spl/bss/start/addr.h) \
    $(wildcard include/config/spl/bss/max/size.h) \
    $(wildcard include/config/sys/uboot/start.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/include/asm/config.h \
    $(wildcard include/config/h/.h) \
    $(wildcard include/config/lmb.h) \
    $(wildcard include/config/sys/boot/ramdisk/high.h) \
    $(wildcard include/config/arm64.h) \
    $(wildcard include/config/phys/64bit.h) \
    $(wildcard include/config/static/rela.h) \
    $(wildcard include/config/ls102xa.h) \
    $(wildcard include/config/cpu/pxa27x.h) \
    $(wildcard include/config/cpu/monahans.h) \
    $(wildcard include/config/cpu/pxa25x.h) \
    $(wildcard include/config/fsl/layerscape.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/config_fallbacks.h \
    $(wildcard include/config/fallbacks/h.h) \
    $(wildcard include/config/spl.h) \
    $(wildcard include/config/spl/pad/to.h) \
    $(wildcard include/config/cmd/fat.h) \
    $(wildcard include/config/fs/fat.h) \
    $(wildcard include/config/cmd/ext4.h) \
    $(wildcard include/config/cmd/ext2.h) \
    $(wildcard include/config/fs/ext4.h) \
    $(wildcard include/config/cmd/ext4/write.h) \
    $(wildcard include/config/ext4/write.h) \
    $(wildcard include/config/cmd/ide.h) \
    $(wildcard include/config/cmd/sata.h) \
    $(wildcard include/config/scsi.h) \
    $(wildcard include/config/cmd/usb.h) \
    $(wildcard include/config/cmd/part.h) \
    $(wildcard include/config/cmd/gpt.h) \
    $(wildcard include/config/systemace.h) \
    $(wildcard include/config/sandbox.h) \
    $(wildcard include/config/partition/uuids.h) \
    $(wildcard include/config/efi/partition.h) \
    $(wildcard include/config/random/uuid.h) \
    $(wildcard include/config/cmd/uuid.h) \
    $(wildcard include/config/bootp/pxe.h) \
    $(wildcard include/config/lib/uuid.h) \
    $(wildcard include/config/lib/rand.h) \
    $(wildcard include/config/lib/hw/rand.h) \
    $(wildcard include/config/api.h) \
    $(wildcard include/config/lcd.h) \
    $(wildcard include/config/cmd/bmp.h) \
    $(wildcard include/config/fit/signature.h) \
    $(wildcard include/config/disable/image/legacy.h) \
    $(wildcard include/config/cmdline.h) \
    $(wildcard include/config/menu.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/environment.h \
    $(wildcard include/config/env/addr.h) \
    $(wildcard include/config/env/offset/redund.h) \
    $(wildcard include/config/env/size/redund.h) \
    $(wildcard include/config/sys/monitor/base.h) \
    $(wildcard include/config/sys/monitor/len.h) \
    $(wildcard include/config/sys/redundand/environment.h) \
    $(wildcard include/config/env/is/embedded.h) \
    $(wildcard include/config/env/is/in/mmc.h) \
    $(wildcard include/config/env/is/in/nand.h) \
    $(wildcard include/config/env/offset/oob.h) \
    $(wildcard include/config/env/is/in/ubi.h) \
    $(wildcard include/config/env/ubi/part.h) \
    $(wildcard include/config/env/ubi/volume.h) \
    $(wildcard include/config/env/ubi/volume/redund.h) \
    $(wildcard include/config/cmd/ubi.h) \
    $(wildcard include/config/env/is/in/onenand.h) \
    $(wildcard include/config/cmd/saveenv.h) \
    $(wildcard include/config/env/aes.h) \
    $(wildcard include/config/needs/manual/reloc.h) \
    $(wildcard include/config/sys/mmc/env/part.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/env_attr.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/env_callback.h \
    $(wildcard include/config/env/callback/list/static.h) \
    $(wildcard include/config/silent/console.h) \
    $(wildcard include/config/splashimage/guard.h) \
    $(wildcard include/config/regex.h) \
    $(wildcard include/config/cmd/dns.h) \
    $(wildcard include/config/net.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/env_flags.h \
    $(wildcard include/config/cmd/net.h) \
    $(wildcard include/config/env/flags/list/static.h) \
    $(wildcard include/config/overwrite/ethaddr/once.h) \
    $(wildcard include/config/cmd/env/flags.h) \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/linker_lists.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/linux/compiler.h \
    $(wildcard include/config/sparse/rcu/pointer.h) \
    $(wildcard include/config/trace/branch/profiling.h) \
    $(wildcard include/config/profile/all/branches.h) \
    $(wildcard include/config/kasan.h) \
    $(wildcard include/config/enable/must/check.h) \
    $(wildcard include/config/enable/warn/deprecated.h) \
    $(wildcard include/config/kprobes.h) \
  /usr/include/search.h \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/include/linux/stringify.h \

tools/common/env_embedded.o: $(deps_tools/common/env_embedded.o)

$(deps_tools/common/env_embedded.o):
