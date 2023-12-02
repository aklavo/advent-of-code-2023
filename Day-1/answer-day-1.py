# Open input file and read lines
with open('input-day-1.txt') as f:
  lines = f.readlines()

# Initialize answer variable  
answer = 0

# Word to number mapping
num_dict = {'one': '1', 
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'}

 
# Loop through each line
for line in lines:
  # Initialize first and last numumber to be found
  first_num = 0
  last_num = 0
  
## WORD SEARCH
  # Initialize indexes and values
  first_word_index = len(line)+1
  last_word_index = 0
  first_word_value = ""
  last_word_value = ""
  
  # loop through keys in map
  for key in num_dict.keys():
    first_index = line.find(key) # find first index of a word (-1 if no word)
    last_index = line.rfind(key) # find last index of a word (-1 if no word)
    # assign first word
    if first_index != -1 and first_index < first_word_index:
       first_word_index = first_index
       first_word_value = num_dict[key]
    # addsign last word
    if last_index >= last_word_index:
       last_word_index = last_index
       last_word_value = num_dict[key]
       
## NUMBER SEARCH     
  char_dict = {}
  # Loop through characters in line
  for i,char in enumerate(line):
   # if it's a digit and not defined yet
    if char.isdigit() and first_num == 0:
    # ...and the digit index is before the index of the first word 
      if i < first_word_index:
        first_num = char
      else:
        # if not the first word is the first number
        first_num = first_word_value
    # if it's a digit
    if char.isdigit():
      #...and the digit index is after the index of the last word
      if i >= last_word_index:
        last_num = char
      else:
        # in not the last word is the last number
        last_num = last_word_value
      
  # Concatenate numbers, convert to an integer and add to running total
  answer += int(first_num + last_num)

# Print answer
print(f"The answer is: {answer}")


