'''''
#determines if all the numbers are different from each other:
my_list = [1, 2, 3, 4]

def check_list(arg):
    for i in arg:
        if arg.count(i) > 1:
            return 'Duplicate'

print(check_list(my_list) == 'Duplicate') #prints T/F answer

#create random strings using all the vowels atleast once:
import random
charlit=['a','e','i','o','u']
random.shuffle(charlit)
print(''.join(charlit))

#printing list in multiple columns:
data = [['a', 'b', 'c'], ['aaaaaaaaaa', 'b', 'c'], ['a', 'bbbbbbbbbb', 'c']]

col_width = max(len(word) for row in data for word in row) + 1  # padding
for row in data:
    print("".join(word.ljust(col_width) for word in row))
#printing data in neat tabular form:
from tabulate import tabulate
print(tabulate([['ManCity',50],['ManUtd',37],['Hotspur',35],
                ['Chelsea',35],['Liverpool',34],['Arsenal',31]],
               headers=['Team','Points']))

def remove_nums(int_list):
    position = 3-1
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (position+idx)%len_list
        print(int_list.pop(idx))
        len_list -= 1
remove_nums([10,20,30,40,50,60,70,80,90,100])

# 2 lists are joined together:
a = ['a',1]
b = ['b',2]
print(tabulate([name_list,roll_list],headers=['name','roll number']))

#finding 3 unique numbers sum=0 in an array:
x = [1, -6, 4, 2, 5, -2, 0, 3, 0]
x.sort()
print('sorted:',x)
res=[]
for i in range(len(x)):
    j=i+1
    k=len(x)-1
    while(j<k):
        sum2=x[i]+x[j]
        if(sum2+x[k]<0):
            j+=1
        elif(sum2+x[k]>0):
            k-=1
        else:
            res.append(x[i])
            res.append(x[j])
            res.append(x[k])
            j+=1
            k-=1
print('Result:',res)

# 3 digit number combo:
numbers=[]
for num in range(1000):
    num=str(num).zfill(3)
    numbers.append(num)
print(numbers) #ans:000-999 all in a single row
print(num) #Ans:999

#print a long text,convert the str to a list and print all the words
#and their frequecies:
string_words = United States Declaration of Independence
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
print('word frquencies:\n {}'.format(str(list(zip(word_list,word_freq)))))

#count each character of a any/text file:
with open('practice.py') as infile:
    words = 0
    characters = 0
    for lineno, line in enumerate(infile, 1):
        wordslist = line.split()
        words += len(wordslist)
        characters += sum(len(word) for word in wordslist)

print(lineno)
print(words)
print(characters)

#get the top stories from google:(could not run)
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
news_url='https://news.google.com/news/?ned=us&gl=US&hl=en'
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()
soup_page=soup(xml_page,'xml')
news_list=soup_page.findAll('item')
for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)

#get a list of locally installed python modules:
import pip
import textwrap
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
for i in installed_packages])
print(installed_packages_list)

#YAHOOO!!!!
#take user inputs as strs
#convert'em to ints
#matke 2 sepr list
#zips and shows in tabular form with col heading
from tabulate import tabulate
a=[]
b=[]
inp=str(input('enter names:'))
names=inp.split(',')
for i in names:
    a.append(i)
print(a)

inp1=input('enter numbers:')
numbers=list(inp1.split(','))
for j in numbers:
    b.append(j)
print(b)
print(tabulate(list(zip(a,b)),headers=['Name','Number']))

#Aubameyang
from tabulate import tabulate
print("\nAubameyang's Last 10 games for B.Dortmund\n" )
print('~'*64)
print('~'*64)
AubaTable = (tabulate([['Frankfurt','A', 0, 0, 6.42],
                ['Hannover 96', 'A', 0, 0, 6.09],
                ['APOEL', 'H', 0, 0, 6.63],
                ['B.Munich', 'H', 0, 0, 6.16],
                ['Hotspur', 'H', 1, 0, 6.74],
                ['Schalke 04', 'H', 1, 1, 7.07],
                ['R.Madrid', 'A', 2, 0, 7.86],
                ['Bremen', 'H', 1, 0, 7.08],
                ['Mainz', 'A', 0, 1, 7.3],
                ['Hoffenheim', 'H', 1, 0, 6.89]],
                headers = ['Opposition','Home/Away','Goals','Assits','Ratings'],
                tablefmt = 'orgtbl'))
print(AubaTable)
'''''
#ROCK PAPERS SCISSORS GAME:
from random import randint
print("\nLet's Play ROCK PAPERS SCISSORS !!!!!!!")
print('''RULES:
        1.Rock Blunts Scissors..So Rock Wins
        2.Rock get covered by Paper...So Paper Wins
        3.Scissors cuts Papers...So Scissors Win\n''')
player = input('Rock(r),Paper(p),Scissors(s)?')
if player == 'r':
       print('000', 'vs', end=' ')
elif player == 'p':
       print('___', 'vs', end=' ')
else:
       print('8< 8< 8<', 'vs', end=' ')
chosen = randint(1,3)
#print(chosen)
if chosen == 1:
       computer = 'r'
       print('000')
elif chosen == 2:
       computer = 'p'
       print('___')
else:
       computer = 's'
       print('>8 >8 >8')
if player == computer: print('It\'s a Draw!!')
elif player == 'r' and computer == 'p': print('Computer Wins!!')
elif player == 'p' and computer == 'r': print('Player Wins!!')
elif player == 'r' and computer == 's': print('Player Wins!!')
elif player == 's' and computer == 'r': print('Computer Wins!!')
elif player == 's' and computer == 'p': print('Player Wins!!')
elif player == 'p' and computer == 's': print('Computer Wins!!')
else: print('NO GAME')