class NPC:
    def __init__(self, name="Civilian", pronouns=0):
        self.name = name
        match pronouns:
            case 0:
                self.subject = "HE"
                self.object = "HIM"
                self.possessive = "HIS"
                self.reflective = "HIMSELF"
            case 1:
                self.subject = "SHE"
                self.object = "HER"
                self.possessive = "HER"
                self.reflective = "HERSELF"
            case 2:
                self.subject = "THEY"
                self.object = "THEM"
                self.possessive = "THEIR"
                self.reflective = "THEMSELVES"

    def talk(self, target, player):
        pass
        #defined in subclass

class Bartender(NPC):
    def __init__(self, name="John",  pronouns=0, personality = 0):
        self.personality = personality
        self.topics = []
        self.state = "introduction"
        if "name" in self.topics:
            self.used_name = self.name
        else:
            self.used_name = "Bartender"
        super().__init__(name, pronouns)
        self.responses = {
            "introduction":
                [(None), [f"{self.object.capitalize()} nods at you once, then returns to what they were doing.",
                        f"{self.used_name}: 'Welcome! Have a seat, what can I get you?",
                        f"{self.object.capitalize()} scowls across the bar.  You ordering or what?"]],
            "menu":
            [("order", "can i have", "i would like"), [f"{self.used_name}: A-yup.  Leave the coins on the bar.",
                                                       f"{self.used_name}: Coming right up!",
                                                       f"{self.used_name}: Coins first"]],
            "name":
        [("your name", "who are you", "you are"), [f"{self.used_name}: {self.name}.  Please to meet you.",
                                                   f"{self.used_name}: I'm {self.name}!  Pleasure!",
                                                   f"{self.used_name}: What's it to you?  {self.name} if you must know."]]}


    def talk(self, target, player):
        responses = self.responses[self.state]
        if responses is None and self.state == "introduction":
            print(responses[1][self.personality])
        elif target in responses[0]:
            print(responses[1][self.personality])