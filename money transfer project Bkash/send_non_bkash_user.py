# ......................./////////////////////  class send money ///////////////////////............
class Non_Bkash_User:
    print("Send Money to Non-bkash User") 
    def __init__(self,n,receiver_id):
        self.receiver_id = receiver_id
        self.n = n
        self.number = receiver_id[0]
    def non_bkash_user(self):
        # ..................///////////////////// file opening ///////////////////////...............
        try :
            user_pin = open("user_data/password/01989488033.csv", "r")
            amount = open("user_data/amount/01989488033.csv","r")
        except Exception as e:
            print(e)
        else:
            pin_code = int(user_pin.read())
            available_amount = float(amount.read())
        # ................../////////////////////// file closing //////////////////////................
        finally:
            user_pin.close()
            amount.close()
        #...............................//////////////// cheaking number len ?? ///////////////////............
        if (len(self.n))==11:
            try:
                send_amount = int(input('Please enter sending amount: '))
                print("To : ",self.number,"\n","Amount : ",send_amount,"TK")
                # ........................../////////////// Charg /////////////////////.....................
                charging_amount = float(1.95)
                charge = round(((send_amount/100)*charging_amount),2)
                # ......................./////////////////// Total send amount ////////////////////............ 
                total_send_amount = send_amount+charge

                # .....................///////////////////// Pin code input ///////////////////////.............
                pin = str(input("Please enter PIN to confirm: "))
            
                # ....................///////////////////// pin code cheaking ////////////////////...............
                if __name__=="__main__":
                    from pin_code import PinCode
                    p = PinCode(pin)
                    p.pin_code()
                    if available_amount > total_send_amount:
                        try:
                            money = open("user_data/amount/01989488033.csv","w")
                        except Exception as e:
                            print(e)
                        else:
                            after_sendmoney =str(round(available_amount - (total_send_amount),2))
                            money.write(after_sendmoney)
                        finally:
                            money.close()
                        # .......................///////////////////// file poening  ////////////////////...............
                        try:
                            currentamount = open("user_data/amount/01989488033.csv","r")
                        except Exception as e:
                            print(e)
                        else:
                            current_amount = currentamount.read()
                        finally:
                            currentamount.close()
                            print("Send Money to Non-bkash User \n\n the send money is successful. \n receiver number: ",self.number,"amount: ",float(send_amount),"TK \n charge: ",charge,"TK \n Current balance: ",current_amount,"TK")      
                    else:
                        print("Amount is not available")  
                else:
                    print("incract pin")
            except Exception as e:
                print(e)
        else:
            print('type the cract number')         
# .....................////////////////////// input numbers for send money ////////////////////////....................
try:
    number_input = input("Please enter receiver account number: ")
    n = list(map(str ,number_input.strip()))    
    receiver_id = (number_input.split())
    # ..................//////////////////// create object for send money /////////////////////................
    try:
        send = Non_Bkash_User(n,receiver_id)
        send.non_bkash_user()
    except Exception as e:
        print(e)
except:
    print("Type your cract number")


