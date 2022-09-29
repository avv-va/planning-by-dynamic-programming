from argparse import Action
from iterative_policy_evaluation import PolicyEvaluation
from grid_world import GridWorld

def get_random_uniform_policy(grid):
    grid_map = grid.map
    policy = []
    # for r_idx, row in enumerate(grid_map):
    #     for c_idx ,cell in enumerate(row):
    #         actions = []
    #         if c_idx == 0:
    #             if grid_map[r_idx][c_idx + 1] != GridWorld.Cell.O:
    #                 actions.append 
    # actions_RD = [Action.R, Action.D]
    # actions_RDL = [Action.R, Action.D, Action.L]
    # actions_DL = [Action.D, Action.L]
    # actions_UDR = [Action.R, Action.D, Action.U]
    actions_RLUD = [GridWorld.Action.R, GridWorld.Action.D, GridWorld.Action.U, GridWorld.Action.L]
    for row in grid_map:
        row_policies = []
        for cell in row:
            row_policies.append(actions_RLUD)
        policy.append(row_policies)
    return policy


if __name__ == "__main__":
    grid = GridWorld()
    policy = get_random_uniform_policy(grid)
    policyEvaluator = PolicyEvaluation(grid, policy)
