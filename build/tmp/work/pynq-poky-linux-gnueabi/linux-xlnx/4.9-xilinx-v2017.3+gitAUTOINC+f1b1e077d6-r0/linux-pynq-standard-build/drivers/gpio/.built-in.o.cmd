cmd_drivers/gpio/built-in.o :=  arm-poky-linux-gnueabi-ld.bfd      -r -o drivers/gpio/built-in.o drivers/gpio/devres.o drivers/gpio/gpiolib.o drivers/gpio/gpiolib-legacy.o drivers/gpio/gpiolib-of.o drivers/gpio/gpiolib-sysfs.o drivers/gpio/gpio-generic.o drivers/gpio/gpio-xilinx.o drivers/gpio/gpio-zynq.o 