from netmiko import ConnectHandler

with open("devices.txt") as routers:
    for IP in routers:
        Router={
            "device_type": "cisco_ios",
            "ip":"sandbox-iosxe-latest-1.cisco.com",
            #"ip": IP,
            "username": "developer",
            "password": "C1sco12345"
        }

        net_connect=ConnectHandler(**Router)

        print('Connecting to '+ IP)
        print("-"*78)
        output=net_connect.send_command('sh ip in bri')
        print(output)
        print()
        print("-"*78)
net_connect.disconnect()