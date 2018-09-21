################################|################################
# 1. Technically in this case I found the first implementation  #
#    easier because coding it was straight forward. Although    #
#    in any other cases making functions would make coding      #
#    alot easier.                                               #
# 2. I don't actually find it more readable than the other      #
#    one. The only thing is every function is named in a way    #
#    that you maybe know better what it does, but that could    #
#    be done with comments.                                     #
# 3. Didn't run in any trouble at the first implementation.     #
#    In this implementation I had troubles breaking up the      #
#    while loops, so to fix that I had to make couple of if     #
#    statements to do so.                                       #
#    I am not very proud of that.                               #
################################|################################

def goGo(a, b):
    if (a == 3 and b == 1):
        return False
    else:
        return True

def whereTo(a, b):
    if a == 1 and b == 1:
        print("You can travel: (N)orth.")
    elif a == 1 and b == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif a == 1 and b == 3:
        print("You can travel: (E)ast or (S)outh.")
    elif a == 2 and b == 1:
        print("You can travel: (N)orth.")
    elif a == 2 and b == 2:
        print("You can travel: (S)outh or (W)est.")
    elif a == 2 and b == 3:
        print("You can travel: (E)ast or (W)est.")
    elif a == 3 and b == 1:
        print("Victory!")
        return False
    elif a == 3 and b == 2:
        print("You can travel: (N)orth or (S)outh.")
    elif a == 3 and b == 3:
        print("You can travel: (S)outh or (W)est.")
    else:
        print("What just happened?")
        return False
    return True

def isGo(d, a, b):
    while x <= INT_MAX and y <= INT_MAX:
        if d == 'n':
            if b == INT_MAX or (a == 2 and b == 2):
                print("Not a valid direction!")
                return (d, a, b)
            else:
                b += 1
                break
        elif d == 's':
            if b == INT_MIN or (a == 2 and b == 3):
                print("Not a valid direction!")
                return (d, a, b)
            else:
                b -= 1
                break
        elif d == 'w':
            if a == INT_MIN or (b == INT_MIN or (a == 3 and b == 2)):
                print("Not a valid direction!")
                return (d, a, b)
            else:
                a -= 1
                break
        elif d == 'e':
            if a == INT_MAX or (b == INT_MIN or (a == 2 and b == 2)):
                print("Not a valid direction!")
                return (d, a, b)
            else:
                a += 1
                break
        else:
            print("Not a valid direction!")
            return (d, a, b)
    return (d, a, b)

x, y = 1, 1
X, Y = 1, 1
INT_MIN = 1
INT_MAX = 3

while True:
    whereTo(x, y)
    if not goGo(x, y):
        break
    while goGo(x, y):
        way = input("Direction: ").lower()
        d, x, y = isGo(way, x, y)
        if X == x and Y == y:
            pass
        else:
            X, Y = x, y
            break