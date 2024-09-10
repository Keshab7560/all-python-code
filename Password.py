import random
import string

# List of sample words (you can customize or expand this list)
word_list = [
    "apple", "banana", "cherry", "date", "elephant", "falcon", "giraffe", "hippo", "iguana", "jaguar",
    "kangaroo", "lemon", "mango", "nectarine", "orange", "peach", "quail", "rabbit", "snake", "tiger"
]

def generate_password(num_words=3, add_numbers=True, add_symbols=True):
    # Choose random words from the word list
    password = ''.join(random.choice(word_list) for _ in range(num_words))
    
    # Optionally, add random numbers
    if add_numbers:
        password += ''.join(random.choice(string.digits) for _ in range(2))
    
    # Optionally, add random symbols
    if add_symbols:
        password += ''.join(random.choice(string.punctuation) for _ in range(2))
    
    return password

# Example usage
print("Generated Password:", generate_password())
