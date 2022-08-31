import glob
import os
import re
from mlask import MLAsk


i=0
textspl=[]
for filename in glob.glob('mainpeople_newanalyse/*.txt'):
   print(filename.replace('mainpeople_newanalyse/',''))
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       
       cut = str(filename.replace('mainpeople_newanalyse/',''))
       FILE_NAME="./mlask/mlask"+cut
       text = f.read()
       for l in re.split("[\t\n]",text):
            if l != "":
                textspl.append(l)
                emotion_analyzer = MLAsk()
                analyse=emotion_analyzer.analyze(l)
                
                if analyse["emotion"] is not None:
                    orientation=analyse["orientation"]
                    emotion=analyse["emotion"]
                    with open(FILE_NAME,"a") as record:
                        record.write(str(orientation)+" "+str(emotion)+"\t")
                        #print(activate,emotion)
                elif analyse["emotion"] is None:
                    #print("感情表現なし")
                    with open(FILE_NAME,"a") as record:
                            record.write("感情表現なし\t")
                
            i+=1        
            if i%3 == 0 and i!=0:
                with open(FILE_NAME,"a") as record:
                    record.write("\n")

       



print(i)

print(len(textspl))