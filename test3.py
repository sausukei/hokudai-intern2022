from transformers import pipeline

classifier = pipeline("zero-shot-classification", model='joeddav/xlm-roberta-large-xnli')

label_sets = [["moral", "neutral", "immoral"],
            ["ethical", "neutral", "unethical"],
            ["good", "neutral", "bad"],
            ["righteous", "neutral", "wicked"],
            ["virtuous", "neutral", "sinful"]]

sentences = open("hokudai-intern2022/mainpeople_newanalyse/探偵.txt","r")


def Checker(inp_sen, candidate_labels):
    result = classifier(inp_sen, candidate_labels)
    sentence = result['sequence']
    labels = result['labels']
    scores = result['scores']
    # print(sentence, labels, scores)
    zipped = list(zip(labels,scores))
    # print(zipped)
    line = sentence+"\t"+zipped[0][0]+"\t"+str(zipped[0][1])+"\t"+zipped[1][0]+"\t"+str(zipped[1][1])+"\t"+zipped[2][0]+"\t"+str(zipped[2][1])+"\n"
    return(line)

fil = open("Second_SimpleMultiNLI_results.tsv","w")
for sen in sentences:
    sentence = sen[0]
    mark = sen[1]
    for labels in label_sets:
        res = Checker(sentence,labels)
        res = mark+"\t"+res
        print(res)
        fil.write(res)
fil.close()
sentences.close()