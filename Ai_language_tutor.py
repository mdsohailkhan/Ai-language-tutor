from googletrans import Translator
# Create a translator object
translator = Translator()

def translate_to_hindi(english_text):
    # Translate text from English to Hindi
    translation = translator.translate(english_text, src='en', dest='hi')
    return translation.text

# Example usage
english_sentence = "Hello, how are you?"
hindi_sentence = translate_to_hindi(english_sentence)
print(f"English: {english_sentence}")
print(f"Hindi: {hindi_sentence}")

vocabulary = {
    "apple": "सेब",
    "book": "किताब",
    "water": "पानी",
    "food": "भोजन",
    "friend": "दोस्त"
}

def practice_vocabulary():
    print("Let's practice some vocabulary!\n")
    for english_word, hindi_word in vocabulary.items():
        print(f"English: {english_word} - Hindi: {hindi_word}")

# Example usage
practice_vocabulary()

import random

def quiz_user():
    print("Let's take a quiz!\n")
    english_word = random.choice(list(vocabulary.keys()))
    user_answer = input(f"What is the Hindi word for '{english_word}'? ")

    if user_answer == vocabulary[english_word]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct word is '{vocabulary[english_word]}'.\n")

# Example usage
quiz_user()
def main_menu():
    while True:
        print("\nSimple English to Hindi Language Tutor")
        print("1. Translate English to Hindi")
        print("2. Practice Vocabulary")
        print("3. Take a Quiz")
        print("4. Exit")

        choice = input("Please select an option (1-4): ")

        if choice == "1":
            sentence = input("Enter an English sentence: ")
            print(f"Hindi Translation: {translate_to_hindi(sentence)}")
        elif choice == "2":
            practice_vocabulary()
        elif choice == "3":
            quiz_user()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
main_menu()
