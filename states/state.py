class State():
    def __init__(self, game):
        self.game = game
        self.prev_state = None 
        
    def update(self, delta_time, actions):
        pass
    
    def render(self, surface):
        pass

    # essentially the push 
    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        # add it to the top of the stack 
        self.game.state_stack.append(self)
    # pop from stack 
    def exit_state(self):
        self.game.state_stack.pop()