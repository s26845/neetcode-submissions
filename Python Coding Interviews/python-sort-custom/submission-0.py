from typing import List

def get_word_lenght(word: str) -> int:
    return len(word)


def sort_words(words: List[str]) -> List[str]:
    return sorted(words, key=get_word_lenght, reverse=True)

def get_abs_value(number: int) ->int:
    return abs(number)


def sort_numbers(numbers: List[int]) -> List[int]:
    return sorted(numbers, key = get_abs_value)


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
