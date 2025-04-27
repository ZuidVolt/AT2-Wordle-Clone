"""Program entry point"""

from typing import TypeGuard

type FiveIntTuple = tuple[int, int, int, int, int]


def is_five_int_tuple(t: tuple[int, ...]) -> TypeGuard[FiveIntTuple]:
    if len(t) == 5:
        return True
    return False


class FiveCharWord(str):
    """
    Represents a 5-character word for Wordle.
    Validates length upon creation.
    Inherits from str, so can be used like a string at runtime.
    """

    __slots__ = ()

    def __new__(cls, value: str) -> "FiveCharWord":
        if len(value) != 5:
            raise ValueError(f"FiveCharWord must be length 5, got '{value}'")
        return str.__new__(cls, value)


def score_guess(
    user_guess: FiveCharWord, target_word: FiveCharWord
) -> FiveIntTuple:
    """Scores a Wordle guess.
    Args:
        user_guess (FiveCharWord): The user's guess.
        target_word (FiveCharWord): The target word
    Returns:
        tuple_score (FiveIntTuple) where 2 means a correct letter and
        1 means correct letter in the wrong place, with 0 being an
        Incorrect letter
    """
    score_list: list[int] = [0] * len(target_word)
    for i in range(len(score_list)):
        if user_guess[i] == target_word[i]:
            score_list[i] = 2
        elif user_guess[i] in target_word:
            score_list[i] = 1
    tuple_score = tuple(score_list)
    if is_five_int_tuple(tuple_score):  # for the type checker only
        return tuple_score
    raise ValueError(f"FiveIntTuple must be length 5, got '{score_list}'")


def read_file_of_words(file_path: str) -> list[FiveCharWord]:
    with open(file_path, encoding="utf-8") as file_handler:
        data = file_handler.read()
        word_list: list[FiveCharWord] = []
        for line in data.splitlines():
            try:
                word_list.append(FiveCharWord(line.strip()))
            except ValueError:
                print(f"Invalid word: {line.strip()}")
        return word_list


def get_valid_words() -> tuple[FiveCharWord, ...]:
    file_path = "./data/all_words.txt"
    word_list = read_file_of_words(file_path)
    print("valid_words:", word_list)  # debug
    return tuple(word_list)


def get_target_words() -> tuple[FiveCharWord, ...]:
    file_path = "./data/target_words.txt"
    word_list = read_file_of_words(file_path)
    print("target words:", word_list)  # debug
    return tuple(word_list)


def tests() -> None:
    test_case_1 = score_guess(FiveCharWord("world"), FiveCharWord("world"))
    test_case_2 = score_guess(FiveCharWord("world"), FiveCharWord("hello"))
    test_case_3 = score_guess(FiveCharWord("world"), FiveCharWord("hello"))
    test_case_4 = score_guess(FiveCharWord("spell"), FiveCharWord("hello"))
    print(test_case_1)
    assert test_case_1 == (2, 2, 2, 2, 2), "should be [2,2,2,2,2]"
    print(test_case_2)
    assert test_case_2 == (0, 1, 0, 2, 0), "should be [0,1,0,2,0]"
    print("the target word is", len(test_case_3), "long")
    assert len(test_case_3) == 5, "the target world should be five letters"
    print(test_case_4)  # debug
    assert test_case_4[3] == 2 and test_case_4[2] == 1, ""


def main() -> None:
    tests()
    # get_valid_words()
    # get_target_words()


if __name__ == "__main__":
    main()
