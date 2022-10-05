
class PolicyEvaluation:

    def __init__(self, grid, policy, actions) -> None:
        self.policy = policy
        self.grid = grid
        self.actions = actions
    
    def init_value_func(self):
        value_func = []
        for idx, _ in enumerate(self.grid.map):
            value_row = []
            for _ in self.grid.map[idx]:
                value_row.append(0)
            value_func.append(value_row)
        return value_func
                
    def successor_states(self, state): pass

    def evaluate_policy(self):
        value_function = self.init_value_func()
        k = 0
        while k < 10:

            for row in range(self.grid.row_size):
                for column in range(self.grid.column_size):
                    state = (row, column)
                    
                    v_s = 0
                    for action in self.actions:
                        successor_states = self.grid.get_successor_states(state, action) # the successor states if I take action action in state state

                        inner_sum = 0
                        for next_state in successor_states:
                            p_s_sp_a = self.grid.transaction_probability(state, next_state, action) # the probability to get to next_state from state with action
                            v_func_prev = value_function[next_state[0]][next_state[1]]
                            inner_sum += p_s_sp_a * v_func_prev
                        
                        policy_a_s = self.policy(self.grid, action, state)  # if you are at state state, probability you take action action
                        reward_s_a = self.grid.reward(action, state) # the reward if I take action action in state state
                        gama = self.grid.gama
                        v_s += policy_a_s * (reward_s_a + gama * inner_sum)

                    value_function[state[0]][state[1]] = v_s







                    

        