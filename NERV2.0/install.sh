#!/bin/bash
echo "Wait a few seconds..."
sleep 1
#log=0
#if [ $log = 0 ]; then
#	exec >> /dev/null #2>&1
#fi

#rpm -q expect tcl python-configobj 
rpm -q expect tcl python-configobj &>/dev/null 
if [ $? -eq 0 ] ;then
	echo "Now you can run \"python nerv.py\" to manage your servers!"
	printf "if it doesn't work, send your question to \033[1;31mfangcun727@aliyun.com\033[0m\n"
else
	rpm -ivh "$PWD"/dependency/tcl-8.5.7-6.el6.x86_64.rpm 
	rpm -ivh "$PWD"/dependency/expect-5.44.1.15-5.el6_4.x86_64.rpm 
	rpm -ivh "$PWD"/dependency/python-configobj-4.7.2-1.el6.noarch.rpm 
	echo "Now you can run \"python nerv.py\" to manage your servers!"
	printf "if it doesn't work, send your question to \033[1;31mfangcun727@aliyun.com\033[0m\n"
fi
