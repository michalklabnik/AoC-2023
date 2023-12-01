from functions import extract_digits, word_to_num
from pathlib import Path

if __name__ == '__main__':
    # file_path = Path(__file__).parent / 'day-1-b-input-test.txt'  # Answer: 281
    file_path = Path(__file__).parent / 'day-1-input.txt'

    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_stripped = line.strip()
            transformed = word_to_num(line_stripped)
            extracted = extract_digits(transformed)
            total += extracted

            print(line_stripped + ' -> ' + transformed + ' -> ' + str(extracted))

    print('Total: ' + str(total))
