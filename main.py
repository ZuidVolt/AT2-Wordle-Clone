"""Program entry point"""


# Cooper, 20146487, 9/4/25
def score_guess(user_guess, target_word):
    score_list: list[int] = [0] * len(target_word)
    if user_guess == target_word:
        for i in range(len(score_list)):
            score_list[i] = 2
    return score_list


def tests():
    test_case_1 = score_guess("world", "world")
    test_case_2 = score_guess("world", "hello")
    assert test_case_1 == [2, 2, 2, 2, 2], "should be [2, 2, 2, 2, 2]"
    print(test_case_1)  # returns [2, 2, 2, 2, 2]
    assert test_case_2 == [0, 0, 0, 0, 0], "should be [0, 0, 0, 0, 0]"
    print(test_case_2)  # returns [0, 0, 0, 0, 0]


def main():
    tests()


if __name__ == "__main__":
    main()
