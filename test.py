import os
import time
subnetmask={4:'/30 255.255.255.252',
            8:'/29 255.255.255.248',
            16:'/28 255.255.255.240',
            32:'/27 255.255.255.224',
            64:'/26 255.255.255.192',
            128:'/25 255.255.255.128',
            256:'/24 255.255.255.0',
            512:'/23 255.255.254.0',
            1024:'/22 255.255.252.0',
            2048:'/21 255.255.248.0',
            4096:'/20 255.255.240.0',
            8192:'/19 255.255.224.0',
            16384:'/18 255.255.192.0',
            32768:'/17 255.255.128.0',}

print(subnetmask[4])
'''def try_again(value,counter=None):
        plus=0
        check=0
        while True:        
            try:            
                if value == 1:

                    main_network=input('enter main network \nexample "192.168.0.0"\n R= ') 
                    for i in main_network:
                        if i =='.':
                            plus+=1
                    if plus==3:
                        me=main_network.split('.')
                        for i in me:
                            if int(i)>=256 or i =='':
                                check+=1
                        if check== 0:                                               
                            return main_network
                        else:
                            check=0
                            plus=0
                            raise ValueError
                            
                    else:
                        raise ValueError
                    
                elif value== 2:
                    networks=int(input('how many subnetworks would you like calculate ? '))
                    return networks
                elif value==3:
                    network=int(input(f'enter host of network  {counter}= '))
                    return network
            except ValueError:
                print("wrong value\n try again")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
main_network=try_again(1)
networks=try_again(2)
network=try_again(3,3)
print(main_network,"",networks,"",network)'''

'''a=[3,5,2,6,34,5,4,3,2,3]
b=a.copy()
b.append('wac')
print(a)
print(b)'''
'''
h=12
def run():
    a=[2,3,5,13,4]
    print(a)
    a.reverse()
    print(a)
    print(type(a))
run()
print(h)'''




'''import imp


import math
main="192.168.0.0"
ass=1
print(type(main.split('.')))
main=main.split('.')
print(main)
print(len(main))
ip_route=main
print(ip_route)
ip_route[3]=1+int(ip_route[3])
print(ip_route)
ip_route=".".join(str(i)for i in ip_route)
print(ip_route)
floa=300/256
print(floa)
a,b=math.modf(floa)
print(a,b)'''
'''
main.insert(3,ass+int(main[3]))
print(main)
main.pop()
print(main)

def run():
    
    str_last_ip=".".join(str(i)for i in main)
    print(str_last_ip)
run()
print(type(main[3]))
'''
