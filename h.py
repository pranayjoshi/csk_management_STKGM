import csv

'''PlayerID: 1
Name: 2
Age: 3
Nationality: 4
Role: 5
Handedness: 6
Health Status: 7
MS Dhoni: 8
Experience: 9
Bid Amount: 10
Cap: 11
Strike Rate: 12
Batting Average: 13
Economy: 14
Bowling Average: 15'''

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

#verifies float
def vfloat(x,l):
    if x in (""," "):
        l.append(None)
    else:
        l.append(float(x))
    return l

#function to return list of capped players
def lcap():
    lcap=[]
    f=open("csk.csv","r")
    r=csv.reader(f)
    next(r,None)
    for i in r:
        if i[10]=="capped":
            lcap.append(i[0])
    return lcap

#function to enter player data
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
        p_id=input(ask)
        ver=vstr(p_id) and vint(p_id) and vplayerID(p_id,lid)
        ask="Enter PlayerID correctly: "
    p_id=int(p_id)
    l.insert(0,p_id)

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
    ba=float(ba)
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

#Function to view all players
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

#function to ask user for the playing 11 team
def roster():
    l=[]
    lrole=[]
    ver=False
    f=open("csk.csv","r")
    r=csv.reader(f)
    next(r,None)
#print players' info to help user choose playing 11
    for i in r:
        l.append(i)
        print("ID:",i[0],",Name:",i[1],",Role:",i[4],",Nationality:",i[3])
    while not ver:
        XI=input("Enter player IDs of the playing XI: ")
        XI=XI.split()
        foreign=0
        for i in XI:
            for j in l:
                if i==j[0]:
                    lrole.append(j[4])
                    if j[3].lower() != "india":
                        foreign+=1
                    break
#check there is atleast 1 wk, 5 bowlers and atmmost 4 foreigners
        if foreign>4:
            print("PlayingXI has too many overseas players")
        elif lrole.count("wicket keeper")<1:
            print("Atleast choose 1 wicketkeeper")
        elif lrole.count("bowler")+lrole.count("all rounder")<5:
            print("Atleast 5 players should be able to bowl")
        else:
            ver=True
    print("PlayingXI is complete")
    askform()

#take players' form
def askform():
    ver=False
    while not ver:
        form=input("Enter the form in which each playingXI player is (h=high,n=normal,l=low) ")
        form=form.split()
        if len(form)==11:
            for i in form:
                if len(i)!=1:
                    print("Enter h,m,l only")
                    ver=False
                else: ver=True
        else:
            print("Give only 11 values")
    return XI,form

#Report to sort players by bidding amount
def bidsort():
    with open("csk.csv","r") as f:
        r=csv.reader(f)
        next(r,None)
        lbid=[]
        ltemp=[]
        for i in r:
            ltemp=[]
            ltemp.append(int(i[9]))
            ltemp.append(i[1])
            ltemp.append(i[0])
            lbid.append(ltemp)
        lbid=sorted(lbid,reverse=True)
        for i in lbid:
            print("ID: ",i[2],", Name: ",i[1],", Bid amount: ",i[0])

#Report to sort by nationality
def nationsort():
    a=""
    with open("csk.csv","r") as f:
        r=csv.reader(f)
        next(r,None)
        lnat=[]
        dnat={}
        ltemp=[]
        for i in r:
            ltemp=[]
            ltemp.append(i[3])
            ltemp.append(i[1])
            ltemp.append(i[0])
            lnat.append(ltemp)
        lnat=sorted(lnat)
        for i in lnat:
            print("ID: ",i[2],", Name: ",i[1],", Nationality: ",i[0])
            dnat[i[0]]=lnat.count(i[0])
        print(dnat)

while True:
    i=input("create,add,view, roster,form, report bid amount, report nationality")
    if i=="a": create()
    elif i=="b": add()
    elif i=="c": view()
    elif i=="d": roster()
    elif i=="e": update form()
    elif i=="f": bidsort()
    elif i=="g": nationsort()
    else:
        break


