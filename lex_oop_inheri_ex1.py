class Apparel:
   counter = 100
   def __init__(self, price, item_type ):
      self.__price = price
      self.__item_type = item_type  #None -> gives error as below lines are dependent upon it directly
      Apparel.counter += 1  #add 'C' / 'S' # C101 S102
      self.__item_id = self.__item_type[0] + str(Apparel.counter) #not mentioned first
   
   def calculate_price(self):
      self.__price *= 1.05    # 5% service tax

   def get_item_id(self):
      return self.__item_id

   def get_price(self):
      return self.__price

   def get_item_type(self):
      return self.__item_type

   def set_price (self, price):
      self.__price = price

   #below is required for cotton class
   def set_item_type (self, item_type):
      self.__item_type = item_type

   def set_item_id(self, item_id):
      self.__item_id = item_id


class Cotton (Apparel):
   
   def __init__(self, price, discount):
      super().__init__(price, 'Cotton') #this is super constructor #here ive to pass item_type = 'Cotton'
      # super().set_item_type('Cotton')  #here item_type -> private ? Can I call private attribute of parent class to child class?
      # super().set_item_id('C' + super().get_item_id())
      self.__discount = discount

   def calculate_price(self):
      super().calculate_price()
      self.set_price( self.get_price() * (1 - self.__discount) )
      self.set_price( self.get_price() * 1.05 ) #vat
      return self.get_price()
   def get_discount (self):
      return self.__discount


class Silk (Apparel):
   def __init__(self, price): 
      super().__init__(price, 'Silk')
      self.__points = 0  
      
   def calculate_price(self):
      super().calculate_price()
      if self.get_price()<=10000 :
         self.__points += 3
      else :
         self.__points += 10
      self.set_price( self.get_price() * 1.10 ) #vat
      return self.get_price()
   def get_points(self):
      return self.__points

# a1 = Apparel (100, 'Cotton')
c1 = Cotton (50, 0.20)
print ( c1.calculate_price() )
print ( c1. get_item_id() )

c2 = Silk (10000)
print (c2.calculate_price())
print (c2.get_points())
print (c2.get_item_id())