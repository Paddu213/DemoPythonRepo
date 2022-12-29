import psutil
network_status=psutil.net_io_counters(pernic=False)
bytes_sent=getattr(network_status,'bytes_sent')
bytes_recv=getattr(network_status,'bytes_recv')
print(bytes_sent)
print(bytes_recv)

print("Bytes Sent = {0} | Bytes Received= {1}".format(bytes_sent,bytes_recv))