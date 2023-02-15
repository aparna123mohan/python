class Publisher:

 def read(self):

  print("Books")

class Book(Publisher):

 def title(self):

  print("Title : Python Programming")

 def author(self):

  print("Author : Ryan Tuner")

class Python(Book):

 def price(self):

  print("Price : 2325/-")

 def pages(self):

  print("Pages : 275")

p=Python()

p.read()

p.title()

p.author()

p.price()

p.pages()
