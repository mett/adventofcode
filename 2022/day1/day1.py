#! /usr/bin/env python3
""" day1 - advent of code

"""


class Elves:
    """Keeps track of elves."""
    elfventory = None

    def __init__(self):
        self.elfventory = []

    def add_elf(self, calories: list):
        """Add calorie count of elf into inventory."""
        self.elfventory.append(sum(calories))

    def get_top_elf(self) -> int:
        """Return the elf with highest calorie count."""
        return max(self.elfventory)

    def get_top_three(self) -> int:
        """Return the calorie count of the top three elfs."""
        return sum(sorted(self.elfventory, reverse=True)[:3])

    @staticmethod
    def parse_elves(source_file: str):
        """Parse given source_file, returning a Elves object."""
        elves = Elves()
        with open(source_file, 'r', encoding='utf-8') as source:
            calories = []
            for line in source:
                if line == '\n':
                    elves.add_elf(calories)
                    calories = []
                else:
                    calories.append(int(line))
        return elves


def main():
    """Parse some elves!"""
    elves = Elves.parse_elves('test-input.txt')
    print(f'top elf: {elves.get_top_elf()}')
    print(f'top three elves: {elves.get_top_three()}')


if __name__ == '__main__':
    main()
