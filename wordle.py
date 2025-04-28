"""Program entry point"""

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
    score_list = [0] * len(target_word)
    if user_guess == target_word:  # early return of correct guess
        score_list = [2] * len(target_word)
        return tuple(score_list)
    for i in range(len(score_list)):
        if user_guess[i] == target_word[i]:
            score_list[i] = 2
        elif user_guess[i] in target_word:
            score_list[i] = 1
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


def display_guess_result(scored_guess):
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
    print_display_list(display_list)


def game_setup(
    valid_words_list=None, target_words_list=None, number_of_user_guesses=None
) -> tuple:
    if valid_words_list == None:
        valid_words_list = get_target_words()
    if target_words_list == None:
        target_words_list = get_target_words()
    if number_of_user_guesses == None:
        number_of_user_guesses = NUMBER_OF_USER_GUESSES
    return valid_words_list, target_words_list, number_of_user_guesses


def game_display():
    pass


def user_input():
    pass


def game_loop(game_setup_param=None):
    if game_setup_param == None:
        setup_data = game_setup()
    else:
        setup_data = game_setup_param
    _valid_words_list, _target_words_list, _number_of_user_guesses = setup_data


def run_tests_quickly():
    from test.test_wordle import test_all

    test_all()


def main():
    run_tests_quickly()
    # x = (1, 2, 0, 0, 1)
    # display_guess_result(x)


if __name__ == "__main__":
    main()
