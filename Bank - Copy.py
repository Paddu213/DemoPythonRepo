class NegitiveError(Exception):
    pass
class HigherValueError(Exception):
    pass


class Bank:
    def __init__(self,bal_amount,limit):
        self.bal_amount=bal_amount
        self.limit=limit

    def Withdraw(self):
        print("enter amount to withdraw")
        self.inp=int(input())
        try:
            if self.inp>self.bal_amount:
                raise NegitiveError
            elif self.inp<self.bal_amount:
                if self.inp>self.limit:
                    raise HigherValueError
            elif self.inp==self.bal_amount:
                if self.inp>self.limit:
                    raise HigherValueError
                else:
                    print("amount withdrawl")
        except NegitiveError:
            print("insufficient balance")
        except HigherValueError:
            print("limit exceeded")

        except IndentationError:
            pass
obj=Bank(1000,500)

obj.Withdraw()




