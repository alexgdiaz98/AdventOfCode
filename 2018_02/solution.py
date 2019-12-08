# def check_id(id_num):
#     letters = {}
#     for letter in id_num:
#         if letter in letters.keys():
#             letters[letter] += 1
#         else:
#             letters[letter] = 1
#     ret_val = [False, False]
#     if 2 in letters.values():
#         ret_val[0] = True
#     if 3 in letters.values():
#         ret_val[1] = True
#     return ret_val

def compare(id1, id2):
    for i in range(len(id1)): # For each character in the ids
        if id1[:i] == id2[:i] and id1[i+1:] == id2[i+1:]: # if they are 1 character off of identical
            if id1 != id2:
                return True
    return False
    
with open('input.txt', 'r') as file:
    arr = []
    for line in file:
        arr.append(line.strip('\n'))
    to_search = arr[1:]
    for i, id_num in enumerate(arr):
        for j, id_num2 in enumerate(to_search):
            if compare(id_num, id_num2):
                print(id_num, id_num2)
        to_search.remove(to_search[0])