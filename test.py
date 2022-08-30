import sys
from transformers import T5Tokenizer, AutoModelForCausalLM

tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")

model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium")

# text = "朝ごはんは食べるためである，牛乳を"
text = sys.argv[1]
input = tokenizer.encode(text, return_tensors="pt")
output = model.generate(input, do_sample=True, max_length=50, num_return_sequences=5)
generated = (tokenizer.batch_decode(output))

output = generated[0].split("</s>")
# for out in output:
#     print(output.index(out), out)
# """
output = output[1]
try:
    sentences = output.split("。")
    sentence = sentences[0]
    out = sentence
except:
    out = output

print("ANSWER:", out+"。")