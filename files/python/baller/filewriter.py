#file writer
#grist
from turtle import *
from turtle import Screen
from random import randint
import time
import os.path

#plain old veriables
a = ""
b = ""
x = 0
y = 0
e = 0
f = 0
g = 0
h = 0
jk = 0
color1 = ""
color2 = ""
existance = ""
a1 = 1
b1 = 2
answer5 = ""
answer6 = ""

#menu begin
print("this script writes the .BALLS files")
time.sleep(1)
print("these are used from the ballsV2 script")
time.sleep(1)
answer6 = input("would you like the extended file use? yes/no")
print("alrighty then!")
time.sleep(1)

e = int(input("what limit would you like for the speed?"))
f = int(input("what limit would you like for the radius?"))
g = int(input("what limit would you like for the tip?"))
h = int(input("what limit would you like for the legnth?"))

def ball_loop():
    print("sorry but that file already eists")
    time.sleep(1)
    answer5 = input("would you like to try again?yes/no")
    if answer5 == ("yes"):
        time.sleep(1)
        print("alrighty then")
    if answer5 == ("no"):
        time.sleep(1)
        print("lets skip this part then")
        a1 = 2

while a1 != 2:
    name1 = input("what would you like the file to be called?")
    name2 = (name1 + ".balls")
    existance = ("false")
    file_exists = os.path.exists(name2)
    if file_exists is True:
        ball_loop();
    else:
        a1 = 2
        e = str(e) + "\n"
        f = str(f) + "\n"
        g = str(g) + "\n"
        h = str(h) + "\n"

if answer6 == ("no"):
    with open(name2, 'w') as l:
        l.write(str(e))
        l.write(str(f))
        l.write(str(g))
        l.write(str(h))
        l.write("no\n")

if answer6 == ("yes"):
    print("so you chose the long way hu?")
    time.sleep(1)
    i = int(input("how many times would you like it to be repeated?"))
    time.sleep(1)
    a = input("what colour would you like the pen to be?")
    time.sleep(1)
    b = input("what colour would you like the background to be?")
    a = str(a) + "\n"
    b = str(b) + "\n"
    i = str(i) + "\n"
    with open(name2, 'w') as l:
        l.write(str(e))
        l.write(str(f))
        l.write(str(g))
        l.write(str(h))
        l.write(str(i))
        l.write(str(a))
        l.write(str(b))

if answer6 == ("egg"):
    print("so you found the easter egg...")
    time.sleep(1)
    i = int(input("how many times would you like it to be repeated"))
    time.sleep(1)
    a = input("what colour would you like the pen to be?")
    time.sleep(1)
    b = input("what colour would you like the background to be?")
    a = str(a) + "\n"
    b = str(b) + "\n"
    i = str(i) + "\n"
    jk = input("would you like spin?yes/no")
    jk = str(jk) + "\n"
    with open(name2, 'w') as l:
        l.write(str(e))
        l.write(str(f))
        l.write(str(g))
        l.write(str(h))
        l.write(str(i))
        l.write(str(a))
        l.write(str(b))
        l.write("egg\n")
        l.write(jk)

print("file succesfully written [:")
