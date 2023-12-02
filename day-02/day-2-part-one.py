from functions import _parse_game_data
from pathlib import Path


# Function to determine possible games
def _determine_possible_games(games: dict[int, list[tuple[str, int]]], bag: dict[str, int]) -> list[int]:
    possible_games = []
    for game_id, cubes in games.items():
        game_possible = True
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        for color, count in cubes:
            max_cubes[color] = max(max_cubes[color], count)

        for color in max_cubes:
            if max_cubes[color] > bag[color]:
                game_possible = False
                break

        if game_possible:
            possible_games.append(game_id)

    return possible_games


# Main execution
if __name__ == '__main__':
    # file_path = Path(__file__).parent / 'day-2-input-test.txt'  # Answer: 8
    file_path = Path(__file__).parent / 'day-2-input.txt'

    with open(file_path, 'r') as file:
        file_content = file.readlines()

    play_bag = {"red": 12, "green": 13, "blue": 14}
    parsed_games = _parse_game_data(file_content)
    result = _determine_possible_games(parsed_games, play_bag)

    print('Possible games: ' + str(result))
    print('Total: ' + str(sum(result)))
