cmd_arch/arm/dts/zynq-zed.dtb := mkdir -p arch/arm/dts/ ; arm-poky-linux-gnueabi-gcc  --sysroot=/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/recipe-sysroot -E -Wp,-MD,arch/arm/dts/.zynq-zed.dtb.d.pre.tmp -nostdinc -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/dts -I/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/dts/include -undef -D__DTS__ -x assembler-with-cpp -o arch/arm/dts/.zynq-zed.dtb.dts.tmp /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/dts/zynq-zed.dts ; dtc -O dtb -o arch/arm/dts/zynq-zed.dtb -b 0 -i /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/dts/  -d arch/arm/dts/.zynq-zed.dtb.d.dtc.tmp arch/arm/dts/.zynq-zed.dtb.dts.tmp ; cat arch/arm/dts/.zynq-zed.dtb.d.pre.tmp arch/arm/dts/.zynq-zed.dtb.d.dtc.tmp > arch/arm/dts/.zynq-zed.dtb.d

source_arch/arm/dts/zynq-zed.dtb := /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/dts/zynq-zed.dts

deps_arch/arm/dts/zynq-zed.dtb := \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/dts/zynq-7000.dtsi \
  /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/work/pynq-poky-linux-gnueabi/u-boot-digilent/1_2016.07-r0/git/arch/arm/dts/skeleton.dtsi \

arch/arm/dts/zynq-zed.dtb: $(deps_arch/arm/dts/zynq-zed.dtb)

$(deps_arch/arm/dts/zynq-zed.dtb):