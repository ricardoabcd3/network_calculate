import math


def run():
    def ticket_network(n,subred,main_network):
        #convert list to str to print with '.'each value
        network_main=".".join(str(i)for i in main_network)
        
        floatnet=(subred+int(main_network[3]))/256
        network_type_D,network_type_C =math.modf(floatnet)
            
        
        ip_route=main_network.copy()
    
        ip_route[3]=1+int(ip_route[3])
        ip_route=".".join(str(i)for i in ip_route)
        str_last_ip=main_network.copy()
        str_last_ip[3]=int(network_type_D*256)
        str_last_ip[2]=int(network_type_C)
        broadcast_ip=str_last_ip.copy()
        broadcast_ip[3]=1+int(broadcast_ip[3])
        main_network[3]=1+int(broadcast_ip[3])
        broadcast_ip=".".join(str(i)for i in broadcast_ip)
        str_last_ip=".".join(str(i)for i in str_last_ip)
        


        print(f'Hosts = {n}')
        print(f'network ={network_main}')# 192.168.0.0
        print(f'Ip route= {ip_route}')#192.168.0.1
        print(f'Last ip usable= {str_last_ip}')#192.168.0.
        print(f'broadcast ip {broadcast_ip}')#
        
        
        
        return main_network
    main_network=input('enter main network = \nexample "192.168.0.0"')
    main_network=main_network.split('.')
    networks=int(input('how many subnetworks would you like calculate ? '))
    counter=0
    list_network=[]
    subred=2
    
    while True:
        #number of network
        counter+=1
        if counter >= networks+1:
            break
        #ask for a host and give a numbere's network 
        network=int(input(f'enter host of network  {counter}= '))
        #make a list of all network
        list_network.append(network)
    #sort list by low number to high number
    list_network=sorted(list_network)
    #sort reverse
    list_network.reverse()
    #for to know useble host for each one network
    for n in list_network:
        while True:
            if n <=subred:
                subred=subred-2
                break
            subred*=2  
        main_network=ticket_network(n,subred,main_network)
    
    
    

'''def ticket_network(host,main_network,subred):
    usable_ip=int(main_network[3])+int(subred)
    usable_ip=subred/256
    if usable_ip<1:
        main=main_network.split('.')            
        print(len(main))
        
        main.insert(3,subred+main)
        main.pop()
        str_last_ip=".".join(str(i)for i in main)
        broadcast_ip=main.insert(3,1+int(main[3]))
        broadcast_ip=main.pop()

        
            

        
        ip_route=main.insert(3,1+int(main[3]))

        

        print(f'Hosts = {host}')
        print(f'network ={main_network}')# 192.168.0.0
        print(f'Ip route= {ip_route}')#192.168.0.1
        print(f'Last ip usable{str_last_ip}')
        print(f'broadcast ip {broadcast_ip}')
        '''
        

            


        

        


    




if __name__=='__main__':
    run()