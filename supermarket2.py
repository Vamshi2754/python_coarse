from datetime import datetime

name=input("Enter your name:")

lists='''
rice     Rs 20/kg 
sugar    Rs 30/kg
salt     Rs 15/kg
oil      Rs 100/liter
maggi    Rs 50/kg
boost    Rs 90/each
paneer   Rs 120/kg
colgate  Rs 70/each 
'''

price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

items={'rice':20,
'sugar':30,
'salt':15,
'oil':100,
'maggi':50,
'Boost':90,
'paneer':120,
'colgate':70}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter the quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","suresh supermarket",25*"=")
            print(28*" ","karimnagar")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",10*" ",'items',3*" ",12*' ','Quantity',1*" ",13*' ','price')
            for i in range(len(pricelist)):
                 print(i,8*' ',3*' ',ilist[i],2*' ',16*' ',qlist[i],' ',20*' ',plist[i],' ')
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",52*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(25*" ","Thanks for visiting")
            print(75*"-")