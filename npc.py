class NPC:
    def __init__(self, name="Civilian", pronouns=0, custom_greeting=None, custom_farewell=None, used_name="???"):
        self.name = name
        self.used_name = used_name
        self.pronouns = pronouns
        self._set_pronouns()
        self.topics = {}
        self.flags = set()
        self.personality = "neutral"
        self.custom_greeting = custom_greeting
        self.custom_farewell = custom_farewell
        self._set_default_responses()

    def _set_name(self):
        if 'knows_name' in self.flags:
            self.used_name = self.name

    def _set_pronouns(self):
        match self.pronouns:
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

    def add_topic(self,topic_id, inputs, response, required=None, set_flag=None, remove_flag=None, repeatable=False):
        if not isinstance(inputs, list):
            inputs = [inputs]
        if not required:
            required = []
        self.topics[topic_id] = {
            'topic_id': topic_id,
            'keywords': inputs,
            'response': response,
            'requires': required,
            'sets_flag': set_flag,
            'removes_flag': remove_flag,
            'repeatable': repeatable
        }
    def _greeting(self):
        greetings = {
            'neutral': f"Hello. Do you need something?",
            'friendly': f"Hello there!",
            'gruff': f"Yes?  What?"
        }
        if self.custom_greeting:
            return self.custom_greeting
        else:
            return greetings[self.personality]


    def _farewell(self):
        farewells= {
            'neutral': 'Bye, then',
            'friendly': 'Goodbye!',
            'gruff': 'Whatever.'
        }
        if self.custom_farewell:
            return self.custom_farewell
        else:
            return farewells[self.personality]


    def _set_default_responses(self):
        self.add_topic(
            topic_id = 'greetings',
            inputs = ['hello', 'hi', 'hey', 'greetings'],
            response = lambda npc, text, state: self._greeting()
        )

        self.add_topic(
            topic_id = 'farewell',
            inputs = ['bye', 'goodbye', 'farewell'],
            response = lambda npc, text, state: self._farewell()
        )

        self.add_topic(
            topic_id = 'name',
            inputs = ['name', 'who are you', 'you are'],
            response = lambda npc, text, state: f"I'm {self.name}",
            set_flag = "knows_name"
        )

    def _default_answer(self):
        default = [
            "I don't understand",
            "What?",
            "I'm not sure what you want.",
            "Do you want something from me?"
        ]
        return default[len(self.flags)%len(default)]

    def determine_response(self, text, state):
        match = None
        exits = False
        for id_, topic in self.topics.items():
            if any(word in text for word in topic['keywords']):
                if all(required in self.flags for required in topic['requires']):
                    match = topic
                    if 'bye' in topic['keywords']:
                        exits = True
                    break

        if not match:
            return self._default_answer(), exits

        response = match['response']
        if callable(response):
            response = response(self, text, state)

        if match['sets_flag']:
            self.flags.add(match['sets_flag'])

        if match['removes_flag']:
            self.flags.discard(match['removes_flag'])
        if not match['repeatable']:
            del self.topics[match['topic_id']]
        return response, exits

    def talk(self, player, state):
        print(f"You begin speaking with {self.used_name}")
        while True:
            question = input(f"{player.name}>>").lower().strip()

            response, exits = self.determine_response(question, state)

            print(f"{self.name}: {response}")
            if exits:
                return

    def save_game(self):
        return {
            "name": self.name,
            "pronouns": self.pronouns,
        }
    def add_topic_helper(self, topic_id, keywords, response):
        for index, text in enumerate(response):
            new_id = f"{topic_id}_{index+1}"
            requires = None if index==0 else f"{topic_id}_{index}"
            sets_flag = new_id
            removes_flag = f"{topic_id}_{index}" if index > 0 else None

            self.add_topic(
                topic_id = new_id,
                inputs = keywords,
                response = text,
                required = requires,
                set_flag = sets_flag,
                remove_flag = removes_flag
            )
        last_id = f"{topic_id}_{len(response)-1}"
        self.topics[last_id]["repeatable"] = True

    @classmethod
    def load_game(cls, save_data):
        return cls(
            name=save_data["name"],
            pronouns=save_data["pronouns"],
        )
