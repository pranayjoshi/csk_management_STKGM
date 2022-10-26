import csv

def create():
    f=open("csk.csv","w",newline="")
    w=csv.writer(f)
    head=("PlayerID","Name","Age","Nationality","Role","Handedness","Health Status","MS Dhoni","Experience","Bid Amount","Cap","Strike Rate","Batting Average","Economy","Bowling Average")
    w.writerow(head)
    f.close()

def idlist():
    lid=[]
    f=open("csk.csv","r")
    r=csv.reader(f)
    for i in r:
        lid.append(i[0])
    f.close()
    return lid

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

def vplayerID(x,lid):
    s=True
    for i in lid:
        if i==x:
            s=False
            break
    return s

def vrole(x):
    if x.lower() not in ("batsman","bowler","all rounder","wicket keeper","wk"):
        return Falsea
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

def lcap():
    lcap=[]
    f=open("csk.csv","r")
    r=csv.reader(f)
    next(r,None)
    for i in r:
        if i[10]="capped":
            lcap.append(i[0])
    return lcap

def add():
    lid=idlist()
    l=[]
    ver=False
    ask="Enter name of the player: "
    while not ver:
        nm=input(ask)
        ver=vstr(nm)
        ask="Enter name correctly: "
    l.append(nm)

    ver=False
    ask="Enter PlayerID of the player: "
    while not ver:
        pid=input(ask)
        ver=vstr(pid)
        ver=vint(pid)
        ver=vplayerID(pid,lid)
        ask="Enter PlayerID correctly: "
    pid=int(pid)
    l.insert(0,pid)

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

    if l[1].lower() in ("ms dhoni","mahendra singh dhoni","dhoni","mahendra dhoni","mahi"):
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
    f=open("csk.csv","a+",newline="")
    w=csv.writer(f)
    w.writerow(l)
    f.seek(0)
    lid=[]
    r=csv.reader(f)
    for i in r:
        lid.append(i[0])
    return l,lid

def view():
    lid=idlist()
    f=open("csk.csv","r")
    r=csv.reader(f)
    for i in r:
        print(i)

    ver=True
    ask="Enter player id "
    while ver:
        choice=input(ask)
        ask="Enter correctly "
        if choice in lid:
            break
    with open("csk.csv","r") as f:
        r=csv.reader(f)
        for i in r:
            if i[0]==choice or i[0]=="PlayerID":
                print(i)

def roster():
    l=lrole=[]
    ver=False
    f=open("csk.csv","r")
    r=csv.reader(f)
    next(r,None)
    for i in r:
        l.append(i)
        prinnt("ID: ",i[0],", Name: ",i[1],end="")
    while not ver:
        for i in range(11):
            XI=input("Enter player IDs of the playing XI: ")
        XI=XI.split()
        foreign=0
        for i in XI:
            for j in l:
                if i==j[0]:
                    lrole.append(j[4])
                    if j[3].lower != "india":
                        foreign+=1
                    break
        if foreign>4:
            print("PlayingXI has too many overseas players")
        elif l.count("wk")<1:
            print("Atleast choose 1 wicketkeeper")
        elif l.count("bowler")+l.count("all rounder")<5:
            print("Atleast 5 players should be able to bowl")
        else:
            ver=True
    print("PlayingXI is complete")
    form=input("Enter the form in which each playingXI player is (h=high,n=normal,l=low) without spaces ")
    form=list(form)
    return XI,form


while True:
    i=input("create,add,view")
    if i=="a": create()
    elif i=="b": add()
    elif i=="c": view()
    else:
        break


