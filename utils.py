from nltk.stem.snowball import SnowballStemmer

def readfile(filename):
    try:
        file = open(filename,"r",encoding="utf-8")
        lines = file.readlines()
        file.close()
        tostr=''
        for i in lines:
            tostr+=i
        return tostr
    except:
        return ''

def cleanString(strin,keepAccents=False): #strin = string input
    
    rimpiazzi = {
        "[$&+:;=?@#|'<>^*()%!-].,\"" : "",
        "áâäàã" : "a" , "ÁÂÄÀÃĀ" : "A",
        "éêëè" : "e" , "ÉÊËÈ" : "E",
        "íîïì" : "i" , "ÍÎÏÌ" : "I", 
        "óôöòõ" : "o" , "ÕÒÖÔÓ" : "O", 
        "úûüù" : "u" , "ÙÜÛÚ" : "U" 
    }
    
    if keepAccents:
        rimpiazzi = { list(rimpiazzi.keys())[0] : "" }

    newstring=''    
    
    for c in strin:
        trovato=False
        for i,j in rimpiazzi.items():
            if c in i:
                newstring += j
                trovato=True
        if not trovato:
            newstring+=c

    return newstring.lower()

#converte un file in un set senza parole duplicate
def file_to_set(filename : str,lang = "italian") -> set:
    st = SnowballStemmer("italian", ignore_stopwords = True)

    text  = readfile(filename)

    ctext = cleanString(text)
    ctext = ctext.replace("\n"," ")

    wset = set()

    for word in ctext.split(" "):
        sword = st.stem(word) #sword = stemmed word
        if len(sword) == 0 or sword in wset:
            continue
            
        wset.add(sword)
    
    return wset

def confront_sets(s1 : set, s2 : set):
    return len(s1.intersection(s2)) / len(s2)