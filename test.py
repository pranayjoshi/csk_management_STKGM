def modify_info():
    f=open("personinfo.csv","r",newline='')
    r=csv.reader(f)
    l = list(r)
    rno=int(input('enter the registration no. to be modified: '))
    for i in l:
        if i[0]==str(rno):
            print('REGISTRATION NUMBER: ',i[0])
            print('NAME: ',i[1])
            print('AGE: ',i[2])
            print('GENDER: ',i[3])
            print('REGISTRATION DATE: ',i[4])
            print('COLLECTED BY: ',i[5])
            print('RECEIVED: ',i[6])
            print('AMOUNT: ',i[7])
            print()
            print('ENTER THE CHANGED VALUES:-')
            nm=input('enter person name: ')
            age=int(input('enter person age: '))
            gen=input('enter person gender(M/F): ')
            rdate=input("enter registration date (dd/mm/yyyy): ")
            coll=input("enter the name of person who collected the blood sample: ")
            time=input('enter at what time blood sample received (00:00 A.M./P.M.): ')
            am=float(input('enter the amount to be paid of blood test report: '))
            i[1]=nm
            i[2]=age
            i[3]=gen
            i[4]=rdate
            i[5]=coll
            i[6]=time
            i[7]=am
            f1=1
        l.append(i)
    f=open("personinfo.csv",'w',newline="\n")
    w=csv.writer(f)
    w.writerows(l)
    f.close()
    if f1==0:
        print('RECORD NOT FOUND')
    else:
        print('RECORD CHANGED SUCCESSFULLY')