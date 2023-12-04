# Open input file and read lines
with open('input-day-3.txt') as f: #input-day-2
    lines = f.readlines()
# initialize answer
answer = 0
grid = []

def has_adjacent_symbols(grid, start_col, end_col, row):
    row_start = row -1
    row_end = row + 1
    col_start = start_col - 1
    col_end = end_col + 1
    
    ## Edge Cases
    # Handle first row
    if row == 0:
        row_start = row
    # Handle last row
    if row == len(grid)-1:
        row_end = row  
    # Handle first column
    if start_col == 0:
        col_start = start_col
    # Handle last column
    if end_col == len(grid[row])-1:
        col_end = end_col
    
    ## Check if there are any adjacent symbols
    for i in range(row_start,row_end+1):
        for j in range(col_start, col_end+1):
            print(grid[i][j])
            if grid[i][j] != "." and not grid[i][j].isdigit():
                return True
    return False

# Make grid with input data
# example: grid[1][3] row 2 col 4       
for line in lines:
    rows = []
    for char in line.strip('\n'):
        rows.append(char)
    grid.append(rows)
      

start_num_pos = "#"
end_num_pos = "#"
number = ""

for i in range(len(grid)): # loop through input rows
    for j in range(len(grid[i])): # loop through input columns within one row
           
        cur_char = grid[i][j]
        print(grid[i][j],f"is at position: ({i},{j})")
            
        # We find the start of a number
        if grid[i][j].isdigit() and start_num_pos == "#":
            start_num_pos = j
            end_num_pos = j
            print("We have the start of a number: ", grid[i][j])
            number += grid[i][j]
            continue
        
        # We find additional digit
        if grid[i][j].isdigit() and start_num_pos != "#":
            number+=grid[i][j]
            print(f"{grid[i][j]} is an additional digit")
            
        # when number is the last character in the line and a number we found the end of a number    
        if j == len(grid[i])-1 and grid[i][j].isdigit():
            end_num_pos = j
            print("We have the end of a number. And it end at the end of a line.")
            print(f"The number is: {number}. Is there an adjacent symbol?")
            print(f"Start index: {start_num_pos} End index: {end_num_pos} Row: {i}")
            if has_adjacent_symbols(grid, start_num_pos, end_num_pos, i):
                print("Yes")
                answer += int(number) 
            else:
                print("No")
                
            # reset number data
            number = ""
            start_num_pos = "#"
            end_num_pos = "#"
                
        # We find the end of number (we find a non-digit)
        if not grid[i][j].isdigit() and start_num_pos != "#":
            end_num_pos = j - 1
            print("We have the end of a number.")
              
            print(f"The number is: {number}. Is there an adjacent symbol?")
            print(f"Start index: {start_num_pos} End index: {end_num_pos} Row: {i}")
            if has_adjacent_symbols(grid, start_num_pos, end_num_pos, i):
                print("Yes")
                answer += int(number) 
            else:
                print("No")
                
            # reset number data
            number = ""
            start_num_pos = "#"
            end_num_pos = "#"
        

 
print(answer)
          
