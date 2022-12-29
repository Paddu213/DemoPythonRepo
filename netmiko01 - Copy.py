from netmiko import ConnectHandler
CSR={
    "device_type": "cisco_ios",
    "ip":"sandbox-iosxe-latest-1.cisco.com",
    "port":22,
    "username": "developer",
    "password": "C1sco12345"
}
net_connect=ConnectHandler(**CSR)
#output=net_connect.send_command('show ip int bri')
#output_clock=net_connect.send_command('show clock')
#output_routers=net_connect.send_command('show ip ro')
output_runconfig=net_connect.send_command('show run ')

print(output_runconfig)
#output_runhost=net_connect.send_command('show run | i host')
#print(output_runhost)

net_connect.disconnect()