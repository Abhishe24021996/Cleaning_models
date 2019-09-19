# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 00:33:48 2019

@author: Abhis
"""

import nltk 
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from string import punctuation
import re
ps = PorterStemmer()

class product_dict_cleaner(object):
        
      
    with open('productnamescleaner.txt','r') as fp:
        lines=fp.read().lower().split()
    clean_n = set(' '.join(lines).split())

    with open('category.txt','r') as f:
    	lines = f.read().lower().split()
    category = set(' '.join(lines).split())

    with open('brand.txt','r') as f:
    	lines = f.read().lower().split()
    brand = set(' '.join(lines).split())

    combine = list(clean_n) + list(brand) + list(category)


    stop_words = stopwords.words('english')+list(punctuation)
    reg = '^[¢‘»®™•°/’!"#$%&\€Ÿ\'()*+\,\,-./:;<=>?@[\]^_`{|}~\“\”]+' # removes from start
    reg1 = '[¢‘»®™•°/’!"#$%&\€Ÿ\'()*+\,\,-./:;<=>?@[\]^_`{|}~\“\”]+$' # removes from end
    reg2 = '^[¢‘»®™•°/’!"#$%&\\'()*+\,\,-./:;<=>?@[\]^_`{|}~\“\”0-9]+$' # if word only had these
    remove_reg = "[!$=?@^~°*º]" 
    ps = PorterStemmer()
    
    with open('stemmeshfinal.txt','r') as f:
        content = f.read().split()
    
    with open('stemplus.txt','r') as f:
        content1 = f.read().split()

    @classmethod
    def pre_clean(cls, text):
        words = text.split(' ')
        #word = [w for w in words if not w.lower() in clean_n]
        final=[]
        for item in words:
            if '/' in item:
                woli = item.split('/')
                new=[]
                for it in woli:
                    if it in cls.clean_n:
                        continue
                    else:
                        new.append(it)
                final.append('/'.join(new))
            else:
                final.append(item)
        wojoi = ' '.join(final)
        return wojoi


    @classmethod
    def tokenise(cls, text):
        mat = nltk.word_tokenize(text)
        mat = ' '.join(mat)
        mat = re.split(r"[:+\.\s|]|\b[0-9]?[a-z]?\'[a-z]?[0-9]?\b|\b[a-z]?\,[a-z]?\b",mat)
        return mat

    @classmethod
    def rem_stopwords(cls, text):
        mat = list(set([w for w in text if not w in cls.stop_words]))
        return mat

    @classmethod
    def rem_reg(cls, text):
        mat1=[]
        for w in text:
            if w=='':
                continue
            w = re.sub("(\'s)$",'',w)
            w = re.sub("(\`s)$",'',w)
            w = re.sub(cls.reg,'',w)
            w = re.sub(cls.reg1,'',w)
            w = re.sub("[\‟\′\'�_]",'',w)
            w = re.sub(cls.reg2,'',w)
            if re.search(cls.remove_reg,w):
                continue
            elif re.search('[mk]?[cmlgin]{0,3}/[mk]?[cmlgin]{0,3}|fig',w):
                continue
            elif re.search('^(.[/-_])+.?$',w):
                continue
            elif 3<=len(w)<45:
                w = re.sub("[\‟\′\'�_]",'',w)
                mat1.append(w)
        return mat1

    # @classmethod   
    # def rem_spac(cls,text):
    #     text = ' '.join(text)
    #     doc = cls.nlp(text)
    #     text1 =[token.text for token in doc if not token.pos_ == "VERB"] #in #['AFX','JJR','JJS','RBR','RBS','VBD','VBN']]
    #     return text1


    @classmethod
    def rem_dic_stem(cls,text):
        text = [ w for w in text if cls.ps.stem(w) not in cls.content]
        text = [w for w in text if w not in cls.content1]
        text = [w for w in text if w not in cls.combine]
        return text


    @classmethod
    def __run__(cls,id_pro_c):
        for key, value in id_pro_c.items():
            mat = cls.pre_clean(text =value.lower())
            mat = cls.tokenise(text=mat)
            mat = cls.rem_stopwords(text=mat)
            mat = cls.rem_reg(text=mat)
            # mat = cls.rem_spac(text=mat)
            mat = cls.rem_dic_stem(text=mat)
            # mat = cls.join_words(text=mat)
            id_pro_c[key] = mat
        return id_pro_c
