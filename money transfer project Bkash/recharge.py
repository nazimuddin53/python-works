from balance import Balance
from pin_code import PinCode

class Reacharge:
    print("bkash mobile reacharge")
    print("1.Prepaid")
    print("2.Postpaid")
    print("3.Auto Reacharge")
    print("0.Main Menu")
    def __init__(self,num):
        self.num = num
    def reacharge(self):
        if self.num == 1 or self.num == 2:
            #>>>>>>>>>>>>>>>>>>>>>>>> Input Mobile No <<<<<<<<<<<<<<<<<<<<<
            try:
                mobile_no = str(input("Mobile No: "))
                #>>>>>>>>>>>>>>>>>>>>>>>>> Type Casting <<<<<<<<<<<<<<<<<<<<<<<
                if 11 == len(mobile_no):
                    try:
                        amount = int(input("Enter your reacharge amount: "))
                        if amount >= 10:
                            if str(amount) >= Balance().balance_check():
                                pin = int(input("Enter your PIN for confirm: "))

                                #>>>>>>>>>>>>>>>>>>>>> import pin_code file for PIN <<<<<<<<<<<<<<<<
                                mypin_code = PinCode().pin_code()

                                #>>>>>>>>>>>>>>>>>>>>>> pin code checking <<<<<<<<<<<<<<<<<<<<<<<<
                                if pin == mypin_code:
                                    
                                    Balance().balance_subtraction(amount)
                                    print("Receied mobile techarge \n request of ",amount, "TK for ",mobile_no,".\n fee tk 0.00 balance \n ",Balance().balance_check()," \n trxid ........... pls wait for confirmation.")
                            else:
                                print("Amount is not available")
                        else:
                            print("minimum recharge amount is 10.0 TK")
                        
                    except ValueError :
                        print("amount is an integer type value")
                else:
                    print("Type the cract number")    
            except ValueError:
                print("This is not a mobile number ")
        

n = int(input("Select a option for recharge: "))
r = Reacharge(n)
r.reacharge()