import time

answer = ""
a = 0

print("so welcome")
time.sleep(1)
print("thanks for choosing to use our service...")
time.sleep(1)
print("the question is which one.")
time.sleep(1)
print("which one would you like to use?")
time.sleep(1)
print("ballsV2")
time.sleep(1)
print("it uses a .BALLS file to create a randomly generated amount of male genitals across the screen")
time.sleep(2)
print("but where do you get a .BALLS file?")
time.sleep(1)
print("file writer")
time.sleep(1)
print("this script creates the .BALLS files using the user input")
time.sleep(1)
print("all the other scripts are under construction")
time.sleep(1)
answer = input("so what will it be?")
time.sleep(1)

def file_writer():
    if answer == "file writer" or "filewriter":
        question = input("question, would you like to run ballsV2 after this? yes/no")
        time.sleep(1)
        print("okay then...")
        time.sleep(1)
        print('''
 .-.   .                       .         
 |  o  |                    o _|_        
-|- .  | .-.   .  .    ._.--.  |  .-..--.
 |  |  |(.-'    \  \  /  |  |  | (.-'|   
 '-' `-`-`--'    `' `'   '-' `-`-'`--'   
        ''')
        time.sleep(1)
        import filewriter
        time.sleep(1)
        if question == "yes":
            print("welp okay you want ballsV2 next")
            time.sleep(1)
            import ballsV2
        a = 1
    
def ballsV2():
    if answer == "ballsV2" or "ballsv2":
        print('''
             U _____ u _       ____   U  ___ u  __  __  U _____ u      _____   U  ___ u       ____      _      _      _     ____     
 __        __\| ___"|/|"|   U /"___|   \/"_ \/U|' \/ '|u\| ___"|/     |_ " _|   \/"_ \/    U | __")uU  /"\  u |"|    |"|   / __"| u  
  \"\      /"/ |  _|"U | | u \| | u     | | | |\| |\/| |/ |  _|"         | |     | | | |     \|  _ \/ \/ _ \/U | | uU | | u<\___ \/   
 /\ \ /\ / /\ | |___ \| |/__ | |/__.-,_| |_| | | |  | |  | |___        /| |\.-,_| |_| |      | |_) | / ___ \ \| |/__\| |/__u___) |   
U  \ V  V /  U|_____| |_____| \____|\_)-\___/  |_|  |_|  |_____|      u |_|U \_)-\___/       |____/ /_/   \_\ |_____||_____|____/>>  
.-,_\ /\ /_,-.<<   >> //  \\ _// \\      \\   <<,-,,-.   <<   >>      _// \\_     \\        _|| \\_  \\    >> //  \\ //  \\ )(  (__) 
 \_)-'  '-(_/(__) (__|_")("_|__)(__)    (__)   (./  \.) (__) (__)    (__) (__)   (__)      (__) (__)(__)  (__|_")("_|_")("_|__)     
        ''')
        time.sleep(1)
        import ballsV2
        a = 1

while a != 1:
    if answer == ("file writer"):
        a = 1
        file_writer()
    if answer == ("ballsV2"):
        a = 1
        ballsV2()
    if answer != "file writer" or "ballsV2":
        print("hmm, so the answer you gave ran neither of the programmes")
        time.sleep(1)
        print("make sure you use the exact terms as i will give now")
        time.sleep(1)
        print("file writer")
        time.sleep(1)
        print("or")
        time.sleep(1)
        print("ballsV2")

time.sleep(1)
print("well thank you for using this service")
time.sleep(1)
print("i think you [:")
time.sleep(1)
print("rember you can always just use this again")
time.sleep(1)
print("all it takes is one f5")
time.sleep(1)
print("byeeee")
