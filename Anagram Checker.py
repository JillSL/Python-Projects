#SAN LUIS, Jillian Joy C.
#Project: Anagram Checker

def are_anagrams():
    word_1 = input("Please type in the first word. \n")
    word_2 = input("Please type in the second word. \n")
    
    # Remove spaces and convert both words to lowercase before sorting
    word_1 = word_1.replace(" ", "").lower()
    word_2 = word_2.replace(" ", "").lower()
    
    if sorted(word_1) == sorted(word_2):
        print("The words you provided are anagrams.")
    else:
        print("The words you provided are NOT anagrams. \n")
        print("Let's try again! \n")
    
    while True:
        user_response = input("Do you want to try again? (yes/no) \n")
        
        if user_response.lower() == "yes" or user_response.lower() == "yes.":
            are_anagrams()
            break
        elif user_response.lower() == "no" or user_response.lower() == "no.":
            print("Goodbye!")
            break
        else:
            print("ERROR! Invalid response. Please type 'yes' or 'no'.")

are_anagrams()
#this is just an initial call to the function
