
from getpass import getpass
from rich import print as rp

username = input('Username: ')
password = getpass('Password: ')
secret   = getpass('Secret: ')

while True:
    if username == 'Automation' and password == 'cisco123' and secret == 'cisco123':
        rp(f'[green] Login Successful!\n')
        break
    else:
        rp(f'[red] Invalid Username and/or Password!')
        username = input('Username: ')
        password = getpass('Password: ')
        secret   = getpass('Secret: ')



