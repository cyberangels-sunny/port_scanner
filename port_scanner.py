# ╔══════════════════════════════╗
# ║       CYB PORT SCANNER       ║  ---complete function 
# ╚══════════════════════════════╝


# Target       : 192.168.1.68
# Ports        : 1-65535
# Open ports   : 3
# Closed ports : 65532
# Time         : 8.21s

# OPEN PORTS
# ----------------
# 22     SSH
# 80     HTTP
# 443    HTTPS    




# version 2 of port scanner 
# command line arguments coming soon 

#cyb -p 80 -t 127.0.0.1 (hostname/target)--done
#cyb -p- -t 127.0.0.1 (hostname/target) all ports --done  
#cyb -p 80 22 12 -t 127.0.0.1 (hostname/target) mulitple ports

#cyb -p 80 -t 127.0.0.1 (hostname/target)
# mulithreading used 

import time , threading , socket , sys 

# store the open ports 
open_ports = []
port_no = []
all  =  0 

# functions 


#cyb -p 80 
# single port scanning 
def single_scan  (ip, port):
    try :
        s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s1.settimeout(2)
        res = s1.connect_ex((str(ip),port))
        if res == 0 :
            open_ports.append(port)
            print("port open ",port)
        else :
            print("port closed ",port)    
        s1.close()
    except Exception:
         print("command not found please try with (cyb -h) for mannual")
         sys.exit()



#cyb -p 80 22 12 mulitple ports
# code = mul 1 
def multiple_scan (ip,ports):
    # port is type of a tupple
    t = []

    for port in ports:
        t1 = threading.Thread(target = single_scan, args = (ip,port))
        t1.start()
        t.append(t1)
    for close in t:
        close.join()




#cyb -p- all ports 
# take ip or port for scanning 
def all_scan (ip):
    threads = []
    for i in range(1,65536):
        t1 = threading.Thread(target = single_scan , args = (ip,i))
        t1.start()
        threads.append(t1)

    for t in threads:
        t.join()


def display (end_time,start_time,open_ports,ip):
    print("\n")
    print("╔══════════════════════════════╗")
    print("║       CYB PORT SCANNER       ║")
    print("╚══════════════════════════════╝ \n \n ")
    print("Target       : ",str(ip))
    if all == 1 :
        print("given ports for scanning   : 1 - 65535 " )
       
    else :
        print("given ports for scanning   :",end = "" )
        for port in port_no :  # ye line kyu nhi chal rahi 
            print(port ," ", end ="" )
        print("") 

      
       
    print("Closed ports : ",(65535- len(open_ports)))
    print("time taken ------> ",end_time-start_time)
    print("OPEN PORTS         " ,len(open_ports))
    print("-------------------------")
    print ("PORT           SERVICE")
    print("-------------------------")
    try :
        for port in open_ports :
            print(port ,"    ",socket.getservbyport(port))
    except OSError :
        print(port ,"    ","service unknown")

#return = "functionchara terminate here"

lis = sys.argv

ipadd  = []



def extract_port():
    try :
        for item in lis :
            if item.isdigit():
                port_no.append(int(item)) 
                   
    except  IndexError :
        print("command not found please try with (cyb -h) for mannual")
        sys.exit()



def extract_ip():
    try:
        for i in range (1,len(lis)):
            if lis[i] =="-t":
                ipadd.append(lis[i+1])
            
    except IndexError :
        print("command not found please try with (cyb -h) for mannual")
        sys.exit()
            

def verify ():
    v = 0 
    if lis[1] == "cyb":
        v = 1 +v 
        for i in range (1,len(lis)):
            if lis[i] == "-p" or  lis[i] == "-p-":
                v = 1 +v 
            elif lis[i] == "-t":
                v =1 + v 

    return v 

start_time = time.time()
extract_port()
extract_ip()
v = verify()
     

# cyb -p 80 -t 127.0.0.1

try :

    if v == 3 and len(port_no) == 1 :
        ip = ipadd[0]
        port =int( port_no[0] )
    
        single_scan (str(ip),port)

    elif v == 3 and len(port_no) > 1:
        ip = ipadd[0]
        multiple_scan(ip,port_no)

    elif v == 3 :

        ip = ipadd[0]
        all_scan(ip)
        all = 1

        
    elif lis[1] =="cyb":
        print("command not found please try with (cyb -h) for mannual") 


    elif lis[1] == "cyb"  and lis[2] == "-h":
        print("==&&==mannual page of a port scanner !")
        print("cyb -p 80 -t 127.0.0.1 (for single scan )")
        print("cyb -p- -t 127.0.0.1 (for all ports) ")
        print("cyb -p 80 22 12 -t 127.0.0.1 mulitple ports")
    
except IndexError :
        print("command not found please try with (cyb -h) for mannual")
        sys.exit()


end_time = time.time()

display (end_time,start_time,open_ports,ip)

