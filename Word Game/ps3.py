# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10,
 '*': 0 }

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    # pass  # TO DO... Remove this line when you implement this function
    wordlen =  len(word)  
    sum_letters_points = 0
    for char in word.lower():   
        sum_letters_points += SCRABBLE_LETTER_VALUES[char]
    other_points = 7*wordlen - 3*(n-wordlen)
    if other_points <= 1:
         return sum_letters_points * 1
    else:
         return sum_letters_points * other_points
        
    
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
                  #num_vowels-1 to hold a place for adding wildCard in place of one vowel
    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
        
    #adding wildCard
    hand["*"] = hand.get("*", 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """    
    # pass  # TO DO... Remove this line when you implement this function
    new_hand = {}
    #deeply copy the dictionary hand to the dictionary new_hand
    for t in hand.items():
        new_hand.update({t[0]:t[1]})     
        
    for char in word.lower():
        #if char found in word and new_hand reduce it's frequency in new_hand
        if new_hand.get(char,0) > 0: 
           new_hand[char] -= 1
        #assert not new_hand[char] < 0, "update_hand() letter frequency is negative"
           
    return new_hand
    

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    
    # pass  # TO DO... Remove this line when you implement this function
    
    #TEST CASE
    #is_valid_word("Ra*ture",{'r': 2, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1, '*': 1 },word_list)
    
    new_hand = {}
    word_lowercase =  word.lower()
    #deeply copy the dictionary hand to the dictionary new_hand
    for t in hand.items():
        new_hand.update({t[0]:t[1]})     
        
    for char in word.lower():
        #if char found in word and new_hand reduce it's frequency in new_hand
        if not new_hand.get(char) == None:
            new_hand[char] -= 1
        #char in word does not exist in hand
        else:
            return False      
    
    #check if char exists in word more than it exists in hand 
    #it will have negative frequency value
    for key in new_hand:
        if new_hand.get(key) < 0:
           return False
    
    #if wildCard exists in word
    if "*" in word_lowercase:
        for i in range(len(VOWELS)):
           word_rplcd_wildCard =  word_lowercase.replace("*", VOWELS[i])
           for tmp_word in word_list:
               if word_rplcd_wildCard == tmp_word.lower():
                   return True
               else:
                   continue
    #wildCard does not exist in word 
    #search for valid word normally
    else:  
        for tmp_word in word_list:
            if word_lowercase == tmp_word.lower():
                return True
            else: 
                continue
    
    return False   

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    #pass  # TO DO... Remove this line when you implement this function
    handlen = 0
    #sum up all letters' frequencies in hand
    for key in hand: 
        handlen += hand[key] 
        
    return handlen

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    #TEST CASES
    #{'a':1, 'j':1, 'e':1,  'f':1,  '*':1,  'r':1,  'x':1}
    #{'a':1, 'c':1, 'f':1, 'i':1, '*':1, 't':1, 'x':1}
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    total_score = 0
    new_hand = update_hand(hand, "")
    handlen = calculate_handlen(new_hand)
    game_over_enumeration = {"!!": 0, "Ran Out of letters": 1}
    game_over_reason = game_over_enumeration["Ran Out of letters"]
    
    # As long as there are still letters left in the hand:
    while handlen > 0:
        
        # Display the hand
        print("current hand:", end=' ')
        display_hand(new_hand)
        # Ask user for input
        word = input("Enter word, or \"!!\" to indicate that you are finished: ").lower()
        
        # If the input is two exclamation points:
        if word == "!!":
            # End the game (break out of the loop)
            game_over_reason = game_over_enumeration["!!"]
            break
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, new_hand, word_list):    
                # Tell the user how many points the word earned,
                # and the updated total score
                word_score = get_word_score(word, handlen)
                total_score += word_score
                print(word, "earned", word_score, "points.", "Total:", total_score, "points")
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("That is not a valid word. Please choose another word.")
                
            # update the user's hand by removing the letters of their inputted word
            new_hand = update_hand(new_hand, word)
            handlen = calculate_handlen(new_hand)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    if game_over_reason == game_over_enumeration["!!"]:
        print("Total score for this hand:", total_score, "points")
    elif game_over_reason == game_over_enumeration["Ran Out of letters"]:
        print("Ran out of letters. Total score for this hand:", total_score, "points")
    print("---------------------")
    # Return the total score as result of function
    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    # pass  # TO DO... Remove this line when you implement this function
    
    #TEST CASES
    #substitute_hand({'a':1, 'j':1, 'e':3,  'f':1,  '*':1,  'r':1,  'x':1}, 'e')
    
    #check if  letter does not exist in hand --> no change, return same hand
    if not letter in hand:
        return hand
    #create string: available_letters contains alphabet letters that are:
    #not in hand and not equal to user's letter
    available_letters = ""
    for char in (VOWELS+CONSONANTS):
        if (not char in hand) and (not char == letter):
            available_letters += char
            
    #program choses letter at random out of available_letters
    substitute_letter = random.choice(available_letters)
    
    # create substitute_hand so that original hand would remain unchanged
    substitute_hand = {}
    # iterate all data in hand to copy them
    for key in hand:
        #if current letter in hand is the letter to be replaced:
        if key == letter:
            #replace the letter with the same frequencies as the old letter
            substitute_hand[substitute_letter] = hand[key]
        # otherwise just copy letters and frequencies from hand to substitute_hand
        else: 
            substitute_hand[key] = hand[key] 
            
    return substitute_hand
    
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    final_score = 0 
    
    #Ask user to input  Asks the user to input a total number of hands
    #they wish to play
    num_hands = int(input("Enter total number of hands: "))
    
    #loop by number of hands
    for i in range(num_hands):
        
        # dict to keep scores of users if user wish to replay hand
        # values should be zeros every loop
        users_scores = {"first score": 0, "second score":0 }
        
        #create hand and display it
        hand = deal_hand(HAND_SIZE)
        print("current hand:", end=' ')
        display_hand(hand)
        
        # ask the user if they want to substitute one letter for another
        answer = input("Would you like to substitute a letter (yes / no) ? ").lower()
        if answer == "yes" or answer == "y":
            letter = input("Which letter would you like to replace: ").lower()
            tmp_hand = substitute_hand(hand,letter)
            del hand
            hand = tmp_hand
            
        #play hand and save score
        users_scores["first score"] = play_hand(hand, word_list)
        
        #ask the user if they would like to replay the hand.
        answer = input("Would you like to replay the hand (yes / no) ? ").lower()
        if answer == "yes" or answer == "y":
            #replay hand and save second_score
            users_scores["second score"] = play_hand(hand, word_list)
        
        #calculate final_score
        if users_scores["first score"] > users_scores["second score"]:
            final_score += users_scores["first score"]
        else:
            final_score += users_scores["second score"]
        
        #continue to next hand
       # END for loop------------------------------------------------------ 
    print("Total score over all hands:", final_score)
    return final_score

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
