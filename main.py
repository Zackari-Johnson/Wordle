import random
import time
from colorama import Fore
wordlist = [
  "Apply", "Awful", "Above", "Apple", "Award", "Angry", "Album", "Avoid", "Ahead", "Allow", "Alive", "Aware", "After", "Adopt", "Admit", "Adapt", "Among", "Apart", "Abuse", "Actor", "About", "Along", "Again", "Aside", "Argue", "Agent", "Agree", "Angle", "Anger", "Arise", "Asset", "Alone", "Alter", "Block", "Bunch", "Bench", "Beach", "Break", "Badly", "Brown", "Brush", "Buyer", "Brief", "Below", "Birth", "Blame", "Basic", "Bible", "Bring", "Broad", "Begin", "Build", "Being", "Blade", "Bread", "Brand", "Board", "Blind", "Blood", "Brain", "Basis", "Crazy", "Check", "Cheek", "Clock", "Chief", "Crack", "Coach", "Couch", "Cheap", "Cycle", "Catch", "Child", "Crowd", "Climb", "Chain", "Cover", "Crash", "Craft", "Civil", "Chart", "Chase", "Chair", "Chest", "Carry", "Claim", "Cream", "Crime", "Cable", "Cabin", "Cloud", "Could", "Cause", "Cross", "Clear", "Count", "Color", "Coast", "Close", "Class", "Clean", "Court", "Dozen", "Depth", "Drink", "Draft", "Daily", "Dirty", "Delay", "Death", "Drive", "Doubt", "Drama", "Dream", "Dance", "Dress", "Enjoy", "Equal", "Exact", "Extra", "Exist", "Empty", "Every", "Enemy", "Eight", "Entry", "Earth", "Early", "Essay", "Event", "Elect", "Eager", "Error", "Elite", "Enter", "Fifty", "Fight", "Faith", "Fully", "Fresh", "Forth", "Flesh", "Funny", "Fewer", "Favor", "Frame", "Force", "Focus", "Fence", "Fiber", "Flame", "Field", "Found", "Final", "First", "Floor", "Fault", "Front", "Fruit", "False", "Float", "Ghost", "Given", "Glove", "Grave", "Group", "Guard", "Guide", "Grand", "Grade", "Grant", "Guest", "Guess", "Giant", "Glass", "Green", "Great", "Grain", "Grass", "Happy", "Heavy", "Honey", "Habit", "Human", "Humor", "Hello", "Horse", "Hotel", "House", "Heart", "Honor", "Index", "Imply", "Image", "Ideal", "Inner", "Issue", "Judge", "Juice", "Joint", "Knock", "Knife", "Lucky", "Lunch", "Light", "Laugh", "Leave", "Layer", "Lover", "Lower", "Level", "Local", "Limit", "Lemon", "Labor", "Label", "Legal", "Large", "Least", "Learn", "Loose", "Later", "Major", "Match", "Maybe", "Maker", "Might", "Month", "Mouth", "Movie", "Mayor", "Marry", "Money", "Music", "Model", "Media", "Metal", "Mouse", "Mount", "Motor", "Moral", "Meter", "Minor", "Newly", "Naked", "Night", "Nerve", "Never", "North", "Novel", "Noise", "Nurse", "Offer", "Occur", "Ought", "Often", "Other", "Owner", "Ocean", "Order", "Onion", "Porch", "Pitch", "Patch", "Prove", "Power", "Photo", "Phone", "Phase", "Proof", "Party", "Peace", "Price", "Prime", "Place", "Paper", "Piece", "Pride", "Proud", "Pound", "Print", "Prior", "Press", "Point", "Plate", "Plant", "Plane", "Pilot", "Piano", "Pause", "Panel", "Paint", "Quick", "Quiet", "Quite", "Quote", "Relax", "Reply", "Reach", "Rough", "Ready", "Right", "Rapid", "River", "Refer", "React", "Round", "Radio", "Range", "Ratio", "Raise", "Route", "Rural", "Shock", "Seize", "Shake", "Stick", "Stock", "Stuff", "Shelf", "Staff", "Speak", "Smoke", "Shift", "Sharp", "Shape", "Sweep", "Shade", "Sight", "Shrug", "Space", "Scope", "Skill", "Stake", "Study", "Swing", "Sweet", "Story", "Spend", "Solve", "Sorry", "South", "Swear", "Speed", "Style", "Slave", "Short", "Sheet", "Share", "Shine", "Shirt", "Shoot", "Shall", "Shore", "Seven", "Shell", "Serve", "Shout", "Sauce", "Split", "Scale", "Super", "Scene", "Score", "Strip", "Storm", "Sport", "Smell", "Sleep", "Smart", "Small", "Slice", "Smile", "Since", "Stand", "Sugar", "Sound", "Slide", "Stage", "Solid", "Salad", "Sales", "Sense", "Solar", "Stair", "Stare", "State", "Steal", "Steel", "Still", "Stone", "Store", "Start", "Thick", "Think", "Thank", "Track", "Throw", "Trick", "Truck", "Theme", "Touch", "Teach", "Twice", "Tough", "Tight", "Today", "Third", "Thing", "Topic", "Tower", "Truly", "Truth", "Their", "Tooth", "There", "Three", "These", "Those", "Terms", "Troop", "Tribe", "Table", "Trace", "Tired", "Trend", "Trade", "Taste", "Trust", "Total", "Title", "Train", "Trial", "Trail", "Treat", "Upper", "Uncle", "Urban", "Under", "Union", "Until", "Usual", "Voice", "Video", "Value", "Virus", "Visit", "Vital", "Voter", "Which", "Watch", "Weigh", "Works", "Whose", "Worth", "Whole", "White", "While", "Where", "Wheel", "Worry", "Woman", "Would", "Wound", "World", "Wrong", "Water", "Write", "Waste", "Youth", "Yield", "Young", "Yours"

]
word = random.choice(wordlist)
word_decon = [x for x in word]

wins = 0
losses = 0
win_ratio = 0
moved = []
games_played = 0

letternum = 0
letterlist = []

guessed_words = []

yessyn = [
  "yes", "yu", "ya", "yea", "uh", "indeed", "of", "sure", "obviously", "mhm"]

move_int = 0
move_dic = {
  0: "first",
  1: "second",
  2: "third",
  3: "fourth",
  4: "fifth",
  5: "final",
}
congrat_dic = {
  1: "on your first try!",
  2: "in only two tries!",
  3: "in only three tries.",
  4: "in four tries.",
  5: "in five tries.",
  6: "in a whopping six tries.",
}
ingame = bool
is_playing = input("Do you want to play Word Guessing Game?\n ")
if any(x in is_playing.lower() for x in yessyn):
  knowshow = input("\nFirst, do you know how to play?\n ")
  if not any(x in knowshow.lower() for x in yessyn):
    print(Fore.BLUE + "\nThat's okay! Here's a brief tutorial:\n\n The objective of the game is to guess a\n random five-letter word in as little\n guesses as possible.")
    print(Fore.BLUE + "\n\nHow to play:\n\n Input a five-letter word. From that word,\n you will get a color-coded response. The\n meaning of that response is as follows:")
    print(Fore.BLUE + "\n\nThe Response:\n\n Each letter from your response tells you\n about the corresponding letter in your word.\n\n- A gray letter means that that letter\n  is not in the solution.\n\n- A yellow letter means that the letter\n  appears in the solution, but is not in\n  the same place.\n\n- A green letter means that the letter\n  appears in the solution and is in  the\n  correct place\n")
    time.sleep(2)
while any(x in is_playing.lower() for x in yessyn):
  ingame = True
  guess = input(Fore.WHITE + "\nWhat's your {} guess?\n ".format(move_dic[move_int])).lower()
  guess_result = []
  guess_decon = [x for x in guess]
  guess_split = [x for x in guess]

  if len(guess_decon) == 5:
    for item in guess_decon:
      letternum += 1
      if item not in word_decon:
        guess_result.append(Fore.LIGHTBLACK_EX)
        guess_result.append(item.upper())
      if item in word_decon:
        if guess_decon.index(item) == word_decon.index(item):
          guess_result.append(Fore.GREEN)
          guess_result.append(item.upper())
        else: 
          guess_result.append(Fore.YELLOW)
          guess_result.append(item.upper())
        word_decon[word_decon.index(item)] = "!"
      guess_decon[guess_decon.index(item)] = "!"
    move_int += 1
    guessed_words.append(guess)
  
  elif len(guess_decon) != 5:
    print("\nPlease pick a 5-letter word.")
  
  elif guess in guessed_words:
    print("\nYou have already guessed that word.")

  guess_result = ''.join(guess_result)
  print("\n", guess_result)
  word_decon = [x for x in word]
  guess_decon = [x for x in guess]
  if guess_decon == word_decon:
    print(Fore.GREEN + "\nCongratulations! You guessed the word", congrat_dic[move_int], "\n")
    moved.append(move_int)
    move_int = 0
    games_played += 1
    wins += 1
    guessed_words = []
    word = random.choice(wordlist)
    word_decon = [x for x in word]
    print(Fore.WHITE + "-------\n")
    print(Fore.GREEN + "Wins:", wins)
    print(Fore.LIGHTBLACK_EX + "Losses:", losses)
    print(Fore.YELLOW + "Average:", round(sum(moved)/games_played, 1), "guesses")
    print(Fore.WHITE + "\n-------")
    is_playing = input(Fore.WHITE + "\nDo you want to play again?\n ")
    
  word_decon = [x for x in word]
  if move_int == 6:
    moved.append(move_int)
    move_int = 0
    games_played += 1
    losses += 1
    guessed_words = []
    word = random.choice(wordlist)
    word_decon = [x for x in word]
    print(Fore.RED + "\nYou could not guess the word in 6 tries.\n The word was '", word.upper(), "'\n")
    print(Fore.WHITE + "-------\n")
    print(Fore.GREEN + "Wins:", wins)
    print(Fore.LIGHTBLACK_EX + "Losses:", losses)
    print(Fore.YELLOW + "Average:", round(sum(moved)/games_played, 1), "guesses.")
    print(Fore.WHITE + "\n-------")
    is_playing = input(Fore.WHITE + "\nDo you want to play again?\n ")
else:
  ingame == False
  print("\nOkay then, goodbye.")
    