import copy
from math import inf
from utilities import get_random_uniform_policy, get_actions
from grid_world import GridWorld


class PolicyIteration:
    def __init__(self, policy_evaluator) -> None:
        self.policy_evaluator = policy_evaluator
        self.grid = policy_evaluator.grid
        self.value_func_tolerance = 0.001

    def find_best_actions(self, policy_evaluation, state):
        best_actions = []
        max_q_s_a = -inf

        for action in get_actions():
            successor_states = self.grid.get_successor_states(state, action)
            inner_sum = 0
            for next_state in successor_states:
                p_s_sp_a = self.grid.transaction_probability(
                    state, next_state, action)
                v_next_state = policy_evaluation[next_state[0]][next_state[1]]
                inner_sum += p_s_sp_a * v_next_state

            gamma = self.grid.gamma
            r_s_a = self.grid.reward(action, state)
            q_s_a = r_s_a + gamma * inner_sum

            if q_s_a > max_q_s_a:
                best_actions = [action]
                max_q_s_a = q_s_a
            elif q_s_a == max_q_s_a:
                best_actions.append(action)
                max_q_s_a = q_s_a

        return best_actions

    def update_policy_based_on_value_function(self, policy_evaluation):
        policy = {}
        for row in range(0, self.grid.row_size):
            for column in range(0, self.grid.column_size):
                state = (row, column)
                policy[state] = {}

                cell_type = self.grid.map[state[0]][state[1]]
                if cell_type == GridWorld.Cell.O:
                    continue

                if cell_type == GridWorld.Cell.G or cell_type == GridWorld.Cell.T:
                    for action in get_actions():
                        policy[state][action] = 0
                        continue

                best_actions = self.find_best_actions(policy_evaluation, state)

                for action in best_actions:
                    policy[state][action] = 1/len(best_actions)

                for action in get_actions():
                    if action not in best_actions:
                        policy[state][action] = 0
        return policy

    def compute_greedy_policy(self):
        policy = get_random_uniform_policy()
        self.policy = copy.deepcopy(policy)

        value_function = self.policy_evaluator.init_value_func()
        self.value_function = copy.deepcopy(value_function)

        policy_has_converged = False
        value_func_has_converged = False

        while (not policy_has_converged) or (not value_func_has_converged):
            value_function = self.policy_evaluator.evaluate_policy_one_iteration(
                value_function, policy)
            policy = self.update_policy_based_on_value_function(value_function)

            policy_has_converged = self.policy_has_converged(policy)
            value_func_has_converged = self.value_func_has_converged(
                value_function)
            self.policy = copy.deepcopy(policy)
            self.value_function = copy.deepcopy(value_function)

    def policy_has_converged(self, policy):
        for row in range(0, self.grid.row_size):
            for column in range(0, self.grid.column_size):
                state = (row, column)
                cell_type = self.grid.map[state[0]][state[1]]
                if cell_type == GridWorld.Cell.O:
                    continue
                if policy[state] != self.policy[state]:
                    return False
        return True

    def value_func_has_converged(self, value_function):
        max_diff = 0
        all_zero = True
        for r_idx, row in enumerate(value_function):
            if all(row) != 0:
                all_zero = False
            for c_idx, _ in enumerate(value_function):
                diff = abs(
                    self.value_function[r_idx][c_idx] - value_function[r_idx][c_idx])

                if diff >= max_diff:
                    max_diff = diff

        return max_diff <= self.value_func_tolerance and not all_zero

    def render_policy(self):
        for row in range(0, self.grid.row_size):
            for column in range(0, self.grid.column_size):
                state = (row, column)
                cell_type = self.grid.map[state[0]][state[1]]
                if cell_type == GridWorld.Cell.O:
                    continue
                actions_to_be_taken = []
                actions = self.policy[state]
                for action in actions:
                    if self.policy[state][action] != 0:
                        actions_to_be_taken.append(action)
                print(f"state: {state}, actions: {actions_to_be_taken}")

    def render_value_function(self):
        for value_row in enumerate(self.value_function):
            print(value_row)
        print("-----")
