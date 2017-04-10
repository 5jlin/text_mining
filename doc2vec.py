import json
import jieba
from gensim.models import doc2vec
from collections import namedtuple
import numpy
doc = []

with open('Boy-Girl-1800-2500.json', encoding = 'utf-8-sig') as data_file:    
    data = json.load(data_file, encoding = 'utf-8-sig')

datalist = data["articles"]
for i in range(len(datalist)):
    datatmp = datalist[i]
    tmp = ""
    if 'article_title' in datatmp:
        title = datatmp["article_title"]
        words = jieba.cut(title, cut_all=False)
        for word in words:
            tmp += word
            tmp += " "
        #if i < 5: print(tmp)
        doc.append(tmp)

docs = []
analyzedDocument = namedtuple('AnalyzedDocument', 'words tags')
for i, text in enumerate(doc):
    words = text.split()
    tags = [i]
    docs.append(analyzedDocument(words, tags))

model = doc2vec.Doc2Vec(docs, size = 100, window = 300, min_count = 1, workers = 4)
#model.save("model.bin")
#dist = numpy.sqrt(numpy.sum(numpy.square(model.docvecs[0] - model.docvecs[1])))
