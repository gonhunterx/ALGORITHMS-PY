digits = [9]

updated_dig = digits + [1]

print(updated_dig)

left, right = 0, len(digits) - 1

single_dig_lst = []

if len(updated_dig) == 2:
    total = 0
    # updated_dig.pop()
    for i in updated_dig:
        total += i
        str_total = str(total)
        for j in str_total:
            single_dig_lst.append(j)

print(single_dig_lst)


print(total)
