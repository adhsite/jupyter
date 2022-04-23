{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f3599334-ec39-4e02-8fe4-8c76ee7fe08e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/python3\n",
    "# -*- coding: utf-8 -*-\n",
    "# 脚本用途：配置国内的pypi源\n",
    "\n",
    "import os\n",
    "\n",
    "aliyun='http://mirrors.aliyun.com/pypi/simple/'\n",
    "qinghua='https://pypi.tuna.tsinghua.edu.cn/simple/'\n",
    "kejidaxue='https://pypi.mirrors.ustc.edu.cn/simple/'\n",
    "huawei='https://repo.huaweicloud.com/repository/pypi/simple'\n",
    "print('请选择pypi源\\n1.华为pypi源\\n2.清华大学pypi源\\n3.中国科技大学pypi源\\n4.阿里云pypi源\\n')\n",
    "number=input(\"请输入数字选择要设置的pypi源:\")\n",
    "for i in range(4): \n",
    "    #判断输入是否是限定的数字   \n",
    "    if number.isdigit() and 0<int(number[:1])<5:\n",
    "        if number == '1':\n",
    "            mirrors=aliyun\n",
    "        elif number == '2':\n",
    "            mirrors=qinghua\n",
    "        elif number == '3':\n",
    "            mirrors=kejidaxue\n",
    "        elif number == '4':\n",
    "            mirrors=huawei\n",
    "    else:\n",
    "        number=input(\"请重新输入数字:\")        \n",
    "\n",
    "#判断是否存在.pip目录，没有就创建\n",
    "if not os.path.isdir(os.path.expanduser('~') + '/.pip'):\n",
    "    os.mkdir(os.path.expanduser('~') + '/.pip')\n",
    "#创建pip.conf文件,并输入内容,在字符串中插入变量;以/分割字符串,获取需要的字符串\n",
    "with open(os.path.expanduser('~') + '/.pip/pip.conf','w+') as f:\n",
    "    f.write('''\n",
    "[global]\n",
    "index-url = %s\n",
    "[install]\n",
    "use-mirrors = true\n",
    "mirrors = %s\n",
    "trusted-host = %s''' % (mirrors,mirrors,mirrors.split('/')[2]))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
