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

def rev_string(x):
    return x[::-1]

mystr = rev_string("!gnirts esrever eht detelpmoc I")
print(mystr)

def zach_num_within(n):
    if n in range(1,9):
        print( " %s is in the range"%str(n))
    else:
        print("The number is outside of the give range")

zach_num_within(1)
zach_num_within(8)
zach_num_within(4)
zach_num_within(12)

def solution_num_within(x,a,b):
  return x in range(a,b+1)
     
print(solution_num_within(3,2,4))     
print(solution_num_within(3,1,3))     
print(solution_num_within(10,2,5))

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)

#pascal is a little confusing. Had to use the solution to get the code right.