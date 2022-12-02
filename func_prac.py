def max_num(a,b,c):
  return max([a,b,c])

print(max_num(15,19,21))

def mult_list(lst):
    if len(lst) == 0:
        return 0
    prod = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i

    return prod
        
print(mult_list([4,17,37]))