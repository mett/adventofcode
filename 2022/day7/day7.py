#! /usr/bin/env python3
"""Advent of code day 7."""


class FileTreeNode:
    """Represents a FileTree node."""
    path = None
    directory = None
    size = None
    parent = None
    children = None

    def __init__(self, path: str, directory=True, size=None):
        self.path = path
        self.directory = directory
        self.children = []
        if not directory:
            if not size:
                raise Exception('Size argument missing for file')
            self.size = size

    def get_child(self, name):
        """Find child with given name and return it."""
        for child in self.children:
            if child.path == name:
                return child
        raise Exception(f'Child {name} not found.')

    def get_size(self) -> int:
        """Return the nodes size."""
        total = 0
        for child in self.children:
            if child.directory:
                total += child.get_size()
            else:
                total += child.size
        return total


    def _node_summary(self):
        if self.directory:
            return f'(dir) dir-size: {self.get_size()}'
        return f'(file, size={self.size})'

    def _calc_depth(self):
        ancestor = self.parent
        depth = 0
        while ancestor:
            ancestor = ancestor.parent
            depth += 1
        return depth

    def __str__(self):
        depth = self._calc_depth()
        tab_char = '\t'
        return (f'{tab_char * depth} - {self.path} {self._node_summary()}\n' +
                ''.join(str(child) for child in self.children))


def get_puzzle_input(example_data: bool=False):
    """Return puzzle input data as an iterable.

    example_data = True will return the example data provided in the problem.
    """
    print(example_data)
    if example_data:
        data = [
            '$ cd /',
            '$ ls',
            'dir a',
            '14848514 b.txt',
            '8504156 c.dat',
            'dir d',
            '$ cd a',
            '$ ls',
            'dir e',
            '29116 f',
            '2557 g',
            '62596 h.lst',
            '$ cd e',
            '$ ls',
            '584 i',
            '$ cd ..',
            '$ cd ..',
            '$ cd d',
            '$ ls',
            '4060174 j',
            '8033020 d.log',
            '5626152 d.ext',
            '7214296 k',
        ]
        for line in data:
            yield line
        return
    with open('./puzzle-input.txt', 'r', encoding='utf-8') as in_file:
        for line in in_file:
            yield line.strip('\n')


def _parse_cmd(cmd_input: str):
    """Parse the command and return it."""
    tokens = cmd_input.split()
    if tokens[0] == '$':
        if len(tokens) > 2:
            return (tokens[1], tokens[2])
    return (tokens[1], None)


def _parse_content(ls_output: str):
    """Parse ls output to something else."""
    (dir_or_size, name) = ls_output.split()
    if dir_or_size == 'dir':
        return FileTreeNode(name)
    return FileTreeNode(name, directory=False, size=int(dir_or_size))


def parse_commands(cmd_inputs: list):
    """Parse commands from list and return a FileTreeNode"""
    root = None
    current_node = None
    parse_content = False

    for inp in cmd_inputs:
        if inp.startswith('$'):
            parse_content = False

        if parse_content:
            child = _parse_content(inp)
            child.parent = current_node
            current_node.children.append(child)

        print(inp)
        (cmd, args) = _parse_cmd(inp)
        if cmd == 'cd' and args == '/':
            root = FileTreeNode(args)
            current_node = root
        elif cmd == 'cd' and args == '..':
            current_node = current_node.parent
        elif cmd == 'cd':
            print(args)
            current_node = current_node.get_child(args)
        if cmd == 'ls':
            parse_content = True
            continue
    return root


def get_relevant_total(root, limit, vals):
    """find relevant folders."""

    for child in root.children:
        if child.directory:
            print(child.path)
            c_size = child.get_size()
            if c_size > limit:
                print(child.path)
                print(c_size)
                vals.append(c_size)
            get_relevant_total(child, limit, vals)



def main():
    """Main function."""
    data = get_puzzle_input(example_data=False)
    root = parse_commands(data)
    vals = []
    diskspace = 70000000
    update_size = 30000000
    current_use = root.get_size()
    current_free = diskspace - current_use
    print(current_use)
    print(current_free)

    get_relevant_total(root, update_size - current_free, vals)
    print(vals)
    print(min(vals))

if __name__ == '__main__':
    main()
