input_value = input()

if int(input_value) == 0:
    print('zero')
if int(input_value) > 0:
    if int(input_value)%2 == 0:
        print('positive-even')
    else:
        print('positive-odd')
if int(input_value) < 0:
    if int(input_value)%2 == 0:
        print('negative-even')
    else:
        print('negative-odd')
    
