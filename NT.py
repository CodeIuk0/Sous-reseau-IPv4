from Network import Network

N = Network()

gen_ip = lambda: '.'.join([randint(1,254).__str__() for x in range(4)])

_NT = N.network(f'{gen_ip()}/24')  # IP/Mask (255.255.255.0 (CIDR : /24))

#print(N.mask) <- output the capacity of mask (in bits) and address of  mask all that in dictionnary positionned in array

_NT.CAPACITY_OUTPUT=254; #change the capacity to output the result of get_hosts(), default is 2**14-2 (16382 /18)

print(_NT.ip_adress(_NT.STR)) #output netowrk address, STR => address in str (string)

print(_NT.network_adress(_NT.STR)) #get network address

print(_NT.__get_format__()) # show all formats you can use

print(_NT.get_hosts()) #show hosts usable between first address and  last address

#_NT.output_data() #output data, mask, address of network, Wildcard Mask, First address, last address, broadcast address, ip class, range address usable etc ... 

print(_NT.firsthost()) #get firsthost usable, you can use format (_NT.STR)
print(_NT.lasthost()) #get lasthost usable, you can use format (_NT.STR)

print(_NT.ip_class()) #get class of ip
