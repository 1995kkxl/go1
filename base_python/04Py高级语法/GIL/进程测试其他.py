#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################
# author: SkyJ
# date  : 2019/7/17
################################################

import os
import sys
import string
import datetime
import time
import paramiko  # 导入paramiko

hostname = "172.16.2.225"
username = "root"
password = "123456"
cmdList = ['ls -l\n', 'df -h\n']


# 第一种ssh连接执行指令方式
def sshRunCmd(hostname, username, password, cmdList):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 创建ssh连接
        client.connect(hostname=hostname, port=22, username=username, password=password)
        # 开启ssh管道
        ssh = client.get_transport().open_session()
        ssh.get_pty()
        ssh.invoke_shell()
        # 执行指令
        for cmd in cmdList:
            ssh.sendall(cmd)
            time.sleep(0.5)
            result = ssh.recv(102400)
            result = result.decode(encoding='UTF-8', errors='strict')
            print(result)
    except Exception as e:
        print("[%s] %s target failed, the reason is %s" % (datetime.datetime.now(), hostname, str(e)))
    else:
        print("[%s] %s target success" % (datetime.datetime.now(), hostname))
    finally:
        ssh.close()
        client.close()


# 第二种ssh连接执行指令方式
def sshRunCmd2(hostname, username, password, cmdList):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 创建ssh连接
        client.connect(hostname=hostname, port=22, username=username, password=password)
        # 执行指令
        for cmd in cmdList:
            stdin, stdout, stderr = client.exec_command(cmd)
            result = stdout.read()
            result = result.decode(encoding='UTF-8', errors='strict')
            print(result)
    except Exception as e:
        print("[%s] %s target failed, the reason is %s" % (datetime.datetime.now(), hostname, str(e)))
    else:
        print("[%s] %s target success" % (datetime.datetime.now(), hostname))
    finally:
        client.close()


if __name__ == '__main__':
    sshRunCmd(hostname, username, password, cmdList)
    sshRunCmd2(hostname, username, password, cmdList)
