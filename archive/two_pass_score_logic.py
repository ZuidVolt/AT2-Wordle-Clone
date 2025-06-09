"""
testing out a two pass dict system for score logic, accurately calculate duplicate letters
"""


def old_score_guess(user_guess, target_word):
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


def new_score_guess(user_guess: str, target_word: str) -> tuple[int, ...]:
    score_list = [0] * 5
    target_word_letter_freq: dict[str, int] = {}
    for letter in target_word:
        target_word_letter_freq[letter] = (
            target_word_letter_freq.get(letter, 0) + 1
        )
    print(target_word_letter_freq)

    if user_guess == target_word:  # early return of correct guess
        score_list = [2] * 5
        return tuple(score_list)

    # green tile pass (look for 2 vals)
    for i in range(5):
        if user_guess[i] == target_word[i]:
            score_list[i] = 2
            target_word_letter_freq[user_guess[i]] -= 1

    # yellow tile pass (look for 1 vals)
    for i in range(5):
        if score_list[i] == 0 and user_guess[i] in target_word:
            if target_word_letter_freq[user_guess[i]] > 0:
                score_list[i] = 1
                target_word_letter_freq[user_guess[i]] -= 1

    print(target_word_letter_freq)
    return tuple(score_list)


def main() -> None:
    result = new_score_guess("world", "hello")
    print(result)
    print()  # should be (0, 1, 0, 2, 0)
    result_2 = new_score_guess("apple", "paper")
    print(result_2)  # should be (1, 1, 2, 0, 1)


if __name__ == "__main__":
    main()
