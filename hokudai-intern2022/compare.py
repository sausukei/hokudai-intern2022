#mlaskとmaxのデータ比較
from email.errors import MultipartConversionError
import glob
import os
import re
i=0
j=0
t=0
muchIndex=0
muched=0
muchedPosi=0
muchedNega=0
muchedNt=0
mlalis=[]
nlilis=[]
mlaidx=[]
positive=0
negative=0
neutral=0
mlaposi=0
mlanega=0
mlaneu=0

fileline=0
fileidx={}
name=[]

mainlis=[]
mainname=[]
for filename in glob.glob('mlask/mlask*.txt'):
    print(filename.replace('mlask/mlask',''))
    
    
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
    
       cut = str(filename.replace('mlask/mlask',''))
       name.append(cut)
       FILE_NAME="./compare/compared"+cut
       text = f.read()
       for l in re.split("[\t\n]",text):
        if str(l) != "":
            mlalis.append(l)
            fileline+=1
            if str(l) != "感情表現なし":
                index= len(mlalis)-1
                mlaidx.append(index)
                dic={index:[cut,fileline]}
                fileidx.update(dic)
                #print(l)
                i+=1
                
                
    
    fileline=0    
    
    




for filename in name:
    FILE_NAME="nlimax/max"+filename
    with open(FILE_NAME,'r') as  f:
        text = f.read()
        print(filename)
        for l in re.split("[\t\n]",text):
            if str(l) != "":
                #print(l)
                nlilis.append(l)
                #print(l)
                j+=1
print(len(nlilis), len(mlalis), len(mainlis))
for filename in name:
    FILE_NAME="mainpeople_newanalyse/"+filename
    with open(FILE_NAME,'r') as  f:
        text = f.read()
        name=filename.replace('mainpeople_newanalyse/','')
        print(filename)
        for l in re.split("[\t\n]",text):
            if str(l) != "":
                #print(l)
                mainlis.append(l)
                mainname.append(filename)
                #print(l)
                t+=1
                

for a in mlaidx:
    trans=float(nlilis[a].split(",")[1]) * 100
    transf=float(nlilis[a-1].split(",")[1]) * 100
    transb=float(nlilis[a+1].split(",")[1]) * 100
    
    if nlilis[a].split(",")[0] == "positive":
        positive+=1
    elif nlilis[a].split(",")[0] == "negative":
        negative+=1
    elif nlilis[a].split(",")[0] == "neutral":
        neutral+=1
        
    
    if mlalis[a].split()[0] == "POSITIVE" or mlalis[a].split()[0] == "mostly_POSITIVE":
        mlaposi+=1
        if nlilis[a].split(",")[0] == "positive":
            #print("ポジティブでマッチ")
            #print("{:s}の割合は{:.2f}%".format(nlilis[a].split(",")[0],trans))
            #print(muchIndex)
            muched+=1
            muchedPosi+=1
            #print(a)
            print(fileidx[a])
            print(mainlis[a],mainname[a])
            FILE_NAME="compare/positive"+mainname[a]
            with open(FILE_NAME,'a') as  f:
                f.write("ポジティブでマッチ\n")
                f.write("nliの{:s}の割合は{:.2f}%で、その前後での割合は、\n前:{:s} {:.2f}%\n後:{:s} {:2f}%\nでした\n"
                        .format(nlilis[a].split(",")[0],trans,nlilis[a-1].split(",")[0],transf,nlilis[a+1].split(",")[0],transb))
                f.write("\n対象部分"+str(fileidx[a])+"\n")
                f.write("\n対象の文\n")
                f.write(mainlis[a]+"\t"+mainname[a]+"\n")
                f.write("\n前後を含めた対象の文\n")
                f.write(mainlis[a-1]+"\n"+mainlis[a]+"\n"+mainlis[a+1])
    elif mlalis[a].split()[0] == "NEGATIVE" or mlalis[a].split()[0] == "mostly_NEGATIVE":
        mlanega+=1
        if nlilis[a].split(",")[0] == "negative":
            #print("ネガティブでマッチ")
            #print("{:s}の割合は{:.2f}%".format(nlilis[a].split(",")[0],trans))
            #print(muchIndex)
            muched+=1
            muchedNega+=1
            #print(a)
            print(fileidx[a])
            print(mainlis[a],mainname[a])
            FILE_NAME="compare/negative"+mainname[a]
            with open(FILE_NAME,'a') as  f:
                f.write("ネガティブでマッチ\n")
                f.write("nliの{:s}の割合は{:.2f}%で、その前後での割合は、\n前:{:s} {:.2f}%\n後:{:s} {:2f}%\nでした\n"
                        .format(nlilis[a].split(",")[0],trans,nlilis[a-1].split(",")[0],transf,nlilis[a+1].split(",")[0],transb))
                f.write("\n対象部分"+str(fileidx[a])+"\n")
                f.write("\n対象の文\n")
                f.write(mainlis[a]+"\t"+mainname[a]+"\n")
                f.write("\n前後を含めた対象の文\n")
                f.write(mainlis[a-1]+"\n"+mainlis[a]+"\n"+mainlis[a+1]+"\n")
                
                
    elif mlalis[a].split()[0] == "NEUTRAL":
        mlaneu+=1
        if nlilis[a].split(",")[0] == "neutral":
            #print("ニュートラルでマッチ")
            #print("{:s}の割合は{:.2f}%".format(nlilis[a].split(",")[0],trans))
            #print(muchIndex)
            muchedNt+=1            
            #print(a)
            print(fileidx[a])
            print(mainlis[a],mainname[a])
            FILE_NAME="compare/neutral"+mainname[a]
            with open(FILE_NAME,'a') as  f:
                f.write("ニュートラルでマッチ\n")
                f.write("nliの{:s}の割合は{:.2f}%で、その前後での割合は、\n前:{:s} {:.2f}%\n後:{:s} {:2f}%\nでした\n"
                        .format(nlilis[a].split(",")[0],trans,nlilis[a-1].split(",")[0],transf,nlilis[a+1].split(",")[0],transb))
                f.write("\n対象部分"+str(fileidx[a])+"\n")
                f.write("\n対象の文\n")
                f.write(mainlis[a]+"\t"+mainname[a]+"\n")
                f.write("\n前後を含めた対象の文\n")
                f.write(mainlis[a-1]+"\n"+mainlis[a]+"\n"+mainlis[a+1]+"\n")
    muchIndex+=1
    
print("mlaskで感情表現があるのは"+str(i))
print("マッチした回数{:d}".format(muched))

print(positive,negative,neutral)
print(mlaposi,mlanega,mlaneu)
print(muchedPosi,muchedNega,muchedNt)
