import random

def game(pseudo, score):
    print("let's start the game")
    
    print("let's start the game\n")
    print ("score: "+ score + "pseudo:"+ pseudo)


def load_words_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip().split('; ') for line in lines]

def main():
    file_path = "korean_verbs.txt"  
    word_list = load_words_from_file(file_path)

    print("Welcome to the word game!")
    print("Type 'quit' to exit the game.")

    #TODO calculate the points
    while True:
        random.shuffle(word_list)

        for index, words in enumerate(word_list, start=1):
            ask_for_conjugation = random.choice([True, False])

            if ask_for_conjugation:
                print(f"\nQuestion {index}: Conjugate the word '{words[1]}'")
                correct_answer = words[2]
            else:
                print(f"\nQuestion {index}: Translate the word '{words[1]}'")
                correct_answer = words[0]

            player_answer = input("Your answer: ")

            if player_answer.lower() == 'quit':
                print("Thanks for playing! Goodbye.")
                return
            elif player_answer.lower() == correct_answer.lower():
                print("Correct! Well done.\n")
            else:
                print(f"Wrong. The correct answer is '{correct_answer}'.\n")

if __name__ == "__main__":
    main()