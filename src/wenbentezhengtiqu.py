#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import jieba
import codecs
from sklearn.feature_extraction.text import CountVectorizer

def loaddata(path, class1):
    allfiles = os.listdir(path)
    textdata=[]
    classall=[]
    for each in allfiles:
        data = codecs.open(os.path.join(path, each), encoding="gbk").read()
        data1 = jieba.cut(data)
        data11 = ""
        for item in data1:
            data11 += item + " "
        textdata.append(data11)
        classall.append(class1)
    return textdata, classall

text1, class1 = loaddata(unicode(r"C:\Users\Administrator\PycharmProjects\machineLearn\data\爱情", "utf8"), "love")
text2, class2 = loaddata(unicode(r"C:\Users\Administrator\PycharmProjects\machineLearn\data\仙侠", "utf8"), "ghost")
train_text = text1 + text2
classall = class1+class2
count_vect = CountVectorizer()
train_x_counts = count_vect.fit_transform(train_text)
print("run0")
#tfidf模型
from sklearn.feature_extraction.text import TfidfTransformer
tf_ts = TfidfTransformer(use_idf=False).fit(train_x_counts)
train_x_tf = tf_ts.transform(train_x_counts)
print("run1")
#训练
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(train_x_tf, classall)
print("run2")
#分类
new_text = ["房间 有鬼", "爱情 等待"]
new_x_counts = count_vect.transform(new_text)
new_x_tfidf = tf_ts.transform(new_x_counts)
predicted = clf.predict(new_x_tfidf)
print(predicted)
