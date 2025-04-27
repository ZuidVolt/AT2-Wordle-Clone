from wordle import score_guess


def test_score_guess() -> None:
    test_case_1 = score_guess("world", "world")
    test_case_2 = score_guess("world", "hello")
    test_case_3 = score_guess("world", "hello")
    test_case_4 = score_guess("spell", "hello")
    print("test case 1, valid guess:")
    # print(test_case_1) # debug
    assert test_case_1 == (2, 2, 2, 2, 2), "should be [2,2,2,2,2]"
    print("PASSED")
    print("test case 2, semi-valid guess logic:")
    # print(test_case_2) # debug
    assert test_case_2 == (0, 1, 0, 2, 0), "should be [0,1,0,2,0]"
    print("PASSED")
    print("test case 3, length of result type is 5:")
    # print("the target word is", len(test_case_3), "long") # debug
    assert len(test_case_3) == 5, "the target world should be five letters"
    print("PASSED")
    print(
        "test case 4, logic handling of guessing with multiples of the same letter:"
    )
    # print(test_case_4)  # debug
    assert test_case_4[3] == 2 and test_case_4[2] == 1, ""
    print("PASSED")


def test_all() -> None:
    test_score_guess()


if __name__ == "__main__":
    test_all()
