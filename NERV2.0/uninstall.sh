#!/bin/bash
echo "Wait a few seconds..."
sleep 2
rpm -e expect
rpm -e tcl
rpm -e python-configobj 
echo "rm the main work directory and finish the uninstall"
printf "If you have some good suggestions or good ideas, please send to \033[1;31mfangcun727@aliyun.com\033[0m Thank you\n"
