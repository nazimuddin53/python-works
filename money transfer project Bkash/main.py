#import all file
from operation import operation_list 
from operation import operation
print('welcome to bkash')
# bkash code
code = str(input("Type the bkash code: "))
try:
    if (code == '*247#'):
        operation_list()
    else:
        print("your entry code is wrong please try again")
except:
    print("Error")

# // input number for operations ///

