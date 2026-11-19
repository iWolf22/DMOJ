# Problem: CCC '01 S1 - Keeping Score (ccc01s1)
# Problem URL: https://dmoj.ca/problem/ccc01s1
# Submission: 3547344 (https://dmoj.ca/submission/3547344)
# Language: 
# Submitted: 2021-04-08T02:35:20+00:00

#CCC '01 S1 - Keeping Score

def split(word): 
    return [char for char in word]

def split_suit(org_phrase):
    return_clubs = []
    return_diamonds = []
    return_hearts = []
    return_spades = []
    suit = ""

    for i in range(len(org_phrase)):
        if org_phrase[i] == "C":
            suit = "C"
        elif org_phrase[i] == "D":
            suit = "D"
        elif org_phrase[i] == "H":
            suit = "H"
        elif org_phrase[i] == "S":
            suit = "S"
        else:
            if suit == "C":
                return_clubs.append(org_phrase[i])
            elif suit == "D":
                return_diamonds.append(org_phrase[i])
            elif suit == "H":
                return_hearts.append(org_phrase[i])
            elif suit == "S":
                return_spades.append(org_phrase[i])
            else:
                print("error")
    
    return(return_clubs,return_diamonds,return_hearts,return_spades)

def point_collector(suit):
    point_counter = 0
    if len(suit) == 0:
        return(3)
    if len(suit) == 1:
        point_counter += 2
    if len(suit) == 2:
        point_counter += 1
    for i in range(len(suit)):
        if suit[i] == "A":
            point_counter += 4
        elif suit[i] == "K":
            point_counter += 3
        elif suit[i] == "Q":
            point_counter += 2
        elif suit[i] == "J":
            point_counter += 1
        else:
            point_counter += 0
    return(point_counter)

def printing(suit_cards,suit_name,suit_points):
    if suit_points >= 10:
        whitespaces = 29 - (len(suit_name) + len(suit_cards) * 2)
    else:
        whitespaces = 30 - (len(suit_name) + len(suit_cards) * 2)
    
    suit_cards_string = ""
    for i in range(len(suit_cards)):
        suit_cards_string = suit_cards_string + " " + suit_cards[i]

    return(suit_name + suit_cards_string + (" ") + str(suit_points))

org_phrase = split(input())

clubs, diamonds, hearts, spades = split_suit(org_phrase)

clubs_points = point_collector(clubs)
diamonds_points = point_collector(diamonds)
hearts_points = point_collector(hearts)
spades_points = point_collector(spades)

clubs_string = printing(clubs,"Clubs",clubs_points)
diamonds_string = printing(diamonds,"Diamonds",diamonds_points)
hearts_string = printing(hearts,"Hearts",hearts_points)
spades_string = printing(spades,"Spades",spades_points)

print("Cards Dealt Points")
print(clubs_string)
print(diamonds_string)
print(hearts_string)
print(spades_string)

total_points = clubs_points + diamonds_points + hearts_points + spades_points

if total_points >= 10:
    print("Total " + str(total_points))
else:
    print("Total " + str(total_points))