"""Program entry point"""


def score_guess(user_guess: str, target_word: str) -> tuple[int, ...]:
    """Scores a Wordle guess.
    Args:
        user_guess (str): The user's guess.
        target_word (str): The target word
    Returns:
        score_list (tuple[int, ...]) where 2 means a correct letter and
        1 means correct letter in the wrong place, with 0 being an
        Incorrect letter
    """
    score_list: list[int] = [0] * len(target_word)
    if user_guess == target_word:  # early return of correct guess
        score_list = [2] * len(target_word)
        return tuple(score_list)
    for i in range(len(score_list)):
        if user_guess[i] == target_word[i]:
            score_list[i] = 2
        elif user_guess[i] in target_word:
            score_list[i] = 1
    return tuple(score_list)


def read_file(file_path: str) -> list[str]:
    with open(file_path, encoding="utf-8") as file_handler:
        data = file_handler.read()
        word_list: list[str] = []
        for line in data.splitlines():
            word_list.append(line.strip())
        return word_list


def get_valid_words() -> tuple[str, ...]:
    file_path = "./data/all_words.txt"
    word_list = read_file(file_path)
    print("valid_words:", word_list)  # debug
    return tuple(word_list)


def get_target_words() -> tuple[str, ...]:
    file_path = "./data/target_words.txt"
    word_list = read_file(file_path)
    print("target words:", word_list)  # debug
    return tuple(word_list)


def game_setup():
    pass


def game_display():
    pass


def user_input():
    pass


def game_loop():
    pass


def main() -> None:
    from test.test_wordle import test_all

    test_all()


if __name__ == "__main__":
    main()
