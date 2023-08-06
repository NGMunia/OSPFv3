
from Devices.Device_list import Routers
from netmiko import ConnectHandler
from rich import print as rp

filepath = input('filepath: ')

'''
Running Configurations
'''
for devices in Routers.values():
    conn = ConnectHandler(**devices)
    conn.enable()
    host = conn.send_command('show version', use_textfsm=True)[0]['hostname']
    
    output = conn.send_command('show run')
    
    with open(f'{filepath}/{host}','w') as f:
        f.write(output)
        conn.disconnect()
    rp(f'Finished backing up {host} running-config\n')
        


    