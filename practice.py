'''''''''
poem='Twinkle, twinkle, little star,'\
     '\n\tHow I wonder what you are!' \
     '\n\t\tUp above the world so high,'\
     '\n\t\tLike a diamond in the sky.'\
    '\nTwinkle, twinkle, little star,'\
              '\n\tHow I wonder what you are'

print(poem)

#sys info print
import sys
print('Python version')
print(sys.version)
print(sys.version_info)

#date and time
import datetime
now=datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print(now.strftime('%H:%M:%S'))

#circle area with radius being user inputted
from math import pi
r=float(input('please, enter the radius:'))
radiusq=(r**2)
Carea=3.1416*(radiusq)
print('Area of the circle is:',Carea,'where radius is:',r)

#printing user's last-first name from input
fname=input('Your first name --')
lname=input('Your last name --')
print("User\'s name:",lname,",",fname,"." )

#tuple and list from input
values=input("give us some numbers seperated by comma:")
list=values.split(",")
tuple=tuple(list)
print('list:',list)
print('tuple:',tuple)

#printing the extension of a file from user
filename=input('your file :')
file_ext=filename.split('.')
print('extension of the file:',repr(file_ext[-1]))

#1st&last print
color_list=['R','G','B','Y','W']
print('first and last color:',color_list[0],'&',color_list[-1])

#time printer
exam_st_date=(11,12,2014)
print("exam start time: %i/%i /%i"%exam_st_date)

#taking an int input in int and do math
a=int(input('put your number:'))
n1=int('%s' % a) #5
n2=int('%s%s' % (a,a)) #55
n3=int('%s%s%s' % (a,a,a)) #555
print(n1+n2+n3) #5+55+555=615

#a Python program to print the documents 
#(syntax, description etc.) of Python built-in
#function(s)
print(abs.__doc__)

#print the calendar
import calendar
y=int(input('input year:'))
m=int(input('input month:'))
d=int(input('input day:')) #will print the exact day and yesterday column
#print(calendar.month(y,m,w=0,l=0)) #w,l not important
print(calendar.month(y,m,d))#y,m will print the full month

#printing string
words=input('a string that you "don\'t" have to escape'\
            '\nThis'\
            '\nis a ..... multi-line'\
            '\nheredoc string ------> example')
print(words)

#diff between two dates
from datetime import date
date1=date(2014,7,2)
date2=date(2014,6,11)
diff=date1-date2
print(diff)

#vol. of sphere
from math import pi
a=float(input('your given radius value:'))
radq=a**3
vol_of_sphere=(4/3)*3.1416*radq
print('sphere vol. is:',vol_of_sphere,'when radius:',a)

#math
a=float(input('enter a number:'))
if  a <= 17:
    b = float(17-a)
    print(b)
else:
    c=float((a-17)*2)
    print(c)
'''''
'''''''''
#finding a number's range
a=float(input('enter a number:'))
if a>=900 and a<=2000:
    print('the number:',a,'is in the range')
else:
    print('out of range input')

#same question as above but diff answer
#ans gives in t/f fashion
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000)) #true
print(near_thousand(900))  #t
print(near_thousand(800))  #f
print(near_thousand(2200)) #f

#more math
print('give three numbers:')
nu1=float(input('1st:'))
nu2=float(input('2nd:'))
nu3=float(input('3rd:'))
sum=nu1+nu2+nu3
if nu1==nu2==nu3:
    mat=float(sum*3)
    print('equal\'s answer:',mat)
else:
    avg=float(sum/3)
    print('average:',avg)

#19 string check and op
#adding "is" infront of the sentence
def changeString():
   give = str(input("Give me a sentence: "))
   if give[:2] == "Is":
       print(give)
   else:
       new = "Is %s" %give
       print(new)
changeString()

#printing multiple copies of a string
def larger_string(str,n):
    result=''
    for i in range(n):
        result=result+str
    return result
print(larger_string('abc',2))
print(larger_string('Hey',3))

#even/odd checker:
def even_odd():
    inp=float(input('enter any number:'))
    check_even=float(inp%2)
    if check_even==0:
        print('your number:',inp,',is an even number')
    else:
        print('your number:',inp,',is an odd number')

even_odd()

#finds&counts the no.4 in a list
def list_count_4(nums):
    count=0
    for num in nums:
        if num==4:
            count +=1
    return count
print(list_count_4([1,2,4,3,5,6,7,4,8,9,4,10]))

#str len>2 print 1st two aplha
#str len<2 print n times
strg=str(input('give any string:'))
if len(strg)<2:
        print(strg*3)
else:
    twoAlphs=strg[:2]
    print(twoAlphs)

#vowel checker
vowels=['a','e','i','o','u']
inp=str(input('pls, enter a letter:'))
if inp in vowels:
    print('the letter you entered:',inp,',is a vowel')
else:
    print('your letter:',inp,',is a consonent')

#t/f if a number in a list:
def is_grp_member(grp_data,n):
    for value in grp_data:
        if n==value:
            return True
    return False
print(is_grp_member([1,5,8,3],3))
print(is_grp_member([1,5,8,3],-1))

#histogram
def histogram(items):
    for n in items:
        output=''
        times= n
        while(times>0):
            output += '*'
            times -= 1
        print(output,n)
print('HISTOGRAM')
histogram([2,10,4,6,9])

#concatenating list into a single string
def concatenate_list_data(list):
    result=''
    for junk in list:
        result += str(junk)
    return result
print(concatenate_list_data([1,22,3,4,5,6]))

#printing even no.'s until a certain no. comes up.
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
for x in numbers:
    if x%2 == 0 :
        print(x)
        x += 1
    else:
        if x == 237:
            break

#printing set element in a set which is not found in second set
color_list_1=set(['White','Black','Red'])
color_list_2=set(['Red','Green'])
print(color_list_1.difference(color_list_2))
#or in list print:
print([c for c in color_list_1 if c not in color_list_2] )

#triangle area:
base=float(input('pls, enter the base value:'))
height=float(input('now, enter the height:'))
Tarea=float((0.5)*base*height)
print('When, height:',height,'and base:',base)
print('triangle area:',Tarea)

#gcd code:
def gcd():

    num1=int(input('number one:'))
    num2=int(input('number two:'))
    if num1%num2==0:
       return num2
    for k in range(int(num2/2),0,-1):#range(start,end,step)
           if num1%k==0 and num2%k==0:
               gcd = k
               break
    print(gcd)
gcd()

#lcm code:
def lcm():
    one=int(input('1st number:'))
    two=int(input('2nd number:'))
    if one>two:
        z=one
    else:
        z=two
    while(True):
        if ((z%one==0) and (z%two==0)):
            lcm=z
            break
        z+=1
    print('lcm:',lcm)
lcm()

#math
def three_numbers():
    x = int(input('1st number:'))
    y = int(input('2nd number:'))
    z = int(input('3rd number:'))
    if x==y or x==z or y==z:
        sum = 0
        print('since any two integers are equal, sum =',sum)
    else:
        sum = x+y+z
        print('sum =',sum)
three_numbers()

#math
def three_numbers():
    x = int(input('1st number:'))
    y = int(input('2nd number:'))
   # z = int(input('3rd number:'))
    if x+y>15 and x+y<20:
        sum = 20
        print('since 15<sum<20 , sum =',sum)
    else:
        sum = x+y
        print('sum =',sum)
three_numbers()

#35 Math:
def test():
    o = float(input('1st #:'))
    p = float(input('2nd #:'))
    if o == 5 or p == 5 or abs(o-p) == 5 or (o+p) == 5:

        print(True)

    else:
        print(False)
test()

#Python program to add two objects if both objects are an integer type
def add_numbers(a,b):

    if not (isinstance(a,int) and isinstance(b,int)):
        raise TypeError('Inputs must be integers')
    sum=a+b
    return sum
print(add_numbers(2,20000))

#using .format for printing multiple lines
def detail_info():
    print('Pls, enter you detail down here.')
    name=str(input('Enter your name:'))
    age=str(input('Enter your age:'))
    address=str(input('Enter your address:'))
    print('detail information:\n'\
          'your name:',name,'\n'\
          'your age:',age,'\n'\
          'address:',address)
detail_info()

#alternate
def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()

#math
def calc():
    x=int(input('value of x:'))
    y=int(input('value of y:'))
    formula=(x+y)*(x+y)
    print('(',x,'+',y,')','^2)','=',formula)
calc()
#Or,
x,y = 4,3

result = x*x+2*x*y+y*y
print('({}+{})^2)={}'.format(x,y,result))

#bank code
def bank_calc():
    amount=float(input('what is your amount:'))
    interest=float(input('your interest rate:'+'%'))
    timeline=float(input('your time:'))
    convert=interest/100
    amnt_inter=amount*convert
    amnt_inter_time=amnt_inter*timeline
    final_amount=amount+amnt_inter_time
    print('Your Final accumulated amount would be: $',final_amount)
bank_calc()

#calculate the amounts value in future:
amt=10000
int=3.5
yrs=7
future_value=amt*((1+(0.01*int))**yrs)
print(round(future_value,2))

#distance calc math code:
import math
def distance_calc():
 x1 = float(input('x1 coordinate:'))
 y1 = float(input('y1 coordinate:'))
 x2 = float(input('x2 coordinate:'))
 y2 = float(input('y2 coordinate:'))
 moder1=(x2-x1)**2
 moder2=(y2-y1)**2
 moder_res=(moder1+moder2)
 distance=math.sqrt(moder_res)
 print('distance between two points:', distance)
distance_calc()

#any file checker:
import os.path
open ('new.txt','w')
print (os.path.isfile('new.txt'))

#python shell bit checker
import struct
print(struct.calcsize('P')*8)

#python vesion etc. checker:
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())

#python site-packages:(only ran in IDLE python
import site
print (site.getusersitepackages())

#python prog. to call an external command:(!!)
from subprocess import call
call(['ls','-l'])

#get the path and file name of the file that is currently using
import os
print('file name:',os.path.realpath(__file__))

#Python program to find out the number of CPUs using
import multiprocessing
print(multiprocessing.cpu_count())

# Python program to parse a string to Float or Integer:
n='246.2458'
print(float(n))
print(int(float(n)))

#Python program to list all files in a directory in Python:
from os import listdir
from os.path import isfile,join
files_list=[f for f in listdir('/Users/home') if isfile(join('/Users/home',f))]
print(files_list)

#print without newline or space:
def drawBoard():
    board = [ [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,3,2,1,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]
            ]
    return board

def printBoard():
    for i in drawBoard():
        print (" ".join(map(str,i))) #lets you print as str& without newline
printBoard()

#determine profiling of Python programs
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')

#python prog. to print to stderr:
import sys
sys.stderr.write('error\n')

#53 python program to access environment variables
import os
print('*---------------------------------------*')
print(os.environ)
print('*---------------------------------------*')
print(os.environ['PATH'])
print('*---------------------------------------*')
print(os.getenv('PATH'))
print('*---------------------------------------*')

#a python program to determine current username:
import getpass
print(getpass.getuser())

#to get current IP address:
import socket
#socket library for low-level networking interface:
#shows you hostname,aliaslist,ipaddress
print(socket.gethostbyname_ex(socket.gethostname()))
#shows you only ip address
print(socket.gethostbyname(socket.gethostname()))
#shows you hname,aliasname,ipaddrlist
print(socket.gethostbyaddr(socket.gethostname()))
#shows your domain name
print(socket.getfqdn(socket.gethostname()))

#WxH of console window:
import shutil
t=shutil.get_terminal_size()
print('Height:{},Width:{}'.format(t.lines,t.columns))

#exe time print:
import time
def sumNubers():
    n=int(input('enter a number that will sum to from 1:' ))
    start=time.time()
    s=0
    for i in range(1,n+1):
        s=s+i
    end=time.time()
    req_time=end-start

    print(n,'to 1 summation is:',s,'and time took:',req_time)
sumNubers()
Ans: enter a number that will sum to from 1:10000
10000 to 1 summation is: 50005000 and time took: 0.0030012130737304688

#sum of n positive integers:
n=int(input('input a number:'))
sum=(n*(n+1))/2
print (sum)

#inches to cm conversion:
h_ft=int(input('feet:'))
h_in=int(input('inch:'))
ftTOinc=h_ft*12
tot_inc=ftTOinc+h_in
tot_cm=round(tot_inc*2.54,2)
print('in inches:',tot_inc,'and in cm:',tot_cm)

#hypotenuse of a triangle:
import math
h=float(input('what is the height?'))
b=float(input('what is the base?'))
hypo_sq=h**2+b**2
hypo=math.sqrt(round(hypo_sq,2))
print(hypo)

#feet to inch,yard,miles:
ft=int(input('distance in feet: '))
print('inch = ',ft*12)
print('yard = ',ft/3)
print('miles = ',ft/5280)

#to get an absolute file path:
def absPath():
  import os
  file=str(input('file name? '))
  print(os.path.abspath(file))
absPath()
#####
import os
print(os.path.realpath("uni track.txt"))

#find mod & craft time of a file:
import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("goku.jpg")))
print("Created: %s" % time.ctime(os.path.getctime("goku.jpg")))

def secondConv():
    time = float(input('what is the second? '))
    day = time // (24*3600)
    time = time%(24*3600)
    hour = time //3600
    time = time%3600
    min = time //60
    time = min%60
    seconds = time
    print('D:H:Min:Sec->%d:%d:%d:%d'%(day,hour,min,seconds))
secondConv()

#atmospheric pressure conversion:
kpa = float(input("Input pressure in in kilopascals? ")) #kilo pascal
psi = kpa / 6.89475729 #pounds_per_square_inch
mmhg = kpa * 760 / 101.325 #mm of mercury
atm = kpa / 101.325 #atmospheric pressure
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))

#sum of digits in int:
num = input('enter any number:')
length=len(num)
i=0
for n in range(0,length):
    i+=int(num[n])
print('total of your number: ',num,'is',i)

#any number entry sorting:
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
import heapq
heapq.heapify(data_list)
new_list = []
while data_list:
    new_list.append(heapq.heappop(data_list))
print(new_list)

#69 put any number in a string user input
#turn and save it in a list
#sort it
#beautiful!
s = input(r'put some numbers here sep by comma: ')
numbers=list(map(int,s.split(',')))
print('your unsorted list: ',numbers)
numbers.sort()
print('your sorted list: ',numbers)
'
#print sorted txt files by date:
import glob
import os
files=glob.glob('*.jpg') #no .txt file in my dir
files.sort(key=os.path.getmtime) #getctime would also work
print('\n'.join(files))

#dir listing sorted by date
import os,time
path = '.'
l = []
for d in os.scandir(path):
    name = d.name
    st = d.stat().st_ctime
    l.append((name,st))
    l.sort(key=lambda pair:pair[1])
    print('__________')
    for i in l:
        print('%43s,%25s'%(i[0],time.ctime(i[1])))

#import the math module
import cmath
math_ls = dir(cmath)
print(math_ls)

#calculate the midpoint of a line
x1=float(input('the value of x1: '))
y1=float(input('the value of y1: '))
x2=float(input('the value of x2: '))
y2=float(input('the value of y2: '))
print('your 1st coordinate:(',x1,',',y1,')')
print('your 1st coordinate:(',x2,',',y2,')')
x_mid_point=((x1+x2)/2)
y_mid_point=((y1+y2)/2)
print('the mid point of the line:(',x_mid_point,',',y_mid_point,')')

#word encoding:
#print(hash('Khalid'))
l_code=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
word=input('input the word to be encoded: ')
word=word.upper()
coded=word[0]
for a in word [1:len(word)]:
    i=65-ord(a) #65 is a code word for 'A'
    coded=coded+str(l_code[i])
print()
print('coded form: ',coded)
print()

#get the copyright info:
import sys
print(sys.copyright)

#command line argument passed to a script:
import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))

#system big-endian/little-endian:
import sys
print()
if sys.byteorder=='little':
    print('little endian platform')
else:
    print('big-endian platform')
print()

# 79 size of an object:
import sys
str1='One'
print('mem size of',str1,'=',str(sys.getsizeof(str1)),'bytes')

#81 concatenate n strings:
l = ['R','G','B']
colors = '-'.join(l)
print(colors)

#sum of all elements in list/container:
s = sum([10,20,500])
print('sum of the container:',s)

#test and find the biggest element in a list:
num = [2,3,4]
print(all(x > 1 for x in num))
print(all(x < 4 for x in num))
#all()=checks if a number is smaller/greater than all other
#elements; even if only one is diff. return false.
#True for x>1
#False for x<4 because, 2,3,4, 4 is equal to 4.

#count the number of occurrence of a specific character in a string
s = 'Hello,how are you..how?'
lit = ['1','2','2','2','4','5']
print(s.count('how'))
print(s.count('w'))
print(lit.count('2'))

#get the file size:
import os
file_size = os.path.getsize('New Microsoft Word Document.docx')
print(file_size)

# math:
x = 30
y = 20
sum = x + y
print('%d+%d=%d'%(x,y,sum))

#copy source_code code:
#SOLUTION 1: print((lambda str='print(lambda str=%r:(str %% str))()':(str % str))())
def file_copy(src,dest):
    with open(src) as f, open(dest,'w') as d:
        d.write(f.read())
file_copy('Init.py','InitCopy.py')

#swap two var:
def swap(a,b):
    print('unswapped:',a,',',b)
    temp = a
    a = b
    b = temp
    print('swapped:',a,',',b)
swap(5,10)

#get the identity of an obj. :
obj1 = object()
obj1_address = id(obj1)
print(obj1_address)

#convert a byte string to a list of integers
x = b'Khalid'
print(list(x))

#check if a string is numeric
str = '12hl'
try:
    i=float(str)
except(ValueError,TypeError):
    print('error')

import time
print(time.ctime())

#terminal screen clear:
import os
import time
os.system('cls')
time.sleep(2)

#100:
import socket
hostName = socket.gethostname()
print('host:',hostName)

#get numbers divisible by 15 from a list using anonymous function:
lit = [5,6,78,15,45,60,90,150,10,150,11,2]
sort_lit = list(sorted(lit))
print('sorted:',sort_lit)
result = list(filter(lambda x:(x%15 == 0),lit))
print('divisible by 15 in the list is/are: ',result)

#make file lists from current directory using a wildcard
import glob
file_list = glob.glob('*.*')
print(file_list)

#to input a number, if it is not a number generate an error msg
while True:
    try:
        a = float(input('input a number: '))
        break
    except (TypeError,ValueError):
        print('\n not a number..try again with a number,please')

#remove the 1st element of a list:
# print elements skipping inbetween
color = ['R','G','B','Y','V']
print('color:',color)
a = color[0::2] 
print(a) # a = ['R','B','V']
del color[0]
print(color) # ['G','B','Y','V']

#print the +ve numbers in a list:
inp = [-43,-1,0,1,2,5]
inp1=(list(filter(lambda i:i>=0,inp)))
print(inp1)

#multiply between elements in a list:
from functools import reduce #important line
nums = [10,2,3,4]
numProd = reduce((lambda x,y:x*y),nums)
print(numProd)

#empty a var without destroying it:
n = 20

d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)()) 

#count the number of elements in a list:
import collections
num = [1,2,3,10,20]
print(sum(collections.Counter(num).values()))

#Check if lowercase letter exists in a str:
str1 = 'A8238i823acdeOUEI'
print(any(c.islower() for c in str1))

#add leading & trailing zeros to a str:
one = '33.33'
print('string:',one)
one = one.ljust(8,'0') #trailing zeros #33.33000
print(one)
one = one.rjust(10,'0') #leading zeros #0033.33000
print(one)

#convert a num to binary and keep leading zeros:
x = 12
print(format(x,'08b'))#00001100
print(format(x,'010b'))#0000001100
print(format(x,'011b'))#00000001100
print(format(x,'05b'))#01100

#decimal to hexadecimal:
x = 20
print(format(x,'03x'))#014

#platform info:
import os, platform
print("Operating system name:")
print(os.name)
print("Platform name:")
print(platform.system())
print("Platform release:")
print(platform.release())

#32 bit or 64 bbit :
import struct
print(struct.calcsize("P") * 8)

#fund min max in a list:
lit = [1,34,56,100]
print(min(lit))
print(max(lit))

def sum_of_cubes(n):
    print('your number is:',n)
    b = n   #for printing purposes copied to b.
    total = 0
    while n > 0:
        total += (n**3)
        n -= 1
    print('sum of cubes smaller than',b,'is:',total)
sum_of_cubes(4)
'''''