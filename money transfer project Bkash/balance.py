class Balance:
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Balance Chacking <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def balance_check(self):
        try:
            balance = open("user_data/amount/01989488033.csv","r")
        except Exception as e:
            print(e)
        else:
            mybalance = balance.read()
            return mybalance
        finally:
            balance.close()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Balance Summation <<<<<<<<<<<<<<<<<<<<<<<<       
    def balance_summation(self,amount):
        try:
            balance = open("user_data/amount/01989488033.csv","r")     
        except Exception as e:
            print("file read : ",e)
        else:
            mybalance = balance.read()
            try:
                present_balance = open("user_data/amount/01989488033.csv","w")
            except Exception as e:
                print("file write : ",e)
            else:
                money =  int(mybalance) + int(amount)
                present_balance.write(str(money))
            finally:
                present_balance.close()
        finally:
            balance.close()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Balance Subtraction <<<<<<<<<<<<<<<<<<<<<
    def balance_subtraction(self,amount):
        try:
            balance = open("user_data/amount/01989488033.csv","r")     
        except Exception as e:
            print("file read : ",e)
        else:
            mybalance = balance.read()
            try:
                present_balance = open("user_data/amount/01989488033.csv","w")
            except Exception as e:
                print("file write : ",e)
            else:
                money =  int(mybalance) - int(amount)
                present_balance.write(str(money))
            finally:
                present_balance.close()
        finally:
            balance.close()


print(Balance().balance_check())
