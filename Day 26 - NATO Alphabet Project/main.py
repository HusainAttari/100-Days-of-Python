import pandas as pd 

alphabet_list = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in alphabet_list.iterrows()}

word = input("Please enter a word: ").upper()
nato_word = [nato_dict[letter] for letter in word]
print(nato_word)