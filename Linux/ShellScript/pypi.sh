#!/bin/bash
# coding: utf-8
# 脚本用途：配置国内pypi源

huawei='https://repo.huaweicloud.com/repository/pypi/simple'
aliyun='http://mirrors.aliyun.com/pypi/simple/'
qinghua='https://pypi.tuna.tsinghua.edu.cn/simple/'
kejidaxue='https://pypi.mirrors.ustc.edu.cn/simple/'

read -n 1 -t 3 -p '请输入数字选择要设置的pypi源:' number
for loop in 1 2 3 4
do
    #[$number]判断变量是否为空
    #[ $(($number+1)) -eq 1 ]判断变量是否是字符
    #[ $number -gt 4 -o $number -eq 0 ] 判断变量是否符合条件    
    if [ $loop -eq 4 ]
    then 
        number=1
        echo "连续输入错误3次,将默认设置为华为pypi源"
    elif [ ! $number ] || [ $(($number+1)) -eq 1 ] || [ $number -gt 4 -o $number -eq 0 ]
    then
        read -n 1 -t 3 -p '输入错误,请重新输入数字选择要设置的pypi源:' number
    fi  
done
case $number in
    1) mirrors=$huawei
    ;;
    2) mirrors=$aliyun
    ;;
    3) mirrors=$qinghua
    ;;
    4) mirrors=$kejidaxue
    ;;
esac

#判断.pip目录是否存在
if [ ! -e $HOME/.pip ];then mkdir $HOME/.pip;fi
#过滤网址
addr=`echo $mirrors | awk -F '/' '{print $3}'`
#输入内容到文件
echo -e "[global]\nindex-url = ${mirrors} \n[install]\nuse-mirrors = true\nmirrors = ${mirrors} \ntrusted-host = ${addr} " > $HOME/.pip/pip.conf
read -n 1 -p '设置成功,按任意键继续...'