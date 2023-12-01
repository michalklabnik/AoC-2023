import re


def extract_digits(s: str) -> int:
    # Regular expression to find all sequences of digits
    numbers = re.findall(r'\d+', s)

    if not numbers:
        return 0  # Return None if no digits are found

    first_number = numbers[0]
    last_number = numbers[-1]

    # Extract the first and last digit of the first and last number
    first_digit = first_number[0]
    last_digit = last_number[-1]

    return int(first_digit + last_digit)


def word_to_num(s: str) -> str:
    number_words = {
        'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6',
        'seven': '7', 'eight': '8', 'nine': '9'
    }

    result = ""
    while s:
        matched = False
        for word, num in number_words.items():
            if s.startswith(word):
                result += num
                # Because of overlaping words, we can't just remove the word and only first character
                # https://www.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2/
                # s = s[len(word):]
                s = s[1:]
                matched = True
                break
        if not matched:
            result += s[0]  # Append the character if it's not a number word
            s = s[1:]

    return result
