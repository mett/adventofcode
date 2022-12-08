#! /usr/bin/env python3


def check_row_up(row, col, forest, height):
    """Check if tree is visible from the top."""
    if forest[row-1][col] < height:
        if row-1 == 0:
            return True
        return check_row_up(row-1, col, forest, height)
    return False

def check_row_down(row, col, forest, height):
    """Check if the tree is visible from the bottom."""
    if forest[row+1][col] < height:
        if row+1 == len(forest)-1:
            return True
        return check_row_down(row+1, col, forest, height)
    return False


def check_col_left(row, col, forest, height):
    """Check if tree is visible to the left."""
    if forest[row][col-1] < height:
        if col-1 == 0:
            return True
        return check_col_left(row, col-1, forest, height)
    return False


def check_col_right(row, col, forest, height):
    """Check if tree is visible to the right."""
    if forest[row][col+1] < height:
        if col+1 == len(forest[row])-1:
            return True
        return check_col_right(row, col+1, forest, height)
    return False


def check_tree_visibility(row, col, forest, height):
    """Verify if tree is visible in all directions."""
    if check_row_up(row, col, forest, height):
        print('visible from up')
        return True
    if check_row_down(row, col, forest, height):
        print('visible from down')
        return True
    if check_col_left(row, col, forest, height):
        print('visible from left')
        return True
    if check_col_right(row, col, forest, height):
        print('visible from right')
        return True
    return False


def count_row_up(row, col, forest, height, can_see):
    """Check the view to the top."""
    if row-1 < 0:
        return

    if forest[row-1][col] < height:
        can_see.append(1)
        count_row_up(row-1, col, forest, height, can_see)
    if forest[row-1][col] >= height:
        can_see.append(1)
    return

def count_row_down(row, col, forest, height, can_see):
    """Check the view to the bottom."""
    if row+1 > len(forest)-1:
        return

    if forest[row+1][col] < height:
        can_see.append(1)
        count_row_down(row+1, col, forest, height, can_see)
    if forest[row+1][col] >= height:
        can_see.append(1)
    return


def count_col_left(row, col, forest, height, can_see):
    """Check the view to the left."""
    if col-1 < 0:
        return

    if forest[row][col-1] < height:
        can_see.append(1)
        count_col_left(row, col-1, forest, height, can_see)
    if forest[row][col-1] >= height:
        can_see.append(1)
    return


def count_col_right(row, col, forest, height, can_see):
    """Check the view to the right."""
    if col+1 > len(forest[row])-1:
        return

    if forest[row][col+1] < height:
        can_see.append(1)
        count_col_right(row, col+1, forest, height, can_see)
    if forest[row][col+1] >= height:
        can_see.append(1)
    return


def scenic_score(row, col, forest):
    """calculate the scenic score of a tree."""
    height = forest[row][col]
    can_see = []
    count_row_up(row, col, forest, height, can_see)
    up_score = sum(can_see)
    can_see = []
    count_row_down(row, col, forest, height, can_see)
    down_score = sum(can_see)
    can_see = []
    count_col_right(row, col, forest, height, can_see)
    right_score = sum(can_see)
    can_see = []
    count_col_left(row, col, forest, height, can_see)
    left_score = sum(can_see)

    return up_score * down_score * right_score * left_score


def build_forest(data: list):
    """Parse data and return a 2-dimensional array with forest data."""
    forest = []
    for row in data:
        row_list = [int(num) for num in row]
        forest.append(row_list)

    return forest


def get_puzzle_input(example: bool=False):
    """Get puzzle input."""
    if example:
        return [
            '30373',
            '25512',
            '65332',
            '33549',
            '35390',
        ]

    with open('./puzzle-input.txt', 'r', encoding='utf-8') as pinput:
        return [line.strip('\n') for line in pinput]


def main():
    """Run the solution."""
    data = get_puzzle_input()
    forest = build_forest(data)
    for row in forest:
        print(row)
    top_score = 0
    top_score_coordinates = None
    for row, tree_data in enumerate(forest):
        for col, _ in enumerate(tree_data):
            score = scenic_score(row, col, forest)
            if score > top_score:
                top_score_coordinates = (row, col)
                top_score = score

    print(top_score_coordinates)
    print(top_score)


if __name__ == '__main__':
    main()
