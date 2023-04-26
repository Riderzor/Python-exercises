# Write your solution here
def most_common_character(string1):
    # creatring the dictionary to store the frequency of char in string
    char_repetation = {}
    for char in string1:
        if char in char_repetation:
            char_repetation[char] += 1
        else:
            char_repetation[char] = 1

    max_repetation = 0
    max_char =" "
    for char, rept in char_repetation.items():
        if rept > max_repetation:
            max_repetation = rept
            max_char = char
    return max_char
    
if __name__ == "__main__":
    print(most_common_character(string1="bananan"))