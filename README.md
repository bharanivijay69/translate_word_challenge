Translate Words Challenge

The task at had is that, given a text file, replace all possible words in English to French using any programming language of choice

What is the input?

    1. A text file that has more than one lakh lines. The file is t8.shakespeare.txt.
    2. A replace words list that has a 1000 words. The words in the list should be replaced with case being maintained. The file is find_words.txt
What needs to be done?

    1. Find an English to French dictionary
    2. Read the text file, replace words and dictionary
    3. Find all words that in the replace words list that has a replacement in the dictionary
    4. Replace the words in the text file
    5. save the processed file
What is the expected output?

    1. Unique list of words that was replaced with French words from the dictionary
    2. Number of times a word was replace
    3. Frequency of each word replaced
    4. Accuracy of the replace in terms of all occurences, casing and special characters to be maintained accurately
    5. Time taken to process
    6. Memory taken to process

frenchtranslate.py
This script is to create a dictionary file. This dictionary file contains the english to french word in dictionary datatype. This script after running generates a pickle file which contains the dictionary. This pickle file can be later used to get the dictionary,so that we dont want to translate everytime to get the dictionary.

final_program.py
This program gets the t8.shakespeare.txt as input. The output is stores in result.txt. This progarm is INCOMPLETE, as the format of the result is not matching with the original format of the text file.
