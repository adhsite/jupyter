{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a4e32fc-1244-4b60-998e-8ada6c5b597b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/bin/bash\n",
    "# coding: utf-8\n",
    "# 脚本用途：配置国内pypi源\n",
    "\n",
    "huawei='https://repo.huaweicloud.com/repository/pypi/simple'\n",
    "aliyun='http://mirrors.aliyun.com/pypi/simple/'\n",
    "qinghua='https://pypi.tuna.tsinghua.edu.cn/simple/'\n",
    "kejidaxue='https://pypi.mirrors.ustc.edu.cn/simple/'\n",
    "\n",
    "read -n 1 -t 3 -p '请输入数字选择要设置的pypi源:' number\n",
    "for loop in 1 2 3 4\n",
    "do\n",
    "    #[$number]判断变量是否为空\n",
    "    #[ $(($number+1)) -eq 1 ]判断变量是否是字符\n",
    "    #[ $number -gt 4 -o $number -eq 0 ] 判断变量是否符合条件    \n",
    "    if [ $loop -eq 4 ]\n",
    "    then \n",
    "        number=1\n",
    "        echo \"连续输入错误3次,将默认设置为华为pypi源\"\n",
    "    elif [ ! $number ] || [ $(($number+1)) -eq 1 ] || [ $number -gt 4 -o $number -eq 0 ]\n",
    "    then\n",
    "        read -n 1 -t 3 -p '输入错误,请重新输入数字选择要设置的pypi源:' number\n",
    "    fi  \n",
    "done\n",
    "case $number in\n",
    "    1) mirrors=$huawei\n",
    "    ;;\n",
    "    2) mirrors=$aliyun\n",
    "    ;;\n",
    "    3) mirrors=$qinghua\n",
    "    ;;\n",
    "    4) mirrors=$kejidaxue\n",
    "    ;;\n",
    "esac\n",
    "\n",
    "#判断.pip目录是否存在\n",
    "if [ ! -e $HOME/.pip ];then mkdir $HOME/.pip;fi\n",
    "#过滤网址\n",
    "addr=`echo $mirrors | awk -F '/' '{print $3}'`\n",
    "#输入内容到文件\n",
    "echo -e \"[global]\\nindex-url = ${mirrors} \\n[install]\\nuse-mirrors = true\\nmirrors = ${mirrors} \\ntrusted-host = ${addr} \" > $HOME/.pip/pip.conf\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Bash",
   "language": "bash",
   "name": "bash"
  },
  "language_info": {
   "codemirror_mode": "shell",
   "file_extension": ".sh",
   "mimetype": "text/x-sh",
   "name": "bash"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
