from iterative_policy_evaluation import PolicyEvaluation
from grid_world import GridWorld

def get_random_uniform_policy(grid, action, state):
    return 1/4 # Random policy in 4 directions


def get_actions():
    actions_RLUD = [GridWorld.Action.R, GridWorld.Action.D, GridWorld.Action.U, GridWorld.Action.L]
    return actions_RLUD

if __name__ == "__main__":
    grid = GridWorld()
    # next_states = grid.get_successor_states((1, 0), GridWorld.Action.R)
    # print(next_states)

    actions = get_actions()
    # policy = get_random_uniform_policy(grid)
    policy = get_random_uniform_policy()
    policyEvaluator = PolicyEvaluation(grid, policy, actions)
