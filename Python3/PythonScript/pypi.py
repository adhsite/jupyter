#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 脚本用途：配置国内的pypi源

import os

aliyun='http://mirrors.aliyun.com/pypi/simple/'
qinghua='https://pypi.tuna.tsinghua.edu.cn/simple/'
kejidaxue='https://pypi.mirrors.ustc.edu.cn/simple/'
huawei='https://repo.huaweicloud.com/repository/pypi/simple'
print('请选择pypi源\n1.华为pypi源\n2.清华大学pypi源\n3.中国科技大学pypi源\n4.阿里云pypi源\n')
number=input("请输入数字选择要设置的pypi源:")
for i in range(4): 
    #判断输入是否是限定的数字   
    if number.isdigit() and 0<int(number[:1])<5:
        if number == '1':
            mirrors=aliyun
        elif number == '2':
            mirrors=qinghua
        elif number == '3':
            mirrors=kejidaxue
        elif number == '4':
            mirrors=huawei
    else:
        number=input("请重新输入数字:")        

#判断是否存在.pip目录，没有就创建
if not os.path.isdir(os.path.expanduser('~') + '/.pip'):
    os.mkdir(os.path.expanduser('~') + '/.pip')
#创建pip.conf文件,并输入内容,在字符串中插入变量;以/分割字符串,获取需要的字符串
with open(os.path.expanduser('~') + '/.pip/pip.conf','w+') as f:
    f.write('''
[global]
index-url = %s
[install]
use-mirrors = true
mirrors = %s
trusted-host = %s''' % (mirrors,mirrors,mirrors.split('/')[2]))
input('设置完成,按任意键退出...')