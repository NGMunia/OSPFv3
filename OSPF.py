from Devices.Device_list import Routers
from netmiko import ConnectHandler
from rich import print as rp
import ntc_templates

'''
VERIFYING OSPFv3 IPv4 NEIGHBORSHIP
'''
for devices in Routers.values():
    conn = ConnectHandler(**devices)
    conn.enable()
    host = conn.send_command('show version', use_textfsm=True)[0]['hostname']
    
    rp(f'\n[cyan]Verifying IPv4 Neighborship on Host {host}\n',('-'*100))
    rp(conn.send_command('show ospfv3 ipv4 neighbor'))
   
print(f'\n{("#"*100)}\n')


'''
VERIFYING OSPFv3 IPv6 NEIGHBORSHIP
'''
for devices in Routers.values():
    conn = ConnectHandler(**devices)
    conn.enable()
    host = conn.send_command('show version', use_textfsm=True)[0]['hostname']
    
    rp(f'\n[cyan]Verifying IPv6 Neighborship on Host {host}\n',('-'*100))
    rp(conn.send_command('show ospfv3 ipv6 neighbor'))
   
print(f'\n{("#"*100)}\n')


'''
Verifying IP OSPFv3 IPv4 INTERFACES
'''    
for devices in Routers.values():
    conn = ConnectHandler(**devices)
    conn.enable()
    host = conn.send_command('show version', use_textfsm=True)[0]['hostname']
    
    rp(f'\n[cyan]Verifying OSPFv3 IPv4 interfaces on Host {host}\n',('-'*100))
    rp(conn.send_command('show ospfv3 ipv4 interface brief'))
    
print(f'\n{("#"*100)}\n')
    

'''
Verifying IP OSPFv3 IPv6 INTERFACES
'''    
for devices in Routers.values():
    conn = ConnectHandler(**devices)
    conn.enable()
    host = conn.send_command('show version', use_textfsm=True)[0]['hostname']
    
    rp(f'\n[cyan]Verifying OSPFv3 IPv4 interfaces on Host {host}\n',('-'*100))
    rp(conn.send_command('show ospfv3 ipv6 interface brief'))

  
print(f'\n{("#"*100)}\n')

'''
Verifying OSPFv3 Timers:
'''
for devices in Routers.values():
    conn = ConnectHandler(**devices)
    conn.enable()
    host = conn.send_command('show version', use_textfsm=True)[0]['hostname']
    
    rp(f'\n[cyan]Verifying OSPFv3 Timers on Host {host}\n',('-'*100))
    rp(conn.send_command('sh ospfv3 interface | include Timer|line'))


