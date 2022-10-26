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
    if x.lower() not in ("right","left"):
        return False
    else: return True

def vhs(x):
    if x.lower() not in ("fit","unfit"):
        return False
    else: return True

def vrr(x):
    if x.lower() not in ("reserve","roster"):
        return False
    else: return True

def vcu(x):
    if x.lower() not in ("capped","uncapped"):
        return False
    else: return True

def vsr(x):


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
    l.append(role)

    ver=False
    ask="Enter handedness of the player: "
    while not ver:
        hand=input(ask)
        ver=vhand(hand)
        ask="Enter handedness correctly: "
    l.append(hand)

    ver=False
    ask="Enter health status of the player: "
    while not ver:
        hs=input(ask)
        ver=vhs(hs)
        ask="Enter health status correctly: "
    l.append(hs)

    ver=False
    ask="Enter experience (no of years) of the player: "
    while not ver:
        exp=input(ask)
        ver=vstr(exp)
        ver=vint(exp)
        ask="Enter experience correctly: "
    age=int(exp)
    l.append(exp)

    ver=False
    ask="Enter bid amount of the player in crore(s): "
    while not ver:
        ba=input(ask)
        ver=vstr(ba)
        ver=vint(ba)
        ask="Enter bid amount correctly: "
    age=int(ba)
    l.append(ba)

    ver=False
    ask="Is the player in roster or in reserve?: "
    while not ver:
        rr=input(ask)
        ver=vrr(rr)
        ask="Enter roster or reserve only: "
    l.append(rr)

    ver=False
    ask="Is the player capped or uncapped?: "
    while not ver:
        cu=input(ask)
        ver=vcu(cu)
        ask="Enter capped or uncapped only: "
    l.append(cu)

    ver=False
    ask="Enter strike rate of the player: "
    while not ver:
        sr=input(ask)
        ver=vsr(sr)
        ask="Enter bid amount correctly: "
    age=int(sr)
    l.append(sr)

    return l

l=add()
print(l)


