import random

def generatePassword(pwlength):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = [] 

    for length in pwlength:
        password = "" 
        for _ in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        
        passwords.append(password) 
    
    return passwords


def replaceWithNumber(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
    
    return pword  # Moved outside the loop to allow multiple replacements


def replaceWithUppercaseLetter(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword)//2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
    
    return pword  # Moved outside the loop to allow multiple replacements


def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    
    print("Generating " + str(numPasswords) + " passwords")
    
    passwordLengths = []

    print("Minimum length of password should be 3")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length < 3:
            length = 3  # Ensure minimum password length is 3
        passwordLengths.append(length)
    
    passwords = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print("Password #" + str(i+1) + " = " + passwords[i])

main()

