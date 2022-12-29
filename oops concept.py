# instance methods

#class methods

#static methods

class Car:
    someclassdummyvar="dummy"
    def sample_car_instance_method(self,a):
        print(a)
        print(self.someclassdummyvar)
carObj=Car()
carObj.sample_car_instance_method("Hello again!")

carObj=Car()
carObj.sample_car_instance_method(2)



class CarSample:
    dummyvar1 = "dummyvar1"
    dummyvar2 = "dummyvar2"
    def __init__(self,name,model):
        self.name = name
        self.model = model
    def displayCarDetails(self):
        print(self.name)
        print(self.model)
carObj=CarSample("Audi","A5")
carObj.displayCarDetails()


#Static Methhod

class StaticClass:
    @staticmethod
    def sample_static_method_addition(x,y):
        return x+y

    @staticmethod
    def sample_static_method_multiplication(x,y):
        return x*y
staticObj=StaticClass()
output_add=staticObj.sample_static_method_addition(2,3)
output_mul=staticObj.sample_static_method_multiplication(2,3)
print(output_add,output_mul)

StaticClass.sample_static_method_addition(2,3)





#Class Method

class ClassMethodExample:
    classVar1=False
    classVar2="ON"
    @classmethod
    def sample_class_method(cls):
        cls.classVar1=True
        cls.classVar2="OFF"
ClassMethodExample.sample_class_method()
print(ClassMethodExample.classVar1)
print(ClassMethodExample.classVar2)



