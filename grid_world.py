class GridWorld:
    class Cell:
        S = 'Start'
        G = 'Goal'
        W = 'White'
        T = 'Trap'
        O = 'Obstacle'
    class Action:
        U = 'Up'
        D = 'Down'
        R = 'Right'
        L = 'Left'

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
