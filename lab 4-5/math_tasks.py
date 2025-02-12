#Task 1
import math
degree = 15
rad = math.radians(degree)
print("radian: " ,rad)

#Task 2
h = int(input())
a = int(input())
b = int(input())
s = (a+b)/2*h
print('area of trapezoid: ',s)

#Task 3

def area_of_regularpolygon(sides,length):
    if side<3:
        return "A polygon must have at least 3 sides"
    else:
        area = (side*length**2)/(4*math.tan(math.pi/side))
        return int(area)
    
side = int(input("Input number of sides:"))
length = float(input("Input the length of a side:"))
result = area_of_regularpolygon(side,length)
print(f"area of the polygon is:{result}")


#Task 4
def area_of_parallelogram(a,h):
    return a*h
a = float(input("length of base:"))
h = float(input("height:"))
res = area_of_parallelogram(a,h)
print(f"Area of parallelogram: {res}")