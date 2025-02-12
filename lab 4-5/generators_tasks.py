#Task 1
def square_of_numbers(n):
    for i in range(1,n+1):
        yield i**2
n = int(input("enter:"))
for s in square_of_numbers(n):
    print(s,end=" ")

#Task 2
def even_generator(num):
    for i in range(num+1):
        if i%2==0:
            yield i
num = int(input("enter:"))
for even in even_generator(num):
    print(even,end=" ")
    
#Task 3
def divisable_generator(number):
    for i in range(number+1):
        if i%3==0 and i%4==0:
            yield i
number = int(input("enter:"))
for div in divisable_generator(num):
    print(div,end=" ")

#Task 4
def reversed_generator(a):
    for i in range(a,-1,-1):
        yield i
a = int(input("enter number:"))
for rev in reversed_generator(a):
    print(rev,end=" ")