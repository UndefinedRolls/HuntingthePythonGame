class Location:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
        self.action = []
        self.npc = []
        self.can_look_at = []
    def describe_exits(self):
        if self.exits:
            print(f"\nFrom {self.name} you can see: {'\n'.join(self.exits)}")
        else:
            print(
                "\nThere are no obvious exits"
            )


    def add_npc(self, npc):
        self.npc[npc.name] = npc

    def describe(self):
        print(f"\n{self.description}")