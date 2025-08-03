name="emati"
print(name[1:3])
print(float(25))
x=True
x=int(x)
y=complex(x,x)
print(str(y))
print(x)
nus=2.33e5
print(nus)
num=['a','b','c','d']
num[2]='f'
print(num)
set1={1,2,3,4}
set1.add(5)
print(set1)
set2=frozenset(set1)
print(type(set2))
for i in range(2,8,2):
    print(i,end=" ")
ex=7
if ex > 5:
    print("\n",ex**2)
#nos1=int(input("Enter the first num: "))
#nos2=int(input("Enter the second num: "))
#if nos1>=nos2:
 #   if nos1==nos2:
  #      print(nos1,"is equal with ",nos2)
   # else:
    #    print(nos1,"greater than",nos2)
#else:
 #   print(nos1,"is smaller than",nos2)
ref=11
sum=0
num1=1
while num1 < ref:
    sum= sum + num1
    num1=num1+1
print(sum)
for i in range(1,len(num)+1):
    print(i+1,end=",")
sum1=0
num3=10
for x in range(num3,23,2):
    sum1=sum1+num3
    num3=num3+2

print("\n",sum1)

lst=[2,3,4,5]
sum2=0
for x in range(0,4):
    print(lst[x]**2,end=" ")

for i in range(0,4):
    sum2=sum2 + lst[i]
avg=sum2 / len(lst)
print("\n",avg)

lst1=[]
for n in range(51,9,-1):
    if n % 2 == 0:
        lst1.append(n)
       
print(lst1)

given="manrniya mnennen"
count=0
for t in range(0,len(given)):
    if given[t] != "n":
        continue
    else:
        count=count+1
print(count)

for x in range(1,6):
    for t in range(0,x):
        print("*",end=" ")
    print('')

for x,t in enumerate(num):
    print("value[", x, "]=",t)    

for i in range(6,len(given)):
    print(given[i],end=" ")
print('\n')
stat="\n Remember, Red, hope is a good thing, maybe the best of things, and no good thing ever dies"
for x in stat.split(","):
    print(x,end=" ")
print("\n")
for i in num[:2]:
    print(i,end=" ") 
print("\n")
dict2 = {"Brand": "BMW", "Color": "Black", "Date": 1964}
for key,value in dict2.items():
    print(key,"->",value)
print("\n")
#num4=int(input("Enter the no: "))
#count1=0
#exc=num4
#while exc >= 10:
 #   count1=count1 + 1
  #  exc=exc / 3
#print(count1)
print("\n")
#num5=int(input("enter the guesss no: "))
#while num5 != 1450:
 #   print("enter the correct no")
  #  num5=int(input("enter the guesss no: "))
#else:
 #   print("proceed to next step")
#num6=int(input("enter the req no: "))
#while num6 > 1:
 #   if num6 % 2 == 0:
  #      print(num6,"is even no")
   #     num6=num6-1
   # else:
    #    print(num6,"is odd no")
     #   num6=num6-1
its=0
while its < 5:
    its1=0 
    while its >= its1:
        print("*",end=" ")
        its1=its1+1
    print(" ")
    its=its+1
numbers = [10, 40, 120, 230]
name2 = 'Jesaa29 Roy'
#acc=input("name of user: ")
x1=0
while x1 < len(name2):
    if name2[x1] == " ":
        break
    print(name2[x1],end=" ")
    x1=x1+1
print("\n")
numbers1 = [2, 3, 11, 7]
for nu in numbers1:
    if nu > 10:
        continue
    print(nu**2,end=" ")
print("\n")
for m in range(1,11):
    print("multi table of: ",m)
    for m1 in range(1,11):
        print(m*m1,end=" ")
    print(" ")
for rec in range(1,6):
    count1=0
    while count1 < 3:
        print("*",end=" ")
        count1=count1+1
    print(" ") 
print("\n")
#sal=input("name,age,marks: ")
#sal1=sal.split()
#name3=sal1[0]
#age=sal1[1]
#marks=sal1[2]
#print("User Details: ", name3,age, marks)

#import sys
#print("Python version:", sys.version)
#print("Script name:", sys.argv[0])
#print("Number of arguments:", len(sys.argv))
#print("Arguments passed:", sys.argv)
import math
print(f"{math.pi**9:*>20,.3f}")
print(f"{'ghost':_^10}")
print(f"{276:b}")
print(f"{'new':5}")
print("{:e}".format(math.pi**9))

#firstName = input("Enter First Name ")
#lastName = input("Enter Last Name ")
#organization = input("Enter Organization Name ")
#print("{f_name {fr} l_name {ls} works at org {or}".format(firstName=fr, lastName=ls, organization=or))
#print(f"{firstName:^5} {lastName:^5} {'works at':^5} {organization:^5}")
print(name.center(20,'-'))
import decimal as de
from decimal import *
import math as m
y1=m.pi
x=4+6j
print(type(x))
import cmath
import itertools
c=cmath.rect(2,3)
print(cmath.polar(c),x.real)
d=20
print(oct(d),hex(d),bin(d))
print(m.isnan(d))
print(d.bit_length())
#print(y1.as_integer_ratio())
print(Decimal((0,(1,1,1,1),-3)))
getcontext().prec = 4
getcontext().rounding = de.ROUND_DOWN
print(Decimal(3) / Decimal(77))
getcontext().clear_flags()
print(Decimal(2).sqrt())
high = "ale","me","yabu",1,2,3
hi1,hi2,hi3,low,high1,loq1 = high
print(high,"the main one",hi1)
ls_high=list(high)
ls_high.append(["eya",4])
high1=tuple(ls_high)
numtu=tuple(num)
em=[]
for t in itertools.chain(high1,numtu):
    em.append(t)
em1=tuple(em)
print(em1)
#print(list(high))
tri={1,2,11,12,3,4,9,8,7}
tri2={2,8,9}
tri3=tri|tri2
print(tri3)
print(tri3.issuperset(tri2))
sor_set=set(sorted(tri))
print(frozenset(high))
print(dict2.keys(),dict2.values(),dict2.items())
for k,v in dict2.items():
    print(f"{k:^10}","->",f"{v:^10}")
dict2.update([("strength","power"),("weakness","fear")])
dict2.setdefault("zip")
dict2.setdefault("state","NY")
dict2.pop("zip")
f_dict2=dict2.keys()
print(dict2,'color' in f_dict2)
student_dict1 = {'Aadya': 1, 'Arul': 2, }
student_dict2 = {'Harry': 5, 'Olivia': 6}
student_dict3 = {'Nancy': 7, 'Perry': 9}
ultimate_dict = {**student_dict1, **student_dict2, **student_dict3,**dict2}
dict2["student1"] = student_dict1
print(sorted(dict2.keys()))
#print(ultimate_dict)
dict3={k1:k1**2 for k1 in lst if k1 > 0} 
print(dict3)
zip1=zip(num,lst)
print(list(zip1))
telephone_book = [1178, 4020, 5786]
persons = ['Jessa', 'Emma', 'Kelly']
zip2=zip(persons, telephone_book)
zip3=dict(zip2)
print(max(zip3.values()))
def assign(name,rate):
    if rate == 1:
        print(f"{name:^10}",f"{'you are with group A':^10}")
    if rate == 2:
        print(f"{name:^10}",f"{'you are with group B':^10}")
    if rate == 3:
        print(f"{name:^10}",f"{'you are with group C':^10}")
    if rate == 4:
        print(f"{name:^10}",f"{'you are with group D':^10}")
    if rate == 5:
        print(f"{name:^10}",f"{'you are with group E':^10}")
assign("emati",5)
#input1=int(input("enter the 1 no: "))
#input2=int(input("enter the 2 no: "))
ran_lst=[]
import random
def random_num(ran1,ran2=100):
    """this function generates a random number between the given range and returns a list of even numbers"""
    global ran_num
    ran_num=random.randint(ran1,ran2)
    for r in range(0,ran_num):
        if r % 2 == 0:
            ran_lst.append(r)
    return ran_lst
re1=random_num(ran1=20,ran2=30)
print(re1)
print(help(random_num))
print(ran_num)
def info(name3,age3):
    try:
        print(f"{name3:^10}",f"{age3:^10}")
    except TypeError as req :
        raise TypeError("the requested data is not available") from req
info("emati",18)
def per_info(*info):
    print("\n","name:",info[-len(info)],"\n","age:",info[-len(info)+1],"\n","marks:",info[-len(info)+2],"\n","school:",info[-len(info)+3])
per_info("emati",18,90,"school1")
def mini_cal(num5):
    try:
        if num5 == 0 :
            return 1,0,0,0
        else:
            factorial=num5 * mini_cal(num5-1)[0]
        square=num5 ** 2
        cubic=num5 ** 3
        sqrt=m.sqrt(num5)
        return factorial, square, cubic, sqrt
    except TypeError:
        print("The requested data is not number")
a,b,c,d = mini_cal(5)
print(f"Factorial: {a}, Square: {b},Cubic: {c},Square root: {d}")
def show_employee(name, salary=9000):
    """This function displays the name and salary of an employee"""
    print(f"Name: {name:^10}, Salary: {salary:^10}")
emp1=show_employee("Emati")
emp2=show_employee("mommye", 12000)
print(emp1,"\n",emp2)
def prop(c,d):
    sum3=0
    def sum():
        nonlocal sum3
        sum3 = c + d
    sum()
    sum3 = sum3 + 5 
    return sum3
addition = prop(10, 20)
print("The sum is:", addition)
class wrong (Exception):
    pass
class overflow (wrong):
    pass
class underflow (wrong):
    pass
class over_length_list(wrong):
    pass
def re_add(num6):
    
    if num6 == 0:
        return 0
    elif num6 < 0:
        raise underflow("Negative numbers are not allowed") 
    elif num6 > 1000:
        raise overflow("Number exceeds the limit of 1000")
    else:
        return num6 + re_add(num6 - 1)
print("The sum of numbers from 1 to 10 is:", re_add(13))
def show_student(name, age):
    def display_student(name, age):
        print(f"Name: {name}, Age: {age}")
    display_student(name,age)
show_student("Emati", 18)
lst2=[]
def gen_even(num7,num8):
    if isinstance(num7, int) and isinstance(num8, int):
        for i in range(num7, num8):
            if i % 2 == 0:
                lst2.append(i)
    else:
        print("Both inputs must be integers")    
    return lst2
gen1=gen_even(4, 20)
print(gen1)
def max_num(req_lst):
    try:
        for i in req_lst:
            if i == max(req_lst):
                return i
    except TypeError:
        print("The list contains non-numeric values")
max=max_num([4, 6, 8, 24, 12, 2])
max=max_num(["a"])
print("The maximum number is:", max)
#try:
    #a = int(input("Enter value of a:"))
    #b = int(input("Enter value of b:"))
    #c = a/b
    #print("The answer of a divide by b:", c)
#except ValueError:
    #print("Entered value is wrong")
#except ZeroDivisionError:
    #print("Can't divide by zero")
#class addition:
  #  def __init__(self, nums, target):
        #self.nums = nums
        #self.target = target

    #def add(self):
        #try:
         #   for i in range(len(self.nums)):
          #      for j in range(i + 1, len(self.nums)):
           #         if self.nums[i] + self.nums[j] == self.target:
            #            print(f"Pair found: {self.nums[i]} + {self.nums[j]} = {self.target}")     
            #found = True
            #if not found:
             #   print("No pair found that adds up to the target.")
        #except TypeError:
         #   print("The input list must contain only integers")  
#try:
  #  ls_inp = input("Enter numbers separated by comma: ")
   # lst_inp = [int(i.strip()) for i in ls_inp.split(",") if i.strip()]

    #if not (2 <= len(lst_inp) <= 10**4):
     #   raise over_length_list("The list must contain between 2 and 10,000 elements.")

   # if any(not (-10**9 <= x <= 10**9) for x in lst_inp):
        #raise overflow("All numbers in the list must be between -1,000,000,000 and 1,000,000,000.")

    #target1 = int(input("Enter the target number: "))
   # if not (-10**9 <= target1 <= 10**9):
      #  raise overflow("The target number must be between -1,000,000,000 and 1,000,000,000.")
#except ValueError:
 #   print("Input error: Please enter only valid integers.")
#two_sum = addition(lst_inp, target1)
#two_sum.add()
class Person:
    grad_uni="aau"
    def __init__(self, name,sex,profession, company, hours):
        self.name = name
        self.sex = sex
        self.profession = profession
        self.company = company
        self.hours = hours


    def working(self):
        print(f"{self.name} is a working {self.profession} at {self.company} .")
    def working_hours(self):
        print(f"{self.name} works {self.hours} hours a day and enrolled in {Person.grad_uni} .")
    def change_uni(self, new_uni):
        Person.grad_uni = new_uni
bruv= Person("Emati","Female","Software Engineer","Google",8)
bruv.working()
bruv.change_uni("MIT")
bruv.working_hours()
class Employee:
    def __init__(self,name,salary,code):
        self.name=name
        self.__salary=salary
        self.__code=code
    def show(self):
        if self.__code == 1997:
            print(f"name:{self.name}""\n"f"salary:{self.__salary}")
        else:
            print("please enter the right code")
emp=Employee("jerry",10000,1997)
emp.show()

