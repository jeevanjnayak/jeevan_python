sentence = input("input the sentence: ")
sent = sentence.split(" ")
print(sent)
sent_dict = {}
for n in sent:
    sent_dict[n] = sent.count(n)
print(sent_dict)
