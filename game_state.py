import npc
class GameState:
    def __init__(self):
        self.current_location = "tavern"
        self.sub_location = "door"
        self.player = None
        self.flags = set()
        self.inventory = []
        self.npcs_met = {}

    def set_flag(self, flag_name):
        self.flags.add(flag_name)

    def has_flag(self, flag_name):
        return flag_name in self.flags

    def save_game(self):
        """Send game state to dictionary"""
        return {
            "current_location": self.current_location,
            "sub_location": self.sub_location,
            "flags": self.flags,
            "inventory": self.inventory,
            "npcs" : {
                name: npc.save_game()
                for name, npc in self.npcs_met.items()
            }
        }

    @classmethod
    def load_game(cls, save_data):
        """Create game state from saved dictionary"""
        state = cls()
        state.current_location = save_data["current_location"]
        state.flags = set(save_data["flags"])
        state.inventory = save_data["inventory"]
        state.npcs_met = {
            name: npc.load_game(npc_data)
            for name, npc_data in save_data["npcs"].items()
        }