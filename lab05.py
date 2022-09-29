########################################################################
##
## CS 101 Lab
## Program #5
## Name: Joseph Peak
## Email: jrp3yp@umsystem.edu
##
## PROBLEM : Lab5 -- Simulate a library card-checking system for a university.
##                      
## ALGORITHM : 
##      1. Get library card input
##      2. Check library card length, first 5 digits, last 3 digits, and check digit
##      3. If library card is invalid
##              print error messages to user
##          else
##              print student grade and department
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
# import statements

# functions
def get_school(library_card):
    school = ''
    if(library_card[5] == '1'):
        school = 'School of Computing and Engineering SCE'
    elif(library_card[5] == '2'):
        school = 'School of Law'
    elif(library_card[5] == '3'):
        school = 'College of Arts and Sciences'
    else:
        school = 'Invalid School'

    return school

def get_grade(library_card):
    if(library_card[6] == '1'):
        grade = 'Freshman'
    elif(library_card[6] == '2'):
        grade = 'Sophomore'
    elif(library_card[6] == '3'):
        grade = 'Junior'
    elif(library_card[6] == '4'):
        grade = 'Senior'
    else:
        grade = 'Invalid Grade'

    return grade

def character_value(character):
    if((ord(character) - 65) >= 0 or (ord(character) <  25)):
        result = ord(character) - 65
    else:
        result = character
    return result

def get_check_digit(library_card):
    check_digit = 0
    for i in range(len(library_card)):
        check_digit += int(character_value(library_card[i])) * int(i+1)

    check_digit %= 10

    return check_digit

def find_bad_character(library_card, alpha_or_digit):
    if(alpha_or_digit == 1):
        for i in range(len(library_card)):
            if(library_card[i].isalpha() == False):
                return [i, library_card[i]]
    elif(alpha_or_digit == 2):
        for i in range(len(library_card)):
            if(library_card[i].isdigit() == False):
                return [i, library_card[i]]


def verify_check_digit(library_card):
    error = ''
    passed = False

    if(len(library_card) != 10):
        error = "The length of the number given must be 10"
        passed = False
    elif((library_card[0:5]).isalpha() == False):
        passed = False
        error = f"The first 5 characters must be A-Z, the invalid character is at {find_bad_character(library_card, 1)[0]} is {find_bad_character(library_card, 1)[1]}"
    elif((library_card[7:10]).isdigit() == False):
        passed = False
        error = f"The last 3 characters must be 0-9, the invalid character is at {find_bad_character(library_card, 2)[0]} is {find_bad_character(library_card, 2)[0]}" 
    elif(get_school(library_card) == 'Invalid School'):
        passed = False
        error = "The sixth character must be 1 2 or 3"
    elif(get_grade(library_card) == 'Invalid Grade'):
        passed = False
        error = "The seventh character must be 1 2 3 or 4" 
    elif(int(get_check_digit(library_card)) != int(library_card[9])):
        passed = False
        error = f"Check Digit {library_card[9]} does not match calculated value {get_check_digit(library_card)}." 
    else:
        passed = True
        error = ''

    return (passed, error)




if __name__ == "__main__":
    # main program
    library_card = input("Enter Library Card. Hit Enter to Exit. ==> ")

    if(library_card == ''):
        quit()
    else:
        if(verify_check_digit(library_card)[0] == False):
            print("Library Card is Invalid")
            print(verify_check_digit(library_card))
        else:
            print("Library Card is Valid")
            print(f"The card belongs to a student in {get_school(library_card)}")
            print(f"The card belongs to a {get_grade(library_card)}")
