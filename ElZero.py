import os, sys,random,time
from colorama import Fore
from colorama import Style
from colorama import init
init(autoreset=True)
init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

try:
    os.mkdir('ElZero')
except:
    pass
def clear():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass
def logo():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = "\n                               ' )     _)             (,     /'          \n                               //  _/~/'                   /'            \n                             /'/_/~ /'  ____             /'____     ____ \n                           /' /~  /'  )'    )--_       /'/'    )--/'    )\n                         /'     /'  /'       /' `    /'/'    /' /(___,/' \n                     (,/'      (_,/'        (_____,/' (___,/'  (________ "  
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.05)

def removeHTTP(url):
	try:
		url = url.replace("http://","")
		url = url.replace("https://","")
		return url
	except Exception as e:
		return url
def split(url):
	url = removeHTTP(url)
	try:
		url = url.split('/')[0]
	except Exception as e:
		print ("Ok")
	print ("{}".format(fg)+url)
	with open('ElZero/urls.txt','a+')as f:
		f.write(url+ ' #ElZero \n')
	

clear()
logo()
x = "                       [Delete urls Extension] [x] Coded By ElZero [x]\n                            FB: https://www.facebook.com/youssefj0oe\n                                   ICQ: @ElZero"
print ("\n")
print (x)
print ("\n")
listS = input('\n\t\t{}[+]{} Give Me Your site List ! : '.format(gr, sb))
if __name__ == '__main__':
	urls = open(listS, 'r')
	for url in urls:
		url = url.strip()
		split(url)