#mlaskとmaxのデータ比較
from email.errors import MultipartConversionError
import glob
import os
import re
import random
i=0
j=0
t=0
maincnt=0
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

unit=0
fileline=0
fileidx={}

mainlis=[]
mainidx=[]
rdm = []
rdmcount=0

def analyze():
    for a in mlaidx:
        if a % 3 == 1:
            global maincnt
            maincnt += 1
            trans=float(nlilis[a].split(",")[1]) * 100
            transf=float(nlilis[a-1].split(",")[1]) * 100
            transb=float(nlilis[a+1].split(",")[1]) * 100
            
            if nlilis[a].split(",")[0] == "positive":
                global positive
                positive+=1
            elif nlilis[a].split(",")[0] == "negative":
                global negative
                negative+=1
            elif nlilis[a].split(",")[0] == "neutral":
                global neutral
                neutral+=1
                
            
            if mlalis[a].split()[0] == "POSITIVE" or mlalis[a].split()[0] == "mostly_POSITIVE":
                global mlaposi
                mlaposi+=1
                if nlilis[a].split(",")[0] == "positive":
                    #print("ポジティブでマッチ")
                    #print("{:s}の割合は{:.2f}%".format(nlilis[a].split(",")[0],trans))
                    #print(muchIndex)
                    global muched
                    muched+=1
                    global muchedPosi
                    muchedPosi+=1
                    #print(a)
                    print(fileidx[a])
                    print(mainlis[a],mainidx[a])
                    FILE_NAME="compare/much/much"+mainidx[a]
                    with open(FILE_NAME,'a') as  f:
                        f.write("ポジティブでマッチ\n")
                        f.write("nliの{:s}の割合は{:.2f}%で、その前後での割合は、\n前:{:s} {:.2f}%\n後:{:s} {:2f}%\nでした\n"
                                .format(nlilis[a].split(",")[0],trans,nlilis[a-1].split(",")[0],transf,nlilis[a+1].split(",")[0],transb))
                        f.write("\n対象部分"+str(fileidx[a])+"\n")
                        f.write("\n対象の文\n")
                        f.write(mainlis[a]+"\t"+mainidx[a]+"\n")
                        f.write("\n前後を含めた対象の文\n")
                        f.write(mainlis[a-1]+"\n"+mainlis[a]+"\n"+mainlis[a+1])
                        f.write("\n###########################################################################################################\n")
                else:
                    FILE_NAME="compare/notmuch/notmuch"+mainidx[a]
                    with open(FILE_NAME,'a') as  f:
                        f.write("mlaskはポジティブでした\n")
                        f.write("nliの{:s}の割合は{:.2f}%で、その前後での割合は、\n前:{:s} {:.2f}%\n後:{:s} {:2f}%\nでした\n"
                                .format(nlilis[a].split(",")[0],trans,nlilis[a-1].split(",")[0],transf,nlilis[a+1].split(",")[0],transb))
                        f.write("\n対象部分"+str(fileidx[a])+"\n")
                        f.write("\n対象の文\n")
                        f.write(mainlis[a]+"\t"+mainidx[a]+"\n")
                        f.write("\n前後を含めた対象の文\n")
                        f.write(mainlis[a-1]+"\n"+mainlis[a]+"\n"+mainlis[a+1])
                        f.write("\n###########################################################################################################\n")
            elif mlalis[a].split()[0] == "NEGATIVE" or mlalis[a].split()[0] == "mostly_NEGATIVE":
                global mlanega
                mlanega+=1
                if nlilis[a].split(",")[0] == "negative":
                    #print("ネガティブでマッチ")
                    #print("{:s}の割合は{:.2f}%".format(nlilis[a].split(",")[0],trans))
                    #print(muchIndex)
                    muched+=1
                    global muchedNega
                    muchedNega+=1
                    #print(a)
                    print(fileidx[a])
                    print(mainlis[a],mainidx[a])
                    FILE_NAME="compare/much/much"+mainidx[a]
                    with open(FILE_NAME,'a') as  f:
                        f.write("ネガティブでマッチ\n")
                        f.write("nliの{:s}の割合は{:.2f}%で、その前後での割合は、\n前:{:s} {:.2f}%\n後:{:s} {:2f}%\nでした\n"
                                .format(nlilis[a].split(",")[0],trans,nlilis[a-1].split(",")[0],transf,nlilis[a+1].split(",")[0],transb))
                        f.write("\n対象部分"+str(fileidx[a])+"\n")
                        f.write("\n対象の文\n")
                        f.write(mainlis[a]+"\t"+mainidx[a]+"\n")
                        f.write("\n前後を含めた対象の文\n")
                        f.write(mainlis[a-1]+"\n"+mainlis[a]+"\n"+mainlis[a+1]+"\n")
                        f.write("\n###########################################################################################################\n")
                else:
                    FILE_NAME="compare/notmuch/notmuch"+mainidx[a]
                    with open(FILE_NAME,'a') as  f:
                        f.write("mlaskはネガティブでした\n")
                        f.write("nliの{:s}の割合は{:.2f}%で、その前後での割合は、\n前:{:s} {:.2f}%\n後:{:s} {:2f}%\nでした\n"
                                .format(nlilis[a].split(",")[0],trans,nlilis[a-1].split(",")[0],transf,nlilis[a+1].split(",")[0],transb))
                        f.write("\n対象部分"+str(fileidx[a])+"\n")
                        f.write("\n対象の文\n")
                        f.write(mainlis[a]+"\t"+mainidx[a]+"\n")
                        f.write("\n前後を含めた対象の文\n")
                        f.write(mainlis[a-1]+"\n"+mainlis[a]+"\n"+mainlis[a+1])
                        f.write("\n###########################################################################################################\n")
            elif mlalis[a].split()[0] == "NEUTRAL":
                global mlaneu
                mlaneu+=1
                if nlilis[a].split(",")[0] == "neutral":
                    #print("ニュートラルでマッチ")
                    #print("{:s}の割合は{:.2f}%".format(nlilis[a].split(",")[0],trans))
                    #print(muchIndex)
                    global muchedNt
                    muchedNt+=1            
                    #print(a)
                    print(fileidx[a])
                    print(mainlis[a],mainidx[a])
                    FILE_NAME="compare/much/much"+mainidx[a]
                    with open(FILE_NAME,'a') as  f:
                        f.write("ニュートラルでマッチ\n")
                        f.write("nliの{:s}の割合は{:.2f}%で、その前後での割合は、\n前:{:s} {:.2f}%\n後:{:s} {:2f}%\nでした\n"
                                .format(nlilis[a].split(",")[0],trans,nlilis[a-1].split(",")[0],transf,nlilis[a+1].split(",")[0],transb))
                        f.write("\n対象部分"+str(fileidx[a])+"\n")
                        f.write("\n対象の文\n")
                        f.write(mainlis[a]+"\t"+mainidx[a]+"\n")
                        f.write("\n前後を含めた対象の文\n")
                        f.write(mainlis[a-1]+"\n"+mainlis[a]+"\n"+mainlis[a+1]+"\n")
                        f.write("\n###########################################################################################################\n")
                else:
                    FILE_NAME="compare/notmuch/notmuch"+mainidx[a]
                    with open(FILE_NAME,'a') as  f:
                        f.write("mlaskはニュートラルでした\n")
                        f.write("nliの{:s}の割合は{:.2f}%で、その前後での割合は、\n前:{:s} {:.2f}%\n後:{:s} {:2f}%\nでした\n"
                                .format(nlilis[a].split(",")[0],trans,nlilis[a-1].split(",")[0],transf,nlilis[a+1].split(",")[0],transb))
                        f.write("\n対象部分"+str(fileidx[a])+"\n")
                        f.write("\n対象の文\n")
                        f.write(mainlis[a]+"\t"+mainidx[a]+"\n")
                        f.write("\n前後を含めた対象の文\n")
                        f.write(mainlis[a-1]+"\n"+mainlis[a]+"\n"+mainlis[a+1])
                        f.write("\n###########################################################################################################\n")
            global muchIndex
            muchIndex+=1
            
def makerdm(rdm,rdmcount):
    for a in mlaidx:
        if a % 3 == 1:
            rdm.append(str(fileidx[a])+"\n"+str(mainlis[a])+"\n")
            rdmcount+=1

            

for filename in glob.glob('mlask/mlask*.txt'):
    print(filename.replace('mlask/mlask',''))
    
    
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
    
       name = str(filename.replace('mlask/mlask',''))
       
       FILE_NAME="./compare/compared"+name
       text = f.read()
       for l in re.split("[\t\n]",text):
        if str(l) != "":
            mlalis.append(l)
            unit+=1
            fileline=int(unit/3)+1
            if str(l) != "感情表現なし":
                index= len(mlalis)-1
                mlaidx.append(index)
                dic={index:[name,fileline]}
                fileidx.update(dic)
                #print(l)
                i+=1
                
    nliname =name
    FILE_NAME="nlimax/max"+nliname
    with open(FILE_NAME,'r') as  f:
        text = f.read()
        print(nliname)
        for l in re.split("[\t\n]",text):
            if str(l) != "":
                #print(l)
                nlilis.append(l)
                #print(l)
                j+=1
                    
    mainname = name
    FILE_NAME="mainpeople_newanalyse/"+mainname
    with open(FILE_NAME,'r') as  f:
        text = f.read()
        
        print(mainname)
        for l in re.split("[\t\n]",text):
            if str(l) != "":
                #print(l)
                mainlis.append(l)
                mainidx.append(mainname)
                #print(l)
                t+=1
    
    analyze()
    makerdm(rdm,rdmcount)
    mlalis=[]
    nlilis=[]
    mlaidx=[]
    fileidx={}
    mainlis=[]
    mainidx=[]
    unit=0    
    
        
print("mlaskで感情表現があるのは"+str(i)+"のうち前後の文を抜いたものは"+str(maincnt))
print("マッチした回数{:d}".format(muched))
print("マッチ率は\n")
posirate=muchedPosi/mlaposi*100
negarate=muchedNega/mlanega*100
neurate=muchedNt/mlaneu*100
rate=muched/maincnt*100
print("ポジティブ{:.2f}%\nネガティブ{:.2f}%\nニュートラル{:.2f}%\n総計{:.2f}%\nでした".format(posirate,negarate,neurate,rate))
with open("result.txt","a") as f:
    f.write("mlaskで感情表現があるのは"+str(i)+"のうち前後の文を抜いたものは"+str(maincnt))
    f.write("マッチした回数{:d}".format(muched))
    f.write("マッチ率は\n")
    f.write("ポジティブ{:.2f}%\nネガティブ{:.2f}%\nニュートラル{:.2f}%\n総計{:.2f}%\nでした\n".format(posirate,negarate,neurate,rate))
print(positive,negative,neutral)
print(mlaposi,mlanega,mlaneu)
print(muchedPosi,muchedNega,muchedNt)
with open("check.txt","w") as f:
    check=random.sample(rdm,50)
    for write in check:
        f.write(write)
        f.write("\n")
        f.write("##############################################################################################################")