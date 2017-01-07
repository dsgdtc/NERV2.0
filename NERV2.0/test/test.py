# -*- coding:utf-8 -*-
import commands
WORKDIR='/root/script/NERV2.0'
user='root'
ip='123123'
passwd='123456'
cmd='lsblk'

status, result = commands.getstatusoutput("%s/include/expect/base_publickey %s %s %s \"%s\"" % (WORKDIR,user,ip,passwd,cmd))
#print result
error_str = "%s@%s\'s password:" % (user,ip)
error = error_str.encode("utf-8")
print type(result),type(error),type(error_str)
if "%r@%r\'s password:" % (user,ip) in result:
    print "-"*100
    print u"\033[33;40;1m服务器 %s 上用户 %s 公钥错误,请检查!\033[0m" % (ip,user)
else:
    print "-" * 100
    print result
