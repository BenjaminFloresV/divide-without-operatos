#!/usr/bin/env python3
def divide(a,b):
    negative_counter = 0
    if a < 0:
        a = int(str(a).replace('-', ''))
        negative_counter += 1
    if b < 0:
        b = int(str(b).replace('-', ''))
        negative_counter += 1
    if a == 0:
        return 0
    count = 0
    aux_a = a
    aux_b = 0
    decimal_zeros = None
    while True:
        if aux_b < aux_a:
            aux_b += b
            count += 1
        elif aux_b == aux_a:
            break
        elif aux_b > aux_a:
            if decimal_zeros is None:
                decimal_zeros = "0."
            else:
                decimal_zeros += "0"
            aux_a = int(str(aux_a) + "0")
    
    if decimal_zeros is not None:
        result = decimal_zeros + str(count)
    result =  count
    
    if negative_counter in (0, 2):
        return result
    return int("-" + str(result))

print(divide(30, 10))