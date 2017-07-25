from gensim.models import word2vec
import pickle
from xml.dom import minidom
xmldoc = minidom.parse('item.xml')
itemlist = xmldoc.getElementsByTagName('cons')
print len(itemlist)

dict={}
count0=0
count1=0
for item in itemlist :
	try :
		count0+=1
		dict[item.attributes['lex'].value]=item.attributes['sem'].value
	except KeyError :
		count1+=1
		continue

print count0-count1,count1

model = word2vec.Word2Vec.load_word2vec_format('/home/shubham/wikipedia-pubmed-and-PMC-w2v.bin', binary=True)
print model['Adderall']
# vocab=model.vocab
# cnt=0
# i=0
# for item in dict.keys():
# 	print i
# 	i+=1
# 	if item in vocab.keys():
# 		cnt+=1

# print cnt
