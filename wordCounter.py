# This function takes a string as input and returns the number of words in the string.
def count_words(text):
    # Split the text into a list of words using whitespace as the delimiter.
    words = text.split()
    # Return the length of the list, which is the number of words.
    return len(words)

# This is the main part of the program.
if __name__ == "__main__":
    # Prompt the user to enter a sentence or paragraph.
    user_input = input("Enter a sentence or paragraph: ")
    # Call the count_words function with the user's input and store the result.
    word_count = count_words(user_input)
    # Print the number of words in the user's input.
    print(f"The number of words in the given text is: {word_count}")
