common_denominators = []

    for i in input_list:
        # if the item is divisble by three
        if not i%3:
            # add the value 3 to the list
            common_denominators.append(3)

        # if the item is divisible by two
        elif not i%2:
            # add the value 2 to the list
            common_denominators.append(2)

        # otherwise
        else:
            # append the value 0
            common_denominators.append(0)

    return common_denominators
