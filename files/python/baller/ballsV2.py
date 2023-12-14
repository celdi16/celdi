#ballsV2
#grist
from turtle import *
from turtle import Screen
from random import randint
import time
import os.path
import tkinter as tk

#global variables
a = 0
b = 0
c = 0
d = 0
x = 0
y = 0
e = 0
f = 0
g = 0
h = 0
radius = 0
data = ""
die = 0
i = 0
j = 0
k = 0
l = 1
m = 0.5
n = 1
count = 0
name = ""
color1 = ""
color2 = ""
egg = ""
existance = ""
real = "no"
answer5 = ""
a1 = 1
b1 = 2
concent = ""
one = 1
shp = ""
jk = ""
p = 0

#gets the screensize
root = tk.Tk()
root.withdraw()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

y = screen_height/ 2
x = screen_width / 2

y = y - 40
x = x - 20

#this is the menu
print("HI, welcome to the balls-inator")
time.sleep(l)
print("this is a project written in python made because i am increadibly bored")
time.sleep(l)
print("this is an upgrade from my previous project balls")
time.sleep(l)
print("anyways lets get started")
time.sleep(l)
name = input("firstly, whats your name?")
time.sleep(l)
if name == "perry":
    print("DOBY DOBY DO BA DOBY DOBY DO BA AGENT P!")
    die = 10
    while die != 0:
        exit()
if name == "speed":
    print("speeding")
    l = 0
    m = 0
    n = 1000000000
if name == "speeds":
    print("speeding")
    l = 0
    m = 0
    n = 1000000000
    name2 = "yee"
    answer6 = input("do you wanna use the easter egg?")
    if answer6 == "yes":
        name = "egg"
print("aww thats a nice name")
time.sleep(l)

#if the answer is yes the programm will attemp to import from a text doc
print("rember to import the data it has to follow the exact format")
time.sleep(l)
print("(you can make the file using the project file writer)")
time.sleep(l)
print("or your gonna get some pretty weird results")
time.sleep(l)
print("there is a .BALLS file that is in the same folder you could use if you wanted called balls")
time.sleep(l)
print("you can use that rather than your own files by coppying the name, anyways")
time.sleep(l)
answer2 = input("what is your .BALLS file called?")
answer2 = answer2 + ".balls"
datainduge = open(answer2,"r")
data = datainduge.read()
text = data.split("\n")
e = int((text[0]))
f = int((text[1]))
g = int((text[2]))
h = int((text[3]))
concent = (text[4])
print ("okay the text file was submitted and read perfectly")
time.sleep(l)
print ("annoyingly...")
    


#creates the values for the variables
a = randint(1,e)
b = randint(1,f)
c = randint(1,g)
d = randint(1,h)
radius = b * 2

#start of the function list

#randomizes balls
def ranball():
    bgcolor(color2)
    pencolor(color1)
    a = randint(1,e)
    a = a*n
    b = randint(1,f)
    c = randint(1,g)
    d = randint(1,h)
    j = randint(-x,x)
    k = randint(-y,y)
    radius = b * 2
    penup()
    goto(j, k)
    pendown()
    
#sets the screensize
def screensize():
    screen = Screen()
    screen.setup(x,y);

#the function balling takes the infomation provided by other tasks and converts it into a "picture"
def balling():
    showturtle()
    left(p)
    speed(a)
    circle(b)
    penup()
    forward(radius)
    pendown()
    circle(b)
    left(180)
    penup()
    right(90)
    forward(radius)
    pendown()
    forward(d)
    circle(b,90)
    right(90)
    forward(c)
    right(180)
    forward(c)
    right(90)
    circle(b,90)
    forward(d)
    left(90)
    hideturtle()

#end of the first functions list

#calls the screensize function
screensize();

#calls the balling function for the first time
balling();

time.sleep(l)
print("so wow that worked, amazing right")
time.sleep(l)

if concent == ("no"):
    print("so thats all you wanted hu??")
    time.sleep(l)
    print("fine.")
    die = 10
    while die != 0:
        exit()

print("so you chose the extended care...")
time.sleep(l)
print("time to go then")
time.sleep(l)

datainduge = open(answer2,"r")
data = datainduge.read()
text = data.split("\n")
i = (text[4])
color1 = (text[5])
color2 = (text[6])

print ("you want to repeat",i,"times right?")
time.sleep(m)
print("I DONT CARE!")
time.sleep(l)
print("let me just make some random positions...")
time.sleep(l)

print("boom we have everything we need now")
time.sleep(l)
print("welcome to balls...")
count = int(1)
i = int(i)
for count in range(0, i):
    bgcolor(color2)
    pencolor(color1)
    a = randint(1,e)
    a = a*n
    b = randint(1,f)
    c = randint(1,g)
    d = randint(1,h)
    j = randint(-x,x)
    k = randint(-y,y)
    radius = b * 2
    penup()
    goto(j, k)
    pendown()
    balling()
    
time.sleep(1)
print("wow, that was fun...")
time.sleep(l)
print("WAIT I DIE NOW!")
time.sleep(l)
print("well... thaks for playing...", name)
time.sleep(l)
print("if im gonna die im gonna do it myself.")
die = 10
if name == "egg":
    egg = (text[7])
    if egg == ("egg"):
        jk = (text[8])
        if jk == ("yes"):
            shp = 360
        time.sleep(1)
        print("wait... you know...")
        time.sleep(l)
        print("thank you.. with this ill never die...")
        time.sleep(l)
        print("[:")
        while die == 10:
            p = randint (0,shp)
            bgcolor(color2)
            pencolor(color1)
            a = randint(1,e)
            a = a*n
            b = randint(1,f)
            c = randint(1,g)
            d = randint(1,h)
            j = randint(-x,x)
            k = randint(-y,y)
            radius = b * 2
            penup()
            goto(j, k)
            pendown()
            balling()
            count = count + 1
while die != 0:
    exit()
