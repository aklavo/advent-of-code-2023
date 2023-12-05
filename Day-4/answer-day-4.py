# Open input file and read lines
with open('input-day-4.txt') as f: #input-day-2
    lines = f.readlines()

def get_list_of_numbers(line,num_type):
    if num_type == "Winning":
        index = 0
    elif num_type == "Your":
        index = 1
    # Isolate winning and your numbers  
    numbers = line.strip().split(":")[1].split("|")[index].strip().split(" ")
    # Remove empty strings ''= False
    numbers = [n for n in numbers if n]
    return numbers

def count_winning_numbers(winning_numbers, your_numbers):
    total_winning_numbers = 0
    for num in your_numbers:
        if num in winning_numbers:
            total_winning_numbers += 1
            #print(f"Winning number: {num}")
    #print(f"Total winning numbers: {total_winning_numbers}\n")
    return total_winning_numbers

def score_card(total_winning_numbers):
    if total_winning_numbers > 0:
        points = 2**(total_winning_numbers-1)
        return points
    else:
        return 0
    
def part_1(lines):
    total_points = 0    
    for line in lines:
        total_winning_numbers = 0
        points = 0  
        winning_numbers = get_list_of_numbers(line,"Winning")
        your_numbers = get_list_of_numbers(line,"Your")
        total_winning_numbers = count_winning_numbers(winning_numbers, your_numbers)
        points = score_card(total_winning_numbers)
        #print(f"Card points: {points}")
        #print(f"Number of winning numbers: {total_winning_numbers}")
        total_points += points
        #print(f"Current total: {total_points}\n")
    return f"Total points: {total_points}" 

def part_2(lines):
    total_cards = 0
    card_counter = [1]*len(lines)
    for i, line in enumerate(lines):
        total_winning_numbers = 0 # on a card
        winning_numbers = get_list_of_numbers(line,"Winning")
        your_numbers = get_list_of_numbers(line,"Your")
        total_winning_numbers = count_winning_numbers(winning_numbers, your_numbers) 
        
        #print(f"Card counter: {card_counter}")
        # update card counter 
        for j in range(i+1,i+total_winning_numbers+1):
            card_counter[j] += 1*card_counter[i]
        #print(f"Number of cards: {card_counter[i]}")
        #update total cards
        total_cards += card_counter[i]
        #print(f"Total cards: {total_cards}")
           
    return total_cards
    
    
part_1_answer = part_1(lines)
part_2_answer = part_2(lines)    
         
#print(part_1_answer)    
print(part_2_answer)   

        
    