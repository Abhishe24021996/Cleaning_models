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

def product_dict_cleaner(id_pro_c):
    
    with open('stemmeshfinal.txt','r') as f:
        contents = f.read().lower().split()      
    stop_words = stopwords.words('english') + list(punctuation) + list(contents) + [" "]  #+list(remwords) + ['','C','','’','•','¢','F.','T.','root','stem','®','™','Dancers','elastase','factor','actitvity','death','beta','chicken','receptor','speede','transcription','ligand','lysates','convertase','iqe','custom','kit','total','analysis','lisa','elisa','iqelisa','human','mouse','rat','cell','based','related','assay','array','recombinant','Infusion','Sporulation','B.','Greenland','Centrifuge','Resuspend','custom','kit','total','analysis','lisa','elisa','iqelisa','human','mouse','rat','cell','based','related','assay','array','recombinant','procured','.A','P.','/m','Gujarat','Co.','E.','St.','Dr.','Ltd.','Inc','U.S.A.','','°C','S.','M.',','B.']
    
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

   
    for key, value in id_pro_c.items():
        words = value.lower().split(' ')
        #word = [w for w in words if not w.lower() in clean_n]
        final=[]
        for item in words:
            if '/' in item:
                newword=[]
                woli = item.split('/')
                new=[]
                for it in woli:
                    if it.lower() in clean_n:
                        continue
                    else:
                        new.append(it)
                        if len(it)>2:
                            newword.append(it)
                final.append('/'.join(new))
                final.extend(newword)
            else:
                final.append(item)
        wojoi = ' '.join(final)
        token = nltk.word_tokenize(wojoi)

        words=[]
        for word in token:
            word=re.sub('^[¢»®™•°/’!"#$%&\€Ÿ\'()*+,-./:;<=>?@[\]^_`{|}~\“\”]+','',word)
            word=re.sub('[¢»®™•°/’!"#$%&\€Ÿ\'()*+,-./:;<=>?@[\]^_`{|}~\“\”]+$','',word)
            #word = re.sub('^[0-9]\/','',word)
            if re.search('^[¢»®™•°/’!"#$%&\\'()*+,-./:;<=>?@[\]^_`{|}~\“\”0-9]+$',word): #eliminate allpunctuation if only 
                continue
            elif re.search('^[¢»®™•°/’!"#$%&\\'()*+,-./:;<=>?@[\]^_`{|}~\“\”0-9]+..$',word): #eliminate allpunctuation if only 
                continue
            elif word == '':
                continue
            elif re.search('m[mlin]{0,3}/[cmlin]+',word):
                continue
            elif re.search('^[μ]',word):
                continue
            elif re.search('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~][A-Za-z0-9][!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~][A-Za-z0-9][!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]',word): #wliminates like #s#3$ #3#a@
                continue
            elif len(word)<=2:
                continue
            elif (len(word)>50):
                continue
            elif word:
                words.append(word) 
        words1 = [word for word in words if not ps.stem(word) in stop_words]
        words2 = [word for word in words1 if not word in combine]
        id_pro_c[key] = words2
    return id_pro_c
