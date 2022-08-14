import math
import os
import time


def run():

    def correction(a,list):
        if a < 256:
            list[3]=a
            return list
        else:
            floatnet=a/256
            network_type_D,network_type_C =math.modf(floatnet)
            list[3]=int(network_type_D*256)
            list[2]=int(network_type_C)+int(list[2])
            return list
    def try_again(value,counter=None):
        plus=0
        check=0
        while True:        
            try:            
                if value == 1:

                    main_network=input('enter main network \nexample "192.168.0.0"\n R= ') 
                    #variable for test without input parameter
                    # main_network='192.168.0.0'
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
                    #variable of test without input networks=5
                    return networks
                elif value==3:
                    network=int(input(f'enter host of network  {counter}= '))
                    
                    return network
            except ValueError:
                print("wrong value\n try again")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
    def ticket_network(n,subred,main_network):
        #convert list to str to print with '.'each value
        network_main=".".join(str(i)for i in main_network)
        
        floatnet=(subred+int(main_network[3]))/256
        network_type_D,network_type_C =math.modf(floatnet)
            
        
        ip_route=main_network.copy()
        a=1+int(ip_route[3])
        ip_route=correction(a,ip_route)      
        ip_route=".".join(str(i)for i in ip_route)               
        str_last_ip=main_network.copy()
        str_last_ip[3]=int(network_type_D*256) 
        str_last_ip[2]=int(network_type_C)+int(str_last_ip[2])
        broadcast_ip=str_last_ip.copy()
        a=1+int(broadcast_ip[3])
        broadcast_ip=correction(a,broadcast_ip)
        main_network=broadcast_ip.copy()
        a=1+int(main_network[3])
        main_network=correction(a,main_network)
        broadcast_ip=".".join(str(i)for i in broadcast_ip)
        str_last_ip=".".join(str(i)for i in str_last_ip)
        


        print(f'Hosts = {n}')
        print(f'network ={network_main}')# 192.168.0.0
        print(f'Ip route= {ip_route}')#192.168.0.1
        print(f'Last ip usable= {str_last_ip}')#192.168.0.
        print(f'broadcast ip {broadcast_ip}')#
        
        
        
        return main_network
    
    main_network=try_again(1)
    main_network=main_network.split('.')
    networks=try_again(2)
    counter=0
    list_network=[]
    
    
    while True:
        #number of network
        counter+=1
        if counter >= networks+1:
            break
        #ask for a host and give a numbere's network 
        network=try_again(3,counter)
        #make a list of all network
        list_network.append(network)
    #sort list by low number to high number
    list_network=sorted(list_network)
    #sort reverse
    list_network.reverse()
    #for to know useble host for each one network
    for n in list_network:
        subred=2
        while True:
            if n <=subred:
                subred=subred-2
                break
            subred*=2  
        main_network=ticket_network(n,subred,main_network)

if __name__=='__main__':
    run()