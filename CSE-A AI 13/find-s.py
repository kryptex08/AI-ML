import csv
co=open('find.csv','r')
cr=csv.reader(co)
h=['0','0','0','0']
for i in cr:
    if h==['0','0','0','0'] and i[-1]=='Yes':
        h=i
    if(i[-1]==h[-1]):
        for j in range(int(len(i))-1):
            if h[j]!=i[j]:
               h[j]='?'
print (h)
