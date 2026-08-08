
import socket 
from datetime import time ,datetime

target = input("Enter a victim ip address to scan  : ")
start_time = datetime.now()

open_ports = []


for port  in range(1,1024):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(0.5)
    res = sock.connect_ex((target,port))
    print(target,port,"processing................")
    if res ==0:
        print("victim ip address is : ",target)
        print("Port",port,"is open")
        open_ports.append(port)
    elif res != 1:
        print("victim ip address is : ",target)
        print("Port",port,"is closed")    
    sock.close()


print("system host ",target)
print("Open ports are : ",open_ports)
print("Scanning completed in : ",datetime.now()-start_time)

# code ready to push on git hub version1 --cyberangels  
