#!/usr/bin/python
import subprocess
import os
import sys
import time

#Configure and install go
#https://golang.org/doc/install#install

def subprocess_cmd(command):
    p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    p.stdout=p.communicate()[0].strip()
    print (p.stdout)
file="go1.13.1.linux-amd64.tar.gz"    
subprocess_cmd('pwd; ls -lart ; sudo apt-get -y update ; mkdir -p $HOME/go/; cd $HOME/go ; curl -O https://storage.googleapis.com/golang/%s ; sudo tar -C /usr/local/ -xvf $HOME/go/%s ; "export GOPATH=$HOME/go" ; "export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin" ;  echo \'PATH=$PATH:/usr/local/go/\' >> $HOME/.profile ; source $HOME/.profile ; cp ./hello.go $HOME/go ; cd $HOME/go/; ./hello.go  ; go version' % (str(file), str(file)))

#sudo snap install go         # version 1.13.3, or
#sudo apt  install golang-go
#sudo apt  install gccgo-go
