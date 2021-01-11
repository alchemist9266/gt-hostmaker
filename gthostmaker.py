#!/usr/bin/env python3
#--------------------#
# Coded By NumeX & Leak

# Import Module
import os, sys, time

# using if else
try:
    print("[+] Host Creator By : NumeX & Leak\n")
    device = input("[1] Android\n[2] Pc/Computer\n-> ")
    if device == "1":
        ipadr = input("[?] Enter Your IP Server : ")
        nameadr = input("[?] Enter Your Host Name (EX - host) : ")
        extadr = input(f"[?] Enter {nameadr} extension (EX - txt) : ")
        pathadr = input(f'[?] Enter {nameadr}.{extadr} Path Where You want to save (EX - \sdcard\) : ')

        fadr = open(f'{pathadr}{nameadr}.{extadr}', 'a+')

        fadr.write(ipadr + ' growtopia1.com\n' + ipadr + ' growtopia2.com')
        fadr.close()

        print('#---------------------#\n')
        print(f'Success make your host with name {nameadr}.{extadr} at path {pathadr}...\n')
        input('Enter any key for close...')

    else:
        ippc = input("[?] Enter Your IP Server : ")
        namepc = input("[?] Enter Your Host Name (EX - host) : ")
        extpc = input(f"[?] Enter {namepc} extension (EX - txt) : ")
        pathpc = input(f'[?] Enter {namepc}.{extpc} Path Where You want to save (EX - C:\) : ')

        fpc = open(f"{pathpc}{namepc}.{extpc}", "a+")

        fpc.write(ippc + ' growtopia1.com\n' + ippc + ' growtopia2.com')
        fpc.close()

        print('#---------------------#\n')
        print(f'Success make your host with name {namepc}.{extpc} at path {pathpc}...\n')
        input('Enter any key for close...')
        time.sleep(1)
        os.system(f"start {pathpc}{namepc}.{extpc}")

except:
    print("This Tools Only support PC / ANDROID...")
    input("Enter any key for close....")