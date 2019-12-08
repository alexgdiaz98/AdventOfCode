with open('input.txt', 'r') as file:
    arr = []
    for line in file:
        arr.append(int(line))
    print(arr)
    found = False
    i = 0
    past_frequencies = [0]
    while not found:
        if (past_frequencies[-1] + arr[i]) in past_frequencies:
            found = True
            print(past_frequencies[-1] + arr[i])
        else:
            past_frequencies.append(past_frequencies[-1] + arr[i])
            #print(arr[i], ' -> ', (past_frequencies[-2] + arr[i]))
        i = (i + 1) % len(arr)
        