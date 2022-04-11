class Mobile_Recharge:
    print("Mobile Recharge \n")
    print("1.Robi")
    print("2.Airtel")
    print("3.Banglalink")
    print("4.Grameenphone")
    print("5.Teletalk")
    print("0.Main Menu")
    def __init__(self,num):
        self.num = num
    def mobile_recharge(self):
        if self.num == 1:
            from recharge import Reacharge

try:
    num = int(input("type the operations number: "))
    try:
        recharge = Mobile_Recharge(num)
    except Exception as e:
        print(e)
except ValueError:
    print("type an integer value")


        
        
        
