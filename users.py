from abc import ABC,abstractmethod
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address

class Customer(User):
    def __init__(self, name,phone,email,address,money):
        super().__init__(name)
        self.__order=None
        self.wallet=money
    
    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self,order):
        self.__order=order
    
    def place_order(self,order):
        self.order=order
        print(f'{self.name} placed and order{order.items}')
    
    def pay(self,amount):
        pass

    def give_tip(self,tips_amount):
        pass

    def write_review(self,stars):
        pass


    def eat_food(self,order):
        print(f'{self.name} item food:{order.items}')
        


class Employee(User):
    def __init__(self, name,phone,email,address,salary,starting_data,departement):
        super().__init__(name)
        self.salary=salary
        self.startring_date=starting_data
        self.department=departement

class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_data, departement,cooking_item):
        super().__init__(name, phone, email, address, salary, starting_data, departement)
        self.cooking_item=cooking_item

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_data, departement):
        self.tips_earning=0
        super().__init__(name, phone, email, address, salary, starting_data, departement)
    
    def take_order(self,order):
        pass
    def transfer_order(self,order):
        pass
    def serve_food(self,order):
        pass
    def receive_tips(self,amount):
        self.tips_earning+=amount



class Manager(Employee):
    pass