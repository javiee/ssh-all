#!/usr/bin/env python

import paramiko
import os
import sys
import argparse

SSH_KEY_PATH = '/home/jcr/.ssh/jcr'

class Main(object):

    def read_file(self):
# This function ideally would be to extract the servers from a db but for just a few are are in text file.

        f = open('office_server.list')
        lines = f.read().splitlines()
        f.close
        return lines

    def connect_host(self, hostname, command):
        failed_host=[]

        for host in hostname:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, username='root', key_filename = SSH_KEY_PATH)
                stdin, stdout,stderr = ssh.exec_command(command)
                print host + ">" + stdout.read()
                ssh.close
            except (paramiko.PasswordRequiredException,paramiko.SSHException):
                print ("Failed to connect")
                failed_host.append(host)
                pass

        if failed_host:
            print "List of  severs that have failed to connect:",failed_host

    def __init__(self):
        opt = argparse.ArgumentParser(description ="SSH and run commands remotely from a file or terminal arguments")
        opt.add_argument("--file", action='store_true', help = "It takes its input from a file called office_server.list within the same path") 
        opt.add_argument('-d', "--dest", help = "Hosts separate by spaces to ssh in",nargs='+')
        opt.add_argument('-r', "--run", help = "Command to be run remotely within "" ",nargs='+')
        args = opt.parse_args()
        if args.file:
            server_name = self.read_file()
        else:
            server_name=args.dest

        command =  ' '.join(args.run)
        self.connect_host(server_name, command)

if __name__ == "__main__":
        Main()
