# store the data
words = ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']

canonical_spellings = ['color','amuck','adviser','pepper']

mappings = {'colour':'color','amok':'amuck','advisor':'adviser'}

#make an empty list
new_list = []
for word in words:
    if word in mappings:
        # if a word is mispelled do something
        # correct the spelling using the mappings dictionary
        corrected_word = mappings[word]
        # add the corrected words
        new_list.append(corrected_word)
    else:
        # if a word is correct do something else
        new_list.append(word)
#compare the words in some way- stemming

# loop over the list of words
print(new_list)
