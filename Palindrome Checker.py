#SAN LUIS, Jillian Joy C.
#Project: Palindrome Checker

def is_palindrome():
    word = input("Please enter a word or phrase: \n")
    
    cleaned_word = ''.join(word.split()).lower()

    if cleaned_word == cleaned_word[::-1]:
        print("The word or phrase is a palindrome.")
    else:
        print("The word or phrase is NOT a palindrome.")

while True:
    is_palindrome()
    
    while True:  # Inner loop to handle retry after error
        user_response = input("Do you want to try again? (yes/no) \n")
        
        if user_response.lower() == "yes" or user_response.lower() == "yes.":
            break  # Exit the inner loop to retry the palindrome check
        elif user_response.lower() == "no" or user_response.lower() == "no.":
            print("Goodbye!")
            exit()  # Exit the program
        else:
            print("ERROR! Invalid response. Please type 'yes' or 'no'.")

is_palindrome()
#this is just an initial call to the function