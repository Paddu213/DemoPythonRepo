class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating
        self.you_save=price-deal_price
    def Display_Product_details(self):
        print("product name : {}".format(self.name))
        print("product price : {}".format(self.price))
        print("deal price : {}".format(self.deal_price))
        print("Ratings : {}".format(self.rating))
        print("you saved :{}".format(self.you_save))
    def get_deal_price(self):
        return self.deal_price

class ElectroncItem(Product):
    def set_warrenty(self,Warrenty_in_months):
       self.Warrenty_in_months=Warrenty_in_months
    def Get_Warrenty(self):
        return self.Warrenty_in_months

class GroceryItem(Product):
    pass

class Order:
    def __init__(self,delivery_speed,delivery_address):
        self.items_in_cart=[]
        self.delivery_speed=delivery_speed
        self.delivery_address=delivery_address
    def add_items(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def Display_order_details(self):
        for product,quantity in self.items_in_cart:
            product.Display_Product_details()
            print("Quantity : {}".format(quantity))
    def Display_total_bill(self):
        total_bill=0
        for product,quantity in self.items_in_cart:
            price=product.get_deal_price()*quantity
            total_bill+=price
            print("Total_bill : {}".format(total_bill))


'''milk=GroceryItem("MILK",40,30,4)

lap=ElectroncItem("laptop",50000,45000,4.5)

order=Order("Prime delivery","Vijayawada")

order.add_items(milk,2)
order.add_items(lap,2)

print("_________________")

order.Display_order_details()

print("_______________________")
order.Display_total_bill()'''

