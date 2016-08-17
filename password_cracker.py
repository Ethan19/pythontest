from sys import platform as _platform

if _platform == 'linux' or _platform == 'linux2':
	import crypt
elif _platform =='darwin':
	import crypt
elif _platform == 'win32':
	try:
		import fcrypt
	except ImportError:
		print("pls install fcrypt")

def testPass(cryptPass):
	salt = cryptPass[0:2]
	# print(salt)
	dictFile = open('dictionary.txt','rw+')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word,salt)
		dictFile.write(cryptWord+'\n')
	dictFile.close()






def main():
	passFile = open('password.txt')
	for line in passFile.readlines():
		if ':' in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip('  ')
			print('[*] password For:'+user+'-----'+cryptPass)
			testPass(cryptPass)



if __name__ == '__main__':
	main()

