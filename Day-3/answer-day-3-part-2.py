import time
start = time.time()
# Open input file and read lines
with open('input-day-3.txt') as f: #input-day-2
    lines = f.readlines()
# initialize answer
answer = 0
grid = []

def has_adjacent_star(grid, start_col, end_col, row):
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
    
    ## Check if there are any adjacent *'s
    for i in range(row_start,row_end+1):
        for j in range(col_start, col_end+1):
            if grid[i][j] == "*":
                star_pos = (i,j)
                return True, star_pos
    return False, ()

def add_star(stars, star_pos, number):
    # append first star found
    if len(stars) == 0:
        first_start = Star(star_pos, [int(number)])
        stars.append(first_start)
        print("First Star: ",first_start.pos, first_start.adjacent_numbers)
        return
    # look in list of starts, if it's already in there, append the number to the adjacent numbers list
    for num_star,star in enumerate(stars):
        if star.pos == star_pos:
            star.adjacent_numbers.append(int(number))
            print("Updated Star: ",star.pos, star.adjacent_numbers)
            return
        if num_star == len(stars)-1:
            stars.append(Star(star_pos, [int(number)]))
            print("New Star: ", star.pos, star.adjacent_numbers)
            return
        
        
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
stars = []

class Star:
    # define a star object with postion tuple and a list of adjacent numbers
    def __init__(self, pos, adjacent_numbers):
        self.pos = pos
        self.adjacent_numbers = adjacent_numbers  
        
        
for i in range(len(grid)): # loop through input rows
    for j in range(len(grid[i])): # loop through input columns within one row
           
        cur_char = grid[i][j]
        #print(grid[i][j],f"is at position: ({i},{j})")
            
        # We find the start of a number
        if grid[i][j].isdigit() and start_num_pos == "#":
            start_num_pos = j
            end_num_pos = j
            #print("We have the start of a number: ", grid[i][j])
            number += grid[i][j]
            continue
        
        # We find additional digit
        if grid[i][j].isdigit() and start_num_pos != "#":
            number+=grid[i][j]
            #print(f"{grid[i][j]} is an additional digit")
            
        # when number is the last character in the line and a number we found the end of a number    
        if j == len(grid[i])-1 and grid[i][j].isdigit():
            end_num_pos = j
            #print("We have the end of a number. And it end at the end of a line.")
            print(f"The number is: {number}. Is there an adjacent star?")
            #print(f"Start index: {start_num_pos} End index: {end_num_pos} Row: {i}")
            
            
            yes_no , star_pos = has_adjacent_star(grid, start_num_pos, end_num_pos, i)
            
            if yes_no:
                print("Yes")
                add_star(stars, star_pos, number)
            else:
                print("No")
                
            # reset number data
            number = ""
            start_num_pos = "#"
            end_num_pos = "#"
                
        # We find the end of number (we find a non-digit)
        if not grid[i][j].isdigit() and start_num_pos != "#":
            end_num_pos = j - 1
            #print("We have the end of a number.")
              
            print(f"The number is: {number}. Is there an adjacent star?")
            #print(f"Start index: {start_num_pos} End index: {end_num_pos} Row: {i}")
            
            yes_no , star_pos = has_adjacent_star(grid, start_num_pos, end_num_pos, i)
            if yes_no:
                print("Yes")
                add_star(stars, star_pos, number)
            else:
                print("No")
                
            # reset number data
            number = ""
            start_num_pos = "#"
            end_num_pos = "#"
       
        
print("-"*25,"\n")
for star in stars:
    print(star.pos, star.adjacent_numbers)
    if len(star.adjacent_numbers) == 2:
        answer += star.adjacent_numbers[0] * star.adjacent_numbers[1]
print("-"*25,"\n",answer, f"Is the answer right: {answer == 467835}")
end_time = time.time()
print(f"Execution time: {end_time - start}")