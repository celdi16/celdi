A = 102400000
B = 0
C ="a"
D = "Yes"
E = 0
name = ""

while B != A:
    C = C + "a"
    B = B + 1

while D == "Yes":
    print(E)
    name = "ball" + str(E) + ".BALLS"
    with open(name,"w") as l:
        l.write(C)
    E = E + 1