Passcode=9848
main_lock=1234
print("'PhonePe' is encrypted ..Please Enter the Passcode")
passcode_1=int(input())
if Passcode==passcode_1:
    print("Phone pe app is opened")
    print("Please enter your lock screen passcode")
    main_lock_1 =int(input())
    if main_lock==main_lock_1:
        class Phone_pe:
            contacts_list = {"Yaseen":9490788769, "Self":6302984983,"Nanna":9848504810,"Venky":9100422329}
            valid_plans=[239,199,699,1225,355,555]
            UPI_Pin = 12345

            def __init__(self, Bank_Balance):
                self.Bank_Balance = Bank_Balance

            def mobile_recharge(self):
                print("Mobile Recharge ")
                print("search by number or name")
                self.number = input()
                if self.number or self.name in self.contacts_list:
                    print("select the number ")
                    print("search for a plan ")
                    self.plan = int(input())
                    if self.plan in self.valid_plans:
                        print("Proceed to pay")
                        print("Pay {}".format(self.plan))
                        if self.plan > self.Bank_Balance:
                            print("Insufficient Balance")
                        else:
                            print(" Enter UPI Pin :")
                            self.pin = int(input())
                            if self.pin == self.UPI_Pin:
                                print("Mobile Recharge Successfull!")
                                self.Bank_Balance = self.Bank_Balance - self.plan
                                print("Current Balance is {}".format(self.Bank_Balance))

                            else:
                                print("Incorrect UPI Pin....Retry")

                    else:
                        print(" Not a Valid plan ")


                else:
                    print("Enter Number")
                    self.num = int(input())
                    print("search for a plan ")
                    self.plan = int(input())
                    print("search for a plan ")
                    self.plan = int(input())
                    if self.plan in self.valid_plans:
                        print("Proceed to pay")
                        print("Pay {}".format(self.plan))
                        if self.plan > self.Bank_Balance:
                            print("Insufficient Balance")
                        else:
                            print(" Enter UPI Pin :")
                            self.pin = int(input())
                            if self.pin == self.UPI_Pin:
                                print("Mobile Recharge Successfull!")
                                self.Bank_Balance = self.Bank_Balance - self.plan
                                print("Current Balance is {}".format(self.Bank_Balance))

                            else:
                                print("Incorrect UPI Pin....Retry")
                    else:
                        print("Not a Valid plan ")


            def check_Balance(self):
                print("Check Bank Balance ")
                print(" Enter UPI Pin :")
                self.pin = int(input())
                if self.pin == self.UPI_Pin:
                    print(self.Bank_Balance)
                    print()
                else:
                    print("Incorrect UPI Pin ")
                    print()


        obj = Phone_pe(10000)
        print("Select Option ")
        print("1. check Bank Balance \n2. Mobile Recharge ")
        Option=int(input())
        if Option==1:
            obj.check_Balance()
        elif Option==2:
            obj.mobile_recharge()
    else:
        print("Incorrect Lock")
else:
    print("Incorrect Passcode")

