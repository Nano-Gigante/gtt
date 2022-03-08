from utils import *
import os

class gtt:
    
    def __init__(self,lang="italian"):
        self.topics = {}
        self.lang = lang

    def train(self,filename : str) -> None:
        wset = file_to_set(filename)
        topicname = filename.split("/")[-1].replace(".txt","") 
        
        self.topics[topicname] = wset

    def guess_the_topic(self,filename,vb = False):
        iset = file_to_set(filename,self.lang)

        scores = { name : confront_sets(iset,self.topics[name]) for name in self.topics }

        mx = max(scores.values())
        ris = list(scores.keys())[ list(scores.values()).index(mx) ]

        if vb:
            for k,v in scores.items():
                print(f'{k if v != mx else k.upper()}: {v/mx*100}')
        
        return ris