s.lower() #returns strings as lowercase
s.split(",") #returns a list of strings split along the specified operator or whitespace as default

# Example 1: Join items in a list separated by space
#separator.join(iterable)
#separator: The string that will be placed between the elements in the iterable.
#iterable: The sequence of strings (e.g., list, tuple) to join together.
lst = ['Never', 'gonna', 'run', 'around', 'and', 'desert', 'you']
joined = ' '.join(lst)
print(joined) # Prints 'Never gonna run around and desert you'
joined = '-'.join(lst)
print(joined) # Prints 'Never-gonna-run-around-and-desert-you'


s.strip(characters) #Removes whitespace or specified characters from either end of the string.
# Example 1: Strip whitespace
s = '       Never gonna say goodbye       '
stripped = s.strip()
print(stripped) # Prints 'Never gonna say goodbye'
# Example 2: Strip question marks
s = '????Never gonna tell a lie and hurt you?????'
stripped = s.strip('?')
print(stripped) # Prints 'Never gonna tell a lie and hurt you'

# s.replace(old, new, count) replaces the substring old in the string s with "new" count is an optional parameter that says how many occurrences of old should be replaced
# Time and space is o(n) since it returns a new str and must traverse the entire string