meme_dict = {
            "LOL": "risadas"
            "EZ": "easy game"
            "GG": "good game"        
            }
word = input ("digite uma palavra moderna que voce nao entende (escreva toda a palavra em letras maiusculas):")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("ainda nao temos essa palavra, mas estamos trabalhando nela!")
