from paramiko import client
from getpass import getpass
import time
hostname="10.132.36.133"
username= input("Enter username: ")
if username =="":
 username="tcl"
print("Using default username",username)
password=getpass(f"Enter password for the user {username}: ") or "tcts"
client_ssh=client.SSHClient()
client_ssh.set_missing_host_key_policy(client.AutoAddPolicy())
client_ssh.connect(hostname=hostname,username=username,password=password,port=22,look_for_keys=False)
print("Successfully connected to the device")
access_device=client_ssh.invoke_shell()
access_device.send("terminal len 0\n")
access_device.send("sh ip int brief\n")
time.sleep(3)
output=access_device.recv(65535)
print(output.decode())
client_ssh.close()