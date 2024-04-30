def reverse_number(num):
  temp = num
  reversed_num = 0
  reversed_num_final = ''

  while temp != 0:
    reversed_num = (reversed_num * 10) + (temp % 10)
    reversed_num_final = f"{reversed_num_final}{reversed_num}" if "0" in str(num) else f"{reversed_num}"
    temp = temp // 10

  return reversed_num_final
 
print(reverse_number(1000))
# 0001

print(reverse_number(584))
# 485

print(reverse_number(41897))
# 79814
