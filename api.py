import requests
import re



url='http://terriblytinytales.com/test.txt'

res=requests.get(url).text

def result(number,res=res):
	para=res.split('\n')
	record=[]
	for sen in para:
		if len(sen):
			record.append(sen)
	words={}
	for sen in record:
		tmp=sen.split(' ')
		for word in tmp:
			if re.match('^[a-zA-Z]*$', word):
				if word not in words:
					words[word]=1
				else:
					words[word]+=1
	maximum_words=len(words)-1
	if number>maximum_words:
# here we have to do
		pass
	response=[]
	for k, v in sorted(words.items(), key=lambda item: item[1],reverse=True):
		if number==0:
			return response
		k=k.lower()
		response.append((k,v))
		number-=1
	# return words[:number]

# print(result(10))
# print(words)
