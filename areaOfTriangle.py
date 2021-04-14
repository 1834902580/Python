# Python Program to find the area of triangle

a = int(input())
b = int(input())
c = int(input())

s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)