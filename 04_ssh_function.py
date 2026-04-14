from paramiko import client
from getpass import getpass
import time
username=input("Enter username: ")
if username == "":
  username="tcl"
  print("Using default username",username)
password=getpass(f"Enter password for the user {username}: ")
if not password:
  password="tcts"
r1_cmd=['enable','cisco','conf t','int gig1/0','ip address 192.168.10.10 255.255.255.0',
        'no shut','exit','exit','wr','sh ip int brief']
r2_cmd=['enable','cisco','conf t','int gig1/0','ip address 192.168.10.20 255.255.255.0',
        'no shut','exit','exit','wr','sh ip int brief']
def cmd_executor(hostname,commands):
    ssh_client=client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
    ssh_client.connect(hostname=hostname,username=username,password=password,port=22,look_for_keys=False)
    print("Successfully connected to the device")
    access_device=ssh_client.invoke_shell()
    access_device.send("terminal len 0\n")
    for cmd in commands:
        access_device.send(cmd+"\n")
        time.sleep(1)
        output=access_device.recv(65535)
        print(output.decode(),end="")
    access_device.send('sh int gig1/0\n')
    time.sleep(2)
    output=access_device.recv(65535)
    print(output.decode())
    ssh_client.close()
cmd_executor("10.132.36.214",r1_cmd)
cmd_executor("10.132.36.133",r2_cmd)