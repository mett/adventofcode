#! /usr/bin/env python3.11
"""Day 8 Advent of Code."""
import itertools


class Knot:
    """Represents an Knot of a rope."""
    coordinates = None
    visited = None
    last_position = None

    def __init__(self):
        self.coordinates = {
            'x': 0,
            'y': 0,
        }
        self.visited = [self.get_coordinates()]

    def count_visited(self):
        """return unique posisitions visited."""
        return len(set(self.visited))

    def move(self, direction, steps):
        """Move the position according to the given instructions."""
        self.last_position = self.get_coordinates()
        match direction:
            case 'R':
                self.coordinates['x'] += steps
            case 'L':
                self.coordinates['x'] -= steps
            case 'U':
                self.coordinates['y'] += steps
            case 'D':
                self.coordinates['y'] -= steps

    def follow(self, coordinates: tuple):
        """Move to coordinates."""
        if coordinates not in self.visited:
            self.visited.append(coordinates)

        print(f'following: {coordinates}')
        self.coordinates['x'] = coordinates[0]
        self.coordinates['y'] = coordinates[1]

    def get_coordinates(self) -> tuple:
        """Return the coordinates as a tuple."""
        return (self.coordinates['x'], self.coordinates['y'])

    def move_adjecent_to(self, obj):
        """Calculate and move to an adjacent coordinate."""
        if self.is_adjacent_to(obj):
            return

        possible_moves = set(self.generate_adjacent_coordinates())
        if obj.last_position in possible_moves:
            self.follow(obj.last_position)
            return
        raise Exception('Illegal move')

    def is_adjacent_to(self, obj) -> bool:
        """Check if this object is adjacent to the given coordinates."""
        adjacent_coordinates = self.generate_adjacent_coordinates()
        (x_co, y_co) = obj.get_coordinates()
        return (x_co, y_co) in adjacent_coordinates

    def generate_adjacent_coordinates(self) -> list:
        """Generate a list of coordinates where we are adjacent."""
        (x_co, y_co) = self.get_coordinates()
        y_range = range(y_co-1, y_co+2)
        x_range = range(x_co-1, x_co+2)

        return itertools.product(x_range, y_range)


def get_puzzle_input(example: bool = False):
    """Get puzzle input."""
    if example:
        return [
            'R 4',
            'U 4',
            'L 3',
            'D 1',
            'R 4',
            'D 1',
            'L 5',
            'R 2',
        ]

    with open('./puzzle-input.txt', 'r', encoding='utf-8') as pinput:
        return [line.strip('\n') for line in pinput]


def parse_input(moves: list) -> list:
    """Parse the move line into tuples of moves."""
    for move in moves:
        (direction, steps) = move.split()
        yield (direction, int(steps))


def main():
    """Main function."""
    instructions = parse_input(get_puzzle_input())
    head = Knot()
    tail = Knot()
    for (direction, steps) in instructions:
        while steps > 0:
            print(f'move: {direction}')
            head.move(direction, 1)
            print(f'head pos: {head.get_coordinates()}')
            tail.move_adjecent_to(head)
            print(f'tail pos: {tail.get_coordinates()}')
            print(tail.count_visited())
            steps -= 1


if __name__ == '__main__':
    main()
