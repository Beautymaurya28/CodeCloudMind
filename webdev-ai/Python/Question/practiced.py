#question 1(add two numbers)
a=5
b=6
print(a+b)
#question 2(find the reminders when a number is divided by  z)
d=6
print("rminder when a is divided by d",a%d)
a=34
b=6
print("reminder when a is divided by b is",a%d)
#question 3(check the type of varibles assigned using input() function)
a=input("enter the value of a: ")
print(type(a))
#question 4(use comparison operators find out a is greater than b or not)
a=34
b=40
print(a>b)
#question 5(find the avg of two numbers entered by user)
number1=int(input("enter the first number: "))
number2=int(input("enter the second number: "))
avg=(number1+number2)/2
print("the avg of both number is: ",avg)
#question 6(find the square of a numbers entered by user)
num=int(input("enter the first number: "))
sqr=num*num
print(sqr)


#question 7
user=input("enter your name: ")
print("Good Afternoon ",user)
print(f"Good Afternoon {user}")

#question 8
letter="""Dear <|Name|>,you are selected ! <|date|>"""
print(letter.replace("<|Name|>","Beauty").replace("<|date|>","23 june 2024"))

#question 9
name="harry is a good boy  and"
print(name.find("  "))

#question 10
name="harry is a good boy  and"
print(name.replace("  "," "))


#question 11
Letter="Dear Beauty, this python course is nice. Thanks!"
print(Letter)
Letter1="Dear Beauty, \nthis python course is nice. \nThanks!"
print(Letter1)


#1.write a program to store seven marks in a list entered by the user
# ]

# m1=int(input("enter the marks name: ")
# marks.append(m1)

# m2=int(input("enter the marks name: ")
# marks.append(m2)

# m3=int(input("enter the marks name: ")
# marks.append(m3)

# m4=int(input("enter the marks name: ")
# marks.append(m4)

# m5=int(input("enter the marks name: ")
# marks.append(m5)

# m6=int(input("enter the marks name: ")
# marks.append(m6)

# m7=int(input("enter the marks name: ")
# marks.append(m7)

# print(marks)

#2.write a program to accept the marks or student and display them in sorted manner

# marks=[]
# m1=int(input("enter the marks name: "))
# marks.append(m1)

# m2=int(input("enter the marks name: "))
# marks.append(m2)

# m3=int(input("enter the marks name: "))
# marks.append(m3)

# m4=int(input("enter the marks name: "))
# marks.append(m4)

# m5=int(input("enter the marks name: "))
# marks.append(m5)

# m6=int(input("enter the marks name: "))
# marks.append(m6)

# marks.sort()
# print(marks)


#3.check that a tupple type that cannot changed in python
# a=(34,56,45,67,89,90,"harry","beauty")
# a[2]="maurya"


#4.write a program to sum a list with 4 numbers
l=[34,56,78,90]
print(sum(l))


#5.write a program to count the zeros in tupple
a=(4,5,0,1,0,7,0)
print(a.count(0))


# words={
#     "madad":"help",
#     "kursi":"chair",
#     "kitab":"books",
#     "ladki":"girl",
#     "ladka":"boy"
# }
# word=input("enter the word which you want to convert in english: ")
# print(words[word])
# type=type(words)
# print(type)

#question 2
# s=set()
# n=input("enter the number 1:")
# s.add(int(n))
# n=input("enter the number 2:")
# s.add(int(n))
# n=input("enter the number 3:")
# s.add(int(n))
# n=input("enter the number 4:")
# s.add(int(n))
# n=input("enter the number 5:")
# s.add(int(n))
# print(s)


#question3
# a=set()
# a.add(18)
# a.add("18")
# print(a)


# qustion5 find the length of given set
# set1=set()
# set1.add(20)
# set1.add(20.0)
# set1.add("20")
# print(len(set1))


#question 5
s={}
print(type(s))

#question6 
# dic={}
# name=input("enter friends name:")
# lang=input("enter lang name:")
# dic.update({name:lang})

# name=input("enter friends name:")
# lang=input("enter lang name:")
# dic.update({name:lang})

# name=input("enter friends name:")
# lang=input("enter lang name:")
# dic.update({name:lang})

# name=input("enter friends name:")
# lang=input("enter lang name:")
# dic.update({name:lang})

# print(dic)


