#You have to write a program that, when run, asks the user to input some text. It can be a phrase, a sentence, or multiple sentences. After it is entered, your program will let the user know if it is a palindrome or not. Use "is a palindrome" and "is not a palindrome" in your output in order for the tests to pass.
#Letter casing and punctuation do not matter when testing a palindrome. All of the following are valid palindromes:

word = str(input("Enter word or sentence here to see if it's a paladrome"))

def clean_text(text):
   """given a text return the text with no punctiation"""
   # text = word.lower()
   # text = word.replace(" ", "")
   # return text
    for char in word:
        if char.isalpha():
        new_text = new_text + char
    return new_text

def is_a_paladrome(chars):
    """check to see if this is a palidrome"""
    text = chars.text
    if len(text) <= 1:
        print (True)
    elif text[0] == text[-1]:
        return is_a_paladrome (text[1:-1])
    else:
        print(False)

if is_a_paladrome(text) == True:
    print("is a palindrone")

else:
    print("not a palindrone")











    