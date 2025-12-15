import random
import webcolors


def roll_stat():
    """Roll 3d6 and return the sum."""
    return sum(random.randint(1, 6) for _ in range(3))

def set_modifier(score):
    return (score - 10)//2


def get_action_target(text):
    temp = text.lower().strip().split()
    if not temp:
        return None, None
    action = temp[0]
    if len(temp) == 1:
        target = None
    elif len(temp) > 2:
        target = " ".join(temp[1:])
    else:
        target = temp[1]
    return action, target


class Player:
    STATS = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    MIN_MOD = -2
    MAX_MOD = 5

    def __init__(self, name, color, clr_txt=None):
        self.name = name
        self.fav_color = color
        if clr_txt is None:
            try:
                self.fav_color_text = webcolors.hex_to_name(self.fav_color)
            except ValueError:
                if self.fav_color.startswith("#"):
                    self.fav_color_text = self.fav_color
                else:
                    self.fav_color_text = "#" + self.fav_color
        else:
            self.fav_color_text = clr_txt
        self.strength = float("inf")
        self.dexterity = float("inf")
        self.constitution = float("inf")
        self.intelligence = float("inf")
        self.wisdom = float("inf")
        self.charisma = float("inf")
        self.set_stats()
        self.stats = {"strength": self.strength, "dexterity": self.dexterity, "constitution": self.constitution,
                      "intelligence": self.intelligence, "wisdom": self.wisdom, "charisma": self.charisma}
    def roll_stats(self):
        while True:
            score = roll_stat()
            modifier = set_modifier(score)
            if self.MIN_MOD <= modifier <= self.MAX_MOD:
                return modifier
    def set_stat(self, stat_name, value=None):
        if stat_name in self.STATS:
            if value is None:
                setattr(self, stat_name, self.roll_stats())
            else:
                setattr(self, stat_name, value)
        else:
            raise ValueError(f'"{stat_name}" is not a valid stat')
    def __str__(self):
        return (f"{self.name}'s favorite color is {self.fav_color_text} and has the following stat modifiers:\nStrength:{self.strength}"
                f"\nDexterity:{self.dexterity}\nConstitution:{self.constitution}"
                f"\nIntelligence:{self.intelligence}\nWisdom:{self.wisdom}\nCharisma:{self.charisma}")

    def set_stats(self):
        for stat in self.STATS:
            self.set_stat(stat)

    def __repr__(self):
        return (f"Player Name:{self.name}\nPlayer Favorite Color:{self.fav_color_text}\n"
                f"Player Favorite Color Hex:{self.fav_color}\nPlayer Stats:\n\n"
                f"Strength:{self.strength}\n"
                f"Dexterity:{self.dexterity}\n"
                f"Constitution:{self.constitution}\n"
                f"Intelligence:{self.intelligence}\n"
                f"Wisdom:{self.wisdom}\n"
                f"Charisma:{self.charisma}")
    def roll_check(self, stat):
        return random.randint(1, 20)+self.stats[stat]

    def save_game(self):
        return {
            "name": self.name,
            "stats": self.stats,
            "favorite_color": self.fav_color,
            "favorite_color_text": self.fav_color_text,
        }
    @classmethod
    def load_game(cls, save_data):
        player = cls(
            name=save_data["name"],
            color=save_data["favorite_color"],
            clr_txt=save_data["favorite_color_text"]
        )
        player.stats = save_data["stats"]
        return player

    def find_action(self, action = None, target =None):
        print("What do you do?")
        choice = input(">>").strip()
        if not choice:
            print("You stand and stare blankly into the room.")
            #action, target = self.find_action(self, action, target)
        else:
            return get_action_target(choice)
        return action, target

    def handle_look(self, description):
        result = self.roll_check("wisdom")
        descriptions = description.split("|")
        checks = result//5
        if checks < len(descriptions):
            checks = len(descriptions)
        for i in range(checks):
            print(descriptions[i])


        return