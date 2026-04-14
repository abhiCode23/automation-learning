 
from paramiko import client
from getpass import getpass
import time
hostname = "10.132.36.214"
username = input("Enter username: ")
key_uni= "\U0001F511"
if not username:
    username = "tcl"
    print(f"Using default username {username}")
password = getpass(f"{key_uni} Enter password of the user {username}:") or "tcts" 

commands=['enable','cisco','conf t','int gig1/0','ip address 10.132.37.222 255.255.255.0','no shut','exit','do sh ip int brief','exit','wr']
ssh_client = client.SSHClient()
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
ssh_client.connect(hostname=hostname, username=username, password=password,port=22,look_for_keys=False)
print("Successfully connected to the device")
device_access= ssh_client.invoke_shell()
device_access.send("terminal len 0\n")
for cmd in commands:
    device_access.send(cmd+'\n')
    time.sleep(1)
    output=device_access.recv(65535)
    print(output.decode(),end="")

device_access.send('sh int gig1/0\n')
time.sleep(4)
output=device_access.recv(65535)
print(output.decode())
ssh_client.close()



 