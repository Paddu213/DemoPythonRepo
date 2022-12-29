class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating
    def Display_Product_details(self):
        print("product name : {}".format(self.name))
        print("product price : {}".format(self.price))
        print("deal price : {}".format(self.deal_price))
        print("Ratings : {}".format(self.rating))


class Electrical(Product):
    def __init__(self,name,price,deal_price,rating,Warrenty):
        Product.__init__(self,name,price,deal_price,rating)
        self.Warrenty=Warrenty
    def Get_Warrenty(self):
        print("Warrenty : {}".format(self.Warrenty))


class Grocery_item(Product):
    def __init__(self,name,price,deal_price,rating,Expiry_Date,Package_Data):
        Product.__init__(self,name,price,deal_price,rating)
        self.Expiry_Date=Expiry_Date
        self.Package_Data=Package_Data
    def Get_Expiry_Date(self):
        print("Expiry Date : {}".format(self.Expiry_Date))
        print("Package Date : {}".format(self.Package_Data))

obj=Product("laptop",50000,35000,4)
obj.Display_Product_details()
print()

objEle=Electrical("mobile",50000,35000,4,"2years")
objEle.Display_Product_details()
objEle.Get_Warrenty()
print()

objGro=Grocery_item("milk",20,15,5,"10/10/2020","11/11/2025")
objGro.Display_Product_details()
objGro.Get_Expiry_Date()






