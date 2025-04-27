import time
from typing import TypeGuard

from main import FiveCharWord


def benchmark_plain_strings():
    """Benchmarks reading words and validating length using plain strings."""
    word_list: list[str] = []
    with open("./data/all_words.txt", encoding="utf-8") as f:
        start = time.time()
        for line in f:
            word = line.strip()
            if len(word) == 5:  # Equivalent validation
                word_list.append(word)
        end = time.time()
    return end - start, len(word_list)


def benchmark_five_char_words():
    """Benchmarks reading words and creating FiveCharWord objects."""
    word_list: list[FiveCharWord] = []
    with open("./data/all_words.txt", encoding="utf-8") as f:
        start = time.time()
        for line in f:
            try:
                # This involves creation and internal validation within FiveCharWord
                word = FiveCharWord(line.strip())
                word_list.append(word)
            except ValueError:
                # Skip words that don't meet FiveCharWord criteria (e.g., not 5 chars)
                pass
        end = time.time()
    return end - start, len(word_list)


def is_five_char_word(
    s: str,
) -> TypeGuard[
    FiveCharWord
]:  # Note: TypeGuard narrows to str here as len(s)==5 doesn't guarantee it's a FiveCharWord instance
    """A TypeGuard that checks if a string has length 5."""
    # This function itself doesn't create FiveCharWord objects,
    # it's purely a runtime check used by the type checker.
    return len(s) == 5


def benchmark_five_char_words_type_guard():
    """Benchmarks reading words and validating length using the TypeGuard function."""
    # Note: The list contains strings because the TypeGuard doesn't *create* FiveCharWord objects,
    # it just helps the type checker understand that 'word' is a 5-char string after the if check.
    word_list: list[str] = []
    with open("./data/all_words.txt", encoding="utf-8") as f:
        start = time.time()
        for line in f:
            word = line.strip()
            if is_five_char_word(
                word
            ):  # Using the TypeGuard function for validation check
                word_list.append(word)
        end = time.time()
    return end - start, len(word_list)


# --- Run Benchmarks ---

print("Starting benchmarks...")

plain_time, plain_count = benchmark_plain_strings()
custom_time, custom_count = benchmark_five_char_words()
type_guard_time, type_guard_count = benchmark_five_char_words_type_guard()


# --- Print Results ---

print("\n--- Benchmark Results ---")
print(
    f"Plain strings (len() check):        {plain_time:.6f}s for {plain_count} words"
)
print(
    f"FiveCharWord (creation):            {custom_time:.6f}s for {custom_count} words"
)
print(
    f"FiveCharWord TypeGuard (check only):{type_guard_time:.6f}s for {type_guard_count} words"
)

# --- Print Overheads ---

print("\n--- Overhead Comparison (vs Plain strings) ---")
# Overhead of creating FiveCharWord objects vs simple string handling
if plain_time > 0:
    overhead_custom = ((custom_time / plain_time) - 1) * 100
    print(f"Overhead (FiveCharWord creation): {overhead_custom:.2f}%")
else:
    print("Overhead (FiveCharWord creation): N/A (Plain time is zero)")


# Overhead of using the TypeGuard function for the check vs simple len() check
# Note: This measures the cost of the function call overhead + the check itself
if plain_time > 0:
    overhead_type_guard = ((type_guard_time / plain_time) - 1) * 100
    print(f"Overhead (TypeGuard check only):  {overhead_type_guard:.2f}%")
else:
    print("Overhead (TypeGuard check only):  N/A (Plain time is zero)")

print(
    "\nNote: TypeGuard overhead measures the cost of the function call itself, not object creation."
)
