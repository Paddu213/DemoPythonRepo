import socket
hostname=socket.gethostname()  #to get hostname
print(hostname)

#to get ip address
ipadd=socket.gethostbyname(hostname)
print(ipadd)

"""
Python -Dynamic + OOP
OOP - Abstraction
exposing:gethostname() -->socket
LOC[lines of codes] lesser
More the LOC-->more the bugs-->more the issues-->more time
lesser the LOC-->More Agile it is ::Agile/Scrum
"""