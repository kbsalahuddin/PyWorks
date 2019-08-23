'''''''''
from collections import Counter

file=open('C:\\Users\\home\\Desktop\\new.txt','r')
wordcount=[]
reading=file.read().split()
for item in reading:
    wordcount.append(item)
    #symbols="~!@#$%^&*()[]{}_+`-=,.<>/?;:'\""

print('\n',wordcount,'\n')


file.close()

with open('new.txt') as infile:
    words = 0
    characters = 0
    for lineno, line in enumerate(infile, 1):
        wordslist = line.split()
        words += len(wordslist)
        characters += sum(len(word) for word in wordslist)

print(lineno)
print(words)
print(characters)
'''''
#print a long text,convert the str to a list and print all the words
#and their frequecies:
'''string_words =United States Declaration of Independence
From Wikipedia, the free encyclopedia
The United States Declaration of Independence is the statement
adopted by the Second Continental Congress meeting at the Pennsylvania State
House (Independence Hall) in Philadelphia on July 4, 1776, which announced
that the thirteen American colonies, then at war with the Kingdom of Great
Britain, regarded themselves as thirteen independent sovereign states, no longer
under British rule. These states would found a new nation – the United States of
America. John Adams was a leader in pushing for independence, which was passed
on July 2 with no opposing vote cast. A committee of five had already drafted the
formal declaration, to be ready when Congress voted on independence.(add triple quote marks before and after)
word_list=string_words.split()
word_freq=[word_list.count(n) for n in word_list]
#print('String:\n{} \n'.format(string_words))
print('List:\n{} \n'.format(str(word_list)))
print('word frquencies:\n {}'.format(str(list(zip(word_list,word_freq)))))'''

from collections import Counter
text = "The details of my project works including the thesis and the technical expertise are described in the attached resume."\
 "I believe that my enthusiasm and strong motivation can actively contribute to Your research."\
 "I hope that you would find my credentials fitting to the impressive standard of Your group and consider"\
 "my application for a graduate student position."
words = text.split()
counter = Counter(words)
topThree = counter.most_common(4)
print(topThree)

