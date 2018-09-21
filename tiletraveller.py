#safe to say, maður byrjar alltaf í 1,1. þannig það fyrsta sem hægt verður að gera er að fara norður, ekkert annað
x = 1
y = 1

while True:
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif x == 2 and y == 2: 
        print("You can travel: (S)outh or (W)est.")
    elif x == 2 and y == 1:
        print("You can travel: (N)orth.")
    elif x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
    elif x == 2 and y == 3: 
        print("You can travel: (E)ast or (W)est.")
    elif x == 3 and y == 3:
        print("You can travel: (S)outh or (W)est.")
    elif x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
    elif x == 3 and y == 1:
        print("Victory!")
        break

    
    
    while True:
        d = input("Direction: ").lower()
        if d == "n":
            if y == 3 or (x == 2 and y == 2):
                print("Not a valid direction!")
            else:
                y += 1
                break

        elif d == "e": #skoða allstaðar þar sem þu getur eki farið austur
            if (y == 1 or x == 3) or (x == 2 and y == 2):
                print("Not a valid direction!")
            else:
                x += 1
                break
        elif d == "s":
            if y == 1 or (x == 2 and y == 3):
                print("Not a valid direction!")
            else:
                y -= 1
                break

        elif d == "w":
            if (x == 1 or y == 1) or (x==3 and y==2):
                print("Not a valid direction!")
            else:
                x -= 1
                break
        
