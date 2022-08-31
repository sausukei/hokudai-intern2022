import glob
import os
import re
from transformers import pipeline
classifier = pipeline("zero-shot-classification",
                      model="joeddav/xlm-roberta-large-xnli")

# we will classify the Russian translation of, "Who are you voting for in 2020?"
sequence_to_classify = ""
# we can specify candidate labels in Russian or any other language above:
candidate_labels = ["positive", "negative", "neutral"]

# {'labels': ['politics', 'Europe', 'public health'],
#  'scores': [0.9048484563827515, 0.05722189322113991, 0.03792969882488251],
#  'sequence': 'За кого вы голосуете в 2020 году?'}


i=1
textspl=[]
print("これから分析")
for filename in glob.glob('mainpeople_newanalyse/*.txt'):
   print(filename.replace('mainpeople_newanalyse/',''))
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       cut = str(filename.replace('mainpeople_newanalyse/',''))
       FILE_NAME="./nli/nli"+cut
       FILE_NAME2="./nlimax/max"+cut
       text = f.read()
       for l in re.split("[\t\n]",text):
        
        if str(l) != "":
            textspl.append(l)
            sequence_to_classify=str(l)
            
            print(l)
            print(max(classifier(sequence_to_classify, candidate_labels)["scores"]))
            tmp = max(classifier(sequence_to_classify, candidate_labels)["scores"])
            idx=classifier(sequence_to_classify, candidate_labels)["scores"].index(tmp)
            print(classifier(sequence_to_classify, candidate_labels)["labels"][idx])
            
            
            with open(FILE_NAME,"a") as record:
                    record.write(str(classifier(sequence_to_classify, candidate_labels)["labels"])
                                +str(classifier(sequence_to_classify, candidate_labels)["scores"])+"\t")
            
            with open(FILE_NAME2,"a") as record2:
                    record2.write(str(classifier(sequence_to_classify, candidate_labels)["labels"][idx])+","+str(tmp)+"\t")
            
            if i%3 == 0:
                with open(FILE_NAME,"a") as record:
                    record.write("\n")
                    print("改行")
                with open(FILE_NAME2,"a") as record2:
                    record2.write("\n")
                    print("改行")
            
            print(i)
        i+=1
        



print("あ"+str(i))
print(len(textspl))