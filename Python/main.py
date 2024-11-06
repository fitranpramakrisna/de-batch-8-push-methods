import math

class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount
        
    def calculate_tax(self, tax_rate):
        if 0 <= tax_rate <= 1:
            return math.floor(self.total_amount * tax_rate)
    
    def display_order(self):
        data_customer = {
            'order_id' : self.order_id,
            'customer_name':self.customer_name,
            'order_date': self.order_date,
            'total_amount':self.total_amount
        }
        return data_customer

    
class OrderProcessor:
    def __init__(self):
        self.list_customer = []
    
    def add_order(self, order):
        self.list_customer.append(order)
        
    def calculate_total_revenue(self):
        total_revenue = 0
        for i in range(len(self.list_customer)):
            total_revenue += self.list_customer[i]['total_amount']
        
        return total_revenue
    
    def calculate_total_tax(self, tax_rate):
        total_tax_revenue = 0
        for i in range(len(self.list_customer)):
            total_tax_revenue += self.list_customer[i]['total_amount']
        
        return math.floor(total_tax_revenue) * tax_rate
    
    def show_orders(self):
        if len(self.list_customer) > 0:
            return self.list_customer
        else:
            return 'Data is still empty. Add your orders first!'
    