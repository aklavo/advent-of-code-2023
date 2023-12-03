## 12 red cubes, 13 green cubes, and 14 blue cubes##

# Open input file and read lines
with open('input-day-2.txt') as f: #input-day-2
    lines = f.readlines()
# initialize answer
answer = 0

# loop through each line
for line in lines:   
    # initialize list to store max cubes for each color
    max_cubes= {
        "red":[],
        "green":[],
        "blue":[]
    }   
    # Split line about ":""
    line_split = line.split(':')
    # Split game about ";" to list all grabs
    grabs = line_split[1].split(";")
    
    # loop through each grab to isolate grabs
    for grab in grabs:
        # Split grabs about "," to list all cube amounts
        cubes = grab.split(",")
    
        # loop through each cube amounts to isolate amount and color
        for cube in cubes:
            amount = int(cube.strip().split(" ")[0])
            color = cube.strip().split(" ")[1]
            # add amount to color list
            max_cubes[color].append(amount)
    # calculate max of each color list and multiple together        
    power = max(max_cubes["red"]) * max(max_cubes["green"]) * max(max_cubes["blue"])
    # add to running total
    answer += power
                
print(answer)            

