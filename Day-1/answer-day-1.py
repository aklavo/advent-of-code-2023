# Open input file and read lines
with open('input-day-1.txt') as f:
  lines = f.readlines()

# Initialize answer variable  
answer = 0
  
# Loop through each line
for line in lines:

  # Initialize first digit
  first_num = 0
    
  # Loop through characters in line
  for char in line:

    # If character is a digit and first isnot set, set first digit and last digit 
    if char.isdigit() and first_num == 0:
      first_num = char
      last_num = char
    # Continue to update last digit to current char if it is a digit
    if char.isdigit():
      last_num = char
        
  # Calculate calibration value from first and last digits    
  calibration_value = int(first_num + last_num)
  
  # Add calibration value to running total
  answer += calibration_value

# Print answer to part 1
print(f"The answer is: {answer}")
