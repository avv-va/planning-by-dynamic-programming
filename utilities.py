from grid_world import GridWorld

RANDOM_UNIFORM_POLICY = {}


def init_random_uniform_policy(grid):
    for row in range(0, grid.row_size):
        for column in range(0, grid.column_size):
            state = (row, column)
            RANDOM_UNIFORM_POLICY[state] = {}
            for action in get_actions():
                RANDOM_UNIFORM_POLICY[state][action] = 1/4


def get_random_uniform_policy():
    return RANDOM_UNIFORM_POLICY


def get_actions():
    actions_RLUD = [GridWorld.Action.R, GridWorld.Action.D,
                    GridWorld.Action.U, GridWorld.Action.L]
    return actions_RLUD
