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

#--------------------Utility Functions-------------------------

def idlist():
    lid=[]
    f=open("csk.csv","r")
    r=csv.reader(f)
    for i in r:
        lid.append(i[0])
    f.close()
    return lid

def DatabyPlayerID(ID):
    f=open("csk.csv","r")
    r=csv.reader(f)
    for i in r:
        if i[0]== ID:
            return i

def ReturnAllData():
    lid=[]
    f=open("csk.csv","r")
    r=csv.reader(f)
    for i in r:
        lid.append(i)
    f.close()
    return lid

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

 #--------------------Verify Functions-------------------------   

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

 #--------------------Main Functions-------------------------   


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
    rco,l)

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





# Modify

def Modify():
    f=open("csk.csv","r",newline='')
    r=csv.reader(f)
    lst = list(r)
    p_id=int(input('Enter the PlayerID to be modified: '))
    ind = 0
    f1 = 0
    for i in lst:
        if i[0]==str(p_id):
            l = []
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
            f1=1
            break
        else:
            ind +=1
    f.close()
    if f1==0:
        print('RECORD NOT FOUND')
        
    else:
        f=open("csk.csv","w",newline="")
        lst.pop(ind)
        lst.insert(ind, l)
        w=csv.writer(f)
        w.writerows(lst)
        f.close()
        print('RECORD CHANGED SUCCESSFULLY')

def Delete():
    f=open("csk.csv","r",newline='')
    r=csv.reader(f)
    f1 = 0
    lst = list(r)
    p_id=int(input('Enter the PlayerID of the record to be Deleted: '))
    ind = 0
    for i in lst:
        if i[0]==str(p_id):
            lst.pop(i)
            f1 = 1
            break
    if f1==0:
        print('RECORD NOT FOUND')
    else:
        f=open("csk.csv","w",newline="")
        w=csv.writer(f)
        w.writerows(lst)
        f.close()
        print("RECORD DELETED SUCCESSFULLY")


# REPORTS>>>>>>>>>>>>.

#--------------------Report 1-------------------------


def isMSD(playingXI): # out of 50
    l = playingXI.keys()
    if "Mahendra Singh Dhoni" in l:
        return True
    else:
        return False

def CalcPercentPForm(formList): # out of 22
    c = 0
    for i in formList:
        if i == "high":
            c+=2
        elif i == "normal":
            c+=1
    return c

def genCappedList(playingXI):
    lst = []
    for i in playingXI:
        l = DatabyPlayerID(i)
        lst.append(l[10])
    return lst

def TotalCappedPlayers(playingXI, cappedP):
    capped
    for i in cappedP:
        if i == "capped":
            capped +=1
    return capped

def CalcPercentCP(totalCP): # out of 28
    percentCP = 0
    if totalCP >=7:
        percentCP += 28
    else:
        percentCP += totalCP / 4
    return percentCP

def CalcCSKWinPercent(playingXI):
    WinPercent = 0
    playingXI, formList = roster()
    if not isMSD(playingXI):
        return WinPercent
    else:
        WinPercent += 50
    cappedP = genCappedList(playingXI)
    totalCP = TotalCappedPlayers(playingXI, cappedP)
    percentCP = CalcPercentCP(totalCP)
    WinPercent += percentCP
    percentForm = CalcPercentPForm(formList)
    WinPercent += percentForm

    return WinPercent


#--------------------Report 2-------------------------


def OrderOutput(ScoreData):
    FinalOutput = dict(sorted(ScoreData.items(), key=lambda item: item[1]))
    return FinalOutput

def CalcDifferenceScore(str_r, bt_avg, eco, bow_avg):
    incF = str_r + bt_avg
    decF = eco + bow_avg
    diffScore = incF - decF
    return diffScore

def OrderFinalReport(FinalOutput):
    PlayerIDs = FinalOutput.keys()
    Data = []
    for i in playingXI:
        l = DatabyPlayerID(i)
        Data.append(l)
    return Data

def CalcPlayerScore(playingXI):
    Data = {}
    for i in playingXI:
        l = DatabyPlayerID(i)
        str_r = i[-4]
        bt_avg = i[-3]
        eco = i[-2]
        bow_avg = i[-1]
        diffScore = CalcDifferenceScore(str_r, bt_avg, eco, bow_avg)
        Data[i[1]] = diffScore
    return Data

def ReportbyPlayerRating(playingXI):
    ScoreData = CalcPlayerScore(playingXI)
    FinalOutput = OrderOutput(ScoreData)
    FinalReport = OrderFinalReport(FinalOutput)
    print(FinalOutput)
    f=open("ReportbyPlayerRating.csv","w",newline="")
    w=csv.writer(f)
    w.writerows(FinalReport)

#--------------------Report 3-------------------------

def GenContryList():
    AllData = ReturnAllData()
    Lst = []
    for i in AllData:
        nation = i[3]
        Lst.append(nation)
    Lst = set(Lst)
    return Lst
def DisplayNationData():
    CountryList = GenContryList()
    AllData = ReturnAllData()
    for i in CountryList:
        print(i+":\n")
        for j in AllData:
            if j[3] == i:
                print("\t"+j[0]+": "+j[1])
    print("---------- The End -----------")

#--------------------Report 4-------------------------
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

#--------------------Report 5-------------------------

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

#------------------Report 6--------------------------

def GenRoleList():
    AllData = ReturnAllData()
    Lst = []
    for i in AllData:
        nation = i[4]
        Lst.append(nation)
    Lst = set(Lst)
    return Lst

def ArrangebyRole():
    AllData = ReturnAllData()
    RoleList = GenRoleList()
    for i in RoleList:
        print(i+":\n")
        for j in AllData:
            if j[4] == i:
                print("\t"+j[0]+": "+j[1])
    print("---------- The End -----------")

# MAIN>>>>>>>>>>>>>>

def Main():
    # while True:
#     i=input("create,add,view, roster,form, report bid amount, report nationality")
#     if i=="a": create()
#     elif i=="b": add()
#     elif i=="c": view()
#     elif i=="d": roster()
#     elif i=="e": update form()
#     elif i=="f": bidsort()
#     elif i=="g": nationsort()
#     else:
#         break
    pass
def if __name__ == '__main__':
    main()