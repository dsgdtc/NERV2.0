# -*- coding:utf-8 -*-
import os,sys,commands,time
import readconfig
import base64
import mydecode
from readconfig import LogFormat
WORKDIR = readconfig.WORKDIR 
result_dict = {}
def traffic_file(add1,add2,user,ip,passwd,method):
	if method == 'publickey':
		status, result = commands.getstatusoutput("%s/include/expect/traffic_publickey %s %s@%s:%s \"%s\"" % (WORKDIR,add1,user,ip,add2,passwd))
#		print result
		if "Connection timed out" in result:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print u"\033[33;40;1m服务器 %s 连接超时!\033[0m" % (ip)
			return
		if "No route to host" in result:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print u"\033[33;40;1m服务器 %s 连接失败!\033[0m" % (ip)
			return
		if "Permission denied (publickey)" in result:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print u"\033[33;40;1m服务器 %s 公钥登录失败!\033[0m" % (ip)
			return
		if "%s@%s\'s password:" % (user,ip) in result:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print u"\033[33;40;1m服务器 %s 上用户%s公钥错误,请检查!\033[0m" % (ip,user)
		else:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print result
			return

	if method == 'password':
		try:
			passwd = mydecode.mydecode(passwd)
		except:
			LogFormat().logging.exception('Exception Logged')
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info("%s 不是一个有效的密码,服务器IP为: %s " % (passwd,ip))
			print u"\033[33;40;1m%s 不是一个有效的密码,服务器IP为: %s \033[0m" % (passwd,ip)
			return
		status, result = commands.getstatusoutput("%s/include/expect/traffic_password %s %s@%s:%s %s" % (WORKDIR,add1,user,ip,add2,passwd))
		if "Connection timed out" in result:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print u"\033[33;40;1m服务器 %s 连接超时!\033[0m" % (ip)
			return
		if "No route to host" in result:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print u"\033[33;40;1m服务器 %s 连接失败!\033[0m" % (ip)
			return
		if "Permission denied" in result:
			if "Permission denied (publickey)" in result:
				LogFormat().logging.info("-"*100)
				LogFormat().logging.info(result)
				print "-"*100
				print u"\033[33;40;1m服务器 %s 禁用密码登录,请使用公钥!\033[0m" % (ip)
			else:
				LogFormat().logging.info("-"*100)
				LogFormat().logging.info(result)
				print "-"*100
				print result
#				print u"\033[33;40;1m服务器 %s 密码错误或%s权限不正确,请检查!\033[0m" % (ip,user)
		else:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print result

def execute_command(user,ip,passwd,cmd,method):
	if method == 'publickey':
		#print "going here,cmd is:",cmd
		#print "%s/include/expect/base_publickey %s %s %s \"%s\"" % (WORKDIR,user,ip,passwd,cmd)
#		passwd = 'null'
		status, result = commands.getstatusoutput("%s/include/expect/base_publickey %s %s \"%s\" \"%s\"" % (WORKDIR,user,ip,passwd,cmd))
		#status, result = commands.getstatusoutput("ssh -tt %s@%s \"%s\"" % (user,ip,cmd))
		#print "going here,status is:",status
		#print result 
# bug fix for unicode
		publickey_error_tmp = "%s@%s\'s password:" % (user,ip)
		#print type(publickey_error_tmp)
		publickey_error = publickey_error_tmp.encode("utf-8")
#		print type(result),type(publickey_error),lalala
		if "Connection timed out" in result:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print u"\033[33;40;1m服务器 %s 连接超时!\033[0m" % (ip)
			return
		elif "No route to host" in result:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print u"\033[33;40;1m服务器 %s 连接失败!\033[0m" % (ip)
			return
		elif "Permission denied (publickey)" in result:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print u"\033[33;40;1m服务器 %s 公钥登录失败!\033[0m" % (ip)
			return
# Found ERROR in following code
#		elif "%s@%s\'s password:" % (user,ip) in result:
		elif publickey_error in result:
#		elif "%r@%r\'s password:" % (user,ip) in result:
#			LogFormat().logging.info("-"*100)
#			LogFormat().logging.info(result)
			print "-"*100
			print u"\033[33;40;1m服务器 %r 上用户 %r 公钥错误,请检查!\033[0m" % (ip,user)
			return
		else:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print result
			return

	elif method == 'password':
		try:
			passwd = mydecode.mydecode(passwd)
		except:
			LogFormat().logging.exception('Exception Logged')
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info("%s 不是一个有效的密码,服务器IP为: %s " % (passwd,ip))
			print u"\033[33;40;1m%s 不是一个有效的密码,服务器IP为: %s \033[0m" % (passwd,ip)
			return
		status, result = commands.getstatusoutput("%s/include/expect/base_password %s %s %s \"%s\"" % (WORKDIR,user,ip,passwd,cmd))
		if "Connection timed out" in result:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print u"\033[33;40;1m服务器 %s 连接超时!\033[0m" % (ip)
			return
		if "No route to host" in result:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print u"\033[33;40;1m服务器 %s 连接失败!\033[0m" % (ip)
			return
		if "Permission denied" in result:
			if "Permission denied (publickey)" in result:
				LogFormat().logging.info("-"*100)
				LogFormat().logging.info(result)
				print "-"*100
				print u"\033[33;40;1m服务器 %s 禁用密码登录,请使用公钥!\033[0m" % (ip)
			else:
				LogFormat().logging.info("-"*100)
				LogFormat().logging.info(result)
				print "-"*100
				print result
#				print u"\033[33;40;1m服务器 %s 密码错误或%s权限不正确,请检查!\033[0m" % (ip,user)
		else:
			LogFormat().logging.info("-"*100)
			LogFormat().logging.info(result)
			print "-"*100
			print result
			return
def test(cmd):
	print "I am test function: %s" % cmd

#execute_command('root','123.123.123.55','1234fda56','lsblk','publickey')
#execute_command('prouser','123.123.123.68','1234fda56','pwd','publickey')
