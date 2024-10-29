#1.)
# Getting a person's name
full_name = input('Enter your first, middle, and last names: ')
names = full_name.split()

# An empty list to append with a for loop
initials = []   
for name in names:
    initials += name[0].upper() + "."
# Printing the output
print("".join(initials))
#=================================================

#2.)
# A problem about adding numbers together
numbers = input('Enter a series of numbers without any spaces or other characters: ')
numbers_convert = []
# A for loop
for i in numbers:
    numbers_convert.append(int(i))
# Printing the output
print(sum(numbers_convert))
#=================================================

#3.)
# Formatting dates
date = input('Enter a date with the format of mm/dd/yyyy: ')
date_list = date.split('/')

# A list containing all the months
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# Assigning the month in date_list to its name
month_name = months[int(date_list[0]) - 1]

# Printing the output
print(f'The date is {month_name} {date_list[1]}, {date_list[2]}')
#=================================================

#4.)
# Converting Morse code
# Couldn't think of how to tackle this problem besides making this big list

morse_codes = [
    # This list should contain alphabetical, numerical, and other characters
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.",
    " ", ".-.-.-", "--..--", "..--..", "-.-.--"
]

# Character list for matching the input
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,?"

# Get user input
user_input = input("Enter a string to convert to Morse code: ").upper()

# a For loop with an if statement to append the blank string
morse_output = ""
for i in user_input:
    if i in characters:
        index = characters.index(i)
        morse_output += morse_codes[index] + " "

# Printing the output
print(morse_output.strip())
#=================================================

#5.)
# Converting phone numbers

# Getting the phone number
phone_number = input('Enter a 10 digit phone number in the format XXX-XXX-XXXX: ')
new_phone = ''
# a For loop to check the values in the phone string
for i in phone_number:
    if i.isdigit():
        new_phone += i
    elif i == '-':
        new_phone += i
# Originally I tried to solve this problem with lists and indexes, but was unable to get it working how I wanted.
# So we've got this ugly list of ifs instead.
    else:
        if i in 'ABC':
                new_phone += '2'
        elif i in 'DEF':
                new_phone += '3'
        elif i in 'GHI':
                new_phone += '4'
        elif i in 'JKL':
                new_phone += '5'
        elif i in 'MNO':
                new_phone += '6'
        elif i in 'PQRS':
                new_phone += '7'
        elif i in 'TUV':
                new_phone += '8'
        elif i in 'WXYZ':
                new_phone += '9'

# Printing the output
print(new_phone)
#=================================================

#6.)
# Average number of words

# Opening the file to read and assigning the lines to the lines variable
with open('text.txt', 'r') as file:
    lines = file.readlines()

# Counter variables for out for loop
total_words = 0
sentence_count = 0

# Processing the lines and using the counter variables
for line in lines:
    words = line.split() 
    total_words += len(words)
    sentence_count += 1

# Calculating the average
average_words = total_words / sentence_count

# Printing the output
print(f'Average number of words per sentence: {average_words}')
#=================================================\

#7.)
# Character analysis
# Counter variables for the loop loop
upper_count = 0
lower_count = 0
number_count = 0
space_count = 0

# Opening the file to read and putting each line into a for loop
with open('text.txt', 'r') as file:
    for line in file:
        for char in line:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
            elif char.isdigit():
                number_count += 1
            elif char.isspace():
                space_count += 1

# Printing the output
print(f"Uppercase count: {upper_count}")
print(f"Lowercase count: {lower_count}")
print(f"Number count: {number_count}")
print(f"Space count: {space_count}")
#=================================================

#8.)
# Sentence Capitals
# A function that creates a list named sentences, and then applies the capitalize method to each value, and then rejoins it back to string
# I had to look up capitize since I don't think the chapter covered it unless I just missed it.
def capitalize_sentences(lines):
    sentences = lines.split('. ')
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]
    return '. '.join(capitalized_sentences)

# Getting the input
user_string = input("Enter some sentences: ")

# Calling the function with a new variable
capital_new_string = capitalize_sentences(user_string)
#Printing the output
print(capital_new_string)
#=================================================

#9.)
# Vowels and Consonants
def main():
    user_str = input('Enter a string of characters: ')
    
    print('That string has', num_vowels(user_str), 'vowels and', \
num_consonants(user_str), 'consonants.')

# vowel function
def num_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    
    for ch in s:
        if ch.lower() in vowels:
            vowel_count += 1

    return vowel_count
# consonant function
def num_consonants(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    conso_count = 0
    
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            conso_count += 1

    return conso_count
#Calling the main function
main()
#=================================================

#10.)
# Counting characters
# Getting user input
user_input = input('Enter a string: ')

# Blank variables for the loop
most_common = ''
max_count = 0

# a For loop to start counting each character in the user input
for i in user_input:
    count = 0
    for c in user_input:
        if i == c:
            count += 1
# Trying to find the value with the highest count as the loops finish
    if count > max_count:
        max_count = count
        most_common = i

# Printing the output
print(f"Most frequent character: '{most_common}'")