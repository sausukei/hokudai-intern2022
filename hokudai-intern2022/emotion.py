import glob
import os
import re
from mlask import MLAsk


i=1
textspl=[]
for filename in glob.glob('mainpeople_newanalyse/*.txt'):
   print(filename)
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       FILE_NAME="./mlask/processed"+".txt"
       text = f.read()
       for l in re.split("[\t\n]",text):
        textspl.append(l)
        emotion_analyzer = MLAsk()
        analyse=emotion_analyzer.analyze(l)
        
        if analyse["emotion"] is not None:
            activate=analyse["activation"]
            emotion=analyse["emotion"]
            with open(FILE_NAME,"a") as record:
                record.write(str(activate)+" "+str(emotion)+"\t")
                print(activate,emotion)
        elif analyse["emotion"] is None:
           print("感情表現なし")
           with open(FILE_NAME,"a") as record:
                record.write("感情表現なし\t")

        
        
        if i%3 == 0:
            with open(FILE_NAME,"a") as record:
                record.write("\n")

        i+=1
       textspl.clear()
       
       print("初期化しました")



print(i)
print(textspl)
print(len(textspl))