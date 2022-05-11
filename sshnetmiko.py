
 # sshnetmiko.py
 #
 # Created: 10/17/2020 
 # Author: Rodrigo Noriega
 # 
 # Script for data collection 

import os
clear = lambda: os.system('cls')
clear()

from netmiko import ConnectHandler

#Cretae log, opens file with name of .txt
f = open("log_2800.txt","w")

#Connect to device
device = ConnectHandler(device_type='cisco_ios', ip='172.27.1.18', username='admin', password='sshadmin')

v = 'show ip interface brief'
w = '17@05cy.!.7'
x = 'show running-config'

#Send Command
f.write('\n' + v + '\n')
print(v,'....... ok!')
output=device.send_command(v)
f.write(output + '\n\n')

f.write('\n' + x + '\n')
print(x,'....... ok!')
output=device.send_command(x)
f.write(output + '\n\n')



#Close ssh sessiond and writing on .txt
device.disconnect()
f.close()

input('\nAl commands where verified!\nPress enter to continue')
clear()