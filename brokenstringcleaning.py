words = ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']
canonical_spellings = ['color','amuck','adviser','pepper']

mappings = {'colour':'color', 'amok':'amuck', 'advisor':'adviser'}

new_list = []
for word in words:
    if word in mappings:
        corrected_word = mappings[word]
        new_list.append(corrected_word)
    else:
        new_list.append(word)
print(new_list)
