lst = [11, 22, 44, 55, 66, 77, 88, 99, 00]

i = 0
j = 1

lst2 = []

while j <= len(lst):
    for item in range(len(lst)):
        if lst[i] * 2 == lst[j]:
            lst2.append(lst[i] * 2)
            i += 1
            j += 1
        else:
            lst2.append((lst[i], lst[j]))

print(lst2)    
        