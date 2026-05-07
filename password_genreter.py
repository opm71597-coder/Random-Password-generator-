from random import choice
strings="qwertyuiopasdfghjklmnbvcxzzxcvbnmkjspqjhdj271243567890(;;##&@_₹()#/)/#::!???*"
num=int(input("enter your passwort lhent :"))
password=""
for i in range(num):
    password+=choice(strings)
print(password)    
    