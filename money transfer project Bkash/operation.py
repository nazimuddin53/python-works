class Operation:
    print('Welcome To Bkash\n')
    print("1.Send Money")
    print("2.Send Money to Non-bkash User")
    print("3.Mobile Recharge")
    print("4.Payment")
    print("5.Cash Out")
    print("6.Pay Bill")
    print("7.App Registration for Tk 25 Bonus")
    print("8.My bkash")
    print("9.Helpline\n")

    #...................////////////////// inharitance ////////////////..............
    def __init__(self,num):
        self.num = num
    # .................//////////////////// Operation list ///////////////................      
    def operation(self):
        try:
            if self.num == 1:
                try:
                    from send_money import SendMoney
                  
                except ImportError:
                    print("send_money import error")
            elif self.num == 2:
                try:
                    from send_non_bkash_user import Non_Bkash_User
               
                except ImportError as i:
                    print(i)
            elif self.num == 3:
                try:
                    from mobile_recharge import Mobile_Recharge      
                except ImportError as i:
                    print(i)
            elif self.num == 4:
                try:
                    from payment import Payment
                except ImportError as i:
                    print(i)
            elif self.num == 5:
                try:
                    from cash_out import Cashout
                except ImportError as i:
                    print(i)
            elif self.num == 6:
                try:
                    from pay_bill import PayBill
                except ImportError as i:
                    print(i)
        except Exception as e:
            print(e)
try:
    n = int(input("type the operations number: "))
except ValueError as v:
    print(v)


o = Operation(n)
o.operation()