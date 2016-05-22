# -*- coding:utf-8 -*-
import logging
from readconfig import ReadConf
from readconfig import LogFormat
from include import function
#show_server=function.Show_Server()
#send_files=function.Send_Files()
#execute_command=function.Execute_Command()
#add_server=function.Add_Server()

class ShowMenu(ReadConf,LogFormat):
	def __init__(self,flag):
		self.flag = flag
		#pass

	def main_menu(self):
		print """\033[1;34m
主菜单
	1:分发文件
	2:执行命令
	3:查看服务器列表
	0:退出\033[0m
    	"""
	def send_files(self):
		while "self.flag":
			print """\033[1;34m
	1:向服务器传送文件
	2:向服务器传送cmd.sh脚本
	0:返回\033[0m
		"""
			choice = function.choose()
			choice_list = ['1','2','0']
			if choice not in choice_list:
				print "\033[33;40;1m没有这个选项,返回主菜单!\033[0m"
				self.flag = 0
				break
			if choice == '1':
				function.SendFiles().send_file()
			if choice == '2':
				pass
				function.SendFiles().send_cmdfile()
			if choice == '0':
				self.flag = 0
				break	
	def execute_cmd(self):
		while "self.flag":
			print """\033[1;34m
	1:在服务器端执行命令
	2:在服务器端执行cmd.sh脚本(root权限执行)
	0:返回\033[0m
		"""
			choice = function.choose()
			choice_list = ['1','2','0']
			if choice not in choice_list:
				print "\033[33;40;1m没有这个选项,返回主菜单!\033[0m"
				self.flag = 0
				break
			if choice == '1':
				pass
				function.ExecuteCommand().execute()
			if choice == '2':
				pass
				function.ExecuteCommand().execute_cmd()
			if choice == '0':
				self.flag = 0
				break
	def show_server(self):
		while "self.flag":
			print """\033[1;34m
	1:查看所有组
	2:查看所有服务器
	0:返回\033[0m
        """
			choice = function.choose()
			choice_list = ['1','2','0']	
			if choice not in choice_list:
				print "\033[33;40;1m没有这个选项,返回主菜单!\033[0m"
				self.flag = 0
				break
			if choice == '1':
				function.ShowServer().show_all_group()
			if choice == '2':
				function.ShowServer().show_all_server()
			if choice == '0':
				self.flag = 0
				break

if __name__ == '__main__':
	#pass
	ShowMenu('1').main_menu()
