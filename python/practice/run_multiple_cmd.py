#!/usr/bin/python
import subprocess
import sys
import os
    
#Using OS and system modules

p=os.popen('pwd').read()
print (p)


#Using subprocess
def subprocess_cmd(command):
    p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    p.stdout=p.communicate()[0].strip()
    print (p.stdout)

subprocess_cmd('ls -lart ; pwd')





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

