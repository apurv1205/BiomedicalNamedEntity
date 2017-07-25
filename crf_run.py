from xml.dom import minidom
import pycrfsuite
from itertools import chain
import nltk
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelBinarizer
import sklearn
import pycrfsuite
import json


NER=[]
'''
xmldoc = minidom.parse('item.xml')
itemlist = xmldoc.getElementsByTagName('cons')
print itemlist[0].firstChild.nodeValue
count0=0
count1=0

for item in itemlist :
	try :
		print count0
		count0+=1
		word=item.firstChild.nodeValue
		if word is not None and word not in NER :
			NER.append(word)
	except KeyError :
		count1+=1
		continue

    
NER.sort(key = lambda s: len(s),reverse=True)

with open('NER', 'w') as outfile:
    json.dump(NER, outfile)

'''
with open('NER') as infile:
    NER=json.load( infile)
print "loaded NERs successfully !",len(NER)

lines=0
count=0
count1=0
train_data=[]
test_data=[]

with open("corpus_new.txt","r") as f:
	for line in f:
		count+=1
		print count
		lst=[]
		count1=0
		words=line.split()
		NNER1=[]
		for ner in NER :
			if line.find(ner) != -1:
				line=line.replace(ner, ' ')

		NNER1=line.split()
		for word in words :
			if word in NNER1 :
				lst.append((word,"","0"))
			else : 
				count1+=1
				lst.append((word,"","1"))

		if count < 9500 :
			train_data.append(lst)
		else : test_data.append(lst)

with open('train_data', 'w') as outfile:
    json.dump(train_data, outfile)
with open('test_data', 'w') as outfile:
    json.dump(test_data, outfile)
print count
'''
		cnt+=1
		print cnt
		for word in words :
			flag=False
    		for ners in dict.keys() :
				if word in ners:
					flag=True
					break
    		
    		if flag==False : 
    			if word not in NNER : NNER.append(word)	
		linelst.append(line) 
		lines+=1
print len(NNER)

sentences = LineSentence('corpus_new.txt')
model=Word2Vec(sentences,min_count=0)

vocab=model.vocab
NNER=[]
	

lines=0
whites=0
linelst=[]
wordss=[]
cnt=0
# with open("corpus.txt","r") as f:
#     for line in f:
#         if line=="\n" or (line[0]=="M" and line[1]=="E" and line[2]=="D" and line[3]=="L") : 
#     		whites+=1
#     	else :
#     		words=line.split()
#     		cnt+=1
#     		print cnt
#     		for word in words :
#     			flag=False
# 	    		for ners in dict.keys() :
# 					if word in ners:
# 						flag=True
# 						break
	    		
# 	    		if flag==False : 
# 	    			if word not in NNER : NNER.append(word)	
#     		linelst.append(line) 
#     		lines+=1
# print len(NNER)
i=0
cnt=0
print len(vocab.keys())
NERS=[]
ners=[]
for ners1 in dict.keys() :
	nr=ners1.split('_')
	for item in nr :
		if item not in NERS :
			NERS.append(item)
for item in NERS:
	if item in vocab.keys():
		cnt+=1
		print item
		ners.append(item)

nners=[]
nners=list(set(vocab.keys())-set(ners))
print len(NERS),cnt 
x_train=[]
y_train=[]
x_test=[]
y_test=[]
i=0

for item in ners:
	if i<=9000:
		x_train.append(word2features(model[item]))
		y_train.append(['1'])
	else:
		x_test.append(word2features(model[item]))
		y_test.append(['1'])
	i+=1
i=0
for item in nners:
	if i<=15000:
		x_train.append(word2features(model[item]))
		y_train.append(['0'])
	else:
		x_test.append(word2features(model[item]))
		y_test.append(['0'])


trainer = pycrfsuite.Trainer(verbose=False)

for xseq, yseq in zip(x_train, y_train):
	print xseq,yseq
	trainer.append(xseq, yseq)

trainer.set_params({
    'c1': 1.0,   # coefficient for L1 penalty
    'c2': 1e-3,  # coefficient for L2 penalty
    'max_iterations': 50,  # stop earlier

    # include transitions that are possible, but not observed
    'feature.possible_transitions': True
})

trainer.train('conll2002-esp.crfsuite')

tagger = pycrfsuite.Tagger()
tagger.open('conll2002-esp.crfsuite')

y_pred = [tagger.tag(xseq) for xseq in x_test]

print(bio_classification_report(y_test, y_pred))

for item in vocab.keys():
	print i
	flag=False
	i+=1
	for ners in dict.keys() :
		if item in ners:
			flag=True
			break
	if flag==False : 
		if item not in NNER : 
			cnt+=1

print cnt
'''