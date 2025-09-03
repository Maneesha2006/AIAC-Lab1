import string

def sentence_palindrome(sentence):
    # Remove punctuation, spaces, and convert to lowercase
    cleaned = ''.join(
        ch.lower() for ch in sentence if ch.isalnum()
    )
    # Check if cleaned string is a palindrome
    return cleaned == cleaned[::-1]

# Take dynamic input
sentence = input("Enter a sentence: ")
if sentence_palindrome(sentence):
    print("Palindrome")
else:
    print("Not Palindrome")
