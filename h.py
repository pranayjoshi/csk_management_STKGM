import csv

def create():
    f=open("csk.csv","w",newline="")
    w=csv.writer(f)
    head=("Name","Age","Nationality","Role","Handedness","Health Status","MS Dhoni","Experience","Bid Amount","Cap","Strike Rate","Batting Average","Economy","Bowling Average")
    w.writerow(head)
    f.close()

def vstr(x):
    x= list(x)
    if len(x)==0 or x[0]==" ":
        return False
    else: return True

def vint(x):
    for i in x:
        if not i.isdigit():
            return False
        else: return True

def vrole(x):
    if x.lower() not in ("batsman","bowler","all rounder","wicket keeper","wk"):
        return False
    else: return True

def vhand(x):
    if x.lower() not in ("right","left","r","l"):
        return False
    else: return True

def vhs(x):
    if x.lower() not in ("fit","unfit"):
        return False
    else: return True

def vcu(x):
    if x.lower() not in ("capped","uncapped","cap","uncap","c","u"):
        return False
    else: return True

def vsr(x):
    if x not in (" ",""):
        for i in x:
            if not i.isdigit():
                return False
            else:
                return True
    else: return True

def vfloat(x,l):
    if x in (""," "):
        l.append(None)
    else:
        l.append(float(x))
    return l

def add():
    l=[]
    ver=False
    ask="Enter name of the player: "
    while not ver:
        nm=input(ask)
        ver=vstr(nm)
        ask="Enter name correctly: "
    l.append(nm)

    ver=False
    ask="Enter age of the player: "
    while not ver:
        age=input(ask)
        ver=vstr(age)
        ver=vint(age)
        ask="Enter age correctly: "
    age=int(age)
    l.append(age)

    ver=False
    ask="Enter nationality of the player: "
    while not ver:
        nat=input(ask)
        ver=vstr(nat)
        ask="Enter nationality correctly: "
    l.append(nat)

    ver=False
    ask="Enter role of the player: "
    while not ver:
        role=input(ask)
        ver=vrole(role)
        ask="Enter role correctly: "
    if role.lower()=="wk": l.append("wicket keeper")
    else: l.append(role)

    ver=False
    ask="Enter handedness of the player: "
    while not ver:
        hand=input(ask)
        ver=vhand(hand)
        ask="Enter handedness correctly: "
    if hand[0]=="r": l.append("right")
    else: l.append("left")

    ver=False
    ask="Enter health status of the player: "
    while not ver:
        hs=input(ask)
        ver=vhs(hs)
        ask="Enter health status correctly: "
    l.append(hs)

    if l[0].lower() in ("ms dhoni","mahendra singh dhoni","dhoni","mahendra dhoni","mahi"):
        l.append("Yes")
    else:
        l.append("No")

    ver=False
    ask="Enter experience (no of years) of the player: "
    while not ver:
        exp=input(ask)
        ver=vstr(exp)
        ver=vint(exp)
        ask="Enter experience correctly: "
    exp=int(exp)
    l.append(exp)

    ver=False
    ask="Enter bid amount of the player in crore(s): "
    while not ver:
        ba=input(ask)
        ver=vstr(ba)
        ver=vint(ba)
        ask="Enter bid amount correctly: "
    ba=int(ba)
    l.append(ba)

    ver=False
    ask="Is the player capped or uncapped?: "
    while not ver:
        cu=input(ask)
        ver=vcu(cu)
        ask="Enter capped or uncapped only: "
    if cu[0].lower()=="c":
        l.append("capped")
    else: l.append("uncapped")

    ver=False
    ask="Enter strike rate of the player: "
    while not ver:
        sr=input(ask)
        ver=vsr(sr)
        ask="Enter bid amount correctly: "
    l=vfloat(sr,l)

    ver=False
    ask="Enter Batting Average of the player: "
    while not ver:
        baa=input(ask)
        ver=vsr(baa)
        ask="Enter Economy correctly: "
    l=vfloat(baa,l)

    ver=False
    ask="Enter Economy of the player: "
    while not ver:
        eco=input(ask)
        ver=vsr(eco)
        ask="Enter Economy correctly: "
    l=vfloat(eco,l)

    ver=False
    ask="Enter Bowling Average of the player: "
    while not ver:
        bwa=input(ask)
        ver=vsr(bwa)
        ask="Enter Bowling Average correctly: "
    l=vfloat(bwa,l)

    print(l)
    f=open("csk.csv","a",newline="")
    w=csv.writer(f)
    w.writerow(l)

create()
l=add()


