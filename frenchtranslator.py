from translate import Translator
import pickle,time
start = time.time()
to_lang = 'fr'
secret = '5deadcc9f92542aba66edd0cbfa0fbc3'     #security key from microsof azure cloud for using translation service
translator = Translator(provider='microsoft', to_lang=to_lang, secret_access_key=secret)
word_file=open("find_words.txt")                #text file which contains the english words that are needed to be translated to french
word_list=[]
for words in word_file:
    temp=words.rstrip('\n')
    word_list.append(temp)
frenchdict=dict()
count=0
for word in word_list:
    result=translator.translate(word)
    frenchdict[word]=result.lower()
    count=count+1
#print(frenchdict)                               #translated english words are stored in dictionary form
file=open('frenchdictionary','wb')              
pickle.dump(frenchdict,file)                    #dictionary is dumped to a file called finaldictionary
file.close()
end = time.time()
print("The number of words translated is ", count)
print("Runtime of the program is",float(end-start))
import os
import psutil
process = psutil.Process(os.getpid())
print("Memory used by this program is",(process.memory_info().rss))
