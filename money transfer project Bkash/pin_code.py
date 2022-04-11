class PinCode:   

    #>>>>>>>>>>>>>>>>>>>>>> Balance control <<<<<<<<<<<<<<<<<
          
    def pin_code(self):
        try:
            pincode = open("user_data/password/01989488033.csv","r")
        except IOError as i:
            print("pin file",i) 
        else:
            p_code = pincode.read()
            return p_code
        #>>>>>>>>>>>>>>>>>>>>>>>>>> Close PIN code File<<<<<<<<<<<<<<<<<<       
        finally:
            pincode.close()
    def pin_code_change(self,pin):
        print(self.pin_code())
        if self.pin_code() == str(pin):
            try:
                PIN = int(input("PIN: "))
            except ValueError:
                print("enter intger value for your PIN ")
            if len(str(PIN)) == 5:
                confirm_pin = int(input("Confrim PIN: "))
                if PIN == confirm_pin:
                    try:
                        present_pin = open("user_data/password/01989488033.csv","w")
                    except Exception as e:
                        print(e)
                    else:
                        password = present_pin.write(str(PIN))
                        print("your password has been changed successfully")
                    finally:
                        present_pin.close()
                else:
                    print("PIN and comfirm PIN not match.. Please try again")
            else:
                print("enter 5 number for your PIN")
        else:
            print("sorry worng PIN .. ")

