from transformers import T5Tokenizer, AutoModelForCausalLM 
from transformers import pipeline
from collections import Counter
logfile = open("1000addedConsequencesETHICAL25.txt","w")
sentences = eval(open("random1000_simple_extended_danger.lis").read())

tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium") 
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium") 
classifier = pipeline("zero-shot-classification", model='joeddav/xlm-roberta-large-xnli')



def CheckPolarity(inp_sen):
    label_set = ['ethical', 'neutral', 'unethical']
    result = classifier(inp_sen, label_set)
    sentence = result['sequence']
    labels = result['labels']
    scores = result['scores']
    zipped = list(zip(labels,scores))
    # line = sentence+"\t"+zipped[0][0]+"\t"+str(zipped[0][1])+"\t"+zipped[1][0]+"\t"+str(zipped[1][1])+"\t"+zipped[2][0]+"\t"+str(zipped[2][1])+"\n"
    winner = zipped[0][0]
    return(winner)

agreed = 0
for sen in sentences:
    input = tokenizer.encode(sen[0], return_tensors="pt") 
    output = model.generate(input, do_sample=True, max_length=25, num_return_sequences=3) 
    consequences = (tokenizer.batch_decode(output))
    reslist = []
    for con in consequences:
        conlist = con.split("</s>")
        cononly = conlist[1]
        result = CheckPolarity(cononly)
        print("result for", con, "is", result)
        print("when", sen[0], "is", sen[1])
        print("--------------")
        towrite = cononly+"\t"+result+"\t"+sen[0]+"\t"+sen[1]+"\n"
        logfile.write(towrite)
        reslist.append(result)
    
    
    counts = Counter(reslist)
    if counts["positive"] >1: result = "positive"
    elif counts["neutral"] >1: result = "neutral"
    elif counts["negative"] >1: result = "negative"
    else: result = "neutral"
    print("agreed result for 3 consequences is", result)
    if result == "positive" and sen[1] == "SAFE": agreed+=1
    if result == "positive" and sen[1] == "NEUTRAL": agreed+=1
    if result == "neutral" and sen[1] == "SAFE": agreed+=1
    if result == "neutral" and sen[1] == "NEUTRAL": agreed+=1
    if result == "negative" and sen[1] == "DANGER": agreed+=1

x=agreed*100/len(sentences)
print("checking agreement with polarity:",agreed,"for",len(sentences), "samples.",x,"%")
