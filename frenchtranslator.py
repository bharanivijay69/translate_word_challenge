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
for word in word_list:
    result=translator.translate(word)
    frenchdict[word]=result.lower()
print(frenchdict)                               #translated english words are stored in dictionary form
file=open('frenchdictionary','wb')              
pickle.dump(frenchdict,file)                    #dictionary is dumped to a file called finaldictionary
file.close()
end = time.time()
print("Runtime of the program is",float(end-start))
