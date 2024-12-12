def single_root_words(root_word, *other_words):
	same_word = []
	for word in other_words:	
		if root_word.lower() in word.lower():
			same_word.append(word)
	#В первом цикле мы выбрали слова, для которых наше слово однокоренное
	#Необходимо также выбрать слова, которые однокоренные к нашему слову и входят в него
	for word in other_words:
		if word.lower() in root_word.lower():
			same_word.append(word)
	return same_word

list_of_same_words_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

list_of_same_words_2 = single_root_words('DiSablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(list_of_same_words_1)
print(list_of_same_words_2)
