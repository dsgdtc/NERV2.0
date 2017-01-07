# -*- coding:utf-8 -*-
import textwrap,termina_size
from readconfig import LogFormat

HeadLine='''\033[32;1m
+=============================================================================================================================+
|                                                                                                                             |
|                                                        NERV 2.0                                                             |
|                                                   Small and Portable                                                        |
|                                                                                                                             |
+=============================================================================================================================+
|                                                                                                                             |
|                                                                                                                             |	
|       Thank you for using NERV 2.0, you will be able to manage large quantities of servers through this small and portable  |
|       software.                                                                                                             |
|                                                                                                                             |\033[31;1m
|       Please be careful with your opreations because right now the key of managing the whole network is in your hand.	      |	
|       You must be very clear about any instruction you input before sending them.                                           |
|       注意,你可以拥有所有的root权限！                                                                                       |\033[32;1m
|                                                                                                                             |
|                                                                                                                             |
|                                                                               Report bug:  fangcun727@aliyun.com            |
|                                                                                                                             |
|_____________________________________________________________________________________________________________________________|
\033[0m'''

HeadLine100='''\033[32;1m
+==============================================================================================+
|                                                                                              |
|                                          NERV 2.0                                            |
|                                     Small and Portable                                       |
|                                                                                              |
+==============================================================================================+
|                                                                                              |
|                                                                                              |
|   Thank you for using NERV 2.0, you will be able to manage large quantities of servers       |
|   through this software.                                                                     |
|                                                                                              |\033[31;1m
|   Please be careful with your opreations because right now the key of managing the           | 
|   whole network is in your hand. You must be very clear about any instruction you input      |
|   before sending them.                                                                       |
|                                                                                              |
|   注意,你可以拥有所有的root权限！                                                            |\033[32;1m
|                                                                                              |
|                                                 Report bug: fangcun727@aliyun.com            |
|                                                                                              |
|______________________________________________________________________________________________|
\033[0m'''

HeadLine65='''\033[32;1m
+===============================================================+
|                                                               |
|                          NERV 2.0                             |
|                     Small and Portable                        |
|                                                               |
+===============================================================+
|                                                               |
|   Thank you for using NERV 2.0, you will be able to manage    |
|   large quantities of servers through this software.          |
|                                                               |\033[31;1m
|   Please be careful with your opreations because right now    |
|   the key of managing the whole network is in your hand.      |
|   You must be very clear about any instruction you input      |
|   before sending them.                                        |
|   注意,你可以拥有所有的root权限！                             |\033[32;1m
|                                                               |
|                       Report bug: fangcun727@aliyun.com       |
|                                                               |
|_______________________________________________________________|
\033[0m'''
def head_line():
	T_size = termina_size.terminal_size()
	if T_size[0] >= 127:
		print HeadLine
	elif T_size[0] >= 100:
		print HeadLine100 
	else: 
		print HeadLine65
		#print T_size

head_line()
