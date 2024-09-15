import getpass

from fabric import Connection, Config 

password =  getpass.getpass("Enter your root password: ")

config =  Config(overrides={'sudo': {'password': password}})

conn = Connection("192.168.4.128", user="maximus", config=config)

conn.run("ls - la")