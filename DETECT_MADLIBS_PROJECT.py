import pygame
import time

# Function to detect parts of speech based on word input
def detect_part_of_speech(word):
    """Detect part of speech based on word input."""
    
    # Lists of common words for each part of speech
    pronouns = ['he', 'she', 'it', 'they', 'we', 'you', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'her', 'its', 'our', 'their']
    prepositions = ['in', 'on', 'at', 'by', 'with', 'under', 'between', 'over', 'through', 'about', 'for', 'during', 'before', 'after', 'against', 'beside', 'underneath']
    conjunctions = ['and', 'but', 'or', 'nor', 'so', 'for', 'yet', 'although', 'because', 'if', 'unless', 'while']
    interjections = ['wow', 'alas', 'yippee', 'ouch', 'oops', 'yay']
    
    # Verb detection (checks for common verb forms like 'run', 'eat', 'sit', etc.)
    verbs = ['run', 'sit', 'eat', 'pick', 'come', 'go', 'speak', 'play', 'read', 'write', 'sleep', 'study']
    
    # Adjective detection (commonly used adjectives and more complex endings)
    adjective_endings = ['y', 'ful', 'ous', 'able', 'ible', 'ic', 'ive']
    
    # Noun detection (proper nouns or common nouns)
    noun_endings = ['tion', 'ment', 'ness', 'ity', 'ance', 'ence', 'ism', 'hood', 'ship','isaS']
    
    # Check for adverb (excluding adjectives that end in 'ly')
    if word.endswith('ly'):
        return 'adverb'

    # Detect pronouns
    if word.lower() in pronouns:
        return 'pronoun'

    # Detect verbs (basic verbs and verbs ending in "ing", "ed", "s")
    if word.lower() in verbs or word.endswith(('ing', 'ed', 's')):  # Simple verb detection
        return 'verb'

    # Detect adjectives (based on common adjective suffixes, but not ending in 'ly')
    if word.endswith(tuple(adjective_endings)) and not word.endswith('ly'):
        return 'adjective'

    # Special case: Treat color words (like red, blue) as adjectives if they are in context
    color_words = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'purple', 'pink', 'orange', 'brown']
    if word.lower() in color_words:
        return 'adjective'

    # Detect prepositions
    if word.lower() in prepositions:
        return 'preposition'

    # Detect conjunctions
    if word.lower() in conjunctions:
        return 'conjunction'

    # Detect interjections (e.g., exclamations like 'wow', 'yay')
    if word.lower() in interjections:
        return 'interjection'

    # Detect nouns (proper nouns or common nouns)
    if word[0].isupper() or word.endswith(tuple(noun_endings)):
        return 'noun'

    return 'unknown'

# Function to handle user input and provide feedback
def mad_libs_check():
    try:
        # Initialize pygame mixer
        pygame.mixer.init()

        # Load sound files (replace with your own file paths)
        correct_sound = pygame.mixer.Sound("mixkit-correct-answer-reward-952.wav")
        wrong_sound = pygame.mixer.Sound("buzzer-or-wrong-answer-20582.mp3")
    except pygame.error as e:
        print("Error loading sound files:", e)
        return

    # Ask the user to input a word
    word = input("Enter a word: ").strip()

    # Ask the user to specify the expected part of speech for validation
    expected_pos = input("What part of speech is this word supposed to be (noun, pronoun, verb, adjective, adverb, preposition, conjunction, interjection)? ").lower()

    # Detect the part of speech first
    detected_pos = detect_part_of_speech(word)
    print(f"Detected part of speech: {detected_pos}")

    # Check if the detected part of speech matches the expected one
    if detected_pos == expected_pos:
        # Play the correct sound only if the answer is correct
        print(f"✔️ Correct! '{word}' is a valid {expected_pos}.")
        correct_sound.play()  # Play correct sound
    else:
        # First play the wrong sound
        wrong_sound.play()  # Play wrong sound
        print(f"❌ Oops! '{word}' is a {detected_pos}, not a {expected_pos}. Here's the correct information.")
        
        # Add a time delay (e.g., 2 seconds)
        time.sleep(2)  # Wait for 2 seconds before showing the correct answer
        
        # Now play the correct sound to confirm the correct answer
        print(f"✔️ Correct! '{word}' is a valid {detected_pos}.")
        correct_sound.play()  # Play correct sound

    # Provide an example sentence for the detected part of speech
    example_templates = {
        'noun': "The *{word}* is in the park.",
        'pronoun': "{word} went to the store.",
        'verb': "I *{word}* every day.",
        'adjective': "The *{word}* car is fast.",
        'adverb': "She runs *{word}*.",
        'preposition': "The book is *{word}* the table.",
        'conjunction': "I like ice cream, *{word}* I prefer chocolate.",
        'interjection': "{word}! I can't believe it."  # Changed from 'exclamation' to 'interjection'
    }

    # Correct way to handle capitalization and insertion into the sentence
    if detected_pos == 'interjection' or detected_pos == 'pronoun':
        print(f"Example: {example_templates[detected_pos].format(word=word.capitalize())}")  # Capitalize for interjections and pronouns
    else:
        print(f"Example: {example_templates[detected_pos].format(word=word)}")  # For other parts of speech, don't capitalize

    # Ask if the user wants to try another word
    ask_to_continue()

def ask_to_continue():
    continue_quiz = input("Do you want to try another word? (yes/no): ").strip().lower()
    if continue_quiz == 'yes':
        mad_libs_check()
    else:
        print("Thanks for playing!")

# Run the mad_libs_check function
mad_libs_check()
