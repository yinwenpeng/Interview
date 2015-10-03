
def word2key(word):
    return ''.join(sorted(map(lambda x:x, word)))

def anagram(dicFile):

    readFile=open(dicFile,'r')
    key2cluster={}
    vocab=[]
    for line in readFile:
        word=line.strip()
        vocab.append(word)
        key=word2key(word)
        cluster=key2cluster.get(key)
        if cluster is None:
            cluster=set()

        cluster.add(word)
        key2cluster[key]=cluster
    readFile.close()
    
    writeFile=open('word2anagram.txt','w')
    for word in vocab:
        key=word2key(word)
        cluster=key2cluster.get(key)
        cluster.remove(word)

        writeFile.write(word)
        if len(cluster)>0:         
            for word in cluster:
                writeFile.write(' '+word)
        writeFile.write('\n')

            
    writeFile.close()
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    anagram('word_list_word2vec.txt')

