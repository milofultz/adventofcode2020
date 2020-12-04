PUZZLE_INPUT = 'aoc03-data'
TREE_SYMBOL = '#'


def main():
    toboggan_ride = TobogganRide()
    toboggan_ride.trajectory = get_trajectory()
    return toboggan_ride.get_number_of_trees_encountered()


class TobogganRide:
    def __init__(self):
        self.terrain = self.create_terrain()
        self.starting_coordinates = {'x': 0, 'y': 0}
        self.trajectory = {'x': 0, 'y': 0}

    def create_terrain(self):
        with open(PUZZLE_INPUT, 'r') as f:
            data = f.read()
        return data.strip().split('\n')

    def get_number_of_trees_encountered(self) -> int:
        current_coordinates = self.starting_coordinates
        terrain_width = len(self.terrain[0])
        tree_count = 0
        while current_coordinates['y'] < len(self.terrain):
            if self.is_tree_at(current_coordinates):
                tree_count += 1
            current_coordinates['x'] = (current_coordinates['x'] + self.trajectory['x']) % terrain_width
            current_coordinates['y'] += self.trajectory['y']
        return tree_count

    def is_tree_at(self, coordinates: dict) -> bool:
        x = coordinates['x']
        terrain_line = self.terrain[coordinates['y']]
        return True if terrain_line[x] == TREE_SYMBOL else False


def get_trajectory() -> dict:
    print('Input X and Y trajectory:')
    coordinates = dict()
    while True:
        try:
            coordinates['x'] = int((input('X: ')))
            coordinates['y'] = int((input('Y: ')))
            return coordinates
        except ValueError:
            print('Ensure the inputs are numbers.')


if __name__ == "__main__":
    print(main())
