
Simple script to ssh into a list of servers (arguments or file) and run commands. 
i.e
```
./ssh-all -d server1 server2 server3 -r uname -r
#Output:
server1>3.2.0-4-amd64
Failed to connect
server3>3.2.0-4-amd64
```
List of  severs that have failed to connect: ['server2']

usage: ssh-all.py [-h] [--file] [-d DEST [DEST ...]] [-r RUN [RUN ...]]

SSH and run commands remotely from a file or terminal arguments

optional arguments:
  -h, --help            show this help message and exit
  --file                It takes its input from a file called office_server.list within the same path
  -d DEST [DEST ...], --dest DEST [DEST ...] Hosts separate by spaces to ssh in
  -r RUN [RUN ...], --run RUN [RUN ...] Command to be run remotely within ""

