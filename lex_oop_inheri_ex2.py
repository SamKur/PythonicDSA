#spice hut tiffin service

class Customer:
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.bill_amount = None #here ??
        self.bill_id = None
    def calculate_bill_amount(self):  #-> abstract ->means blueprint, yet to implement
        # self.bill_amount = None #here ??
        # self.bill_id = None
        pass

    def get_customer_name (self):
        return self.__customer_name

class OccassionalCustomer (Customer):
    _counter = 1000 #private & static
    # delivery_charge = 0
    
    def __init__(self, customer_name, distance_in_kms):
        super().__init__(customer_name)
        self.__distance_in_kms = distance_in_kms
        OccassionalCustomer._counter += 1
        self.bill_id = 'O' + str (OccassionalCustomer._counter) #bill_id from parent. Allowed ??
        self.delivery_charge = 0 # I created this #or above

    def validate_distance_in_kms (self):
        if 1 <= self.__distance_in_kms <= 5:
            return True
        return False

    def calculate_bill_amount(self):
        super().calculate_bill_amount()
        if self.validate_distance_in_kms :
            if 1<= self.__distance_in_kms <=2 :
                self.delivery_charge = 5 * self.__distance_in_kms
            elif 3<= self.__distance_in_kms <=5 :
                self.delivery_charge = 7.5 * self.__distance_in_kms
            else: 
                return -1
            self.bill_amount = 50 + self.delivery_charge    
        else:
            self.bill_amount = -1
        return self.bill_amount
    
    def get_distance_in_kms(self):
        return self.__distance_in_kms

class RegularCustomer (Customer):
    _counter = 1000 # private & static

    def __init__(self, customer_name, no_of_tiffin):
        super().__init__(customer_name)
        self.__no_of_tiffin = no_of_tiffin
        RegularCustomer._counter += 1
        self.bill_id = 'R' + str (RegularCustomer._counter)

    def validate_no_of_tiffin(self):
        if 1 <= self.__no_of_tiffin <= 7 :
            return True
        else:
            return False

    def calculate_bill_amount(self):
        super().calculate_bill_amount()
        if self.validate_no_of_tiffin :
            if 1 <= self.__no_of_tiffin <= 2:
                self.bill_amount = 50 * self.__no_of_tiffin
            elif 3 <= self.__no_of_tiffin <= 5:
                self.bill_amount = 50 * self.__no_of_tiffin * 0.90
            elif 6 <= self.__no_of_tiffin <= 7:
                self.bill_amount = 50 * self.__no_of_tiffin * 0.70
        else:
            self.bill_amount = -1
        return self.bill_amount
    
    def get_no_of_tiffin(self):
        return self.__no_of_tiffin
    

cust1 = RegularCustomer('Sam Wilcox', 7)
print (cust1.calculate_bill_amount())
print (cust1.bill_id)

cust2 = RegularCustomer('Nathan Drake', 2)
print(cust2.calculate_bill_amount())
print(cust2.bill_id)

cust3 = OccassionalCustomer('Willy Wonka', 10)
print (cust3.calculate_bill_amount())
print (cust3.bill_id)

cust4 = OccassionalCustomer('Steve Rogers', 4)
print (cust4.calculate_bill_amount())
print (cust4.bill_id)
print (cust4.get_customer_name())