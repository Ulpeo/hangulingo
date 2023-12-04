import random

def delete_line(file_name, line_number):
    # Read the file and store each line in a list
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Check if the line number is valid
    if 1 <= line_number <= len(lines):
        # Delete the specified line
        del lines[line_number - 1]

        # Rewrite the file with the remaining lines
        with open(file_name, 'w') as modified_file:
            modified_file.writelines(lines)
        print(f"Line {line_number} successfully deleted.")
    else:
        print("Invalid line number.")


def save(pseudo, points):
    save_file = open("scores.txt",'r+')
    lines = save_file.readlines()
    count =0

    for line in lines:
        count += 1
        line = line.rstrip()
        part = line.split(" ")
        if (part[0] == pseudo):
            found = True
            delete_line("scores.txt", count)
            save_file.close()
        else:
            save_file.close()
    save_file = open("scores.txt",'a+')

    save_file.write(pseudo +" "+str(points)+"\n")
    save_file.close()


def load_words_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip().split('; ') for line in lines]

def game(pseudo, total_points):
    file_path = "korean_verbs.txt"
    word_list = load_words_from_file(file_path)
    total_points = int(total_points)

    print("Welcome to the word game!")
    print("Type 'quit' to exit the game.")

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
                print(f"Your total points: {total_points}")
                save(pseudo, total_points)
                return
            elif player_answer.lower() == correct_answer.lower():
                print("Correct! Well done.\n")
                total_points += 1 
            else:
                print(f"Wrong. The correct answer is '{correct_answer}'.\n")



