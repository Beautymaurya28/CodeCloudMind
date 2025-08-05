# #1. area of the triangle
# base=int(input("enter the base: "))
# height=int(input("enter the height: "))
# area=(base*height)/2
# print("the area of triangle is: ",area)

# #2. check even num
# num=int(input("enter the number: "))

# #without conditional statement
# ans=num%2
# print("is it even: ",ans==0)


# #with conditonal statement
# if(num%2==0):
#  print("num is even")
# else:
#   print("no the num is not even.")

# #3.Total amount
# #total amount=1+r(100)*t;
# # 2.ci=totalamount-principal
# p=1000 
# n=1
# t=3
# A=p*(1+r/n)**(n*t)
# ci=A-p
# print("compound interest is:",ci)
# print("total amount is :",A)


# #4. compare two value
# a=int(input("enter the first number: "))
# b=int(input("enter the second number: "))
# print("a>b: ",a>b)
# print("a<=b: ",a<=b)

# c=float(input("enter the third num: "))
# print("a<=c",a<=c)

# #5.convert into temperature
# #celcius to kelvin
# #celcius to fahrenheit\
# def cal_to_fahr(c):
#     return (c*9/5)+32
# def cal_to_kel(c):
#     return c+273.15
 
# temp=25
# print(cal_to_kel(temp))
# print(cal_to_fahr(temp))

# #6. concatenate and repeat
# a="beauty"
# c="maurya"
# d=a+c
# print(d*5)

# #7. write a program to convert given time in second to time in hour,min and sec
# time=int(input("enter the time in sec: "))
# hour=time/3600
# min=time/60
# print("convert time to hour: ",hour)
# print("convert time to min: ",min)


# #8. logical operator
# a=True
# b=False
# print("a and b: ",a and b)
# print("a or b: ",a or b)
# print("!a",not a)
# print("!b: ",not b)

# #9. membership operator
# num=[1,34,23,67,90]
# print("20 in nums: ",20 in num)
# print("34 in num",34 in num)
# print("34 not in num: ",34 not in num)

# #10. convert min to sec
# min=int(input("enter the min: "))
# sec=min*60
# print("second: ",sec)

# #11. write a program to input marks scored by a student in 3 subject and compute the percentage obtained
# sub1=int(input("enter the first sub marks: "))
# sub2=int(input("enter the sec sub marks: "))
# sub3=int(input("enter the third sub marks: "))
# obtainedmarks=sub1+sub2+sub3
# percentage=(obtainedmarks/300)*100
# print("the score is: ",percentage)

# #12. swap without using third 
# a=5
# b=2
# a=a+b
# b=a-b
# a=a-b
# print("a=",a)
# print("b=",b)