import os
import subprocess
import sys




subnet = sys.argv[1]

if os.name=='posix':
	myping = 'ping -c 2 '
elif os.name in ('nt','dos','ce'):
	myping = 'ping -n 2 '


f = open('ping_'+subnet+'.log','w')

for ip in range(2,5):
	ret= subprocess.call(myping + str(subnet)+"."+str(ip),shell=True,stdout=False,stderr=subprocess.STDOUT)
	if ret == 0:
		# print(subnet+"."+str(ip)+" is alive"+"\n")
		f.write(subnet+"."+str(ip)+" is alive"+"\n")
	else:
		# print(subnet+"."+str(ip)+" not respon"+"\n")
		f.write(subnet+"."+str(ip)+" is not respon"+"\n")