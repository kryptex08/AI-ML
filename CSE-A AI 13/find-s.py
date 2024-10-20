import pandas as pd
import numpy as np
data=pd.read_excel('find.csv.xlsx')
print("Data:\n",data)

d=np.array(data)[:, :-1]
target=np.array(data)[:,-1]
print("\n Features:\n",d)
print("\nTarget:\n", target)

def train(c,t):
    specific_hypothesis=None
    for i,val in enumerate(t):
        if val=="Yes":
            specific_hypothesis=c[i].copy()
            break
    for i,val in enumerate(c):
        if t[i]=="Yes":
            for x in range(len(specific_hypothesis)):
                if val[x]!=specific_hypothesis[x]:
                    specific_hypothesis[x]='?'
                    

    return specific_hypothesis
final_hypothesis=train(d,target)
print("\n The final hypothesis is: ",final_hypothesis)