my_list = [1,1]

for n in range(1,9):
  my_list.append(my_list[n] + my_list[n-1])
  
print(my_list)