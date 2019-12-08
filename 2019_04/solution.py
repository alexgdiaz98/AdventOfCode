def valid(num):
    double = False
    cur_double = 0
    for i, letter in enumerate(num):
        if i != 0 and num[i] == num[i-1]:
            if cur_double == 0:
                cur_double = 2
                if i == len(num)-1:
                    double = True
            else:
                cur_double += 1
        elif cur_double == 2:
            double = True
            cur_double = 0
        elif cur_double != 0:
            cur_double = 0
        if i != 0 and int(num[i]) < int(num[i-1]):
            return False # Decreasing Numbers
    return double

total = 0
for i in range(347312, 805915):
    if valid(str(i)):
        total += 1

print(total)