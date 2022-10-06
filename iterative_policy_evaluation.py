import copy
from grid_world import GridWorld


class PolicyEvaluation:
    def __init__(self, grid, actions) -> None:
        self.grid = grid
        self.actions = actions
        self.tolerance = 0.001

    def init_value_func(self):
        value_func = []
        for idx, _ in enumerate(self.grid.map):
            value_row = []
            for _ in self.grid.map[idx]:
                value_row.append(0)
            value_func.append(value_row)
        return value_func

    def evaluate_policy_one_iteration(self, value_function, policy):
        for row in range(0, self.grid.row_size):
            for column in range(0, self.grid.column_size):
                state = (row, column)
                cell_type = self.grid.map[state[0]][state[1]]
                if cell_type == GridWorld.Cell.O:
                    continue

                v_s = 0
                for action in self.actions:
                    # the successor states if I take action action in state state
                    successor_states = self.grid.get_successor_states(
                        state, action)

                    inner_sum = 0
                    for next_state in successor_states:
                        # the probability to get to next_state from state with action
                        p_s_sp_a = self.grid.transaction_probability(
                            state, next_state, action)

                        v_func_prev = value_function[next_state[0]
                                                     ][next_state[1]]
                        inner_sum += p_s_sp_a * v_func_prev
                        if cell_type == GridWorld.Cell.G or cell_type == GridWorld.Cell.T:
                            inner_sum = 0

                    # if you are at state state, probability you take action action
                    policy_a_s = policy[state][action]
                    # the reward if I take action action in state state
                    reward_s_a = self.grid.reward(action, state)
                    gamma = self.grid.gamma
                    v_s += policy_a_s * (reward_s_a + gamma * inner_sum)

                value_function[state[0]][state[1]] = v_s
        return value_function

    def evaluate_policy(self, policy):
        value_function = self.init_value_func()
        self.value_function = copy.deepcopy(value_function)
        has_converged = False
        while not has_converged:
            value_function = self.evaluate_policy_one_iteration(
                value_function, policy)
            has_converged = self.has_converged(value_function)
            self.value_function = copy.deepcopy(value_function)

    def has_converged(self, value_function):
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

        return max_diff <= self.tolerance and not all_zero

    def render_value_function(self):
        for value_row in enumerate(self.value_function):
            print(value_row)
