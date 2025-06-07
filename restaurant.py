class Restaurant:
    def __call__(self,name):
        self.name=name
        self.chef=None
        self.employee=[]
        self.server=[]
        self.manager=None
        self.menu=[]
        self.revenue=0
        self.profit=0
        self.order=[]

    def add_employee(self,employee,employee_type)
        if employee_type == 'chef':
            self.chef=employee
        elif employee_type == 'server':
            self.server.append(employee)
        elif employee_type == 'Manager':
            self.manager=employee
    
    def receive_payment(self, order,amount,customer):
        if amount >=order.bill:
            self.revenue+=amount
            


        