import time
import random

# List of sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and easy-to-learn programming language.",
    "Typing tests are a great way to improve your speed and accuracy.",
    "Good coding practices lead to better code and fewer bugs.",
    "Artificial Intelligence is changing the way we live and work."
]

def typing_test():
    # Select a random sentence from the list
    sentence = random.choice(sentences)
    print("Typing Test! Try to type the following sentence as quickly as possible:\n")
    print(f"'{sentence}'\n")
    
    # Start the timer
    input("Press Enter when you're ready to start...")
    start_time = time.time()
    
    # Player types the sentence
    typed_sentence = input("\nStart typing: ")
    
    # End the timer
    end_time = time.time()
    
    # Calculate time taken
    time_taken = end_time - start_time

    # Calculate accuracy without shifting or displacing letters
    correct_characters = 0
    for i in range(min(len(sentence), len(typed_sentence))):
        if sentence[i] == typed_sentence[i]:
            correct_characters += 1
    
    accuracy = (correct_characters / len(sentence)) * 100

    # Calculate Words Per Minute (WPM)
    wpm = (len(typed_sentence) / 5) / (time_taken / 60)

    # Display results
    print("\nResults:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"WPM: {wpm:.2f}")
    
    if accuracy == 100:
        print("Perfect typing! Great job!")
    elif accuracy >= 90:
        print("Excellent job!")
    elif accuracy >= 75:
        print("Good job, but there's room for improvement.")
    else:
        print("Keep practicing! You're getting there.")

# Run the typing test
typing_test()
