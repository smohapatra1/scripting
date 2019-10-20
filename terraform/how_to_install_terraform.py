# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import subprocess
import paramiko
import cmd
import time

#Install terraform through command line

#How to run multiple shell commands in python
'''
def subprocess_cmd(command):
    process=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    proc_stdout=process.communicate()[0].strip()
    print (proc_stdout)
subprocess_cmd('ls -lart ; who ; pwd ')
'''

mycmd=os.popen('ls -lart').read()
print (mycmd)
for i in mycmd :
    print (mycmd.strip())


#paramiko method
'''
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', username='cisco', password='cisco')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
chan = ssh.invoke_shell()

chan.send('ls -lart')
chan.send('\n')
time.sleep(1)
resp = chan.recv(9999)
output = resp.decode('ascii').split(',')
'''

#os.system(sudo apt-get update)
#os.system(sudo apt-get install wget unzip)
#mkdir -p $HOME/terraform
#curl -O https://releases.hashicorp.com/terraform/0.12.2/terraform_0.12.2_linux_amd64.zip
#cp terraform_0.12.2_linux_amd64.zip $HOME/terraform
#sudo unzip $HOME/terraform/terraform_0.12.2_linux_amd64.zip –d /usr/local/bin

