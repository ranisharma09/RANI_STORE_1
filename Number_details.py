#RANI TRICKER CODING BY 🤙
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
logo = """   _____            _   _ _____ 
 |  __ \     /\   | \ | |_   _|
 | |__) |   /  \  |  \| | | |  
 |  _  /   / /\ \ | . ` | | |  
 | | \ \  / ____ \| |\  |_| |_ 
 |_|  \_\/_/    \_\_| \_|_____| """
print(57*'_')                              
print(logo)
print(57*'_')                               
number=input("Enter Your NUMBER. with: ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number (phone)
car=carrier.name_for_number (phone, "en")
reg=geocoder.description_for_number(phone, "en")
print (phone) 

print(time)

print(car)
print(reg)
