from email import iterators
from lib2to3.refactor import MultiprocessRefactoringTool


def run():
    main_network=input('enter main network = \nexample "192.168.0.0"')
    networks=int(input('how many subnetworks would you like calculate ? '))
    counter=0
    list_network=[]
    subred=2
    float_ip=0
    while True:
        counter+=1
        if counter >= networks+1:
            break 
        network=int(input(f'enter host of network  {counter}= '))
        list_network.append(network)
    list_network=sorted(list_network)
    for i in list_network:
        while True:
            if i >=subred-2:
                subred=subred-2
                break
            subred=subred^2
        float_ip=subred/256
        if float_ip <1:
            for i in MultiprocessRefactoringTool
        else:
            pass


    




if __name__=='__main__':
    run()