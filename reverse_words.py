def spin_words(sentence):
	res = []

	for i in sentence.split(' '):
		if len(i) >= 5:
			res.append(''.join(list(reversed(i))))
		else:
			res.append(i)

	return ' '.join(res)
