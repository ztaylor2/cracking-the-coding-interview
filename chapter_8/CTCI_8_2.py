"""Robot in a grid."""


def robot_path(grid):
    """Return a path for the robot."""
    rows = len(grid)
    cols = len(grid[0])
    valid_paths = []

    def traverse_grid(i=0, j=0, path=[]):
        if i > rows - 1 or j > cols - 1:
            return
        if grid[i][j] == 1:
            return
        if i == rows - 1 and j == cols - 1:
            valid_paths.append(path)
        traverse_grid(i + 1, j, path + ['down'])
        traverse_grid(i, j + 1, path + ['right'])
    traverse_grid()
    return valid_paths
