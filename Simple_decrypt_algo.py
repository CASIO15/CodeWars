from string import ascii_lowercase

def decrypt(string):
	count_dic = {}
	ascii_offset = {k: v for v, k in enumerate(ascii_lowercase)}
	raw = list('0' * 26)

	for i in string:
		if i in count_dic:
			count_dic[i] += 1
		else:
			if i in ascii_lowercase:
				count_dic[i] = 1

	for k, v in ascii_offset.items():
		if k in count_dic:
			raw[v] = count_dic.get(k)

	return ''.join(map(str, raw))


print(decrypt('$aaaa#bbb*ccfff!z'))

# result = 43200300000000000000000001
