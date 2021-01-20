import sys


def zerodepth_solve(input_list: list):
    """
    Calculates the minimum and maximum depths of zeroes in a recursive list of ints.

    Example input_list: [1,[5,0,2],0,[7,[2,[0],3]],[[0]]]
    Expected result: [1,4]
    """

    if not isinstance(input_list, list):
        return None, None

    def recursive_solver(
        input_l: list,
        depth: int = 1,
        min_d: int = sys.maxsize,
        max_d: int = -1,
    ):
        for member in input_l:
            if isinstance(member, int):
                if member == 0:
                    min_d = min(depth, min_d)
                    max_d = max(depth, max_d)

            elif isinstance(member, list):
                new_min_d, new_max_d = recursive_solver(member, depth + 1, min_d, max_d)
                min_d = min(min_d, new_min_d)
                max_d = max(max_d, new_max_d)

        return min_d, max_d

    min_depth, max_depth = recursive_solver(input_list)

    if min_depth == sys.maxsize:
        min_depth = None
    if max_depth == -1:
        max_depth = None

    return min_depth, max_depth
