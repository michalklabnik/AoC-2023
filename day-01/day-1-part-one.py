from functions import extract_digits
from pathlib import Path

if __name__ == '__main__':
    # file_path = Path(__file__).parent / 'day-1-part-one-input-test.txt'  # Answer: 142
    file_path = Path(__file__).parent / 'day-1-input.txt'

    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_stripped = line.strip()
            extracted = extract_digits(line_stripped)
            total += extracted

            print(line_stripped + ' -> ' + str(extracted))

    print('Total: ' + str(total))
