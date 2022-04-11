try:
    send_amount = int(input('Please enter sending amount: '))
except ValueError as e:
    print(e)
