from sqlite3 import adapt
from pyknp import Juman
jumanpp = Juman()
flag=0
FILE_NAME="0"
senlis =[]
with open("clean.txt", mode="r",encoding="UTF-8") as source:
    lines = source.read()
    for l in lines.split("\n"):
        
        if len(l) != 0:
            senlis.append(l)
print("appended")
idx=0
check=0
tmp=""
for sen in senlis:
    
    result = jumanpp.analysis(sen)
    print("解析しました")
    for mrph in result.mrph_list():
        
        if "人" in mrph.imis and not "人工物" in mrph.imis and flag == 0 or mrph.midasi=="人名" and flag == 0:
            FILE_NAME="./newanalyse/"+mrph.midasi+".txt"
            with open(FILE_NAME, mode="a") as f:
                print("ファイル書き込み",idx,check,sen)
               
                if idx == 0 and check == idx:
                    f.write("START\t")
                elif idx > 0 and check != idx:
                    f.write(senlis[idx-1]+"\t") 
                elif idx > 0 and check == idx:
                    f.write
                f.write(mrph.midasi)
                tmp=mrph.midasi
            flag=1

        elif "。" in mrph.midasi and flag == 1 or "！" in mrph.midasi and flag == 1 or "？" in mrph.midasi and flag == 1:
            with open(FILE_NAME, mode="a") as f:
                f.write(mrph.midasi)
                f.write("\t")
    
                if idx == len(senlis)-1:
                    f.write("END\n")
                else:
                    f.write(senlis[idx+1]+"\n")

            tmp+=mrph.midasi
            print("ファイルクローズ")
            flag=0
            check=idx

        elif flag == 1:
            with open(FILE_NAME, mode="a") as f:
                f.write(mrph.midasi) 
    idx+=1
        
        
   
    

