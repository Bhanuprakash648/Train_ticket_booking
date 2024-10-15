from datetime import *
from calendar import *
from random import *
import os
#class for details of customer and train

class mod2:
    age:int#age
    train:int#select the train in (int)
    seat:int#preference of seating(int)
    CLass:int#select the coach selection
    name:chr#name
    phn:chr#phone number
    AAdhar:chr#AAdhar number
    fcity:chr#From city
    gender:chr#Gender
    Train:chr#Selected train(str)
    dcity:chr#destination city
    Class:chr#Class of(int)
    Seat:chr#seat preference(str)
    start:eval#selecting from city
    dest:int#destnation
    year:str#year
    month:str#month
    date:str#date
    berth:dict#combo of prices and preferences
    li:list#prices of berths
    pnr:str#to generate pnr

#class for payment 
#class for checking validity of the debit/credit card
class mod3:
    card_number:chr#Account holder Card number
    name_of_holder:chr#name of account holder
    cvv:int#cvv
    validity:chr#validity
    yearv:str#validity year
    monthv:str#validity month
    ids:str#to check upi
#class for showing details of seats

class mod4:
    ac_l:list#ac coach seats
    non_acl:list#non_ac coach seats
    sleeper_l:list#sleeper coach seats
    sleeper1A_l:list#sleeper 1A coach seats
    sleeper2A_l:list#sleeper 2A coach seats
    seatn:int#seat
    sleeper3A_l:list#sleeper 3A seats

today_date=date.today()
today_date=datetime.now()
current_time = today_date.strftime("%H:%M:%S")
tdn2=mod4()#obj of node1
tdn1=mod2()#obj of customer details
pm=mod3()#obj of payment
tdn1.berth={}#berth dictionary
tdn2.ac_l=[]#ac coach seats
tdn2.non_acl=[]#non ac coach seats
tdn2.sleeper_l=[]#sleeper coach seats
tdn2.sleeper1A_l=[]#sleeper 1A coach seats
tdn2.sleeper2A_l=[]#sleeper 2A coach seats
tdn2.sleeper3A_l=[]#sleeper 3A coach seats

f4=open("data.txt","a")

def heading():#function for function
     print("*"*80,file=f4)
     print("*"*80)
     print(""*24,"Welcome to TRAIN ticket booking",""*23,file=f4)
     print(""*24,"Welcome to TRAIN ticket booking",""*23)
     print("*"*80)
     print("*"*80,file=f4)
     PNR()
     YEAR()
def PNR():#function for creating pnr number
    tdn1.pnr=""
    pnrl=[]
    pnrl.append(randint(0, 9))
    for i in range(1, 10):
        pnrl.append(randint(0,9))
    for i in pnrl:
        tdn1.pnr+=str(i)
def func():#function for checking the seats
    if os.path.exists(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt"):
        file1=open(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt","r")
        tdn2.ac_l=[]
        tdn2.non_acl=[]
        tdn2.sleeper1A_l=[]
        tdn2.sleeper2A_l=[]
        tdn2.sleeper3A_l=[]
        tdn2.sleeper_l=[]
        f1=file1.read().split("\n")
        file1.close()
        for i in f1[0].split(" "):
            if i.strip():
                tdn2.ac_l.append(int(i))
        for i in f1[1].split(" "):
            if i.strip():
                tdn2.non_acl.append(int(i))
        for i in f1[2].split(" "):
            if i.strip():
                tdn2.sleeper_l.append(int(i))
        for i in f1[3].split(" "):
            if i.strip():
                tdn2.sleeper1A_l.append(int(i))
        for i in f1[4].split(" "):
            if i.strip():
                tdn2.sleeper2A_l.append(int(i))
        for i in f1[5].split(" "):
            if i.strip():
                tdn2.sleeper3A_l.append(int(i))

        if tdn1.Class=="CHAIR CAR":
            if tdn2.seatn in tdn2.non_acl:
                tdn2.non_acl.remove(tdn2.seatn)
                flag=1
            else:
                flag=0
        if tdn1.Class=="A/C CHAIR CAR":
            if tdn2.seatn in tdn2.ac_l:
                tdn2.ac_l.remove(tdn2.seatn)
                flag=1
            else:
                flag= 0
        if tdn1.Class=="A/C SLEEPER 1A":
            if tdn2.seatn in tdn2.sleeper1A_l:
                tdn2.sleeper1A_l.remove(tdn2.seatn)
                flag= 1
            else:
                flag= 0
        if tdn1.Class=="A/C SLEEPER 2A":
            if tdn2.seatn in tdn2.sleeper2A_l:
                tdn2.sleeper2A_l.remove(tdn2.seatn)
                flag= 1
            else:
                flag= 0
        if tdn1.Class=="A/C SLEEPER 3A":
            if tdn2.seatn in tdn2.sleeper3A_l:
                tdn2.sleeper3A_l.remove(tdn2.seatn)
                flag= 1
            else:
                flag= 0
        if tdn1.Class=="SLEEPER":
            if tdn2.seatn in tdn2.sleeper_l:
                tdn2.sleeper_l.remove(tdn2.seatn)
                flag= 1
            else:
                flag= 0
        f=open(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt","w")
        for i in tdn2.ac_l:
            f.write(str(i))
            f.write(" ")
        f.write("\n")
        for i in tdn2.non_acl:
            f.write(str(i))
            f.write(" ")
        f.write("\n")
        for i in tdn2.sleeper_l:
            f.write(str(i))
            f.write(" ")
        f.write("\n")
        for i in tdn2.sleeper1A_l:
            f.write(str(i))
            f.write(" ")
        f.write("\n")
        for i in tdn2.sleeper2A_l:
            f.write(str(i))
            f.write(" ")
        f.write("\n")
        for i in tdn2.sleeper3A_l:
            f.write(str(i))
            f.write(" ")
        f.close()
        return flag
    else:
        file=open(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt","w")
        ac=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        non_ac=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        Ac_sleeper1A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        Ac_sleeper2A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        Ac_sleeper3A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        sleeper=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        for i in ac:
            file.write(str(i))
            file.write(" ")
        file.write("\n")
        for i in non_ac:
            file.write(str(i))
            file.write(" ")
        file.write("\n")
        for i in sleeper:
            file.write(str(i))
            file.write(" ")
        file.write("\n")
        for i in Ac_sleeper1A:
            file.write(str(i))
            file.write(" ")
        file.write("\n")
        for i in Ac_sleeper2A:
            file.write(str(i))
            file.write(" ")
        file.write("\n")
        for i in Ac_sleeper3A:
            file.write(str(i))
            file.write(" ")
        file.write("\n")
        file.close()
        if tdn1.Class=="A/C CHAIR CAR":
            if tdn2.seatn in ac:
                ac.remove(tdn2.seatn)
        if tdn1.Class=="CHAIR CAR":
            if tdn2.seatn in non_ac:
                non_ac.remove(tdn2.seatn)
        if tdn1.Class=="SLEEPER":
            if tdn2.seatn in sleeper:
                sleeper.remove(tdn2.seatn)
        if tdn1.Class=="A/C SLEEPER 1A":
            if tdn2.seatn in Ac_sleeper1A:
                Ac_sleeper1A.remove(tdn2.seatn)
        if tdn1.Class=="A/C SLEEPER 2A":
            if tdn2.seatn in Ac_sleeper2A:
                Ac_sleeper2A.remove(tdn2.seatn)
        if tdn1.Class=="A/C SLEEPER 3A":
            if tdn2.seatn in Ac_sleeper3A:
                Ac_sleeper3A.remove(tdn2.seatn)
        file2=open(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt","w")
        for i in ac:
            file2.write(str(i))
            file2.write(" ")
        file2.write("\n")
        for i in non_ac:
            file2.write(str(i))
            file2.write(" ")
        file2.write("\n")
        for i in sleeper:
            file2.write(str(i))
            file2.write(" ")
        file2.write("\n")
        for i in Ac_sleeper1A:
            file2.write(str(i))
            file2.write(" ")
        file2.write("\n")
        for i in Ac_sleeper2A:
            file2.write(str(i))
            file2.write(" ")
        file2.write("\n")
        for i in Ac_sleeper3A:
            file2.write(str(i))
            file2.write(" ")
        file2.write("\n")
        file2.close()
    flag=1

def display():
    if os.path.exists(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt"):
        file=open(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt","r")
        fr=file.read().split("\n")
        if tdn1.Class=="A/C CHAIR CAR":
            for i in fr[0].split(" "):
                if i.strip():
                    print("[  {}  ]".format(i),end=" ")
        elif tdn1.Class=="CHAIR CAR":
            for i in fr[1].split(" "):
                if i.strip():
                    print("[  {}  ]".format(i),end=" ")
        elif tdn1.Class=="SLEEPER":
            for i in fr[2].split(" "):
                if i.strip():
                    print("[  {}  ]".format(i),end=" ")
        elif tdn1.Class=="A/C SLEEPER 1A":
            for i in fr[3].split(" "):
                if i.strip():
                    print("[  {}  ]".format(i),end=" ")
        elif tdn1.Class=="A/C SLEEPER 2A":
            for i in fr[4].split(" "):
                if i.strip():
                    print("[  {}  ]".format(i),end=" ")
        elif tdn1.Class=="A/C SLEEPER 3A":
            for i in fr[5].split(" "):
                if i.strip():
                    print("[  {}  ]".format(i),end=" ")
        file.close()
    else:
        file=open(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt","w")
        ac=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        non_ac=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        Ac_sleeper1A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        Ac_sleeper2A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        Ac_sleeper3A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        sleeper=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        for i in ac:
            file.write(str(i))
            file.write(" ")
        file.write("\n")
        for i in non_ac:
            file.write(str(i))
            file.write(" ")
        file.write("\n")
        for i in sleeper:
            file.write(str(i))
            file.write(" ")
        file.write("\n")
        for i in Ac_sleeper1A:
            file.write(str(i))
            file.write(" ")
        file.write("\n")
        for i in Ac_sleeper2A:
            file.write(str(i))
            file.write(" ")
        file.write("\n")
        for i in Ac_sleeper3A:
            file.write(str(i))
            file.write(" ")
        file.write("\n")
        file.close()
        display()

def YEAR():#year function for checking correct year
    tdn1.year=input("\nEnter The year Of Your Journey in the format of (YYYY):")
    if len(tdn1.year)==4:
        if int(tdn1.year)<today_date.year:
            print("\nYou Have Entered Invalid Year.Please Enter valid year")
            YEAR()
        elif int(tdn1.year)==today_date.year:
            MONTH1()
        if int(tdn1.year)>today_date.year:
            MONTH2()
    else:
        print("\nYou Have Entered Invalid Year.Please Enter valid year")
        YEAR()

def MONTH1():
    tdn1.month=input("\nEnter The Month of your journey in the format of(MM):")
    if len(tdn1.month)>0 and len(tdn1.month)==2:
        if int(tdn1.month)<today_date.month:
            print("\nYou Have Entered Invalid Month,Please Enter valid Month in the format(MM)")
            MONTH1()
        elif int(tdn1.month)==today_date.month and int(tdn1.month) <=12:
            DAY1()
        elif int(tdn1.month)>=today_date.month and int(tdn1.month) <=12:
            DAY2()
        elif int(tdn1.month)>12:
            print("\nYou Have Entered Invalid Month,Month should less than or equal to 12 not greater than 12")
            MONTH1()
    else:
        print("\nYou Have Entered Invalid Month,it should be in the format of (MM)")
        MONTH1()

def MONTH2():
    tdn1.month=input("\nEnter The month of your journey in the format of (MM) :")
    if len(tdn1.month)>0 and len(tdn1.month)==2:
        if int(tdn1.month)>=1 and int(tdn1.month)<=12:
            DAY3()
        else:
            print("\nYou Have Entered Invalid Month,Month should less than or equal to 12 not greater than 12")
            MONTH2()
    else:
        print("\nYou Have Entered Invalid Month,it should be in the format of (MM)")
        MONTH2()

def DAY1():
    tdn1.date=input("\nEnter The date of your journey in the format of (DD) :")
    if len(tdn1.date)>0 and len(tdn1.date)==2:
        mr=monthrange(int(tdn1.year),int(tdn1.month))
        if int(tdn1.date)>=today_date.day and int(tdn1.date)<=mr[1]:
            name()
        else:
            print("\nYou Have Entered Invalid date,Please Enter valid date")
            DAY1()
    else:
        print("\nYou Have Entered Invalid date,it should be in the format of (DD)")
        DAY1()

def DAY2():
    tdn1.date=input("\nEnter The date of your journey in the format of (DD) :")
    if len(tdn1.date)>0 and len(tdn1.date)==2:
        mr1=monthrange(int(tdn1.year),int(tdn1.month))
        if int(tdn1.date)>=1 and int(tdn1.date)<=mr1[1]:
            name()
        else:
            print("\nYou Have Entered Invalid date,Please Enter valid date")
            DAY2()
    else:
        print("\nYou Have Entered Invalid date,it should be in the format of (DD)")
        DAY2()

def DAY3():
    tdn1.date=input("\nEnter The date of your journey in the format of (DD) :")
    if len(tdn1.date)>0 and len(tdn1.date)==2:
        mr2=monthrange(int(tdn1.year),int(tdn1.month))
        if int(tdn1.date)>=1 and int(tdn1.date)<=mr2[1]:
            name()
        else:
            print("\nYou Have Entered Invalid date,Please Enter valid date")
            DAY3()
    else:
        print("\nYou Have Entered Invalid date,it should be in the format of (DD)")
        DAY3()

#To check month is valid or not
def name():
     tdn1.name=input("\nEnter name of the passenger :")
     if len(tdn1.name)>20 or len(tdn1.name)<3:
          print("\nInvalid ,Max range of first name is 20 & min is 2\n")
          name()
     elif len(tdn1.name)>3 and len(tdn1.name)<20:
            age()
     else:
          print("\nInvalid ,name contains invalid characher \n")
          name()

def age():
    tdn1.age=int(input("\nEnter age of the passenger:"))
    if tdn1.age<0:
        print("Enter correct age")
        age()
    else:
        Gender()

def Gender():
     tdn1.gender=input("\nEnter your gender :")
     gender_list=["MALE","FEMALE","Others","M","F"]
     if tdn1.gender.upper() in gender_list:
        phn_no()
     else:
        print("Please enter correct gender")
        Gender()

#To check phone number is valid or not
def phn_no():
     tdn1.phn=str(input("\nEnter contact number of passenger :"))
     if len(tdn1.phn)==10:
         if tdn1.phn.isdigit():
             aadhar()
         else:
              print("\nInvalid ,phone number contains invalid character \n")
              phn_no()
     else:
         print("\nENTER A VALID PHONE NUMBER\n")
         phn_no()

#To check AADHAR number is valid or not
def aadhar():
    tdn1.AAdhar=str(input("\nEnter aadhar number of the passenger :"))
    if len(tdn1.AAdhar)==12:
         if tdn1.AAdhar.isdigit():
              starting()
         else:
               print("\n Invalid ,AADHAR NUMBER contains invalid characher \n")
               aadhar()
    else:
         print("\nENTER A VALID AADHAR NUMBER\n")
         aadhar()
def starting():
     print("\nSelect Your Starting city:")
     print("\n1) Vijaywada \n2) Hyderabad \n3) Delhi \n4) Mumbai \n5) Chennai \n6) Kolkata \n7 Benguluru \n8) Pune \n9) Viskapatnam \n")
     list=["Vijaywada","Hyderabad","Delhi","Mumbai","Chennai","Kolkata","Benguluru","Pune","Viskapatnam"]
     tdn1.start=eval(input("Choose from the above list:"))
     for j in range(1,len(list)+1):
         if tdn1.start==j:
             tdn1.fcity=list[tdn1.start-1]
             print("\nyou are starting from ",tdn1.fcity)
             destination()
         if tdn1.start==0 or tdn1.start >len(list):
            print("\nInvalid, please select the boarding city again")
            starting()
def destination():
     print("\nSELECT THE DESTINATION:")
     print("\n1) Vijaywada \n2) Hyderabad \n3) Delhi \n4) Mumbai \n5) Chennai \n6) Kolkata \n7 Benguluru \n8) Pune \n9) Viskapatnam \n")
     list=["Vijaywada","Hyderabad","Delhi","Mumbai","Chennai","Kolkata","Benguluru","Pune","Viskapatnam"]
     tdn1.dest=int(input("Choose from the above list:"))
     for i in range(1,len(list)+1):
         if tdn1.dest==i:
             tdn1.dcity=list[tdn1.dest-1]
             print("\nyour destination is",tdn1.dcity)
             print("\nYour Are Travelling from {} to {}".format(tdn1.fcity.upper(),tdn1.dcity.upper()))
             select()
     if tdn1.dest==0 or tdn1.dest>len(list):
         print("\nInvalid, please select the destination city again")
         destination()
def select1():
    print("\nAVAILABLE TRAINS ARE:")
    print("\n1) Pinakini , 6:00am \n2) Rajadani , 10:00pm\n3) Intercity , 4:30pm\n")
    train_list1=["Pinakini, 6 00am","Rajadani , 10 00pm","Intercity , 4 30pm"]
    tdn1.train=int(input("select train timings:"))
    for nk in range(1,len(train_list1)+1):
        if tdn1.train==nk:
            tdn1.Train=train_list1[tdn1.train-1]
        if tdn1.train==0 or tdn1.train>len(train_list1):
            print("\nThe selected option is invalid,Plase select again")
            select1()
def select2():
    print ("\nAVAILABLE TRAINS ARE:")
    print ("\n1) Konark 7:40am\n2) Sangamithra 11:45pm\n3) Gangakaveri 9:50pm\n")
    train_list2=["Konark 7 40am","Sangamithra 11 45pm","Gangakaveri 9 50pm"]
    tdn1.train=int(input("select timings:"))
    for jk in range(1,len(train_list2)+1):
        if tdn1.train==jk:
            tdn1.Train=train_list2[tdn1.train-1]
        if tdn1.train==0 or tdn1.train>len(train_list2):
            print("\nThe selected option is invalid,Plase select from the above")
            select2()

def select3():
    print ("\nAVAILABLE TRAINS ARE:")
    print ("\n1) Krishna 11:00am\n2) GrandTrunk 2:30am\n3) MumbaiLLT 1:25pm\n")
    train_list3=["Krishna 11 00am","GrandTrunk 2 30am","MumbaiLLT 1 25pm"]
    tdn1.train=int(input("select timings:"))
    for jkl in range(1,len(train_list3)+1):
        if tdn1.train==jkl:
            tdn1.Train=train_list3[tdn1.train-1]
        if tdn1.train==0 or tdn1.train>len(train_list3):
            print("\nThe selected option is invalid,Plase select again")
            select3()

def select4():
    print("\nAVAILABLE TRAINS ARE:")
    print ("\n1) Udayan 8:40pm \n2) Mysuru 10:45pm\n3) Rajkot 7:00am\n")
    train_list4=["Udayan 8 40pm","Mysuru 10 45pm","Rajkot 7 00am"]
    tdn1.train=int(input("select timings:"))
    for klm in range(1,len(train_list4)+1):
        if tdn1.train==klm:
            tdn1.Train=train_list4[tdn1.train-1]
        if tdn1.train==0 or tdn1.train>len(train_list4):
            print("\nThe selected option is invalid,Plase select again")
            select4()
            
def bookseat():
     train_seat=["LOWER","UPPER","SIDE LOWER","SIDE UPPER"]
     rth=[100,200,300,400,500]
     for i in range(len(train_seat)):
        tdn1.berth[train_seat[i]]=rth[i]
     if tdn1.age>0 and tdn1.age<=3 or tdn1.age>=65:
          tdn1.Seat=train_seat[0]
          pass
     else:
          print("\nCHOOSE THE PREFERENCE OF SEATING:")
          print("\n1) LOWER\n2) UPPER \n3) SIDE LOWER \n4) SIDE UPPER\n")
          tdn1.seat=int(input("Select The Preference of seating from above list:"))
          flag=0
          for i in range(1,len(train_seat)+1):
              if tdn1.seat==i:
                  flag=1
                  tdn1.Seat=train_seat[tdn1.seat-1]
                  return
          if flag==0:
               print("\nThe selected option is invalid,please select again\n")
               bookseat()

def book():
    print("\nCHOOSE THE Coach OF TRAINS:")
    print("\n1)A/C CHAIR  - 200\n2)CHAIR  -100  \n3) SLEEPER - 300\n4) A/C SLEEPER 1A -600\n5) A/C SLEEPER 2A - 500\n6) A/C SLEEPER 3A - 400\n")
    train_list5=["A/C CHAIR CAR","CHAIR CAR","SLEEPER","A/C SLEEPER 1A","A/C SLEEPER 2A","A/C SLEEPER 3A"]
    tdn1.li=[200,100,300,600,500,400]
    tdn1.CLass=int(input("\nPlease Select class of trains from above list:"))
    if tdn1.CLass<=6:
        if tdn1.CLass==1:
            tdn1.Class="A/C CHAIR CAR"
            print("The avaliable seats are")
            display()
            tdn2.seatn=int(input("\nEnter your seat :"))
            check()
            if tdn2.seatn>0 and tdn2.seatn<=20:
                k=func()
                while(k!=1):
                    print("The seat is already booked!!,please enter another seat number")
                    dis=int(input("Enter 1 to display the empty seats in selected class Or Enter 0 To Exit"))
                    if dis==1:
                        print("The avaliable seats are")
                        display()
                        print("\n")
                        tdn2.seatn=int(input("Enter another seat :"))
                    else:
                        tdn2.seatn=int(input("Enter another seat :"))
                    k=func()
                print("Seat is booked")
                pay()
            else:
                print("\nEntered seat is not in the Train")
                print("Enter seat number greater then 1 and less than or equal to 20")
                book()
        elif tdn1.CLass==2:
            tdn1.Class="CHAIR CAR"
            print("The avaliable seats are")
            display()
            tdn2.seatn=int(input("\nEnter your seat :"))
            check()
            if tdn2.seatn>0 and tdn2.seatn<=20:
                k=func()
                while(k!=1):
                    print("The seat is already booked!!,please enter another seat number")
                    dis=int(input("Enter 1 to display the empty seats in selected class Or Enter 0 To Exit"))
                    if dis==1:
                        print("The avaliable seats are")
                        display()
                        print("\n")
                        tdn2.seatn=int(input("Enter another seat :"))
                    else:
                        tdn2.seatn=int(input("Enter another seat :"))
                    k=func()
                print("Seat is booked")
                pay()
            else:
                print("\nEntered seat is not in the Train")
                print("Enter seat number greater then 1 and less than or equal to 20")
                book()
        elif tdn1.CLass==3:
            tdn1.Class="SLEEPER"
            print("The avaliable seats are")
            display()
            tdn2.seatn=int(input("\nEnter your seat :"))
            check()
            if tdn2.seatn>0 and tdn2.seatn<=20:
                k=func()
                while(k!=1):
                    print("The seat is already booked!!,please enter another seat number")
                    dis=int(input("Enter 1 to display the empty seats in selected class Or Enter 0 To Exit"))
                    if dis==1:
                        print("The avaliable seats are")
                        display()
                        print("\n")
                        tdn2.seatn=int(input("Enter another seat :"))
                    else:
                        tdn2.seatn=int(input("Enter another seat :"))
                    k=func()
                print("Seat is booked")
                pay()
            else:
                print("\nEntered seat is not in the Train")
                print("Enter seat number greater then 1 and less than or equal to 20")
                book()
        elif tdn1.CLass==4:
            tdn1.Class="A/C SLEEPER 1A"
            print("The avaliable seats are")
            display()
            tdn2.seatn=int(input("\nEnter your seat :"))
            check()
            if tdn2.seatn>0 and tdn2.seatn<=20:
                k=func()
                while(k!=1):
                    print("The seat is already booked!!,please enter another seat number")
                    dis=int(input("Enter 1 to display the empty seats in selected class Or Enter 0 To Exit"))
                    if dis==1:
                        print("The avaliable seats are")
                        display()
                        print("\n")
                        tdn2.seatn=int(input("Enter another seat :"))
                    else:
                        tdn2.seatn=int(input("Enter another seat :"))
                    k=func()
                print("Seat is booked")
                pay()
            else:
                print("\nEntered seat is not in the Train")
                print("Enter seat number greater then 1 and less than or equal to 20")
                book()
        elif tdn1.CLass==5:
            tdn1.Class="A/C SLEEPER 2A"
            print("The avaliable seats are")
            display()
            tdn2.seatn=int(input("\nEnter your seat :"))
            check()
            if tdn2.seatn>0 and tdn2.seatn<=20:
                k=func()
                while(k!=1):
                    print("The seat is already booked!!,please enter another seat number")
                    dis=int(input("Enter 1 to display the empty seats in selected class Or Enter 0 To Exit"))
                    if dis==1:
                        print("The avaliable seats are")
                        display()
                        print("\n")
                        tdn2.seatn=int(input("Enter another seat :"))
                    else:
                        tdn2.seatn=int(input("Enter another seat :"))
                    k=func()
                print("Seat is booked")
                pay()
            else:
                print("\nEntered seat is not in the Train")
                print("Enter seat number greater then 1 and less than or equal to 20")
                book()
        elif tdn1.CLass==6:
            tdn1.Class="A/C SLEEPER 3A"
            print("The avaliable seats are")
            display()
            tdn2.seatn=int(input("\nEnter your seat :"))
            check()
            if tdn2.seatn>0 and tdn2.seatn<=20:
                k=func()
                while(k!=1):
                    print("The seat is already booked!!,please enter another seat number")
                    dis=int(input("Enter 1 to display the empty seats in selected class Or Enter 0 To Exit"))
                    if dis==1:
                        print("The avaliable seats are")
                        display()
                        print("\n")
                        tdn2.seatn=int(input("Enter another seat :"))
                    else:
                        tdn2.seatn=int(input("Enter another seat :"))
                    k=func()
                print("Seat is booked")
                pay()
            else:
                print("\nEntered seat is not in the Train")
                print("Enter seat number greater then 1 and less than or equal to 20")
                book()
        else:
            print("\nThe selected option is invalid,Plase select again")
            book()
        k=func()
    else:
        print("Select valid class of train")
        book()

def check():
    if os.path.exists(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt"):
        file=open(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt","r")
        fr=file.read().split("\n")
        if tdn1.Class=="A/C CHAIR CAR":
            if len(fr[0])==0:
                print("{} coach is booked".format(tdn1.Class))
                print("Please book another coach")
                book()
        else:
            pass
        if tdn1.Class=="CHAIR CAR":
            if len(fr[1])==0:
                print("{} coach is booked".format(tdn1.Class))
                print("Please book another coach")
                book()
        else:
            pass
        if tdn1.Class=="SLEEPER":
            if len(fr[2])==0:
                print("{} coach is booked".format(tdn1.Class))
                print("Please book another coach")
                book()
        else:
            pass
        if tdn1.Class=="A/C SLEEPER 1A":
            if len(fr[3])==0:
                print("{} coach is booked".format(tdn1.Class))
                print("Please book another coach")
                book()
        else:
            pass
        if tdn1.Class=="A/C SLEEPER 2A":
            if len(fr[4])==0:
                print("{} coach is booked".format(tdn1.Class))
                print("Please book another coach")
                book()
        else:
            pass
        if tdn1.Class=="A/C SLEEPER 3A":
            if len(fr[5])==0:
                print("{} coach is booked".format(tdn1.Class))
                print("Please book another coach")
                book()
        else:
            pass
    else:
        pass

def num():
    pm.card_number=input("\nEnter Your Debit/Credit (16 Digit) Card Number: ")
    if len(pm.card_number)==16 :
        if pm.card_number.isdigit():
            pass
        else:
            print("\nInvalid card number")
            print("\nPlese enter the card number again,Your number consists of ")
            num()
    else:
        print("\nInvalid card number")
        print("\nPlese enter the card number again")
        num()

def holder():

    pm.name_of_holder=input("Enter the Name of the card holder")
    if  len(pm.name_of_holder)>3 and len(pm.name_of_holder)<20:
         pass
    else:
        print("\nInvalid holder name")
        print("\nPlese enter the holder name again")
        holder()

def YEAR1():

    pm.yearv=input("\nEnter The year of the walidity in format of (YYYY) :")
    if len(pm.yearv)==4:
        if int(pm.yearv)<today_date.year:
            print("\nPlease Enter valid year\n")
            YEAR1()
        elif int(pm.yearv)==today_date.year:
            MONTH3() 
        if int(pm.yearv)>today_date.year:
            MONTH4()
    else:
        print("\nPlease Enter valid year\n")
        YEAR1()

def MONTH3():

    pm.monthv=input("\nEnter The Month of the walidity in format of (MM) :")
    if len(pm.monthv)>0 and len(pm.monthv)==2:
        if int(pm.monthv)<today_date.month:
            print("\nEnter a valid month\n")
            MONTH3()
        elif int(pm.monthv)==today_date.month and int(pm.monthv) <=12:
            pass
        elif int(pm.monthv)>=today_date.month and int(pm.monthv) <=12:
            pass
        elif int(pm.monthv)>12:
            print("\nEnter a valid month\n")
            MONTH3()
    else:
        print("\nEnter a valid month\n")
        MONTH3()

def MONTH4():

    pm.monthv=input("\nEnter The Month of the walidity in format of (MM) :")
    if len(pm.monthv)>0 and len(pm.monthv)==2:
        if int(pm.monthv)>=1 and int(pm.monthv)<=12:
            pass
        else:
            print("\nEnter a valid month\n")
            MONTH4()
    else:
        print("\nEnter a valid month\n")
        MONTH4()
def CVV():

    pm.cvv=input("\nEnter your 3 digit cvv number :")
    if len(pm.cvv)==3:
        if pm.cvv.isdigit():
            pass
    else:
        print("\nPlease enter correct cvv\n")
        CVV()
        
def upi():

    pm.ids=str(input("\nENTER UPI ID:ex:(9*@*):\n"))
    if len(pm.ids)==14:
        if pm.ids[10]=="@":
             print("\nOPEN THE UPI MOBILE APP AND APPROVE THE PAYMENT\n")
    else:
        print("\nPlease enter the ct orrect upi id\n")
        upi()

def select():

     if tdn1.start==tdn1.dest:
          print("\nInvalid,Both the boarding and destination are same, please select again!!!\n")
          starting()
     elif tdn1.start!=tdn1.dest:
         if tdn1.start<=5:
            if tdn1.dest<=5:
                select1()
                bookseat()
                book()
            elif tdn1.dest>=6:
                select2()
                bookseat()
                book()
         else:
             if tdn1.dest<=5:
                 select3()
                 bookseat()
                 book()
             if tdn1.dest>=6:
                 select4()
                 bookseat()
                 book()

# To print recceipt
def receipt():

    print("\n")
    print("*"*80)
    print("*"*80,file=f4)
    print ("\t\t\t\t\tRECEIPT")
    print ("\t\t\t\t\tRECEIPT",file=f4)
    print("*"*80)
    print("*"*80,file=f4)
    print("Current Time =", current_time,file=f4)
    print("Current Time =", current_time)
    print("Current Time =", current_time,file=f4)
    print("The Pnr number is:",tdn1.pnr)
    print("The Pnr number is:",tdn1.pnr,file=f4)
    print("\n\nThe name of the passenger is \t\t\t:",tdn1.name)
    print("\n\nThe name of the passenger is \t\t\t:",tdn1.name,file=f4)
    print("\n\nThe Gender of the passenger is \t\t\t:",tdn1.gender.upper())
    print("\n\nThe Gender of the passenger is \t\t\t:",tdn1.gender.upper(),file=f4)
    print("\n\nThe age of the passenger is \t\t\t:",tdn1.age)
    print("\n\nThe age of the passenger is \t\t\t:",tdn1.age,file=f4)
    print("\n\nThe contact number of passenger is \t\t:",tdn1.phn)
    print("\n\nThe contact number of passenger is \t\t:",tdn1.phn,file=f4)
    print("\n\nThe Seat number is\t\t\t\t:",tdn2.seatn)
    print("\n\nThe Seat number is\t\t\t\t:",tdn2.seatn,file=f4)
    print("\n\nThe aadhar number of passenger is \t\t:",tdn1.AAdhar)
    print("\n\nThe aadhar number of passenger is \t\t:",tdn1.AAdhar,file=f4)
    print("\n\nThe selected date is \t\t\t\t:",tdn1.date,tdn1.month,tdn1.year)
    print("\n\nThe selected date is \t\t\t\t:",tdn1.date,tdn1.month,tdn1.year,file=f4)
    print("\n\nSelected staring city is\t\t\t:",tdn1.fcity)
    print("\n\nSelected staring city is\t\t\t:",tdn1.fcity,file=f4)
    print("\n\nselected destination is\t\t\t\t:",tdn1.dcity)
    print("\n\nselected destination is\t\t\t\t:",tdn1.dcity,file=f4)
    print("\n\nThe selected train \t\t\t\t:",tdn1.Train)
    print("\n\nThe selected train \t\t\t\t:",tdn1.Train,file=f4)
    print("\n\nThe selected class of seat \t\t\t:",tdn1.Class)
    print("\n\nThe selected class of seat \t\t\t:",tdn1.Class,file=f4)
    print("\n\nThe selected preference of seating\t\t:",tdn1.Seat)
    print("\n\nThe selected preference of seating\t\t:",tdn1.Seat,file=f4)
    print ("\n\nCOST OF TRAVELLING(Including of all taxes) \t:",calculation())
    print ("\n\nCOST OF TRAVELLING(Including of all taxes) \t:",calculation(),file=f4)
    print("\n\n")

def pay():
    if tdn1.age>0 and tdn1.age<=3 or tdn1.age>=85:
        receipt()
        cancel()
        previous()
    else:
        if calculation()=="FREE TICKET":
            receipt()
            cancel()
            previous()
        else:
            print("The amount of tarvelling is {}".format(calculation()))
            cor=int(input(("If you want to continue enter 1 enter 0 to cancel:")))
            if cor==1:
                print("\nSELECT ONE OF THE PAYMENT OPTIONS\n")
                print("1)CREDIT/DEBIT CARD\n2)UPI")
                opt=int(input("\nEnter your option:"))
                if opt==1:
                    num()
                    holder()
                    YEAR1()
                    CVV()
                    receipt()
                    cancel()
                    previous()
                elif opt==2:
                    upi()
                    receipt()
                    cancel()
                    previous()
                else:
                    print("\nPlease Enter valid option\n")
                    pay()
            if cor==0:
                if tdn1.Class=="CHAIR CAR":
                    tdn2.non_acl.append(tdn2.seatn)
                if tdn1.Class=="A/C CHAIR CAR":
                    tdn2.ac_l.append(tdn2.seatn)
                if tdn1.Class=="A/C SLEEPER 1A":
                    tdn2.sleeper1A_l.append(tdn2.seatn)
                if tdn1.Class=="A/C SLEEPER 2A":
                    tdn2.sleeper2A_l.append(tdn2.seatn)
                if tdn1.Class=="A/C SLEEPER 3A":
                    tdn2.sleeper3A_l.append(tdn2.seatn)
                if tdn1.Class=="SLEEPER":
                    tdn2.sleeper_l.append(tdn2.seatn)
                f=open(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt","w")
                for i in tdn2.ac_l:
                    f.write(str(i))
                    f.write(" ")
                f.write("\n")
                for i in tdn2.non_acl:
                    f.write(str(i))
                    f.write(" ")
                f.write("\n")
                for i in tdn2.sleeper_l:
                    f.write(str(i))
                    f.write(" ")
                f.write("\n")
                for i in tdn2.sleeper1A_l:
                    f.write(str(i))
                    f.write(" ")
                f.write("\n")
                for i in tdn2.sleeper2A_l:
                    f.write(str(i))
                    f.write(" ")
                f.write("\n")
                for i in tdn2.sleeper3A_l:
                    f.write(str(i))
                    f.write(" ")
                f.close()
                re_enter=int(input("Press 1 to Re-enter the details press 0 to exit "))
                if re_enter==1:
                    starting()
                if re_enter==0:
                    exit
            else:
                pass

def previous():
    print("\nEnter 1 to view previous Receipts ")
    print("Enter 0 to exit\n")
    pb=int(input())
    if pb==1:
        print("Enter Password to view previous passwords(your PNR number):")
        password=input()
        if str(password)==tdn1.pnr:
            f5=open("data.txt","r")
            datap=f5.read()
            print(datap)
            f5.close()
        else:
            print("\nEnter correct password")
            previous()
    if pb==0:
        pass

def calculation():
     if tdn1.age<=3:
         return "Free Ticket"
     elif tdn1.age>3 and tdn1.age<=10:
         return (tdn1.li[tdn1.CLass-1]//2)+(tdn1.berth[tdn1.Seat])+(tdn1.li[tdn1.CLass-1]*7.5)/100
     elif tdn1.age>10 and tdn1.age<85:
         return (tdn1.li[tdn1.CLass-1]//2)+(tdn1.berth[tdn1.Seat])+(tdn1.li[tdn1.CLass-1]*8.5)/100
     else:
         return "Free Ticket"

def cancel():
    canc=int(input("\nPress 1 If You want to cancel the train ticket (or) press 0 to not to cancel your train ticket:\n"))
    if canc==1:
        if calculation()=="Free Ticket":
            if tdn1.Class=="A/C CHAIR CAR":
                tdn2.ac_l.append(tdn2.seatn)
            if tdn1.Class=="CHAIR CAR":
                tdn2.non_acl.append(tdn2.seatn)
            if tdn1.Class=="SLEEPER":
                tdn2.sleeper_l.append(tdn2.seatn)
            if tdn1.Class=="A/C SLEEPER 1A":
                tdn2.sleeper1A_l.append(tdn2.seatn)
            if tdn1.Class=="A/C SLEEPER 2A":
                tdn2.sleeper2A_l.append(tdn2.seatn)
            if tdn1.Class=="A/C SLEEPER 3A":
                tdn2.sleeper3A_l.append(tdn2.seatn)
            f=open(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt","w")
            tdn2.ac_l.sort()
            tdn2.non_acl.sort()
            tdn2.sleeper1A_l.sort()
            tdn2.sleeper_l.sort()
            tdn2.sleeper2A_l.sort()
            tdn2.sleeper3A_l.sort()
            for i in tdn2.ac_l:
                f.write(str(i))
                f.write(" ")
            f.write("\n")
            for i in tdn2.non_acl:
                f.write(str(i))
                f.write(" ")
            f.write("\n")
            for i in tdn2.sleeper_l:
                f.write(str(i))
                f.write(" ")
            f.write("\n")
            for i in tdn2.sleeper1A_l:
                f.write(str(i))
                f.write(" ")
            f.write("\n")
            for i in tdn2.sleeper2A_l:
                f.write(str(i))
                f.write(" ")
            f.write("\n")
            for i in tdn2.sleeper3A_l:
                f.write(str(i))
                f.write(" ")
            f.close()
            print("\nYour ticket has been cancelled ")
        else:
            if canc==1:
                canc2=int(input("\nYour money will reduced by 10 % and {} will be credited to your account".format(float((int(calculation()))-int((calculation())*10)/100))))
                print("if you want to continue press 1 (or) press 0 to cancel")
                if tdn1.Class=="A/C CHAIR CAR":
                    tdn2.ac_l.append(tdn2.seatn)
                if tdn1.Class=="CHAIR CAR":
                    tdn2.non_acl.append(tdn2.seatn)
                if tdn1.Class=="SLEEPER":
                    tdn2.sleeper_l.append(tdn2.seatn)
                if tdn1.Class=="A/C SLEEPER 1A":
                    tdn2.sleeper1A_l.append(tdn2.seatn)
                if tdn1.Class=="A/C SLEEPER 2A":
                    tdn2.sleeper2A_l.append(tdn2.seatn)
                if tdn1.Class=="A/C SLEEPER 3A":
                    tdn2.sleeper3A_l.append(tdn2.seatn)
                f=open(str(tdn1.Train)+str(tdn1.date)+str(tdn1.month)+str(tdn1.year)+".txt","w")
                tdn2.ac_l.sort()
                tdn2.non_acl.sort()
                tdn2.sleeper1A_l.sort()
                tdn2.sleeper_l.sort()
                tdn2.sleeper2A_l.sort()
                tdn2.sleeper3A_l.sort()
                for i in tdn2.ac_l:
                    f.write(str(i))
                    f.write(" ")
                f.write("\n")
                for i in tdn2.non_acl:
                    f.write(str(i))
                    f.write(" ")
                f.write("\n")
                for i in tdn2.sleeper_l:
                    f.write(str(i))
                    f.write(" ")
                f.write("\n")
                for i in tdn2.sleeper1A_l:
                    f.write(str(i))
                    f.write(" ")
                f.write("\n")
                for i in tdn2.sleeper2A_l:
                    f.write(str(i))
                    f.write(" ")
                f.write("\n")
                for i in tdn2.sleeper3A_l:
                    f.write(str(i))
                    f.write(" ")
                f.close()
            if canc2==1:
                print("\nYour ticket has been cancelled ")
                print("\nYour Money will be credited within 48 hours")
            if canc2==0:
                print("\nYour ticket has not cancelled")
    else:
        print("\nYour Ticket has not cancelled")

heading()#main function

while(1):
    pass_no=input("\nIf U want to Book another ticket\n Press 'y' or'Y' else enter 'N' or 'n'")
    if pass_no=="Y" or pass_no=="y":
        heading()#calling from starting
    else:
         break
f4.close()#closing of file
