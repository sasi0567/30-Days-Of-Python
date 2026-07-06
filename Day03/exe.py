#Soloving Some questions
age = 18          #Integer
weight = 58.2     #Float
x = 2+4j          #Complex number
#Area of triangle
b=float(input("Enter the base: "))
h=float(input("Enter the height: "))
print("Area of the Triangle is: ",0.5*b*h)
#Area & Perimeter of rectangle 
l=float(input("Enter the the length of the rectangle: "))
w=float(input("Enter the width of the rectangle: "))
print("Area of the rectangle is: ",l*w)
print("perimeter of the rectangle is: ",2*l*w)
#Area & Circumference of the circle
r=float(input("Enther the radius of the circle: "))
pi=3.14
print("Area of the circle is: ",pi*r**2)
print("Circumference of the circle is: ",2*pi*r)
#Odd or Even
Number=int(input("Enter the number: "))
if Number % 2 == 0:
    print("Even")
else:
    print("Odd")
#Calculating Weekly Earinngs
hrs=float(input("Enter hours: "))
rate=float(input("Enter rate per hour: "))
pay=hrs*rate
print("Your weekly earings is : ",pay)
#Calcutaling How many seconds have you lived per year
yrs=int(input("Enter hoe many years have you lived: "))
sec=yrs*365*24*60*60
print("You have lived for",sec,"seconds.")