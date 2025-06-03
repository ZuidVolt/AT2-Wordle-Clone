# ---- Unit Tests ----
def test_score_guess():
    from wordle import score_guess

    test_case_1_mock_data = ("world", "world")
    test_case_2_mock_data = ("world", "hello")
    test_case_3_mock_data = ("world", "hello")
    test_case_4_mock_data = ("spell", "hello")

    print("--- TEST score_guess() CASES ---")

    print("test case 1, valid guess logic:")
    test_case_1 = score_guess(
        test_case_1_mock_data[0], test_case_1_mock_data[1]
    )
    # print(test_case_1) # debug
    assert test_case_1 == (2, 2, 2, 2, 2), "should be [2,2,2,2,2]"
    print("PASSED")

    print("test case 2, semi-valid guess logic:")
    test_case_2 = score_guess(
        test_case_2_mock_data[0], test_case_2_mock_data[1]
    )
    # print(test_case_2) # debug
    assert test_case_2 == (0, 1, 0, 2, 0), "should be [0,1,0,2,0]"
    print("PASSED")

    print("test case 3, length of result type is 5:")
    test_case_3 = score_guess(
        test_case_3_mock_data[0], test_case_3_mock_data[1]
    )
    # print("the target word is", len(test_case_3), "long") # debug
    assert len(test_case_3) == 5, "the target world should be five letters"
    print("PASSED")

    print(
        "test case 4, logic handling of guessing with multiples of the same letter:"
    )
    test_case_4 = score_guess(
        test_case_4_mock_data[0], test_case_4_mock_data[1]
    )
    # print(test_case_4)  # debug
    assert test_case_4[3] == 2 and test_case_4[2] == 1, ""
    print("PASSED")


def test_read_file_to_word_list():
    from wordle import VALID_WORDS_FILE_PATH, read_file_to_word_list

    test_case_1_mock_data = VALID_WORDS_FILE_PATH
    test_case_2_mock_data = "./todo.md"
    test_case_3_mock_data = "./does-not-exist"

    print("--- TEST read_file_to_word_list CASES ---")

    print("test case 1, logic for reading a valid wordle file")
    test_case_1 = read_file_to_word_list(test_case_1_mock_data)
    # print(test_case_1)  # debug
    assert test_case_1[0] == "aahed", "file was not read correctly"
    print("PASSED")

    print("test case 2, logic for reading a valid file but not a wordle file")
    test_case_2 = read_file_to_word_list(test_case_2_mock_data)
    # print(test_case_2)  # debug
    assert test_case_2 == [], "Should return none"
    print("PASSED")

    print(
        "test case 3, logic for reading a invalid file path (should raise OSError)"
    )
    try:
        _test_case_3 = read_file_to_word_list(test_case_3_mock_data)
        # print(test_case_3)  # debug
    except:
        print("Failed as expected")
        print("PASSED")
    else:
        print(
            "the expected failed test passed without an error: Something has gone very wrong"
        )
        print("Failed")


# ---- Integration Tests ----


def test_game_loop():
    print("--- TEST Integration though game_loop() CASES ---")
    from wordle import game_loop, game_setup

    print(
        "test case 1, check scoring logic result given a single user guesses"
    )
    mock_user_input_words = ["apple"]
    mock_game_setup = game_setup(
        target_words_list=["paper"], number_of_user_guesses=1
    )
    test_case_1 = game_loop(
        mock_game_setup,
        mock_user_input_words,
    )
    # print(test_case_1) # debug
    assert test_case_1 == (1, 1, 2, 0, 1), (
        "two pass score guess logic is incorrect"
    )
    print("PASSED")

    print("test case 2, check scoring logic result given two user guesses")
    mock_user_input_words = ["apple", "funny"]
    mock_game_setup = game_setup(
        target_words_list=["bunny"], number_of_user_guesses=2
    )
    test_case_2 = game_loop(
        mock_game_setup,
        mock_user_input_words,
    )
    # print(test_case_2)  # debug
    assert test_case_2 == (0, 2, 2, 2, 2), (
        "two pass score guess logic is incorrect"
    )
    print("PASSED")

    print(
        "test case 3, check scoring logic result given single correct user guesses"
    )
    mock_user_input_words = ["apple"]
    mock_game_setup = game_setup(
        target_words_list=["apple"], number_of_user_guesses=1
    )
    test_case_3 = game_loop(
        mock_game_setup,
        mock_user_input_words,
    )
    # print(test_case_3)  # debug
    assert test_case_3 == (2, 2, 2, 2, 2), (
        "two pass score guess logic is incorrect"
    )
    print("PASSED")

    print(
        "test case 4 check scoring logic result given single correct user guesses after 4 guesses"
    )
    mock_user_input_words = ["hello", "hello", "hello", "hello", "apple"]
    mock_game_setup = game_setup(
        target_words_list=["apple"], number_of_user_guesses=5
    )
    test_case_4 = game_loop(
        mock_game_setup,
        mock_user_input_words,
    )
    # print(test_case_4)  # debug
    assert test_case_4 == (2, 2, 2, 2, 2), (
        "two pass score guess logic is incorrect"
    )
    print("PASSED")


def test_all() -> None:
    test_score_guess()
    test_read_file_to_word_list()
    test_game_loop()


if __name__ == "__main__":
    test_all()
    # test_game_loop()
