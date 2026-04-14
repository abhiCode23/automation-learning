from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "10.132.36.214",
    "username": "tcl",
    "password": "tcts",
}

connection = ConnectHandler(**router)

output = connection.send_command("show ip interface brief")
print(output)
print("=====================================")
output=connection.send_command("ping 8.8.8.8")
print(output)

connection.disconnect()