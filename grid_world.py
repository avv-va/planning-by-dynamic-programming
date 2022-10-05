class GridWorld:
    class Cell:
        S = 'Start'
        G = 'Goal'
        W = 'White'
        T = 'Trap'
        O = 'Obstacle'
    class Action:
        U = (-1, 0)
        D = (1, 0)
        R = (0, 1)
        L = (0, -1)
        
        NOT_INTENDED = {
            U: [R, L],
            D: [R, L],
            R: [U, D],
            L: [U, D]
        }

    def __init__(self) -> None:
        self.rewards = {
            self.Cell.G: 50,
            self.Cell.T: -50,
            self.Cell.W: -1,
            self.Cell.S: -1,
            self.Cell.O: None}
        self.map = [[self.Cell.W, self.Cell.W, self.Cell.W, self.Cell.G],
                     [self.Cell.W, self.Cell.O, self.Cell.W, self.Cell.T],
                     [self.Cell.W, self.Cell.W, self.Cell.W, self.Cell.W],
                     [self.Cell.W, self.Cell.S, self.Cell.W, self.Cell.W]]
        self.row_size =  len(self.map)
        self.column_size = len(self.map[0])
        self.gamma = 0.9
    
    def reward(self, action, state):
        cell_type = self.map[state[0]][state[1]]
        return self.rewards[cell_type]

    def validate_states_index(self, next_states, current_state):
        for idx, next_st in enumerate(next_states):
            row = next_st[0]
            column = next_st[1]
            if row == -1:
                row += 1
            elif row == self.row_size:
                row += -1
            if column == -1:
                column += 1
            elif column == self.column_size:
                column += -1
            
            next_states[idx] = (row, column)
            if self.map[row][column] == self.Cell.O:
                next_states[idx] = current_state            

        return next_states

    def get_successor_states_for_trans_prob(self, current_state, action):
        next_states = []
        if self.map[current_state[0]][current_state[1]] in [self.Cell.G, self.Cell.T]:
            return next_states

        state_intended = (current_state[0] + action[0], current_state[1] + action[1])
        next_states.append(state_intended)
        actions_not_intended = self.Action.NOT_INTENDED[action]
        for not_int_a in actions_not_intended:
            state_not_intended = (current_state[0] + not_int_a[0], current_state[1] + not_int_a[1])
            next_states.append(state_not_intended)

        next_states_validated = self.validate_states_index(next_states, current_state)
        return next_states_validated        

    def get_successor_states(self, current_state, action):
        next_states = self.get_successor_states_for_trans_prob(current_state, action)
        return list(set(next_states))
    
    def transaction_probability(self, current_state, next_state, action):
        p = 0.7  # probability to get into the intended state
        q = 1 - p

        state_intended = (current_state[0] + action[0], current_state[1] + action[1])
        state_intended_vd = self.validate_states_index([state_intended], current_state)[0]

        next_states_vd = self.get_successor_states_for_trans_prob(current_state, action)
        count_ = next_states_vd.count(next_state)

        if next_state == state_intended_vd:
            if count_ == 2:
                return p + q/2
            elif count_ == 1:
                return p
            elif count_ == 0:
                return 0
        else:
            if count_ == 2:
                return q
            elif count_ == 1:
                return q/2
            elif count_ == 0:
                return 0
