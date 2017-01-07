# -*- coding:utf-8 -*-
import os
import sys
import re
from configobj import ConfigObj, ConfigObjError, flatten_errors, get_extra_values
WORKDIR = os.path.dirname(os.path.dirname(__file__))
#FOR direct execution,use: WORKDIR = '/root/script/NERV2.0'
#print WORKDIR
global CHEKC_FLAG
CHECK_FLAG = 0

class LogFormat():
	import logging
	logging.basicConfig(
				level=logging.DEBUG,
				format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#				datefmt='%a, %d %b %Y %H:%M:%S',
				filename=WORKDIR + "/log/nerv.log",
				filemode='a')

class ReadConf(LogFormat):

	config_path = WORKDIR + "/conf/nerv.conf"
	config = ConfigObj(config_path ,encoding='UTF8')
	config_group_path = WORKDIR + "/conf/group.conf"
	try:
		config_group = ConfigObj(config_group_path,encoding='UTF8')
	except:
		print "\033[1;35m组ID不唯一,请修改./conf/group.conf\033[0m"
		os._exit(0)

	def __init__(self):
		self.all_group_id = self.config_group.keys() # This is not group name ,it is group id
		self.process_num = self.config["global"]["process_num"]
		self.default_user = self.config["global"]["default_user"]
		self.global_cmdsh_dir = self.config["global"]["global_cmdsh_dir"]

	def read_server_list(self):
		server_list=[]
		with open ("%s/conf/server.conf" % WORKDIR) as f:
			for line in f.readlines():
				p = re.compile(r'^#')
				if not p.match(line):
					server_list.append(line.split())
		return server_list

	def read_server_dict(self):
		server_dict={}
		with open ("%s/conf/server.conf" % WORKDIR) as f:
			for line in f:
				p = re.compile(r'^#')
				if not p.match(line):
#					server_dict[line.split()[0]] = {line.split()[1]:line.split()[2:]} 
					server_dict[line.split()[0]] = line.split()[1:] 
		return server_dict

	def read_group_name(self,gid):
		return self.config_group[gid]['group_name']

	def read_group_content(self,gid):
		return self.config_group[gid]['group_content']

	def re_ip(self,text):
		p = re.compile(r'(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])')
		if p.findall(text):
			return p.findall(text)[0]
		else:
			return 0

	def re_user(self,text):
		p = re.compile(r'\(.*?\)')
		if p.findall(text):
			return p.findall(text)[0].replace("(","").replace(")","")
		else:
			return self.default_user

readconf = ReadConf()
def check_server_ip():
	result = []
	def check_ip(text):
		ip_last_segment = text.split('.')[3]
		p = re.compile(r'(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])')
		p2 = re.compile(r'^[0-9]+$')
		if p.match(text) and p2.match(ip_last_segment) and int(ip_last_segment) < 256:
			pass
		else:
			global CHECK_FLAG
			CHECK_FLAG = '1'
			print u"\033[1;35m%s  不是合法的IP! 请修改./conf/server.conf文件\033[0m" % text
	for server in readconf.read_server_list():
		ip = server[1]
		check_ip(ip)

def check_ssh_method():
	for server in readconf.read_server_list():
		method = server[4]
		if method not in [ "password", "publickey" ]:
			global CHECK_FLAG
			CHECK_FLAG = '1'
			print "\033[1;35m%s  不支持这种SSH认证方式,请修改./conf/server.conf文件\033[0m" % method

def check_group_id():
	for item in readconf.all_group_id:
		if item.isdigit():pass
		else:
			global CHECK_FLAG
			CHECK_FLAG = '1'
			print "\033[1;35m组ID必须是数字,请修改./conf/group.conf文件\033[0m"

def check_server_lookup():
	server_and_user = []
	for item in readconf.read_server_list():
		server_and_user.append([item[1],item[2]])
	
#	print readconf.all_group_id
	for item in readconf.all_group_id:
		gid = item
		group_content = readconf.read_group_content(str(gid))
		for server in group_content:
			server_ip = ReadConf().re_ip(server)
			server_user = ReadConf().re_user(server)
			cell = [server_ip,server_user]
			if cell in server_and_user:pass
			else:
				global CHECK_FLAG
				CHECK_FLAG = '1'
				print "\033[1;35m%s  不在./conf/server.conf中,请添加\033[0m" % cell

def check_server_uniq():
	server_and_user = []
	server_and_user_uniq = []
	for item in readconf.read_server_list():
		combine = item[1]+" "+item[2]
		server_and_user.append(combine)
#	for x in server_and_user if x not in server_and_user:
	server_and_user_uniq = set(server_and_user)
	for cell in server_and_user_uniq:
		if server_and_user.count(cell) > 1:
			global CHECK_FLAG
			CHECK_FLAG = '1'
			print "\033[1;35m%s  存在 %d 个,请修改./conf/server.conf\033[0m" % (cell,server_and_user.count(cell))
# check functions
check_server_ip()
check_ssh_method()
check_group_id()
check_server_lookup()
check_server_uniq()
if CHECK_FLAG == '1':
	os._exit(0)

if __name__ == '__main__':
	pass
	LogFormat().logging.info('hahaha')
#	print "ReadConf().all_group_id:\n" ,ReadConf().all_group_id
#	print "ReadConf().process_num:\n" ,ReadConf().process_num
#	print "ReadConf().default_user:\n" ,ReadConf().default_user
	print "ReadConf().read_server_list():\n" ,ReadConf().read_server_list()
#	print "ReadConf().read_server_dict():\n" ,ReadConf().read_server_dict()
#	print "ReadConf().read_group_name('1'):\n" ,ReadConf().read_group_name('1')
#	print "ReadConf().read_group_content('1'):\n" ,ReadConf().read_group_content('1')
