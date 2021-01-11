import os, sys, time

#Made by Leak#5749
#Thanks to Numex
print("GTPS-HostMaker made by Leak#5749")
print("Repo Project")
print("Github : https://github.com/leak37")
print("Thanks to Numex")
print("=================================")

sip = input("Server IP : ")
fn = input("File Name : ")
extns = input("File Ext (Ex = bin)' : ")

h = open(f'{fn}.{extns}', 'a+')
h.write(str(sip + " growtopia1.com\n" + sip + " growtopia2.com"))

h.close()
print(f'File {fn} has been succesfully created with IP {sip}')
input("Touch enter to close this program.")