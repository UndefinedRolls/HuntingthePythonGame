class Location:
    def __init__(self, name, description, exits, look_at, npcs=[]):
        self.name = name
        self.description = description
        self.exits = exits
        self.action = []
        self.npc = npcs
        self.can_look_at = look_at
        self.target_aliases = {}
    def describe_exits(self):
        if self.exits:
            print(f"\nFrom {self.name} you can see: {'\n'.join(self.exits)}")
        else:
            print(
                "\nThere are no obvious exits"
            )

    def normalize_target(self, string):
        if not string:
            return None

        target_lower = string.lower()
        for target, alias in self.target_aliases.items():
            if target in target_lower:
                return alias

        if target_lower in self.can_look_at:
            return target_lower

        return 'other'
    def add_npc(self, npc):
        self.npc[npc.name] = npc

    def describe(self):
        print(f"\n{self.description}")