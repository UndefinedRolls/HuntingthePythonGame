class Location:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

    def move_to(self, game):
        game.current_location = self
    def describe(self):
        print(self.description)
    def go_to(self, location, game):
        location.move_to(game)
    def describe_exits(self):
        print(f"From {self.name} you can see:")
        for exit, _ in self.exits.items():
            print(f"- {exit}")

class Bar(Location):
    def __init__(self, name, description, exits):
        super().__init__(name, description, exits)
        self.actions = {}
        self.npc = {}

    def add_npc(self, npc):
        self.npc[npc.name] = npc