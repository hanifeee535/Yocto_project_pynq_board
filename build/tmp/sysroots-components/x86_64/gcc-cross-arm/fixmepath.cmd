sed -e 's:^:FIXMEFINALSSTATEINST:g' /home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/sysroots-components/x86_64/gcc-cross-arm/fixmepath | xargs sed -i -e 's:FIXMESTAGINGDIRTARGET:FIXMEFINALSSTATETARGET:g; s:FIXMESTAGINGDIRHOST:FIXMEFINALSSTATEHOST:g' -e 's:FIXME_HOSTTOOLS_DIR:/home/student/Desktop/yocto_pynq/Yocto_project_pynq_board/build/tmp/hosttools:g'