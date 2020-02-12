import datetime

test_cases = int(input())
midnight = datetime.datetime.strptime('00.00', '%H.%M')
for input_line in range(test_cases):
    case = input().split()
    time = case[0] + "." + case[1]
    time = datetime.datetime.strptime(time, '%H.%M')
    minutes = midnight - time
    print(int(minutes.seconds / 60))