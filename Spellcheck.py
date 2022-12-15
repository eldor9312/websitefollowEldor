from textblob import Word

def correct_word_spelling(word):
     word = Word(word)
     result = word.spellcheck()
     #res_and_value=result.split
     if not result[0][0]==word and float(result[0][1])>0.9 and not word==result[0][0]+'s':
        complete=result[0][0]
     return complete
     