# JustChat

Calculate the frequency of words in text file, frequency data further can be use to create wordcloud. To compute this task I fetched the content from the website.
Further removed all special character containing words.
<img width='50%' height='50%' src="https://miro.medium.com/max/980/1*gsushK-1kjqsSxPWbbkvPA.png">


## Usage

Website Link: https://deepakdhull80.pythonanywhere.com/

## Components

### Frequency calculator of resource file

<pre> 
<code> 
def result(number,res=resource):
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
		return False
	response=[]
	for k, v in sorted(words.items(), key=lambda item: item[1],reverse=True):
		if number==0:
			return response
		k=k.lower()
		response.append((k,v))
		number-=1 
</code> 
</pre> 

