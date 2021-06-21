# Numer0n

import random
import numpy as np

def eat_bite(x,y,z,w,a,b,c,d):
    global eat
    eat = 0
    if x == a:
        eat += 1
    if y == b:
        eat += 1
    if z == c:
        eat += 1
    if w == d:
        eat += 1
    global bite
    bite = 0
    if y == a or z == a or w == a:
        bite += 1
    if z == b or w == b or x == b:
        bite += 1
    if w == c or x == c or y == c:
        bite += 1
    if x == d or y == d or z == d:
        bite += 1
        
def my_eat_bite(x,y,z,w,a,b,c,d):
    global my_eat
    my_eat = 0
    if x == a:
        my_eat += 1
    if y == b:
        my_eat += 1
    if z == c:
        my_eat += 1
    if w == d:
        my_eat += 1
    global my_bite
    my_bite = 0
    if y == a or z == a or w == a:
        my_bite += 1
    if z == b or w == b or x == b:
        my_bite += 1
    if w == c or x == c or y == c:
        my_bite += 1
    if x == d or y == d or z == d:
        my_bite += 1
        
'''def your_eat_bite(x,y,z,w,a,b,c,d):
    global your_eat
    your_eat = 0
    if x == a:
        your_eat += 1
    if y == b:
        your_eat += 1
    if z == c:
        your_eat += 1
    if w == d:
        your_eat += 1
    global your_bite
    your_bite = 0
    if y == a or z == a or w == a:
        your_bite += 1
    if z == b or w == b or x == b:
        your_bite += 1
    if w == c or x == c or y == c:
        your_bite += 1
    if x == d or y == d or z == d:
        your_bite += 1'''
    
def ope_00(x,y,z,w):
    global s_00
    s_00 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 0 and bite == 0:
                            s_00.append(str(a) + str(b) + str(c) + str(d))

def ope_01(x,y,z,w):
    global s_01
    s_01 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 0 and bite == 1:
                            s_01.append(str(a) + str(b) + str(c) + str(d))
                        
def ope_02(x,y,z,w):
    global s_02
    s_02 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 0 and bite == 2:
                            s_02.append(str(a) + str(b) + str(c) + str(d))
                        
def ope_03(x,y,z,w):
    global s_03
    s_03 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 0 and bite == 3:
                            s_03.append(str(a) + str(b) + str(c) + str(d))
                        
def ope_04(x,y,z,w):
    global s_04
    s_04 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 0 and bite == 4:
                            s_04.append(str(a) + str(b) + str(c) + str(d))
                        
def ope_10(x,y,z,w):
    global s_10
    s_10 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 1 and bite == 0:
                            s_10.append(str(a) + str(b) + str(c) + str(d))
                        
def ope_11(x,y,z,w):
    global s_11
    s_11 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 1 and bite == 1:
                            s_11.append(str(a) + str(b) + str(c) + str(d))
                        
def ope_12(x,y,z,w):
    global s_12
    s_12 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 1 and bite == 2:
                            s_12.append(str(a) + str(b) + str(c) + str(d))
                        
def ope_13(x,y,z,w):
    global s_13
    s_13 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 1 and bite == 3:
                            s_13.append(str(a) + str(b) + str(c) + str(d))
                        
def ope_20(x,y,z,w):
    global s_20
    s_20 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 2 and bite == 0:
                            s_20.append(str(a) + str(b) + str(c) + str(d))
                        
def ope_21(x,y,z,w):
    global s_21
    s_21 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 2 and bite == 1:
                            s_21.append(str(a) + str(b) + str(c) + str(d))
                        
def ope_22(x,y,z,w):
    global s_22
    s_22 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 2 and bite == 2:
                            s_22.append(str(a) + str(b) + str(c) + str(d))
                        
def ope_30(x,y,z,w):
    global s_30
    s_30 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        eat_bite(x,y,z,w,a,b,c,d)
                        if eat == 3 and bite == 0:
                            s_30.append(str(a) + str(b) + str(c) + str(d))
                            
def ope_40(x,y,z,w):
    global s_40
    s_40 = [str(x) + str(y) + str(z) + str(w)]
                            
def det(x,y,z,w,et,bt):
    global t
    t = []
    ope_00(x,y,z,w)
    ope_01(x,y,z,w)
    ope_02(x,y,z,w)
    ope_03(x,y,z,w)
    ope_04(x,y,z,w)
    ope_10(x,y,z,w)
    ope_11(x,y,z,w)
    ope_12(x,y,z,w)
    ope_13(x,y,z,w)
    ope_20(x,y,z,w)
    ope_21(x,y,z,w)
    ope_22(x,y,z,w)
    ope_30(x,y,z,w)
    ope_40(x,y,z,w)
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        e = str(a) + str(b) + str(c) + str(d)
                        if (et,bt) == (0,0) and e in s_00:
                            t.append([e,1])
                        elif (et,bt) == (0,1) and e in s_01:
                            t.append([e,1])
                        elif (et,bt) == (0,2) and e in s_02:
                            t.append([e,1])
                        elif (et,bt) == (0,3) and e in s_03:
                            t.append([e,1])
                        elif (et,bt) == (0,4) and e in s_04:
                            t.append([e,1])
                        elif (et,bt) == (1,0) and e in s_10:
                            t.append([e,1])
                        elif (et,bt) == (1,1) and e in s_11:
                            t.append([e,1])
                        elif (et,bt) == (1,2) and e in s_12:
                            t.append([e,1])
                        elif (et,bt) == (1,3) and e in s_13:
                            t.append([e,1])
                        elif (et,bt) == (2,0) and e in s_20:
                            t.append([e,1])
                        elif (et,bt) == (2,1) and e in s_21:
                            t.append([e,1])
                        elif (et,bt) == (2,2) and e in s_22:
                            t.append([e,1])
                        elif (et,bt) == (3,0) and e in s_30:
                            t.append([e,1])
                        elif (et,bt) == (4,0) and e in s_40:
                            t.append([e,1])
                        else:t.append([e,0])

def difense():
    global call
    call = input('call:')
    if call in u1:
        call_1 = int(int(call) % 10)
        call_10 = int(((int(call) - call_1) / 10) % 10)
        call_100 = int(((int(call) - call_10 - call_1) / 100) % 10)         
        call_1000 = int((int(call) - call_100 - call_10 - call_1) / 1000)
        my_eat_bite(call_1000,call_100,call_10,call_1,my_1000,my_100,my_10,my_1)

def attack():
    global digit1000
    global digit100
    global digit10
    global digit1
    global v
    global w
    youreat = input('____________________eat:')
    yourbite = input('____________________bite:')
    if (youreat,yourbite) in u2 + [('4','0')]:
        global your_eat
        your_eat = int(youreat)
        global your_bite
        your_bite = int(yourbite)
    elif youreat == 'stop' or yourbite == 'stop':
        (your_eat,your_bite) = (5,5)
    else:
        (your_eat,your_bite) = (6,6)
    if (your_eat,your_bite) in u3 + [(4,0)]:
        det(digit1000,digit100,digit10,digit1,your_eat,your_bite)
        if v == []:
            w = []
            for i in range(0,len(t)):
                 v.append(t[i])
            for i in range(0,len(v)):
                if v[i][1] == 1:
                    w.append(v[i][0])
        else:
            w = []
            for i in range(0,len(v)):
                v[i][1] *= t[i][1] 
            for i in range(0,len(v)):
                if v[i][1] == 1:
                    w.append(v[i][0])
        if w != []:
            war = np.array(w)
            random.shuffle(war)
            digit1 = int(int(war[0]) % 10)
            digit10 = int(((int(war[0]) - digit1) / 10) % 10)
            digit100 = int(((int(war[0]) - digit10 - digit1) / 100) % 10)            
            digit1000 = int((int(war[0]) - digit100 - digit10 - digit1) / 1000)
        else:
            digit1 = 0
            digit10 = 0
            digit100 = 0      
            digit1000 = 0

def numer0n():
    dar = np.array([0,1,2,3,4,5,6,7,8,9])
    random.shuffle(dar)
    global my_1000
    my_1000 = dar[0]
    global my_100
    my_100 = dar[1]
    global my_10
    my_10 = dar[2]
    global my_1
    my_1 = dar[3]
    my_number = str(my_1000) + str(my_100) + str(my_10) + str(my_1)
    aar = np.array([0,1,2,3,4,5,6,7,8,9])
    random.shuffle(aar)
    global digit1000
    digit1000 = aar[0]
    global digit100
    digit100 = aar[1]
    global digit10
    digit10 = aar[2]
    global digit1
    digit1 = aar[3]
    global v
    v = []
    global w
    w = []
    global my_eat
    my_eat = 5
    global my_bite
    my_bite = 5
    global your_eat
    global your_bite
    global u1
    u1 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        e = str(a) + str(b) + str(c) + str(d)
                        u1.append(e)
    global u2
    u2 = []
    for i in range(0,5):
        for j in range(0,5):
            if i + j <= 4:
                u2.append((str(i),str(j)))
    u2.remove(('3','1'))
    u2.remove(('4','0'))
    global u3
    u3 = []
    for i in range(0,5):
        for j in range(0,5):
            if i + j <= 4:
                u3.append((i,j))
    u3.remove((3,1))
    u3.remove((4,0))
    while True:
        difense()
        if call in u1 and (my_eat,my_bite) == (4,0):
            print('YOU WIN!')
            break
        elif call == 'stop':
            print('THANK YOU FOR PLAYING!')
            break
        elif call in u1 and (my_eat,my_bite) != (4,0):
            print(str(my_eat) + 'eat_' + str(my_bite) + 'bite')
            while True:
                print('____________________' + str(digit1000) + str(digit100) + str(digit10) + str(digit1))
                attack()
                if (your_eat,your_bite) in u3 + [(4,0),(5,5)]:
                    break
                else:
                    continue
            if (your_eat,your_bite) == (4,0):
                print('I WIN!')
                break
            elif (your_eat,your_bite) == (5,5):
                print('THANK YOU FOR PLAYING!')
                break
            elif str(digit1000) + str(digit100) + str(digit10) + str(digit1) == '0000':
                print('YOU HAVE MISTAKEN!')
                break
        else:
            continue

def difense_first():
    dar = np.array([0,1,2,3,4,5,6,7,8,9])
    random.shuffle(dar)
    global my_1000
    my_1000 = dar[0]
    global my_100
    my_100 = dar[1]
    global my_10
    my_10 = dar[2]
    global my_1
    my_1 = dar[3]
    my_number = str(my_1000) + str(my_100) + str(my_10) + str(my_1)
    aar = np.array([0,1,2,3,4,5,6,7,8,9])
    random.shuffle(aar)
    global digit1000
    digit1000 = aar[0]
    global digit100
    digit100 = aar[1]
    global digit10
    digit10 = aar[2]
    global digit1
    digit1 = aar[3]
    global v
    v = []
    global w
    w = []
    global my_eat
    my_eat = 5
    global my_bite
    my_bite = 5
    global your_eat
    global your_bite
    global u1
    u1 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        e = str(a) + str(b) + str(c) + str(d)
                        u1.append(e)
    global u2
    u2 = []
    for i in range(0,5):
        for j in range(0,5):
            if i + j <= 4:
                u2.append((str(i),str(j)))
    u2.remove(('3','1'))
    u2.remove(('4','0'))
    global u3
    u3 = []
    for i in range(0,5):
        for j in range(0,5):
            if i + j <= 4:
                u3.append((i,j))
    u3.remove((3,1))
    u3.remove((4,0))
    while True:
        difense()
        if call in u1 and (my_eat,my_bite) == (4,0):
            print('YOU WIN!')
            break
        elif call == 'stop':
            print('THANK YOU FOR PLAYING!')
            break
        elif call in u1 and (my_eat,my_bite) != (4,0):
            print(str(my_eat) + 'eat_' + str(my_bite) + 'bite')
            while True:
                print('____________________' + str(digit1000) + str(digit100) + str(digit10) + str(digit1))
                attack()
                if (your_eat,your_bite) in u3 + [(4,0),(5,5)]:
                    break
                else:
                    continue
            if (your_eat,your_bite) == (4,0):
                print('I WIN!')
                break
            elif (your_eat,your_bite) == (5,5):
                print('THANK YOU FOR PLAYING!')
                break
            elif str(digit1000) + str(digit100) + str(digit10) + str(digit1) == '0000':
                print('YOU HAVE MISTAKEN!')
                break
        else:
            continue
    if (your_eat,your_bite) == (4,0):
        while True:
            choice = input('0:stop 1:continue ')
            if choice == '0':
                break
            elif choice == '1':
                while (my_eat,my_bite) != (4,0):
                    difense()
                    if (my_eat,my_bite) != (4,0):
                        print(str(my_eat) + 'eat_' + str(my_bite) + 'bite')
                    elif (my_eat,my_bite) == (4,0):
                        print('YOU ARE RIGHT! MY NUMBER IS ' + my_number + ' !')
                        break
                    elif my_eat == 'stop' or my_bite == 'stop':
                        break
                break
            else:
                continue

def attack_first():
    dar = np.array([0,1,2,3,4,5,6,7,8,9])
    random.shuffle(dar)
    global my_1000
    my_1000 = dar[0]
    global my_100
    my_100 = dar[1]
    global my_10
    my_10 = dar[2]
    global my_1
    my_1 = dar[3]
    my_number = str(my_1000) + str(my_100) + str(my_10) + str(my_1)
    aar = np.array([0,1,2,3,4,5,6,7,8,9])
    random.shuffle(aar)
    global digit1000
    digit1000 = aar[0]
    global digit100
    digit100 = aar[1]
    global digit10
    digit10 = aar[2]
    global digit1
    digit1 = aar[3]
    global v
    v = []
    global w
    w = []
    global my_eat
    my_eat = 5
    global my_bite
    my_bite = 5
    global your_eat
    global your_bite
    global u1
    u1 = []
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a != b and a != c and a != d and b != c and b != d and c != d:
                        e = str(a) + str(b) + str(c) + str(d)
                        u1.append(e)
    global u2
    u2 = []
    for i in range(0,5):
        for j in range(0,5):
            if i + j <= 4:
                u2.append((str(i),str(j)))
    u2.remove(('3','1'))
    u2.remove(('4','0'))
    global u3
    u3 = []
    for i in range(0,5):
        for j in range(0,5):
            if i + j <= 4:
                u3.append((i,j))
    u3.remove((3,1))
    u3.remove((4,0))
    while True:
        print('____________________' + str(digit1000) + str(digit100) + str(digit10) + str(digit1))
        attack()
        if (your_eat,your_bite) == (4,0):
            print('I WIN!')
            break
        elif (your_eat,your_bite) == (5,5):
            print('THANK YOU FOR PLAYING!')
            break
        elif str(digit1000) + str(digit100) + str(digit10) + str(digit1) == '0000':
            print('YOU HAVE MISTAKEN!')
            break
        elif (your_eat,your_bite) in u3:
            while True:
                difense()
                if call in u1 and (my_eat,my_bite) == (4,0):
                    break
                elif call == 'stop':
                    break
                elif call in u1 and (my_eat,my_bite) != (4,0):
                    print(str(my_eat) + 'eat_' + str(my_bite) + 'bite')
                    break
                else:
                    continue
            if (my_eat,my_bite) == (4,0):
                print('YOU WIN!')
                break
            elif (my_eat,my_bite) == (5,5):
                print('THANK YOU FOR PLAYING!')
                break
        else:
            continue
    if (your_eat,your_bite) == (4,0):
        while True:
            choice = input('0:stop 1:continue __________')
            if choice == '0':
                print('THANK YOU FOR PLAYING!')
                break
            elif choice == '1':
                while (my_eat,my_bite) != (4,0):
                    difense()
                    if (my_eat,my_bite) != (4,0):
                        print(str(my_eat) + 'eat_' + str(my_bite) + 'bite')
                    elif (my_eat,my_bite) == (4,0):
                        print('YOU ARE RIGHT! MY NUMBER IS ' + my_number + ' !')
                        break
                    elif my_eat == 'stop' or my_bite == 'stop':
                        break
                break
            else:
                continue

def numer0n_order():
    while True:
        order = input('0:YOU FIRST 1:I FIRST 2:RANDOM __________')
        if order == '2':
            oar = ('0','1')
            order = random.choice(oar)
            if order == '0':
                print('YOU CALL FIRST!')
            elif order == '1':
                print('I CALL FIRST!')
        if order == '0':
            difense_first()
            break
        elif order == '1':
            attack_first()
            break
        else:
            continue

if __name__ == "__main__":
    numer0n_order()