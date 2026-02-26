class Pruduct():
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def buy(self, quantity):
        if quantity<=self.stock:
            self.stock-= quantity
            print("purchased", quantity, "of", self.name)
            return True
        else:
            print("not enough stock")
            return False

    def show_info(self):
        print("pruduct", self.name, "price", self.price, "stock", self.stock)

class Customer():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def purchase(self, pruduct, quantity):
        total_cost = pruduct.price * quantity
        if self.balance >= total_cost:
            if pruduct.buy(quantity):
                self.balance -= total_cost
                print(self.name, "purchased", quantity, pruduct.name)
        else:
            print(self.name, "has insufficient fundes!")

class PremiumCustumer(Customer):
    def __init__(self, name, balance, discount):
        super().__init__(name, balance)
        self.discount = discount

    def purchase(self, pruduct, quantity):
         total_cost = pruduct.price * quantity
         if self.balance >= total_cost:
             if pruduct.buy(quantity):
              self.balance -= total_cost
              print("premium", self.name, "bought", quantity, pruduct.name, "with", self.discount*100, "% off! balance :", self.balance )
             else:
                 print(self.name, "has insufficient funds")

         class Pruduct():
            def __init__(self, name, price, stock):
                self.name = name
                self.price = price
                self.stock = stock

            def buy(self, quantity):
                    if quantity<=self.stock:
                        self.stock-= quantity
                        print("purchased", quantity, "of", self.name)
                    else:
                        print("not enough stock")

            def show_info(self):
                            print("pruduct", self.pruduct, "price", self.price, "stock", self.stock)

class Customer():
    def __init__(self, name, balance):
        self.name = name
        self,balance = balance

    def purchase(self, pruduct, quantity):
        total_cost = pruduct.price * quantity
        if self.balance>= total_cost:
            print(self.name, "purchase", quantity, pruduct.name, "s.")
        else:
            print(self.name, "has insufficient fundes!")

class PremiumCustumer():
    def __init__(self, name, balance, discount):
        super().__init__(name, balance)
        self.discount = discount

    def purchase(self, pruduct, quantity):
         original_cost = pruduct.price * quantity
         discount_cost = original_cost * (1 - self.discount)
         if self.balance >= discount_cost:
             if pruduct.buy(quantity):
              self.balance -= discount_cost
              print("premium", self.name, "bought", quantity, Pruduct.name, "with", self.discount*100, "% off! balance :", self.balance )
             else:
                 print(self.name, "has insufficient funds")

         laptop = Pruduct("laptop", 100, 5)
         mouse = Pruduct("mouse", 20, 10)

         normal_customer = Customer("MOTASEM", 1200)
         Premium_customer = PremiumCustumer("BALSAM", 1500, 0.1)

         print("testing normal customer")
         laptop.show_info()

         normal_customer.purchase(laptop, 2)
         laptop.show_info()

         print("testing primium customer")
         mouse.show_info()

         Premium_customer.purchase(mouse, 5)
         mouse.show_info()

         print("tseting out of stock")
         normal_customer.purchase(laptop, 20)

         input("enter")
