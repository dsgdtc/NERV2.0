# -*- coding:utf-8 -*-
import os,sys
from include import tab
from include import showmenu
from include import readconfig
from include import function 
from include import headline
from termcolor import colored


showmenus=showmenu.ShowMenu(0)
headline
while True:
	showmenus.main_menu()
	try:
		choice = function.choose()
		choice_list = ['1','2','3','0','exit','quit']
		if choice not in choice_list:
			#print "\033[33;40;1m没有这个选项,返回主菜单!\033[0m" 
			info = "没有这个选项,返回主菜单!"
			print colored(info,color='yellow',on_color=None,attrs=['bold'])
			continue
		if choice == '1':
			pass
			showmenus.flag = 1
			showmenus.send_files()
		if choice == '2':
			pass
			showmenus.flag = 1
			showmenus.execute_cmd()
		if choice == '3':
#			pass
			showmenus.flag  = 1
			showmenus.show_server()
		if choice == '0' or choice == 'exit' or choice == 'quit':
			print "\033[33;40;1m谢谢使用^_^\033[0m "
			os._exit(0)
	except KeyError as e:
		#print "\033[33;40;1m选择错误!\033[0m "
		print "\033[33;40;1m没有这个选项,返回主菜单! \033[0m ",e
#		sys.exit()
	except KeyboardInterrupt:
		print "\n\033[33;40;1m退出.\033[0m "
		sys.exit()
	except EOFError:
		print "\n\033[33;40;1m退出.\033[0m "
	except ValueError as e:
		print "\033[33;40;1m选择错误! %s \033[0m ",e
	except AttributeError as e:
		print "\033[33;40;1m没有这个选项,返回主菜单! \033[0m "
	except IOError as e:
		print "\033[33;40;1m请在主目录下运行python nerv.py \033[0m ",e
#	except AttributeError:
#		print '\n\033[31;1mSome error happend,please send bug to dsgdtc@163.com AttributeError\033[0m'
#	else:
#		print "\033[33;40;1m遇到了一些没有想到的BUG,请提交到fangcun@aliyun.com/dsgdtc@163.com. \033[0m "
