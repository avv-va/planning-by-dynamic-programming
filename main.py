from iterative_policy_evaluation import PolicyEvaluation
from policy_iteration import PolicyIteration
from grid_world import GridWorld
from utilities import get_actions, init_random_uniform_policy, get_random_uniform_policy

if __name__ == "__main__":
    grid = GridWorld()
    init_random_uniform_policy(grid)

    actions = get_actions()
    policy = get_random_uniform_policy()

    policy_evaluator = PolicyEvaluation(grid, actions)
    policy_evaluator.evaluate_policy(policy)
    print("value function q1, part1: -------------")
    policy_evaluator.render_value_function()

    policy_iterator = PolicyIteration(policy_evaluator)
    policy_iterator.compute_greedy_policy()
    print("policy q1, part2: ---------------")
    policy_iterator.render_policy()
    print("value function q1, part2: -----------------")
    policy_iterator.render_value_function()
