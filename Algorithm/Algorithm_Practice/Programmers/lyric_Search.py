# Problem : https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3
# Ref : https://blog.ilkyu.kr/entry/파이썬에서-Trie-트라이-구현하기
# 2020 Kakao Blind Recuritment
# Tag : Trie 

from collections import defaultdict
class Node:
    def __init__(self,key,children):
        self.key = key
        self.children = children



def solution(words,queries):
    def InsertNode(head,word):
        curr_node = head
        wordptr = 0
        while curr_node:
            if wordptr == len(word):
                return 0
            
            letter = word[wordptr]
            if letter in curr_node.children.keys():
                # Go Next Node
                curr_node = curr_node.children[letter]
            else:
                # Insert Node
                curr_node.children[letter] = Node(key=letter,children={})
                # Go Next
                curr_node = curr_node.children[letter]   
            
            #Increase Word Pointer
            wordptr +=1
    def SearchWord(head,query):
        curr_node = head 
        wordptr = 0
        while curr_node:
            if wordptr == len(query):
                return
        
            if curr_node.key == query[wordptr]:
                print(curr_node.key)
                wordptr+=1
                if len(curr_node.children.keys()) > 0:
                    curr_node = curr_node.children[query[wordptr]]
                else:
                    return
            else:
                curr_node = curr_node.children[query[wordptr]] 

    Trie = Node(key=None,children = {})
    InsertNode(Trie,words[0])
    SearchWord(Trie,words[0])


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]	

solution(words,queries)