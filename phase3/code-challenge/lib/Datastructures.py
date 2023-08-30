#Stack
def is_balanced(expression):
    # Initialize an empty stack to track opening brackets.
    stack = []
    
    # Define a dictionary to map closing brackets to their corresponding opening brackets.
    brackets = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the expression.
    for char in expression:
        # If it's an opening bracket, push it onto the stack.
        if char in '({[':
            stack.append(char)
        # If it's a closing bracket, check if it matches the top of the stack.
        elif char in ')}]':
            # If the stack is empty or the top of the stack doesn't match, it's unbalanced.
            if not stack or stack.pop() != brackets[char]:
                return False
    
    # If the stack is empty after processing all characters, it's balanced.
    return len(stack) == 0












#Sequences
def remove_duplicates(sequence):
    seen = set()  # Initialize a set to keep track of seen elements.
    result = []   # Initialize an empty list to store unique elements in order.
    
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

















#Dictionaries

import string

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase.
    cleaned_sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Split the sentence into words.
    words = cleaned_sentence.split()
    
    # Initialize a dictionary to store word frequencies.
    word_freq = {}
    
    # Count the frequency of each word.
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq