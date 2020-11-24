import nltk,pickle,re,time
from nltk.tokenize.treebank import TreebankWordDetokenizer
start = time.time()
file_to_read = open("frenchdictionary", "rb")
final_dictionary = pickle.load(file_to_read)
count={}
file_content = open("t8.shakespeare.txt").read()
tokens = nltk.word_tokenize(file_content)
print(tokens)
final=[]
for word in tokens:
    if word in final_dictionary:
        final.append(final_dictionary[word])
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    else:
        final.append(word)
f=open("result.txt","w+")
answer=TreebankWordDetokenizer().detokenize(final)
print(answer)
f.write(answer)
f.close()
print("Number of time the words are replaced",count)
end = time.time()
print("Runtime of the program is",float(end-start))
