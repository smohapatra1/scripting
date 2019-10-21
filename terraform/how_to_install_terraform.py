# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import subprocess
import paramiko
import cmd
import time

#Install terraform through command line
#Create terraforom dir
#Download terraform
#Unzil the terraform file
#copy terraform file to /usr/local/bin folder
#Verify terraform version
def subprocess_cmd(command):
    p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    p.stdout=p.communicate()[0].strip()
    print (p.stdout)

file="terraform_0.12.12_linux_amd64.zip"

subprocess_cmd('ls -lart ;  mkdir -p $HOME/terraform/ ; cd $HOME/terraform/ ; rm -rf terraform_0.* ; curl -O https://releases.hashicorp.com/terraform/0.12.12/%s; sudo rm -rf /usr/local/bin/terraform ; sudo unzip $HOME/terraform/%s  -d /usr/local/bin ; ls -lrt /usr/local/bin/terraform ; terraform -v' % (str(file), str(file)) ) 


#os.system(sudo apt-get update)
#os.system(sudo apt-get install wget unzip)
#mkdir -p $HOME/terraform
#curl -O https://releases.hashicorp.com/terraform/0.12.2/terraform_0.12.2_linux_amd64.zip
#cp terraform_0.12.2_linux_amd64.zip $HOME/terraform
#sudo unzip $HOME/terraform/terraform_0.12.2_linux_amd64.zip –d /usr/local/bin

