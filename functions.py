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


def _parse_game_data(lines: list[str]) -> dict[int, list[tuple[str, int]]]:
    games = {}
    for line in lines:
        # Ensure the line has the correct format
        if ': ' not in line:
            continue
        parts = line.strip().split(': ')
        game_id_parts = parts[0].split(' ')
        if len(game_id_parts) < 2:
            continue  # Skip lines that don't have a valid game ID format
        game_id = int(game_id_parts[1])
        cubes_data = parts[1].split('; ')

        # Parsing the cube data for each game
        cubes = []
        for data in cubes_data:
            cube_parts = data.split(', ')
            for cube in cube_parts:
                count, color = cube.split(' ')
                cubes.append((color.strip(), int(count)))  # Stripping whitespace from color
        games[game_id] = cubes

    return games


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
