#a material section cleaner script                      
import spacy 
# Load English tokenizer, tagger,  
# parser, NER and word vectors 
nlp = spacy.load("en_core_web_sm")
import re
import nltk
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from string import punctuation
from nltk.stem import PorterStemmer 
ps = PorterStemmer()

f=open('stemmeshfinal.txt','r',encoding='utf8')
contents = f.read().lower()
f.close()
contents = contents.split()    
stop_words = stopwords.words('english') + list(punctuation) + list(contents) + ['','»','’','O.lM','/mg','â€Ÿs','•','/mg-','/ml','-up','\'7gre','\'la.ter','-70°C','¢','F.','T.','','root',':250','°/o','stem','®','™','-1','lmM','i.e','U.K','ng/ml','g/L','w.r.t','.A','P.','/m','Gujarat','Co.','Corp.','E.','St.','Dr.','Ltd.','Inc','U.S.A.','','°C','S.','M.','Prof.','-20°C','C.','U.S.A','·','-3','±','L.','A.','‘','-2','N-','J.','K.','Co.Usa','','~g/ml','O.D','D.','J.l','O.lM','B.']
remwords=['','»','’','O.lM','/mg','â€Ÿs','•','/mg-','/ml','-up','\'7gre','\'la.ter','-70°C','¢','F.','T.','','root',':250','°/o','stem','®','™','-1','lmM','i.e','U.K','ng/ml','g/L','w.r.t','.A','P.','/m','Gujarat','Co.','Corp.','E.','St.','Dr.','Ltd.','Inc','U.S.A.','','°C','S.','M.','Prof.','-20°C','C.','U.S.A','·','-3','±','L.','A.','‘','-2','N-','J.','K.','Co.Usa','','~g/ml','O.D','D.','J.l','O.lM','B.']    
                      
#a material section string is given

class cleaner(object):
	def __init__(self, material):
		self.material = material

	def tokenise(self):
	    wospl = self.material.split('. ')
	    wojoi = ','.join(wospl)
	    wospl = wojoi.split(',')
	    wojoi=' '.join(wospl)
	    token = nltk.word_tokenize(wojoi)
	    return token

	def regsub_clean(self):
	    li=[]
	    for word in self.material:
	        word=re.sub('^[¢»®™•°/’!"#$%&\€Ÿ\'()*+,-./:;<=>?@[\]^_`{|}~\“\”]+',' ',word)
	        word=re.sub('[¢»®™•°/’!"#$%&\€Ÿ\'()*+,-./:;<=>?@[\]^_`{|}~\“\”]+$',' ',word)
	        #word=re.sub('^[¢»®™•°/’!"#$%&\\'()*+,-./:;<=>?@[\]^_`{|}~\“\”]{1,6}[0-9]+$','',word)
	        word=re.sub('^[¢»®™•°/’!"#$%&\\'()*+,-./:;<=>?@[\]^_`{|}~\“\”0-9]+$',' ',word)
	        #word=re.sub('^[0-9]{4,8}?.+','',word) 
	        if re.search('^[0-9x./]+[a-z]?[a-z]?',word):
	            continue 
	        elif word == '':
	            continue
	        elif re.search('m[mlin]{0,3}/[cmlin]+|fig',word):
	            continue
	        elif re.search('^[μ]',word):
	            continue  
	        elif re.search('[~°]',word):
	            continue
	        elif re.search('[\.-/_]{2,}',word):
	            continue
	        elif (len(word)<=2):
	            continue
	        elif (len(word)>45):
	            continue
	        elif len(word)<=5 and re.search('^.[-/_\.].[-/_\.].$|^.[-/_\.].$',word):
	            continue  
	        li.append(word)        
	    lis = [ word for word in li if not word in remwords]
	    return lis



	def lemm(self):
	    words = [word for word in self.material if not ps.stem(word.lower()) in stop_words]
	    return words

	#removes word with the help of spacy library and gives final result
	def spac(self): 
	    if self.material is None:
	        return self.material
	    new=[]
	    for item in self.material:
	        doc = nlp(item)
	        tok = [token.text for token in doc if not token.pos_ == "VERB"]
	        tok = ''.join(tok)
	        new.append(tok)
	    return new
	    

	def rem_af_spac(self):
	    li=[]
	    for word in self.material:
	        word=re.sub('^[¢»®™•°/’!"#$%&\€Ÿ\'()*+,-./:;<=>?@[\]^_`{|}~\“\”]+','',word)
	        word=re.sub('[¢»®™•°/’!"#$%&\€Ÿ\'()*+,-./:;<=>?@[\]^_`{|}~\“\”]+$','',word)
	        word=re.sub('^[¢»®™•°/’!"#$%&\\'()*+,-./:;<=>?@[\]^_`{|}~\“\”0-9]+$','',word)
	        word=re.sub('^[0-9]{4,8}?.+','',word) 
	        if re.search('^[0-9]+$',word):
	            continue 
	        elif word == '':
	        	continue
	        elif re.search('m[mlin]{0,3}/[cmlin]+',word):
	            continue
	        elif re.search('^[μ]',word):
	            continue              
	        elif (len(word)<=2):
	            continue
	        elif (len(word)>45):
	            continue
	        li.append(word) 
	    return li
                      
