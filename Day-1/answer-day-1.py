with open('input-day-1.txt') as f:
  lines = f.readlines()
  print(lines[0])
  answer = 0
  for line in lines:
    for char in lines:
      if char.isdigit():
        first_num = char
        last_num = char
        two_digit_num = int(first_num + last_num)
    answer += two_digit_num
