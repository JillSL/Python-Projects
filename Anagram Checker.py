#SAN LUIS, Jillian Joy C.
#Project: Anagram Checker

def are_anagrams():
    word_1 = input("Please type in the first word. \n")
    word_2 = input("Please type in the second word. \n")
    
    if sorted(word_1) == sorted(word_2):
        print("The words you provided are anagrams.")
    else:
        print("The words you provided are NOT anagrams. \n")
        print("Let's try again! \n")
    
    while True:  # Loop until valid input is provided
        user_response = input("Do you want to try again? (yes/no) \n")
        
        if user_response.lower() == "yes" or user_response.lower() == "yes.":
            are_anagrams()  # Recursively call the function if "yes"
            break  # Break the loop if the user enters "yes"
        elif user_response.lower() == "no" or user_response.lower() == "no.":
            print("Goodbye!")
            break  # Exit the loop if "no" is entered
        else:
            print("ERROR! Invalid response. Please type 'yes' or 'no'.")

are_anagrams()
#this is just an initial call to the function