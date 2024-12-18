cmd_sysklogd/lib.a := rm -f sysklogd/lib.a; arm-poky-linux-gnueabi-ar  rcs sysklogd/lib.a sysklogd/klogd.o sysklogd/logread.o sysklogd/syslogd_and_logger.o
