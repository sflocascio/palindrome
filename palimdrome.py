#You have to write a program that, when run, asks the user to input some text. It can be a phrase, a sentence, or multiple sentences. After it is entered, your program will let the user know if it is a palindrome or not. Use "is a palindrome" and "is not a palindrome" in your output in order for the tests to pass.
#Letter casing and punctuation do not matter when testing a palindrome. All of the following are valid palindromes:

def main_page():

    word_1 = str(input("Enter word or sentence here to see if it's a paladrome"))

    def clean_text(word):
        """given a text return the text with no punctiation"""
        word = word.lower()
        new_text = ""
        for char in word:
            if char.isalpha():
                new_text = new_text + char
        return new_text

    new = clean_text(word_1)
    print (new)  

    def is_a_paladrome(chars):
        """check to see if this is a palidrome"""
        
        if len(chars) <= 1:
            return True
        elif chars[0] == chars[-1]:
            return is_a_paladrome (chars[1:-1])
        else:
            return False

    if is_a_paladrome(new) == True:
        print("is a palindrone")

    else:
        print("not a palindrone")

    again = (input("would you like to try again? Y for yes"))
    if again == 'Y':
        main_page()
    else:
        print("goodbye")
   


main_page()










    