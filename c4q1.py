class Rectangle1:

  def __init__(self, length, breadth):

     self.length = length

     self.breadth = breadth

  def area1(self):

     return self.length * self.breadth

a = int(input("Enter length of 1st rectangle: "))

b = int(input("Enter breadth of 1st rectangle: "))

r1= Rectangle1(a,b)

print("Area of 1st rectangle:", r1.area1())

class Rectangle2:

  def __init__(self, length, breadth):

    self.length = length

    self.breadth = breadth

  def area2(self):

    return self.length * self.breadth

c= int(input("Enter length of 2nd rectangle: "))

d = int(input("Enter breadth of 2nd rectangle: "))

r2 = Rectangle2(c,d)

print("Area of 2nd rectangle:", r2.area2())

if (r1.area1()>r2.area2()):

 print("1st rectangle large")

else:

 print("2nd rectangle large")
