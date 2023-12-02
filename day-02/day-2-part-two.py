from functions import _parse_game_data
from pathlib import Path


def _calculate_minimum_cubes_and_power(games: dict[int, list[tuple[str, int]]]) -> tuple[dict[int, dict[str, int]], dict[int, int], int]:
    min_cubes = {}
    powers = {}

    for game_id, cubes in games.items():
        # Tracking the maximum number of each color cube shown at any one time in the game
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        for color, count in cubes:
            max_cubes[color] = max(max_cubes[color], count)

        min_cubes[game_id] = max_cubes
        # Calculating the power of the set of cubes
        powers[game_id] = max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]

    # Calculating the total power across all games
    total = sum(powers.values())

    return min_cubes, powers, total


# Main execution
if __name__ == '__main__':
    # file_path = Path(__file__).parent / 'day-2-input-test.txt'  # Answer: 2286
    file_path = Path(__file__).parent / 'day-2-input.txt'

    with open(file_path, 'r') as file:
        file_content = file.readlines()

    parsed_games = _parse_game_data(file_content)
    minimum_cubes, game_powers, total_power = _calculate_minimum_cubes_and_power(parsed_games)

    print("Minimum cubes for each game:", minimum_cubes)
    print("Power of cubes for each game:", game_powers)
    print("Total:", total_power)
