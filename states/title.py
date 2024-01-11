from states.state import State 
from states.game_world import Game_World

# inherit from state class
class Title(State):
    def __init__(self, game):
        State.__init__(self, game)
        
    def update(self, delta_time, actions):
        # if player presses start create new instance of game world 
        if actions["start"]:
            new_state = Game_World(self.game)
            # enter state adds the state to the top of the stack 
            new_state.enter_state()
        self.game.reset_keys()
        
    def render(self, display):
        display.fill((255, 255, 255))
        self.game.draw_text(display, "Press 'Enter' to Play!", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2)