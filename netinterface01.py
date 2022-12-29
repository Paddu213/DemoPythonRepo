'''
import ifaddr
adapters=ifaddr.get_adapters()
for adapter in adapters:
    print("IPs of network adapter "+adapter.nice_name) #nice_name :fetches the name of the "adapter"
    for ip in adapter.ips:
        print(" %s/%s"%(ip.ip,ip.network_prefix))'''

import ifaddr
adapters=ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("IPs of network adapter "+adapter.nice_name) #nice_name :fetches the name of the "adapter"
    if adapter.ips:
        for ip in adapter.ips:
            print(" %s/%s"%(ip.ip,ip.network_prefix))
    else:
        print(" No IPs configured")

