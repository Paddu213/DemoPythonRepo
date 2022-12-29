class Shopping:
    dictionary = {"mobile": 10000, "laptop": 200000}
    def add_items(self):
        print("Enter item name: ")
        item=input()
        print("Enter item value: ")
        value=int(input())
        self.dictionary[item]=value
    def avail_items(self):
        for key in self.dictionary.keys():
             print(key,end=" ")
        print()
    def rem_items(self):
        print("Enter item to remove: ")
        ite=input()
        del self.dictionary[ite]
        print(self.dictionary)
    def total_price(self):
        list_a=[]
        for value in self.dictionary.values():
            list_a.append(value)
        print("total price"+str(sum(list_a)))
    def add_price(self):
        print("enter item: ")
        items=input()
        print("Enter price to update: ")
        price=int(input())
        for key in self.dictionary.keys():
            if key==items:
                self.dictionary[key]=price
        print(self.dictionary)
obj=Shopping()
obj.add_items()
obj.avail_items()
obj.rem_items()
obj.total_price()
obj.add_price()


    