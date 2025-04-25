"""Program entry point"""

type FiveIntTuple = tuple[int, int, int, int, int]


def score_guess(user_guess: str, target_word: str) -> FiveIntTuple:
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
    if user_guess == target_word:
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


def tests() -> None:
    test_case_1 = score_guess("world", "world")
    test_case_2 = score_guess("world", "hello")
    test_case_3 = score_guess("world", "hello")
    test_case_4 = score_guess("spell", "hello")
    # print(test_case_1)
    assert test_case_1 == (2, 2, 2, 2, 2), "should be [2,2,2,2,2]"
    # print(test_case_2)
    assert test_case_2 == (0, 1, 0, 2, 0), "should be [0,1,0,2,0]"
    # print("the target word is", len(test_case_3), "long")
    assert len(test_case_3) == 5, "the target world should be five letters"
    # print(test_case_4)  # debug
    assert test_case_4[3] == 2 and test_case_4[2] == 1, ""


def main() -> None:
    tests()
    # get_valid_words()
    # get_target_words()


if __name__ == "__main__":
    main()
