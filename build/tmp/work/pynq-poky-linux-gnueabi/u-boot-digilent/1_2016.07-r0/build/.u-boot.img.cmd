cmd_u-boot.img := ./tools/mkimage -A arm -T firmware -C none -O u-boot -a 0x4000000 -e 0x4000000 -n "U-Boot 2016.07 for zynq board" -d u-boot.bin u-boot.img 
