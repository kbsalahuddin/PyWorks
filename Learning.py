'''''''''
def beef():
    print('A,B,C,D')

def tk_to_usd(tk):
    amount = tk/80
    print('$',amount, 'USD')
tk_to_usd(3000)
'''''
'''''''''''
def allowed_dating_age(my_age):
    girl_age= (my_age / 2) + 7
    return girl_age
my_limit = allowed_dating_age(25)
print('I can date girls age of',my_limit,'or older')
'''
''''''''''
def get_gender(sex='unknown'):
    if sex is 'm':
        sex='male'
    elif sex is 'f':
        sex='female'
    print(sex)
get_gender('m')
get_gender('f')
get_gender()
'''''
'''''''''
a = 123
def corn():
    print(a)
def fudge():
    print(a)
corn()
fudge()
'''
'''''''''
def func(name='Khalid', action='ate', item='tuna'):
    print(name, action, item)
func()
func('Sally', 'farts', '...ok')
func(item='pie')
func(name='becky',item='salad')
'''
'''''''''
#felxible number of arguments code
def add_numbers(*args):
# *args can be named *anything
  total = 0
  for a in args:
      total += a
      print(total)
add_numbers(3,2323,44)
'''
'''''''''
#unpacking arguments
def health_cal(age, fruit, cigs):
    answer =(100-age)+(fruit*3.5)-(cigs*2)
    print(answer)
my_data=[27,9,10]
health_cal(my_data[0], my_data[1], my_data[2])
health_cal(*my_data)
'''
'''''''''
#walmart
groceries = {'cereal','butter','tomato','chips','tape','tissue box'}
print(groceries)
if 'milk' in groceries:
    print('you already have milk')
else:
    print('you need to buy milk')
'''
'''''''''
classmates ={'tom':' cool','yan':' eater','ron':' brilliant','vlad':' bully'}
print(classmates)
print(classmates['vlad'])

for k,v in classmates.items():
    print(k+v)
'''
'''''''''
#creating module
import Tuna
import random

Tuna.fish()

x = random.randrange(1, 100)
print(x)
'''

'''''''''
#download an image from web
import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name)+ '.jpg'
    urllib.request.urlretrieve(url,full_name)
download_web_image("https://pre00.deviantart.net/41a3/th/pre/f/2016/356/3/2/battle_ready_by_bleachmore-dashus4.png")
'''
'''''''''
#how to read/write files
fw = open('sample.txt', 'w') #fw for file opening variable
fw.write('A B C D E\n')
fw.write('2nd line\n')
fw.close()
fr = open('sample.txt', 'r')
text_read_str_var_save=fr.read()
print(text_read_str_var_save)
fr.close()
'''
''''
#dwnld a file from web
from urllib import request
goog_url= "https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1511439356&period2=1514031356&interval=1d&events=history&crumb=y4YI13/aGeH"
def download_stock_date(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url= r'goog.csv'
    fw = open(dest_url,'w')
    for line in lines:
        fw.write(line + '\n')
    fw.close()
download_stock_date(goog_url)
'''
'''''''''
#web crawler
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page =1
    while page<= max_pages:
        url = "https://readms.net/manga"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll("a",{"class":"chapter-link"}):
            href = "https://readms.net" + link.get('href')
            title = link.string
            print(href)
            print(title)
        page+=1
trade_spider(1)
'''''
'''''''''
#dynamic web_crawler
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page =1
    while page<= max_pages:
        url = "https://readms.net/manga"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll("a",{"class":"chapter-link"}):
            href = "https://readms.net" + link.get('href')
            title = link.string
            print(href)
            print(title)
            get_single_item_data(href)
        page+=1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll("th", {"class":"row content"}):
        print(item_name.string)
trade_spider(3)
'''''
'''''''''
#Classes & Objs
class Enemy:
    life = 3
    def attack(self):
        print('ouch!')
        self.life -=1
    def checkLife(self):
        if self.life <= 0:
            print("i'm dead!")
        else:
            print(str(self.life) + " life left")
enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()
'''''
'''''''''
#init
class Tuna:
    def __init__(self):
        print('Hey!')
    def swim(self):
        print('I am swimming!')
flipper = Tuna()
flipper.swim()
#Ex-2
class Enemy:
    def __init__(self,x):
        # __init__(self,parameter1)=oop constructor
        self.energy = x
    def get_energy(self):
        print(self.energy)
jason = Enemy(5)
sandy = Enemy(18)
jason.get_energy()
sandy.get_energy()
'''''
'''''''''
#classes vs instance var
class Girl:
    gender = 'female'
    def __init__(self,name):
        self.name = name
r = Girl('Rachel')
s = Girl('Sally')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)

#inheritance
class Parent():
    def print_last_name(self):
        print('Roberts')
class Child(Parent):
    def print_first_name(self):
        print('Bucky')
    def print_last_name(self):
        print('Sanders')
bucky = Child()
bucky.print_first_name()
bucky.print_last_name()

#multiple inheritance
class Mario():
    def move(self):
        print('Hola!')
class Shroom():
    def eat_shroom(self):
        print('i am now big!')
class bigMario(Mario, Shroom):
    pass #you need a line to avoid syntax error
bm = bigMario()
bm.move()
bm.eat_shroom()
'''
'''''''''
#Threading
#when multiple things works at the same time
import threading
class messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
x = messenger(name = 'send out msgs')
y = messenger(name = 'receive msgs')
x.start() #start goes to class and look for run
y.start()
'''''
'''
#word counter
import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for headline_text in soup.findAll('a', {'class': 'chapter-link'}):
        content = headline_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "~!@#$%^&*()[]{}_+`-=,.<>/?;:'\""
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            #print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)
def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key,'--', value)
start('https://readms.net/manga')
# start('https://seattle.craigslist.org/search/jjj')
'''
'''''''''
#unpacking list/tuples
date,name,price = ['1/1/2017', 'Milk', '$9.99']
print(name)

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle)/ len(middle)
    print(avg)
drop_first_last([66,45,89,99,70])
'''
'''''''''
#zip file = combining two lists
first = ['Bucky', 'Tom', 'Tim']
last = ['Arren', 'Boss', 'Lard']
names = zip(first, last)
for a, b in names:
    print(a,b)
'''
'''''''''
#lambda = small function who has no name 
answer = lambda x: x*7
print(answer(4))
'''
'''''''''
#min,max,sort dictionary
stocks = {'GOOG': 520.23,
          'FB': 200.25,
          'AMZN': 120.00,
          'APL': 456.89,
          'AOL': 456.89
          }
print(sorted(zip(stocks.values(), stocks.keys())))
'''
'''''''''
#Pillow = to open picture through python
from PIL import Image
imageObj = Image.open('goku.jpg')
print(imageObj.size)
print(imageObj.format)
imageObj.show()
'''
'''''''''
#cropping image
from PIL import Image
img = Image.open('goku.jpg')
area = (100, 100, 200, 200)
cropped_goku = img.crop(area)
img.show()
cropped_goku.show()
'''
'''''''''
#combining images
from PIL import Image
two = Image.open('goku.jpg')
one = Image.open('gokuvegetaberuss.jpg')
print(one.size)
print(two.size)
area = (490,400)
one.paste(two,area)
one.show()
'''''
'''''''''
#individual channels
from PIL import Image
one = Image.open('goku.jpg')
print(one.mode) #Ans:RGB
r,g,b = one.split()
r.show()
g.show()
b.show()
'''
'''''''''
#Merging image channels = needs two similar sized pics
from PIL import Image
two = Image.open('goku.jpg')
one = Image.open('gokuvegetaberuss.jpg')
r1,g1,b1 = one.split()
r,g,b = two.split()

newImg = Image.merge('RGB',(r,b1,g))
newImg.show()
'''''
'''''''''
#image transformations
from PIL import Image

one = Image.open('goku.jpg')
oneRes = one.resize((514,238))
oneFlip = one.transpose(Image.FLIP_LEFT_RIGHT)
oneSpin = one.transpose(Image.ROTATE_90)
one.show()
oneRes.show()
oneFlip.show()
oneSpin.show()
'''''
'''''''''
#modes and filters
from PIL import Image
from PIL import ImageFilter

one = Image.open('goku.jpg')
oneConvert = one.convert('L')
#L=black&white
oneConvert.show()
print(oneConvert.mode)
#to confirm the change of the color format
oneBlur = one.filter(ImageFilter.BLUR)
oneBlur.show()
oneEdges = one.filter(ImageFilter.FIND_EDGES)
oneEdges.show()
oneDetail = one.filter(ImageFilter.DETAIL)
oneDetail.show()
'''''
''''
#struct
from struct import *

# Store as bytes data for to send through network
packData = pack('iif',6,19,4.73)
#iif=2int+1float
print(packData)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))
#get data back to normal
originalData = unpack('iif',packData)
print(originalData)
#another way to do so
print(unpack('iif',b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))
'''''
'''''''''
#map function

income = [10,30,75]
def double_money(dollars):
    return dollars * 2
new_income = list(map(double_money, income))
print(new_income)
'''
'''''''''
#bitwise operator
a=20
b=30
c=a & b #binary addition
print(c)
#binary right shift
x=240
y=x>>2
print(y)
#finding largest or smallest items
import heapq
#heapq=heap algo
grades = [32,43,654,34,132,66,99,532]
print(heapq.nlargest(3,grades))

stocks = [
    {'ticker':'APL','price':201},
    {'ticker':'BPL','price':209},
    {'ticker':'CPL','price':301},
    {'ticker':'DPL','price':101},
    {'ticker':'EPL','price':401}
]
print(heapq.nsmallest(3,stocks,key=lambda stock: stock['price']))
'''''
'''''''''
#dictionary calculations
stocks={'GOOG':400,
        'AAPL':365,
        'FB':245,
        'AMZN':321,
        'MSFT':112
        }
minPrice=min(zip(stocks.values(),stocks.keys()))
print(minPrice)
'''''
'''
#finding most frequent words
from collections import Counter
text = "The details of my project works including the thesis and the technical expertise are described in the attached resume."\
 "I believe that my enthusiasm and strong motivation can actively contribute to Your research."\
 "I hope that you would find my credentials fitting to the impressive standard of Your group and consider"\
 "my application for a graduate student position."
words = text.split()
counter = Counter(words)
topThree = counter.most_common(4)
print(topThree)
'''
#ditionary multiple key sort
from operator import itemgetter
user =[
{'fname':'Harry','lname':'Kane'},
{'fname':'Barry','lname':'Mane'},
{'fname':'Larry','lname':'Sane'},
{'fname':'Parry','lname':'Oane'},
{'fname':'Farry','lname':'Jane'},
{'fname':'Garry','lname':'Dane'},
{'fname':'Jarry','lname':'Pane'},
{'fname':'Tarry','lname':'Ane'},
{'fname':'Sorry','lname':'Kane'},
{'fname':'Harry','lname':'Bane'}
    ]
for x in sorted(user, key=itemgetter('lname')):
    print(x)
print('---------')
for x in sorted(user, key=itemgetter('fname','lname')):
    print(x)