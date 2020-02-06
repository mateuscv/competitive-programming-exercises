from math import floor
t = int(input())

for test_case in range(t):

    s = int(input())
    cashback = 0
    temp_s = s

    while (temp_s >= 10):

        remainder = temp_s % 10 # get the remainder of the current money stack 's' / 10. Optimal buying happens with full integer cashbacks (values of 's' divisible by 10).
        divisible_by_ten_value_of_s = temp_s - remainder # get the value of s which doesn't have the remainder (e.g. 4500 instead of 4506)
        
        temp_s -= divisible_by_ten_value_of_s # keep only the remainder in the temp_s variable (e.g. 4506 - 4500 = 6)

        cashback += divisible_by_ten_value_of_s / 10 # sum the cashback total value with the cashback from the current operation (e.g. 0 + 450...)

        temp_s += divisible_by_ten_value_of_s / 10 # sum the / 10 of the value without the remainder (4500/10) with the remainder (e.g. 450 + 6). This is the value of 's' for the next
                                                   # loop, since all the rest of the stack has been spent buying (read: divided by 10 and deducted from the total)

        
    print(int(s + cashback))

    