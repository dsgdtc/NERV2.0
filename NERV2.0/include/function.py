# -*- coding:utf-8 -*-
import os
import sys
import re
import multiprocessing
import time
import commands
import command_tool
import readconfig
from readconfig import ReadConf
from readconfig import LogFormat
WORKDIR = readconfig.WORKDIR
def choose():
	choose = raw_input("\033[0;32minput your choice:\033[0m").strip()
	return choose

class Common(ReadConf):
	
	def __init__(self):
		self._process_num = ReadConf().process_num
		self._default_user = ReadConf().default_user
		self._all_group = ReadConf().all_group_name
		self._global_cmdsh_dir = ReadConf().global_cmdsh_dir
		#LogFormat().logging.info("test:" %self._global_cmdsh_dir)	
#		self._workdir = ReadConf().WORKDIR

	def show_group_name(self):
		print "\033[1;34m"
		for gid in self._all_group:
			print "\t%s: %s" % (gid , ReadConf().read_group_name(gid))
		print "\t0: 返回\033[0m"

	def show_group(self,group_num):
		#print "\033[1;36m共%s个组在控制中\033[0m" % (len(self._all_group))
		group_content = ReadConf().read_group_content(group_num)
		group_name = ReadConf().read_group_name(group_num)
		for ip in group_content:
			print ip
		print "\033[1;36m%s" % (group_name),"里有%s台服务器\033[0m" % (len(group_content))

#	def re_ip(self,text):
#		p = re.compile(r'(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])')
#		if p.findall(text):
#			return p.findall(text)[0]
#		else:
#			return 0

#	def re_user(self,text):
#		p = re.compile(r'\(.*?\)')
#		if p.findall(text):
#			return p.findall(text)[0].replace("(","").replace(")","")
#		else:
#			return self._default_user

	def multiprocessing_handler(self,func,gid,add1,add2,cmd):
		pool = multiprocessing.Pool(processes = int(self._process_num))
		group_name = ReadConf().read_group_name(gid)
		group_content = ReadConf().read_group_content(gid)
		for server in group_content:
			server_ip = ReadConf().re_ip(server)
			server_user = ReadConf().re_user(server)
			for cell in ReadConf().read_server_list():
				if cell[1] == server_ip and cell[2] == server_user:
					server_id = cell[0]
					#server_ip == cell[1]
					#server_user == cell[2]
					server_passwd = cell[3]
					server_method = cell[4]
					if func == 'send_file':
#						print func,gid,add1,add2,cmd,server_ip,server_user,server_passwd,server_method
						pool.apply_async(command_tool.traffic_file, (add1,add2,server_user,server_ip,server_passwd,server_method, ))
					if func == 'send_cmdfile':
#						print func,gid,add1,add2,cmd,server_ip,server_user,server_passwd,server_method
						pool.apply_async(command_tool.traffic_file, (add1,add2,server_user,server_ip,server_passwd,server_method, ))
					if func == 'execute':
#						print func,gid,add1,add2,cmd,server_ip,server_user,server_passwd,server_method
						pool.apply_async(command_tool.execute_command, (server_user,server_ip,server_passwd,cmd,server_method, ))
#						pool.apply_async(command_tool.test, (cmd, ))
					if func == 'execute_cmd':
#						print func,gid,add1,add2,cmd,server_ip,server_user,server_passwd,server_method
						pool.apply_async(command_tool.execute_command, (server_user,server_ip,server_passwd,cmd,server_method, ))
		pool.close()
		pool.join()

class ShowServer(Common):

	def show_all_server(self):
		all_server = ReadConf().read_server_list()
		print "ip          ","user"
		for ip in all_server:
		# eg all_server:['1', '172.30.25.37', 'root', 'Y3QKfoUTQ34YYT@@', 'publickey']
			print ip[1],ip[2]
		print u"\033[1;36m共%s台服务器在控制中\033[0m" % (len(all_server))
		raw_input()

	def show_all_group(self):
		Common().show_group_name()
		g_num = raw_input("\033[0;32minput your choice:\033[0m").strip()
		if g_num == '0':
			return
		else:
			Common().show_group(g_num)
		raw_input()

class SendFiles(ShowServer):

	def send_file(self):
		func_type = 'send_file'
		cmd = '2'
		Common().show_group_name()
		g_num = raw_input("\033[0;32minput your choice:\033[0m").strip()
		if g_num == '0':
			return
		else:
			Common().show_group(g_num)

		add1=raw_input("\033[0;32m本地文件(绝对路径):\033[0m").strip()
		if not add1:
			print "\n\033[33;40;1m输入的是空文件,请重新选择.\033[0m "
			return
		if add1 == 'quit' or add1 == 'exit':return
		add2=raw_input("\033[0;32m远端服务器目的地址(绝对路径):\033[0m").strip()
		if not add2:
			print "\n\033[33;40;1m输入的是空文件,请重新选择.\033[0m "
			return
		if add2 == 'quit' or add2 == 'exit':return

		Common().multiprocessing_handler(func_type,g_num,add1,add2,cmd)

	def send_cmdfile(self):	
		func_type = 'send_cmdfile'
		cmd = '2'
		Common().show_group_name()
		g_num = raw_input("\033[0;32minput your choice:\033[0m").strip()
		if g_num == '0':
			return
		else:
			Common().show_group(g_num)
		#print type(self._global_cmdsh_dir.encode("utf-8"))
		sure = raw_input("\033[0;32m确定分发cmd.sh到各服务器%s目录下[ Y/N Y为缺省值 ]:\033[0m" % self._global_cmdsh_dir.encode("utf-8")).strip()
		if len(sure) == 0:sure = 'Y'
		if sure == 'Y' or sure == 'y':
			add1 = "%s/cmd.sh" % (WORKDIR)
			add2 = self._global_cmdsh_dir

			Common().multiprocessing_handler(func_type,g_num,add1,add2,cmd)
		else:return
			
class ExecuteCommand(ShowServer):

	def execute(self):
		func_type = 'execute'
		(add1,add2) = ('2','2')
		Common().show_group_name()
		g_num = raw_input("\033[0;32minput your choice:\033[0m").strip()
		if g_num == '0':
			return
		else:
			Common().show_group(g_num)
		cmd=raw_input("\033[0;32m输入要执行的命令(不能带引号):\033[0m").strip()
		if not cmd:
			print "\n\033[33;40;1m输入的是空指令,请重新选择.\033[0m "
			return

		Common().multiprocessing_handler(func_type,g_num,add1,add2,cmd)

	def execute_cmd(self):
		func_type = 'execute_cmd'
		(add1,add2) = ('2','2')
		Common().show_group_name()
		g_num = raw_input("\033[0;32minput your choice:\033[0m").strip()
		if g_num == '0':
			return
		else:
			Common().show_group(g_num)
		cmd = os.path.join(self._global_cmdsh_dir,"cmd.sh")
		cmd = cmd.encode("utf-8")
		#sure = raw_input("\033[0;32m确定到服务器上执行%s脚本(root用户,用于执行cmd.sh脚本)[ Y/N Y为缺省值 ]:\033[0m" % cmd).strip()
		sure = raw_input("\033[0;32m确定到服务器上执行%s脚本[ Y/N Y为缺省值 ]:\033[0m" % cmd).strip()

		if len(sure) == 0:sure = 'Y'
		if sure == 'Y' or sure == 'y':
			Common().multiprocessing_handler(func_type,g_num,add1,add2,cmd)
		else:return

if __name__ == '__main__':
#	Print_Group().Print_Group()
	#ShowServer().show_all_group()
	ShowServer().show_all_server()
