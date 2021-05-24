import requests,os,sys,time,webbrowser
from tqdm import tqdm , trange
from bs4 import BeautifulSoup as BS
html=requests.get("https://pastebin.com/tJpCf6Xt").text   #pass
s=BS(html, "html.parser")
h=s.find("div" ,{"class":"de1"})
html2=requests.get("https://pastebin.com/LEXfcxsV").text  #url
s2=BS(html2, "html.parser")
h2=s2.find("div" ,{"class":"de1"})
ho=h2.text
html23=requests.get("https://pastebin.com/bdG8WRU1").text  #watch  
s23=BS(html23, "html.parser")
h23=s23.find("div" ,{"class":"de1"})
ho3=h23.text
html234=requests.get("https://pastebin.com/e3HsTcT1").text  #sub
s234=BS(html234, "html.parser")
h234=s234.find("div" ,{"class":"de1"})
ho34=h234.text
html3=requests.get("https://pastebin.com/7XAWpy3v").text  #statues
s3=BS(html3, "html.parser")
h3=s3.find("div" ,{"class":"de1"})
ho2=h3.text
tries = 4
mainpassword = h.text
zx=("\033[1;92m--------------- Design BY Dark ---------------")
for ecv in zx:
 sys.stdout.write(ecv)
 sys.stdout.flush()
 time.sleep(0.03)
print()
print(ho2)
print("\033[1;92m-"*50)
inputpassword = input("\033[1;92mEnter Password:")

while inputpassword != mainpassword:
	tries -=1
	print("\033[1;92m-"*50)
	print(f"\033[1;91mIncorrect password, { 'Last' if tries == 0 else tries } left ")
	print("\033[1;92m-"*50)
	inputpassword = input("\033[1;92mEnter Password: ")
	if tries == 0:
		webbrowser.open("https://t.me/Dark_Free_Bot")
		sys.exit()
		break
else:
        print("\033[1;92m-"*50)
        print("\033[1;92mcorrect password")
        print("\033[1;92m-"*50)
        time.sleep(2)
        os.system("clear")    
l=("\033[1;92mPlease Wait.......")
for n in l:
 sys.stdout.write(n)
 sys.stdout.flush()
 time.sleep(0.03)
with tqdm(total=100) as pbar:
	for bar in range(10):
		time.sleep(0.3)
		pbar.update(10)
os.system("clear")
def logo():
	f=("\033[1;92m--------------- Design BY Dark ---------------")
	for e in f:
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
	print()
	print(ho2) 
	logo1='''\033[1;92m

 /$$$$$$$                      /$$            
| $$__  $$                    | $$            
| $$  \ $$  /$$$$$$   /$$$$$$ | $$   /$$      
| $$  | $$ |____  $$ /$$__  $$| $$  /$$/      
| $$  | $$  /$$$$$$$| $$  \__/| $$$$$$/       
| $$  | $$ /$$__  $$| $$      | $$_  $$       
| $$$$$$$/|  $$$$$$$| $$      | $$ \  $$      
|_______/  \_______/|__/      |__/  \__/      
                                              
                                              
'''
	for y in logo1:
		sys.stdout.write(y)
		sys.stdout.flush()
		time.sleep(0.003)
	print('Send Message To Join In Channel')	
	p=("https://t.me/Dark_Free_Bot")
	for e in p:
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)
	print()  
	l=("\033[1;92m--------------- Script Fog Tube Vip ---------------")
	for v in l:
		sys.stdout.write(v)
		sys.stdout.flush()
		time.sleep(0.02)
logo()		  
print()
print("\033[1;92m(1) Subscribes")
print("\033[1;92m-"*50)
print("\033[1;92m(2) Watch Videos")
print("\033[1;92m-"*50)
print("\033[1;92m(3) Payments")
print("\033[1;92m-"*50)
print("\033[1;92m(4) Check Coins")
print("\033[1;92m-"*50)
put=input('Enter Select:')
print("\033[1;92m-"*50)
os.system("clear")
if put=='1':
    logo()
    print()
    email=input('\033[1;92mEnter Your Email:')
    print("\033[1;92m-"*50)
    ide=input('\033[1;92mEnter Your Id:')
    print("\033[1;92m-"*50)
    nam=input('\033[1;92mEnter Your Name:')
    print("\033[1;92m-"*50)
    token=input('\033[1;92mEnter Your Token:')
    print("\033[1;92m-"*50)
    dev=input('\033[1;92mEnter Your Device Id:')
    print("\033[1;92m-"*50)
    os.system("clear")
    logo()
    print()
    while True:
        html2=requests.get("https://pastebin.com/LEXfcxsV").text  #url
        s2=BS(html2, "html.parser")
        h2=s2.find("div" ,{"class":"de1"})
        ho=h2.text
        hd={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url=ho
        data={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r=requests.post(url,headers=hd,data=data).json()
        check=r['message']
        print(check)
        print("\033[1;92m-"*50)
        c=r['data']
        m=c['api_token']
        hd2={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url2=("http://app.fogtube.net/api/v1/unsubscribed-campaigns?api_token={}".format(m))
        data2={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r2=requests.get(url2,headers=hd2,data=data2).json()
        k=r2['data']
        Dark=k['id']
        hd3={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        html234=requests.get("https://pastebin.com/e3HsTcT1").text  #sub
        s234=BS(html234, "html.parser")
        h234=s234.find("div" ,{"class":"de1"})
        ho34=h234.text
        url3=ho34
        data3={"api_token":m,"campaign_id":Dark}
        r3=requests.post(url3,headers=hd3,data=data3).json()
        watch=r3['message']
        print(watch)
        print("\033[1;92m-"*50)
        hd3={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url3=("http://app.fogtube.net/api/v1/my-coins?api_token={}".format(m))
        data3={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r3=requests.get(url3,headers=hd3,data=data3).json()
        dog=r3['data']
        coin=dog['count_coins']
        print("Done Win Now You Have==>",coin)
        print("\033[1;92m-"*50)
os.system("clear")        
if put=='2':
    logo()
    print()
    email=input('\033[1;92mEnter Your Email:')
    print("\033[1;92m-"*50)
    ide=input('\033[1;92mEnter Your Id:')
    print("\033[1;92m-"*50)
    nam=input('\033[1;92mEnter Your Name:')
    print("\033[1;92m-"*50)
    token=input('\033[1;92mEnter Your Token:')
    print("\033[1;92m-"*50)
    dev=input('\033[1;92mEnter Your Device Id:')
    print("\033[1;92m-"*50)
    os.system("clear")
    logo()
    print()
    while True:
        html2=requests.get("https://pastebin.com/LEXfcxsV").text  #url
        s2=BS(html2, "html.parser")
        h2=s2.find("div" ,{"class":"de1"})
        ho=h2.text
        hd={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url=ho
        data={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r=requests.post(url,headers=hd,data=data).json()
        check=r['message']
        print(check)
        print("\033[1;92m-"*50)
        c=r['data']
        m=c['api_token']
        hd2={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url2=("http://app.fogtube.net/api/v1/all-video-campaigns?api_token={}".format(m))
        data2={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r2=requests.get(url2,headers=hd2,data=data2).json()
        k=r2['data']
        vi=k['id']
        hd3={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        html23=requests.get("https://pastebin.com/bdG8WRU1").text  #watch
        s23=BS(html23, "html.parser")
        h23=s23.find("div" ,{"class":"de1"})
        ho3=h23.text
        url3=ho3  
        data3={"api_token":m,"video_id":vi}
        r3=requests.post(url3,headers=hd3,data=data3).json()
        watch=r3['message']
        print(watch)
        print("\033[1;92m-"*50)
        hd4={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url4=("http://app.fogtube.net/api/v1/my-coins?api_token={}".format(m))
        data4={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r4=requests.get(url4,headers=hd4,data=data4).json()
        dog=r4['data']
        coin=dog['count_coins']
        print("Done Win Now You Have==>",coin)
        print("\033[1;92m-"*50)
if put=='3':
    logo()
    print()
    print("\033[1;92m(1) Vodafone Cash (15 EG)")
    print("\033[1;92m-"*50)
    print("\033[1;92m(2) Orange Cash (15 EG)")
    print("\033[1;92m-"*50)
    print("\033[1;92m(3) Etisalat Cash (15 EG)")
    print("\033[1;92m-"*50)
    print("\033[1;92m(4) PUPG (60 UC)")
    print("\033[1;92m-"*50)
    print("\033[1;92m(5) Orange Recharge (30 EG )")
    print("\033[1;92m-"*50)
    print("\033[1;92m(6) Vodafone Recharge (30 EG)")
    print("\033[1;92m-"*50)
    print("\033[1;92m(7) Etisalat Recharge (30 EG)")
    print("\033[1;92m-"*50)          
    put2=input('Enter Select:')
    os.system("clear")
    logo()
    print()
    if put2=='1':
        print('You Select Vodafone Cash (15 EG)')
        print("\033[1;92m-"*50)
        email=input('\033[1;92mEnter Your Email:')
        print("\033[1;92m-"*50)
        ide=input('\033[1;92mEnter Your Id:')
        print("\033[1;92m-"*50)
        nam=input('\033[1;92mEnter Your Name:')
        print("\033[1;92m-"*50)
        token=input('\033[1;92mEnter Your Token:')
        print("\033[1;92m-"*50)
        dev=input('\033[1;92mEnter Your Device Id:')
        print("\033[1;92m-"*50)
        number=input('\033[1;92mEnter Your Mobile Number:')
        print("\033[1;92m-"*50)
        os.system("clear")
        logo()
        print()
        html2=requests.get("https://pastebin.com/LEXfcxsV").text
        s2=BS(html2, "html.parser")
        h2=s2.find("div" ,{"class":"de1"})
        ho=h2.text
        hd={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url=ho
        data={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r=requests.post(url,headers=hd,data=data).json()
        check=r['message']
        print(check)
        print("\033[1;92m-"*50)
        c=r['data']
        m=c['api_token']
        hdD={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlA=("http://app.fogtube.net/api/v1/payments?api_token={}".format(m))
        dataR={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        rK=requests.get(urlA,headers=hdD,data=dataR).json()
        hd0={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlDa=("http://app.fogtube.net/api/v1/withdrawal-requests")
        dataRK={"api_token":m,"payment_method_id":'92',"mobile":number,"use_root":'0'}
        r2Dark=requests.post(urlDa,headers=hd0,data=dataRK).json()
        print(r2Dark)
        ccheck=r2Dark['message']
        print(ccheck)
        print("\033[1;92m-"*50)
    if put2=='2':
        print('You Select Orange Cash (15 EG)')
        print("\033[1;92m-"*50)
        email=input('\033[1;92mEnter Your Email:')
        print("\033[1;92m-"*50)
        ide=input('\033[1;92mEnter Your Id:')
        print("\033[1;92m-"*50)
        nam=input('\033[1;92mEnter Your Name:')
        print("\033[1;92m-"*50)
        token=input('\033[1;92mEnter Your Token:')
        print("\033[1;92m-"*50)
        dev=input('\033[1;92mEnter Your Device Id:')
        print("\033[1;92m-"*50)
        number=input('\033[1;92mEnter Your Mobile Number:')
        print("\033[1;92m-"*50)
        os.system("clear")
        logo()
        print()
        html2=requests.get("https://pastebin.com/LEXfcxsV").text
        s2=BS(html2, "html.parser")
        h2=s2.find("div" ,{"class":"de1"})
        ho=h2.text
        hd={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url=ho
        data={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r=requests.post(url,headers=hd,data=data).json()
        check=r['message']
        print(check)
        print("\033[1;92m-"*50)
        c=r['data']
        m=c['api_token']
        hdD2={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlA2=("http://app.fogtube.net/api/v1/payments?api_token={}".format(m))
        dataR2={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        rK2=requests.get(urlA2,headers=hdD2,data=dataR2).json()
        hd04={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlDa2=("http://app.fogtube.net/api/v1/withdrawal-requests")
        dataRK2={"api_token":m,"payment_method_id":'99',"mobile":number,"use_root":'0'}
        r2Dark2=requests.post(urlDa2,headers=hd04,data=dataRK2).json()
        ccheck2=r2Dark2['message']
        print(ccheck2)
        print("\033[1;92m-"*50)
    if put2=='3':
        print('You Select Etisalat Cash (15 EG)')
        print("\033[1;92m-"*50)
        email=input('\033[1;92mEnter Your Email:')
        print("\033[1;92m-"*50)
        ide=input('\033[1;92mEnter Your Id:')
        print("\033[1;92m-"*50)
        nam=input('\033[1;92mEnter Your Name:')
        print("\033[1;92m-"*50)
        token=input('\033[1;92mEnter Your Token:')
        print("\033[1;92m-"*50)
        dev=input('\033[1;92mEnter Your Device Id:')
        print("\033[1;92m-"*50)
        number=input('\033[1;92mEnter Your Mobile Number:')
        print("\033[1;92m-"*50)
        os.system("clear")
        logo()
        print()
        html2=requests.get("https://pastebin.com/LEXfcxsV").text
        s2=BS(html2, "html.parser")
        h2=s2.find("div" ,{"class":"de1"})
        ho=h2.text
        hd={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url=ho
        data={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r=requests.post(url,headers=hd,data=data).json()
        check=r['message']
        print(check)
        print("\033[1;92m-"*50)
        c=r['data']
        m=c['api_token']
        hdD23={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlA23=("http://app.fogtube.net/api/v1/payments?api_token={}".format(m))
        dataR23={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        rK23=requests.get(urlA23,headers=hdD23,data=dataR23).json()
        hd043={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlDa23=("http://app.fogtube.net/api/v1/withdrawal-requests")
        dataRK23={"api_token":m,"payment_method_id":'98',"mobile":number,"use_root":'0'}
        r2Dark23=requests.post(urlDa23,headers=hd043,data=dataRK23).json()
        ccheck23=r2Dark23['message']
        print(ccheck23)
        print("\033[1;92m-"*50)
    if put2=='4':
        print('You Select PUPG (60 UC)')
        print("\033[1;92m-"*50)
        email=input('\033[1;92mEnter Your Email:')
        print("\033[1;92m-"*50)
        ide=input('\033[1;92mEnter Your Id:')
        print("\033[1;92m-"*50)
        nam=input('\033[1;92mEnter Your Name:')
        print("\033[1;92m-"*50)
        token=input('\033[1;92mEnter Your Token:')
        print("\033[1;92m-"*50)
        dev=input('\033[1;92mEnter Your Device Id:')
        print("\033[1;92m-"*50)
        mobile2=input('\033[1;92mEnter Your ID PUBG:')
        print("\033[1;92m-"*50)
        os.system("clear")
        logo()
        print()
        html2=requests.get("https://pastebin.com/LEXfcxsV").text
        s2=BS(html2, "html.parser")
        h2=s2.find("div" ,{"class":"de1"})
        ho=h2.text
        hd={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url=ho
        data={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r=requests.post(url,headers=hd,data=data).json()
        check=r['message']
        print(check)
        print("\033[1;92m-"*50)
        c=r['data']
        m=c['api_token']
        hdD234={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlA234=("http://app.fogtube.net/api/v1/payments?api_token={}".format(m))
        dataR234={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        rK234=requests.get(urlA234,headers=hdD234,data=dataR234).json()
        hd0434={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlDa234=("http://app.fogtube.net/api/v1/withdrawal-requests")
        dataRK234={"api_token":m,"payment_method_id":'89',"mobile":mobile2,"use_root":'0'}
        r2Dark234=requests.post(urlDa234,headers=hd0434,data=dataRK234).json()
        ccheck234=r2Dark234['message']
        print(ccheck234)
        print("\033[1;92m-"*50)
    if put2=='5':
        print('You Select Orange Recharge (30 EG )')
        print("\033[1;92m-"*50)
        email=input('\033[1;92mEnter Your Email:')
        print("\033[1;92m-"*50)
        ide=input('\033[1;92mEnter Your Id:')
        print("\033[1;92m-"*50)
        nam=input('\033[1;92mEnter Your Name:')
        print("\033[1;92m-"*50)
        token=input('\033[1;92mEnter Your Token:')
        print("\033[1;92m-"*50)
        dev=input('\033[1;92mEnter Your Device Id:')
        print("\033[1;92m-"*50)
        email22=input('\033[1;92mEnter Your Number:')
        print("\033[1;92m-"*50)
        os.system("clear")
        logo()
        print()
        html2=requests.get("https://pastebin.com/LEXfcxsV").text
        s2=BS(html2, "html.parser")
        h2=s2.find("div" ,{"class":"de1"})
        ho=h2.text
        hd={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url=ho
        data={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r=requests.post(url,headers=hd,data=data).json()
        check=r['message']
        print(check)
        print("\033[1;92m-"*50)
        c=r['data']
        m=c['api_token']
        hdD2345={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlA2345=("http://app.fogtube.net/api/v1/payments?api_token={}".format(m))
        dataR2345={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        rK2345=requests.get(urlA2345,headers=hdD2345,data=dataR2345).json()
        hd04345={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlDa2345=("http://app.fogtube.net/api/v1/withdrawal-requests")
        dataRK2345={"api_token":m,"payment_method_id":'96',"mobile":email22,"use_root":'0'}
        r2Dark2345=requests.post(urlDa2345,headers=hd04345,data=dataRK2345).json()
        ccheck2345=r2Dark2345['message']
        print(ccheck2345)
        print("\033[1;92m-"*50)
    if put2=='6':
        print('You Select Vodafone Recharge (30 EG)')
        print("\033[1;92m-"*50)
        email=input('\033[1;92mEnter Your Email:')
        print("\033[1;92m-"*50)
        ide=input('\033[1;92mEnter Your Id:')
        print("\033[1;92m-"*50)
        nam=input('\033[1;92mEnter Your Name:')
        print("\033[1;92m-"*50)
        token=input('\033[1;92mEnter Your Token:')
        print("\033[1;92m-"*50)
        dev=input('\033[1;92mEnter Your Device Id:')
        print("\033[1;92m-"*50)
        mobile22=input('\033[1;92mEnter Your Number:')
        print("\033[1;92m-"*50)
        os.system("clear")
        logo()
        print()
        html2=requests.get("https://pastebin.com/LEXfcxsV").text
        s2=BS(html2, "html.parser")
        h2=s2.find("div" ,{"class":"de1"})
        ho=h2.text
        hd={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url=ho
        data={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r=requests.post(url,headers=hd,data=data).json()
        check=r['message']
        print(check)
        print("\033[1;92m-"*50)
        c=r['data']
        m=c['api_token']
        hdD23456={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlA23456=("http://app.fogtube.net/api/v1/payments?api_token={}".format(m))
        dataR23456={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        rK23456=requests.get(urlA23456,headers=hdD23456,data=dataR23456).json()
        hd043456={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlDa23456=("http://app.fogtube.net/api/v1/withdrawal-requests")
        dataRK23456={"api_token":m,"payment_method_id":'95',"mobile":mobile22,"use_root":'0'}
        r2Dark23456=requests.post(urlDa23456,headers=hd043456,data=dataRK23456).json()
        ccheck23456=r2Dark23456['message']
        print(ccheck23456)
        print("\033[1;92m-"*50)
    if put2=='7':
        print('You Select Etisalat Recharge (30 EG)')
        print("\033[1;92m-"*50)
        email=input('\033[1;92mEnter Your Email:')
        print("\033[1;92m-"*50)
        ide=input('\033[1;92mEnter Your Id:')
        print("\033[1;92m-"*50)
        nam=input('\033[1;92mEnter Your Name:')
        print("\033[1;92m-"*50)
        token=input('\033[1;92mEnter Your Token:')
        print("\033[1;92m-"*50)
        dev=input('\033[1;92mEnter Your Device Id:')
        print("\033[1;92m-"*50)
        email222=input('\033[1;92mEnter Your Number:')
        print("\033[1;92m-"*50)
        os.system("clear")
        logo()
        print()
        html2=requests.get("https://pastebin.com/LEXfcxsV").text
        s2=BS(html2, "html.parser")
        h2=s2.find("div" ,{"class":"de1"})
        ho=h2.text
        hd={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        url=ho
        data={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        r=requests.post(url,headers=hd,data=data).json()
        check=r['message']
        print(check)
        print("\033[1;92m-"*50)
        c=r['data']
        m=c['api_token']
        hdD234567={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlA234567=("http://app.fogtube.net/api/v1/payments?api_token={}".format(m))
        dataR234567={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
        rK234567=requests.get(urlA234567,headers=hdD234567,data=dataR234567).json()
        hd0434567={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
        urlDa234567=("http://app.fogtube.net/api/v1/withdrawal-requests") #pay
        dataRK234567={"api_token":m,"payment_method_id":'97',"mobile":email222,"use_root":'0'}
        r2Dark234567=requests.post(urlDa234567,headers=hd0434567,data=dataRK234567).json()
        ccheck234567=r2Dark234567['message']
        print(ccheck234567)
        print("\033[1;92m-"*50)
if put=='4':
    logo()
    print()
    email=input('\033[1;92mEnter Your Email:')
    print("\033[1;92m-"*50)
    ide=input('\033[1;92mEnter Your Id:')
    print("\033[1;92m-"*50)
    nam=input('\033[1;92mEnter Your Name:')
    print("\033[1;92m-"*50)
    token=input('\033[1;92mEnter Your Token:')
    print("\033[1;92m-"*50)
    dev=input('\033[1;92mEnter Your Device Id:')
    print("\033[1;92m-"*50)
    os.system("clear")
    logo()
    print()
    html2=requests.get("https://pastebin.com/LEXfcxsV").text  #url
    s2=BS(html2, "html.parser")
    h2=s2.find("div" ,{"class":"de1"})
    ho=h2.text
    hd={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
    url=ho
    data={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
    r=requests.post(url,headers=hd,data=data).json()
    check=r['message']
    print(check)
    print("\033[1;92m-"*50)
    c=r['data']
    m=c['api_token']
    hd2={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
    url2=("http://app.fogtube.net/api/v1/unsubscribed-campaigns?api_token={}".format(m))
    data2={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
    r123=requests.get(url2,headers=hd2,data=data2).json()
    print(r123)
    k=r123['data']
    Dark=k['id']
    hd12345678={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.fogtube.net"}
    url12345678=("http://app.fogtube.net/api/v1/my-coins?api_token={}".format(m))
    data12345678={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
    r12345678=requests.get(url12345678,headers=hd12345678,data=data12345678).json()
    dog=r12345678['data']
    coin=dog['count_coins']
    print('\033[1;92mSir You Have ==>',coin)
    print("\033[1;92m-"*50)