import csv
with open("find.csv",'r') as co:
    cr=csv.reader(co)
    h=None
    for i in cr:
        if h is None and i[-1]=="Yes":
            h=i[:-1]
        elif i[-1]=="Yes":
            for j in range(len(h)):
                if h[j]!=i[j]:
                    h[j]='?'
    print(h)
