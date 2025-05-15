"""Program entry point"""

import random

# --- constants ---
VALID_WORDS_FILE_PATH = "./data/all_words.txt"  # unix path (hardcoded)
TARGET_WORDS__FILE_PATH = "./data/target_words.txt"  # unix path (hardcoded)
NUMBER_OF_USER_GUESSES = 5


def score_guess(user_guess, target_word):
    """Scores a Wordle guess.
    Args:
        user_guess (str): The user's guess.
        target_word (str): The target word
    Returns:
        score_list (tuple[int, ...]) where 2 means a correct letter and
        1 means correct letter in the wrong place, with 0 being an
        Incorrect letter
    """
    score_list = [0] * 5
    target_word_letter_freq = {}
    for letter in target_word:
        target_word_letter_freq[letter] = (
            target_word_letter_freq.get(letter, 0) + 1
        )
    # print(target_word_letter_freq)  # debug

    if user_guess == target_word:  # early return of correct guess
        score_list = [2] * 5
        return tuple(score_list)

    # green tile pass (look for 2 vals)
    for i in range(5):
        if user_guess[i] == target_word[i]:
            score_list[i] = 2
            target_word_letter_freq[user_guess[i]] -= 1

    # yellow tile pass (look for possible 1 vals)
    for i in range(5):
        if score_list[i] == 0 and user_guess[i] in target_word:
            if target_word_letter_freq[user_guess[i]] > 0:
                score_list[i] = 1
                target_word_letter_freq[user_guess[i]] -= 1

    # print(target_word_letter_freq)  # debug
    return tuple(score_list)


def is_five_elements_long(collection):
    if len(collection) == 5:
        return True
    return False


def read_file_to_word_list(file_path):
    try:
        with open(file_path, encoding="utf-8") as file_handler:
            data = file_handler.read()
            word_list: list[str] = []
            for line in data.splitlines():
                line = line.strip()
                if is_five_elements_long(line):
                    word_list.append(line)
                else:
                    # print("line: '", line, "' was not 5 letters long")  # debug
                    pass
            return word_list
    except OSError as e:
        raise OSError from e


def get_valid_words():
    file_path = VALID_WORDS_FILE_PATH
    word_list = read_file_to_word_list(file_path)
    # print("valid_words:", word_list)  # debug
    return tuple(word_list)


def get_target_words():
    file_path = TARGET_WORDS__FILE_PATH
    word_list = read_file_to_word_list(file_path)
    # print("target words:", word_list)  # debug
    return tuple(word_list)


def print_display_list(display_list):
    print(
        display_list[0],
        display_list[1],
        display_list[2],
        display_list[3],
        display_list[4],
    )


def get_display_list(scored_guess):
    display_list = []
    for i in scored_guess:
        if i == 0:
            display_list.append("_")  # wrong guess
        elif i == 1:
            display_list.append("0")  # wrong position
        elif i == 2:
            display_list.append("X")  # right position
        else:
            raise ValueError(
                "A scored_guess Should only have elements values from 0-2 got:",
                i,
            )
    return display_list


def display_past_guesses(past_valid_guesses_list):
    for past_valid_words, past_display_lists in past_valid_guesses_list:
        print_display_list(past_valid_words)
        print_display_list(past_display_lists)


def display_guess_after_win(past_valid_guesses_list, guesses_count):
    for past_valid_words, past_display_lists in past_valid_guesses_list:
        print_display_list(past_valid_words)
        print_display_list(past_display_lists)
    print("you found the word in", guesses_count, "guesses")


def user_input(valid_words_list):
    user_guess = input("Enter your guess: ").lower()
    is_valid = (
        user_guess in valid_words_list
    )  # don't need to worry about len case as all valid words are the same length
    return user_guess, is_valid


def game_setup(
    valid_words_list=None,
    target_words_list=None,
    number_of_user_guesses=None,
):
    if valid_words_list is None:
        valid_words_list = get_valid_words()
    if target_words_list is None:
        target_words_list = get_target_words()
    if number_of_user_guesses is None:
        number_of_user_guesses = NUMBER_OF_USER_GUESSES
    return valid_words_list, target_words_list, number_of_user_guesses


def get_random_word_target_word(target_words_list):
    return random.choice(target_words_list)


def game_loop(
    game_setup_param=None,
    mock_user_valid_guesses: list[str] | None = None,
):
    if game_setup_param is None:
        setup_data = game_setup()
    else:
        setup_data = game_setup_param
    valid_words_list, target_words_list, number_of_user_guesses = setup_data

    past_valid_guesses_list: list[tuple[str, list[str]]] = []
    user_won_the_game = False
    guesses_count = 0

    target_word = get_random_word_target_word(target_words_list)

    if mock_user_valid_guesses is None:
        print("Debug: Target word:", target_word)  # debug
        print("Welcome to Wordle!")
        print(f"You have {number_of_user_guesses} guesses.")

    try:
        for turn_number in range(number_of_user_guesses):
            if mock_user_valid_guesses is None:
                display_past_guesses(past_valid_guesses_list)
            while True:
                if not mock_user_valid_guesses is None:
                    user_guess = mock_user_valid_guesses[turn_number]
                    guesses_count += 1
                    break
                else:
                    print("-" * 20)
                    user_guess, is_valid = user_input(valid_words_list)
                    if is_valid:
                        guesses_count += 1
                        break
                print("Invalid guess. Please try again.")
                if mock_user_valid_guesses is None:
                    display_past_guesses(past_valid_guesses_list)

            guess_result = score_guess(user_guess, target_word)

            if guess_result == (2, 2, 2, 2, 2):
                display_guess = get_display_list(guess_result)
                past_valid_guesses_list.append(
                    ((user_guess).upper(), display_guess)
                )
                user_won_the_game = True
                break
            else:
                display_guess = get_display_list(guess_result)
                past_valid_guesses_list.append(
                    ((user_guess).upper(), display_guess)
                )
        if mock_user_valid_guesses is None:
            if user_won_the_game:
                print("Congratulations! You won!")
                display_guess_after_win(past_valid_guesses_list, guesses_count)
            else:
                print("Sorry, you lost. The word was:", target_word.upper())
        else:
            return guess_result
    except KeyboardInterrupt:
        print()
        print("Game interrupted by user.")


def run_tests_quickly():
    from test.test_wordle import test_all

    test_all()


def main():
    game_loop()

    # w = ["apple"]
    # x = game_loop(
    #     game_setup(target_words_list=["paper"], number_of_user_guesses=1), w
    # )
    # print(x)

    # run_tests_quickly()

    # # x = (1, 2, 0, 0, 1)
    # display_guess_result(x)

    # past_valid_guesses_list: list[tuple[str, list[str]]] = [
    #     ("hello", ["0", "X", "X", "X", "0"]),
    #     ("world", ["0", "X", "X", "X", "0"]),
    #     ("crane", ["0", "0", "X", "X", "0"]),
    # ]
    # display_past_guesses(past_valid_guesses_list)


if __name__ == "__main__":
    main()
    # run_tests_quickly()
