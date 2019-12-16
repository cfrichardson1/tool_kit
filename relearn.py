# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:39:04 2019

@author: crich
"""

# old formating
 def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

# In[]
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return f"x = {self.x}, y = {self.y}"

p = Point(7,6)
print(p)

# In[]


# In[]

class Cereal:
    
    def __init__(self, name, brand, fiber):
        
        self.name = name
        self.brand = brand
        self.fiber = fiber
    
    def __str__(self):
        return f"{self.name} is produced by {self.brand} and has {self.fiber} grams of fiber in every serving!"
        
# In[]
c1 = Cereal('Corn Flakes', "Kellogg's", 2)        
        
# In[]
print(c1)

# In[]
class Cereal:
    
    def __init__(self, name, brand, fiber):
        
        self.name = name
        self.brand = brand
        self.fiber = fiber
    
    def __str__(self):
        return "{} is produced by {} and has {} grams of fiber in every serving!".format(self.name, self.brand,self.fiber)
    
c1 = Cereal('Corn Flakes', "Kellogg's", 2)        
c2 = Cereal('Honey Nut Cheerios', "General Mills", 3)


# In[]

class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print("-----sorted by price, referencing a class method-----")
for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)

print("---- one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)


# In[]

#yo = [0,1,2,3,4,5]
#[x**2 for x in yo]


# In[]
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

import test

#testing instance variables x and y
p = Point(3, 4)
test.testEqual(p.y, 4)
test.testEqual(p.x, 3)

#testing the distance method
p = Point(3, 4)
test.testEqual(p.distanceFromOrigin(), 5.0)

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
test.testEqual(p.x, 1)
test.testEqual(p.y, 7)


# In[]

    
'Foo'.isupper()


# In[20.12]
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

import test

#testing instance variables x and y
p = Point(3, 4)
test.testEqual(p.y, 4)
test.testEqual(p.x, 3)

#testing the distance method
p = Point(3, 4)
test.testEqual(p.distanceFromOrigin(), 5.0)

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
test.testEqual(p.x, 1)
test.testEqual(p.y, 7)



# In[]

# [lists].sort() sorts the instance itself, but returns None
lists = [5,7,9,2,4,1,6]

sorted_ = lists.sort()

cars = ['Ford', 'Toyota', 'BMW', 'Volvo']

fsorted_ = cars.sort() # returns none!


# In[]

    






# In[]


# In[]





# In[]


# In[]

    






# In[]


# In[]





# In[]


# In[]

    
