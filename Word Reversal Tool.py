#SAN LUIS, Jillian Joy C.
#Project: Word Reversal Tool

def reverse_letters():
    word = input("Enter a word: ")
    reversed_word = word[::-1]
    print("Reversed word:", reversed_word)

while True:
    reverse_letters()
    
    while True:
        user_response = input("Do you want to try again? (yes/no) \n")
        
        if user_response.lower() == "yes" or user_response.lower() == "yes.":
            break
        elif user_response.lower() == "no" or user_response.lower() == "no.":
            print("Goodbye!")
            exit()
        else:
            print("ERROR! Invalid response. Please type 'yes' or 'no'.")