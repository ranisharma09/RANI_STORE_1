# Source Generated with Decompyle++
# File: bexm.pyc (Python 3.10)

import os

try:
    import requests
finally:
    pass

import requests
import os
import re
import bs4
import platform
import sys
import json
import time
import random
import datetime
import subprocess
import threading
import itertools
import base64
import uuid
import zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'Agustus',
    'September',
    'October',
    'November',
    'December']

try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
finally:
    pass

current = None if ValueError else datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m'
M = '\x1b[1;96m'
H = '\x1b[1;94m'
K = '\x1b[1;93m'
B = '\x1b[1;97m'
U = '\x1b[1;97m'
O = '\x1b[1;97m'
N = '\x1b[0m'
my_color = [
    P,
    M,
    H,
    K,
    B,
    U,
    O,
    N]
warna = random.choice(my_color)
data = { }
data2 = { }
(aman, cp, salah) = (0, 0, 0)
ubahP = []
fuck = []
pwBaru = []
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = 'https://lookup-id.com/'
url_mb = 'https://m.facebook.com'
url_ip = 'https://www.httpbin.org/ip'
header_grup = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]' }
bulan_ttl = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'Augustus',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December' }
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def main_apv():
    imt = 'SXB=='
    ak = 'SXB '
    os.system('clear')
    print(logo)
    
    try:
        key1 = open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()
    finally:
        pass

    r1 = None if IOError else requests.get('https://raw.githubusercontent.com/SXB-PRO/Lite/main/Approval.txt').text
    if key1 in r1:
        R()
        return None
    None.system('clear')
    print(logo)
    print('\x1b[1;37m-----------------------------------------')
    print('\x1b[1;94mGIVE ME 350RS FOR APROVAL RIAZ')
    print('\x1b[1;32mYOUR KEY : ' + ak + key1)
    print('Key And Sent Me WP Approvel Your Key ')
    print('\x1b[1;37m-----------------------------------------')
    time.sleep(3.5)
    tks = 'Dear%20Admin,%20Please%20Apporved%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20' + ak + '' + key1
    os.system('am start https://wa.me/+923465435447?text=' + tks)

logo = '\n      \x1b[1;32m██████   █████  ██ ██████  \n      \x1b[1;33m██   ██ ██   ██ ██ ██   ██ \n      \x1b[1;34m██████  ███████ ██ ██   ██ \n      \x1b[1;35m██      ██   ██ ██ ██   ██ \n      \x1b[1;36m██      ██   ██ ██ ██████ \n                           \n\x1b[1;37m-----------------------------------------\n[*] Author  : JUNAID KHAN\n[*] Github  : SXB-PRO\n[*] Version : BOTH\n[*] STATUS  : PAID\n[*] Wp      : 03465435447\n[*]\x1b[1;37m-----------------------------------------'

def R():
    os.system('clear')
    print(logo)
    print('\x1b[1;37m[\x1b[1;31mC\x1b[1;37m] SXB VERSION 0.0.3 \x1b[1;32m[COOKIES]\x1b[1;37m ')
    print('\x1b[1;37m[\x1b[1;31mS\x1b[1;37m] SXB VERSION 0.0.1 \x1b[1;32m[Update]\x1b[1;37m')
    print('\x1b[1;37m-----------------------------------------')
    key = input(' [*] Choose : ')
    print('\x1b[1;37m-----------------------------------------')
    if key in ('',):
        print('\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] Please Select Correct Option')
        exit()
        return None
    if None in ('C', '0C'):
        os.system('python Lite1.py')
        return None
    if None in ('S', '0S'):
        os.system('python Power.py')
        time.sleep(0.5)
        return None

main_apv()
