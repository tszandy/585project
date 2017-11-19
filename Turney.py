import collections
import numpy as np
import json
import time


def read_amazon_review_detail(filename):
    allreviews=open(filename, 'r')
    reviews=[]
    for review in allreviews:
        reviews.append(json.loads(review))
    return reviews

def read_amazon_review(filename):
    reviews_detail=read_amazon_review_detail(filename)
    reviews=[]
    for review_detail in reviews_detail:
        reviews+=[review_detail['reviewText']]
    return reviews

def printword(pos_list,neg_list,reviews):
    countwords=collections.defaultdict(int)
    countreview_pos=0
    countreview_neg=0
    countword_pos=collections.defaultdict(int)
    countword_neg=collections.defaultdict(int)

    for review in reviews:
        words=review.split()
        postag=0
        negtag=0
        for i in pos_list:
            if i in review:
                postag=1
        for i in neg_list:
            if i in review:
                negtag=1
        if postag:
            countreview_pos+=1
        if negtag:
            countreview_neg+=1
        for word in words:
            if postag:
                countword_pos[word]+=1
            if negtag:
                countword_neg[word]+=1
            countwords[word]+=1
    for i in pos_list:
        if i in countwords:
            countwords.pop(i)
    for i in neg_list:
        if i in countwords:
            countwords.pop(i)

    droplist=[]
    for i in countwords:
        if countwords[i]<500:
            droplist.append(i)
    for i in droplist:
        countwords.pop(i)

    polarity={}
    for i in countwords.keys():
        countpos=1.0*(countword_pos[i]+1)/(countreview_pos+1)
        countneg=1.0*(countword_neg[i]+1)/(countreview_neg+1)
        polarity[i]=np.log(countpos/countneg)
    polarityitem=sorted(polarity.iteritems(), key=lambda (k,v): (v,k))
    posrange=polarityitem[::-1]
    negrange=polarityitem
    print('top 50 postive word:')
    for i in posrange[:50]:
        (a,b) = i
        print(a+','+str(b))
    print()
    print('top 50 negative word:')
    for i in negrange[:50]:
        (a,b) = i
        print(a+','+str(b))


def findword(word,reviews):
    count=0
    for review in reviews:
        words=review.split()
        if word in words:
            print(review)
            count+=1
        if count>=10:
            break
