from pwn import *


#Connect without SSH
conn = remote('2018shell.picoctf.com',10493)

#Receive individual lines
for x in range(4):
    print(conn.recvline())
"""
Do some math operation here
 
 
Send Response back to server
 """
result = '251.71.156.29'

conn.sendline(result)

#Receive multiple lines until timeout -> Output is a LIST of lines
lst = conn.recvlines(timeout=2)

for x in lst:
    print (x.decode('UTF-8'))


"""

Remove multiline comment to use SSH connection

#Make SSH connection
shell = ssh('USERNAME', 'HOST', password='')

#Check which user you're running as
x = shell['whoami']
print(x)

#Check what files are in your current working directory
x = shell['ls']
print(x)

#Spin up a shell
sh = shell.run('sh')

#Send and receive shell commands/responses
b = sh.sendline(b'sleep 3; echo hello world;')
x = sh.recvline(timeout=5)
print(x)

sh.sendline(b'sleep 1; echo hello world;')
sh.sendline(b'sleep 1; echo hello world;')
sh.sendline(b'sleep 1; echo hello world;')
sh.sendline(b'sleep 1; echo hello world;')
sh.sendline(b'sleep 1; echo hello world;')

# Get lines from the buffer
b = sh.recvlines(timeout=4)

for x in b:
    print(x)

shell.close()
"""

