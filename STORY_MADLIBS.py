import pygame
import time

# Function to initialize pygame mixer and load sound files
def initialize_sounds():
    try:
        pygame.mixer.init()

        # Load sound files (make sure you have WAV files)
        funny_sound = pygame.mixer.Sound("wow-2-242639.mp3")  # Sound after generating story
        thanks_sound = pygame.mixer.Sound("thank-you-sweet-man-235977.mp3")  # Sound when finishing the game
        return funny_sound, thanks_sound
    except pygame.error as e:
        print("Error loading sound files:", e)
        return None, None

# Function to detect parts of speech based on word input
def detect_part_of_speech(word):
    """Detect part of speech based on word input."""
    
    # List of parts of speech (simplified)
    adjectives = ['happy', 'blue', 'angry', 'fast', 'green']
    nouns = ['dog', 'cat', 'school', 'ball', 'house']
    verbs = ['run', 'jump', 'eat', 'sleep', 'dance']
    adverbs = ['quickly', 'slowly', 'loudly', 'gracefully', 'happily']
    
    # Check for part of speech
    if word.lower() in adjectives:
        return 'adjective'
    elif word.lower() in nouns:
        return 'noun'
    elif word.lower() in verbs:
        return 'verb'
    elif word.lower() in adverbs:
        return 'adverb'
    
    # Default if not found
    return 'unknown'

# Function to ask the user for words and create a story
def collect_words_and_create_story(funny_sound, thanks_sound):
    print("Let's create a funny story! Please provide the following:")
    
    # Collect user words without sound effects during input phase
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adjective1 = input("Enter an adjective: ")
    adverb1 = input("Enter an adverb: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")
    
    # Make a funny story by inserting the collected words
    story_template = f"Once upon a time, a {adjective1} {noun1} decided to {verb1} {adverb1}. It ran through the forest and found a {noun2}. The {noun2} was very {adjective1} and decided to {verb2} with the {noun1}. It was a crazy adventure!"
    
    # Print the funny story
    print("\nHere's your funny story:\n")
    print(story_template)
    
    # Play funny sound after the story is created
    if funny_sound:
        funny_sound.play()
        time.sleep(2)  # Wait for the sound to finish before asking to continue
    
    # Ask if the user wants to play again
    ask_to_continue(funny_sound, thanks_sound)

# Function to ask if the user wants to continue
def ask_to_continue(funny_sound, thanks_sound):
    continue_quiz = input("\nDo you want to create another funny story? (yes/no): ").strip().lower()
    
    # Play the thanks sound when ending the game
    if continue_quiz == 'no':
        thanks_sound.play()
        time.sleep(2)  # Wait for the thanks sound to finish
        print("Thanks for playing! Have a funny day!")
    elif continue_quiz == 'yes':
        collect_words_and_create_story(funny_sound, thanks_sound)

# Main function to start the Mad Libs game
def start_mad_libs():
    funny_sound, thanks_sound = initialize_sounds()
    
    if funny_sound and thanks_sound:
        print("Starting the Mad Libs game...\n")
        collect_words_and_create_story(funny_sound, thanks_sound)
    else:
        print("Error: Could not load sound files!")

# Run the Mad Libs game
start_mad_libs()  # Play the thanks sound when ending the game here
