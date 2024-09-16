import paramiko
import time
from getpass import getpass

import paramiko.ssh_exception

host = '192.168.4.128'
user = 'maximus'

if __name__ == '__main__':
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
        password = getpass('Enter your password: ')
        client.connect(host, username=user, password=password)

        while True:
            try:
                cmd = input("$> ")
                if cmd == "exit": break
                stdin, stdout, stderr = client.exec_command(cmd)
                print(stdout.read().decode())
            except KeyboardInterrupt:
                break                
        client.close()
        
    except paramiko.ssh_exception.AuthenticationException as e:
        print('Has fallado')