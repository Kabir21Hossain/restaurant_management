from datetime import datetime


class MenuItem:
    def __init__(self,item_id:str,name:str,price:float,category:str,available:bool):
        self.item_id=item_id
        self.name=name
        self.price=price
        self.category=category
        self.is_available=available

    def update_price(self,new_price:float):
        self.price=new_price
    def check_availability(self)->bool:
        return self.is_available
    def update_description(self,name:str):
        self.name=name
    
    def __repr__(self):
        return f'item-name:{self.name}->Price:{self.price}'
    

        

class Menu:
    def __init__(self):
        self.items=[]
    
    def add_item(self,item:MenuItem):
        self.items.append(item)
    
    def remove_item(self,item:MenuItem):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'this item {item} is not found')
            
    def display_menu(self):
        print('Available Items:')
        for x in self.items:
            print(x)

    def update_item(self,item_id:str,new_item:MenuItem):
        for i,item in enumerate(self.items):
            if item.id==item_id:
                self.item[i]=new_item


class Customer:
    def __init__(self,name,customer_id:str,phone:str,email:str):
        self.name=name
        self.customer_id=customer_id
        self.phone=phone
        self.email=email
    
    def place_order(self,order):
        order.customer=self

    def make_payment(self,amount:float):
        return Payment(order_id=None,amount=amount,payment_method='card',payment_time=datetime.now())
    
    def reserve_table(self,table,no_of_people:int):
        table.reserve()
    def cancel_order(self,order):
        order.status='Cancelled'
    

class Table:
    def __init__(self,table_id:int,capacity:int):
        self.table_id=table_id
        self.capacity=capacity
        self.status='Available'
    
    def reserve(self):
        self.status='Reserved'
    
    def release(self):
        self.status='Available'
    
    def assign(self,customer:Customer):
        self.status=f'Assigned to{customer.name}'
    

class Order:
    def __init__(self,order_id:str,date):
        self.order_id=order_id
        self.date=date
        self.total_amount=0.0
        self.status='New'
        self.items=[]
        self.customer=None
    
    def add_item(self,item:MenuItem):
        self.items.append(item)
        self.calculate_total()

    def remove_item(self,item:MenuItem):
        if item in self.items:
            self.items.remove(item)
            self.calculate_total()
        
    def calculate_total(self):
        self.total_amount=sum(item.price for item in self.items)
    
    def update_status(self,status):
        self.status=status

class Payment:
    def __init__(self,order_id:str,amount:float,payment_method:str,payment_time:datetime):
        self.payment_id=f'PMT-{int(datetime.now().timestamp())}'
        self.order_id=order_id
        self.amount=amount
        self.payment_method=payment_method
        self.payment_time=payment_time
    
    def process_payment(self):
        print(f"Processing payment of ${self.amount} for Order ID: {self.order_id}")

    def issue_refund(self):
        print(f"Refund issued for Payment ID: {self.payment_id}")

class Staff:
    def __init__(self, staff_id: str, name: str, role: str, salary: float):
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.salary = salary
    
    def take_order(self,order:Order):
        order.update_status('In Progress')

    def serve_order(self,order:Order):
        order.update_status('Served')
    
    def manage_inventory(self):
        print('Managing inventory___')
    

class Restaurant:
    def __init__(self,restaurant_id:int,name:str,address:str,phone:str,hours:str):
        self.restaurant_id=restaurant_id
        self.name=name
        self.number=phone
        self.address=address
        self.operating_hours=hours
        self.staffs=[]
        self.orders=[]
        self.menu=Menu()
    
    def open_restaurant(self):
        print(f'{self.name} is now open')

    def close_restaurant(self):
        print(f'{self.name} is now closed')

    def manage_operations(self):
        print('Managing daly operations...')
    
    def add_staff(self,staff):
        self.staffs.append(staff)

    def __repr__(self):
        return f'{self.restaurant_id}\n{self.name}\n{self.address}\n{self.number}\n{self.operating_hours}\n'


    
if __name__=='__main__':
    restaurant = Restaurant(1, "Ocean View Dine", "123 Seaside Ave", "123-456-7890", "9 AM - 9 PM")
    staff1 = Staff("S01", "Alice", "Waiter", 2500)
    staff2 = Staff("S02", "Bob", "Chef", 3000)
    restaurant.staffs.extend([staff1, staff2])

    # Add Menu Items
    item1 = MenuItem("M01", "Burger", 8.5, "Fast Food", True)
    item2 = MenuItem("M02", "Pasta", 12.0, "Italian", True)
    restaurant.menu.add_item(item1)
    restaurant.menu.add_item(item2)
    restaurant.menu.display_menu()


    # Create Customer and Place Order
    customer = Customer("C01", "Charlie", "555-1234", "charlie@example.com")
    order = Order("O01", datetime.today())
    customer.place_order(order)
    order.add_item(item1)
    order.add_item(item2)
    print(f"Order Total: ${order.total_amount}")

    staff1.take_order(order)
    print(f"Order Status: {order.status}")
    staff1.serve_order(order)
    print(f"Order Status: {order.status}")

    # Customer Cancels Order (should override previous status)
    customer.cancel_order(order)
    print(f"Order Status After Cancel: {order.status}")

    payment = Payment(order.order_id, order.total_amount, "card", datetime.now())
    payment.process_payment()

    payment.issue_refund()


        

