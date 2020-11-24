from translate import Translator
import pickle
to_lang = 'fr'
secret = '5deadcc9f92542aba66edd0cbfa0fbc3'
translator = Translator(provider='microsoft', to_lang=to_lang, secret_access_key=secret)
word_file_name=input("ENTER FILE NAME:")
word_file=open(word_file_name)
word_list=[]
for words in word_file:
    temp=words.rstrip('\n')
    word_list.append(temp)
frenchdict=dict()
for word in word_list:
    result=translator.translate(word)
    frenchdict[word]=result
print(frenchdict)
file=open('frenchdictionary','wb')
pickle.dump(frenchdict,file)
file.close()
file_to_read = open("frenchdictionary", "rb")
final_dictionary = pickle.load(file_to_read)
print(final_dictionary)
count=0
for words in final_dictionary:
    count=count+1
print("\n The number of words translated is ",count)
