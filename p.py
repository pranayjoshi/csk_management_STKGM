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


def DatabyPlayerID(ID):
	f=open("csk.csv","r")
    r=csv.reader(f)
    for i in r:
    	if i[0]== ID:
    		return i

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


