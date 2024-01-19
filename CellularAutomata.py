import numpy as np

class CellularAutomata:

    '''
    Used to simulate the evolution of the system
    over time as terminal output.
    '''

    def __init__(self, rule=173, columns=30, timesteps=60) -> None:
        '''Constructor'''
        self.rule = rule
        self.columns = columns
        self.rows = timesteps
        self.timesteps = range(timesteps)

        self.transition_table = None
        self.state = None
        self.time = 0

        self.set_transition_table()
        self.set_initial_state()

    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#

    def set_transition_table(self) -> None:
        '''Sets the transition table based on the rule number'''
        binary = bin(self.rule)[2:].zfill(8)
        transition_table = {
            (0,0,0): int(binary[0]),
            (0,0,1): int(binary[1]),
            (0,1,0): int(binary[2]),
            (0,1,1): int(binary[3]),
            (1,0,0): int(binary[4]),
            (1,0,1): int(binary[5]),
            (1,1,0): int(binary[6]),
            (1,1,1): int(binary[7]),
        }
        self.transition_table = transition_table
    
    def set_initial_state(self) -> None:
        '''Sets the initial state of the system'''
        self.state = np.random.randint(2, size=self.columns)
        
    def get_next_state(self) -> None:
        '''Calculates the next state of the system'''
        next_state = np.zeros(self.columns, dtype=int)

        for i in range(self.columns):
            
            left = self.state[(i-1)%self.columns]
            center = self.state[i]
            right = self.state[(i+1)%self.columns]
            
            next_state[i] = self.transition_table[(left, center, right)]

        self.state = next_state
        self.time += 1

    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#

    def run(self):
        '''Runs the simulation'''
        print('Rule:', self.rule)
        state = self.state
        state_str = ''.join(['█' if i==1 else ' ' for i in state])
        print(state_str) # initial state
        for t in self.timesteps:
            self.get_next_state()
            state = self.state
            state_str = ''.join(['█' if i==1 else ' ' for i in state])
            print(state_str)


if __name__ == '__main__':
    ca = CellularAutomata(rule=173, columns=100, timesteps=200)
    ca.run()
