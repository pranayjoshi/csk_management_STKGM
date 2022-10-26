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

#Report 1

def isMSD():
	pass
def totalMainRoasterPlayers():
	pass
def TotalCappedPlayers():
	pass
def CSKWinPercent(playingXI):
	pass

