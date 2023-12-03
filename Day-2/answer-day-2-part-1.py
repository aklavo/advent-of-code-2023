## 12 red cubes, 13 green cubes, and 14 blue cubes##

# Open input file and read lines
with open('input-day-2.txt') as f: #input-day-2
    lines = f.readlines()


answer = 0
cube_limits = {
    "red":12,
    "green":13,
    "blue":14
}   

for line in lines:
    # Split line about ":""
    line_split = line.split(':')
    
    # Split game about ";" to isolate each handful of cubes
    grabs = line_split[1].split(";")
    print(f"Current {answer}")
    print("\n"+line+"\n")
    possible = True
    # loop through each handful to isolate cubes
    for grab in grabs:
        print(f"possible={possible}")
        # check if possible to continue game
        if possible:
            print(f"Grab: || {grab} ||")
            cubes = grab.split(",")
            for cube in cubes:
                print(cube)
                amount = int(cube.strip().split(" ")[0])
                color = cube.strip().split(" ")[1]
                print(f"{color} Limit: " + str(cube_limits[color]))
                if amount > cube_limits[color]:
                    possible = False
                    print(f"Not possible (possible={possible})\n")
                    break
                else:
                    print("Cube Possible \n")
                # if you get to the end of the cube list, grab is possible
                if cube == cubes[-1]:
                    print("------Grab possible----------- \n")
        else: 
            break        
        # if you get to the end of the grab list and it's possible the game is possible
        if grab == grabs[-1] and possible:
            possible = True
            print("------------------Game possible--------------------------\n")
            # Store game number as int if possible
            game_number = int(line_split[0][4:].strip())
            answer += game_number
            print(f"Game possible, number = {game_number}, total answer = {answer} \n")
                    
print("\n",answer)            

