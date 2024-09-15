from sys import stderr, stdin, stdout
import time
import paramiko
from getpass import getpass

HOST = '192.168.100.82'
USER = 'maximus'


if __name__== '__main__':
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    password = getpass('Enter your password: ')
    client.connect(HOST, username=USER, password='password')

    stdin, stdout, stderr,  client.exec_command('ls')

    time.sleep(1)

    result = stdout.read().decode()

    print(result)

    
    

    