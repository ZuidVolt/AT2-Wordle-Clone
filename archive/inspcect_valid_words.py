from wordle import get_valid_words

valid_wordle_list = get_valid_words()

first_five_words = valid_wordle_list[:5]
last_five_words = valid_wordle_list[-5:]

print("First five valid words:", first_five_words)
print("Last five valid words:", last_five_words)
