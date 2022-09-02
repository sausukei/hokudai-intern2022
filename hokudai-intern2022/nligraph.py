import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import os 
import re

data=[]
value=[]
condition=[]
cnt=[]
count=0
tmp=0
plt.ylim(-1,1)
for filename in glob.glob('nlimax/max*.txt'):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       
       cut = str(filename.replace('nlimax/max',''))
       cut = str(cut.replace(".txt",""))
       print(cut)
       metadata=f.read()
       
       for l in re.split("[\t\n]",metadata):
            if str(l) != "":
                data=l.split(",")
                print(data)
                condition.append(data[0])
                if data[0] == "positive":
                    value.append(tmp+float(data[1]))
                    tmp+=float(data[1])
                elif data[0] == "negative":
                    value.append(tmp+float(data[1])*-1)
                    tmp-=float(data[1])*-1
                elif data[0] == "neutral":
                    value.append(tmp)
                """
                with open("graph/graph"+cut,"a") as graph:
                    graph.write(l+"\n")
                    data=l.split(",")
                """
                cnt.append(count)
                count+=1
       
       print(value)
       print(condition)
       plt.plot(cnt, value, label="test")
       plt.legend()
       plt.savefig("graph/graph"+cut+"2.png")
       plt.clf()
               
       value=[]
       condition=[]
       cnt=[]
       count=0

     
       