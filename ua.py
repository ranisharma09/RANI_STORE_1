#coding by raNi TRIXCKER 
#fb Id'z https://www.facebook.com/mistyxd0.2

# https://youtube.com/channel/UCbT--Z1XzQpSUgjD6bfzzUA

#coding=utf


P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 


import os
try:
    import my_fake_useragent
except ImportError:
    print('\n [✓] installing pip wait !...\n')
    os.system('pip install my_fake_useragent')
from my_fake_useragent import UserAgent
import random
logo = """  \x1b[1;97m
\033[1;32m  _____            _   _ _____ 
 |  __ \     /\   | \ | |_   _|
 | |__) |   /  \  |  \| | | |  
 |  _  /   / /\ \ | . ` | | |  
 | | \ \  / ____ \| |\  |_| |_ 
 |_|  \_\/_/    \_\_| \_|_____|
 
 RANI TRIXCKER 
 """
                               
                               
x = UserAgent(family='edge')
b1 =x.random()
b2 = x.random()
b3 = x.random()
b4 = x.random()
b5= x.random()
b6 = x.random()
b7 = x.random()
b8 = x.random()
b10 = x.random()
  
#randomly printing any 5 useragent
os.system('clear') 
print(logo)

print ('user agent save > chrome-ua.txt')
print ('\x1b[1;97m')
print(b1)
print('')
print(b2)
print('')
print(b3)
print('')
print(b4)
print('')
print(b5)
print('')
print(b6)
print('')
print(b7)
print('')
print(b8)
print('')
#print(b9)
print('')
print(b10)
print('')



open("edge-ua.txt","a").write(b1+'\n')
open ("edge-ua.txt","a").write(b2+'\n')
open ("edge-ua.txt","a").write(b3+'\n')
open ("edge-ua.txt","a").write(b4+'\n')
open ("edge-ua.txt","a").write(b5+'\n')
open ("edge-ua.txt","a").write(b6+'\n')
open ("edge-ua.txt","a").write(b7+'\n')
open ("edge-ua.txt","a").write(b8+'\n')
#open ("edge-ua.txt","a").write(b9+'\n')
open ("edge-ua.txt","a").write(b10+'\n')