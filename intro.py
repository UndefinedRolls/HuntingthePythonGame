from npc import NPC
import location

def create_bartender():
    bartender = NPC("Myev", 1, used_name="Bartender", custom_greeting="What?")
    bartender.personality = "gruff"
    bartender.add_topic_helper(
        topic_id='gnome',
        keywords=['gnome', 'drunk', 'man on barstool', 'regular', 'Vorlin'],
        response=["Ask him yourself.  I ain't your momma.",
                  "Still on about that?  He's a regular.  You leave him alone now.",
                  "He's Vorlin, alright.  Go talk to him and leave me out of it."]
    )
    bartender.add_topic_helper(
        topic_id='woman',
        keywords=['woman', 'trouble'],
        response=["Don't ask about her.  She's trouble.",
                  "She's gotten in over her head, and she's dragging me with her.  Do yourself a favor and leave her be."]
    )
    bartender.add_topic(
        topic_id='name',
        inputs=['name', 'who are you', 'you are'],
        response="What's it to you?",
        set_flag='name_0'
    )
    bartender.add_topic_helper(
        topic_id='name',
        keywords=['name', 'who are you', 'you are'],
        response=[
            "What do you care?",
            "Gods Above, it's Myev, happy now?"
        ]
    )
    bartender.add_topic_helper(
        topic_id="guards",
        keywords=['young men', 'guards', 'card players'],
        response=[
            "Why so many questions?  Order something or get lost.",
            "Insistent much?  They're caravan guards, showed up this morning.",
            "Why don't you just go talk to them."
        ]
    )
    bartender.add_topic(
        topic_id="order",
        inputs=["order", "I'd like", "I want", "give me"],
        response="Yeah, here.  Don't throw up on my bar."
    )
    bartender.topics['name_1']['removes_flag'] = 'name_0'
    return bartender
def create_bar(bartender, gnome):

    bar_descriptions = {
        'bar': "\nThe bar was once quite nice, but now is covered in a layer of alcohol, sweat and dirt that hides any of the beauty it might once have had|"
               "\nA drunk gnome sits on one of the barstools designed for small-folk, nursing a drink.\nIt smells strongly of rye spirit.\nThough it pales"
               "in comparison to the smell of the gnome's breath|The bartender scowls at you, cleaning a glass with a rag probably dirtier that the glass itself.|"
               "\nShe keeps casting looks at a woman sitting at a table in the corner.",
        'tavern': "\nAt you back is a dirty room, filled with less dirty patrons|\nThe door to the street outside has been propped open with an old stone.",
        'storage': "\nThere is a storage room to your right, but you can't see inside from here.",
        'stairs': "\nThere is a staircase to your left, but you can't see much of it from here.",
        'tables': "\nThree of the half dozen tables in the room are filled.|A group of rowdy young guards are playing at cards.  The one in green in winning.|"
                  "\nTwo old men are sharing stories and a drink on the other side of the room.|A young woman sits near the bar, her back to the door.  She casts furtive glances at the bartender.",
        'old men': "\nThe old men give you a smile and raise a glass to you, you think they'd welcome your company.",
        'guards': "\nThe guards are busy with their game, you think the one in red may be cheating.",
        'young woman': "\nThe young woman won't meet your eyes.  From the amount of ale on the table, you think she's probably spilled more than she's drunk||\nShe seems terrified, and keeps looking at the"
                       "bartender, as if for reassurance.",
        'gnome': "\nThe gnome sways slightly in his seat, his eyes half closed.  His breath smells strongly of the drink in front of him.|\n"
                 "You also catch the smell of rotten fish, and body odor from him.  His hair is unwashed but his clothing is expensive, and cleaner than the rest of him.",
        'other': "\nYou can't see that from here."}
    bar = location.Location("bar",
                            "You stand before a long, mahogany bar that likely hasn't seen a good clean in months, if not years."
                            "\nThere is a drunk gnome sitting precariously on a stool to your left, and an orcish bartender "
                            "\nwho gives you a glare but says nothing.", ["tavern door"], bar_descriptions,
                            [bartender, gnome])

    bar.target_aliases = {
        'room': 'bar',
        'main room': 'tavern',
        'stairway': 'stairs',
        'staircase': 'stairs',
        'table': 'tables',
        'card players': 'guards',
        'young men': 'guards',
        'patrons': 'tables',
        'farmers': 'old men',
        'storytellers': 'old men',
        'woman': 'young woman',
        'doorway': 'storage',
        'the back': 'storage',
        'drunk': 'gnome'
    }
    return bar
def create_tables(young_woman, old_men, guards):
    table_descriptions = {
        'young woman': '\nThe woman keeps both hands wrapped tightly around her drink|\nHer face is mostly in shadow,'
                       'but you can see her eyes are closed|\nYou see a small black bag beneath the table tucked'
                       ' between her feet',
        'bag': "\nBetween the young woman's feet sits a small black bag.  Made of leather, the seams are cracked and the "
               "metal handle tarnished||\nThis wear was done purposefully, and artfully; to the casual observer the bad is"
               "old and worn, and not the new, expensive bag it really is.",
        'guards': '\nFive young men sit playing at cards.  Two wear caravan guard coats, the others have theirs hanging on the back of their chairs'
                  '|\nThey all appear to be in their early to mid twenties.  The dealer has long black hair pulled back into '
                  'a tail and dark eyes.  To his right sits a man with close shaved blond hair and deep green eyes.  His nose is crooked,'
                  'as if broken one too many times.  To the left of the dealer is the youngest of the group, a brown haired '
                  'man wearing spectacles wearing his coat with the pride of one who newly earned it.|\nThe other two have their back to the door.  '
                  'The one with his coat one has long brown hair in many braids, he is losing quite spectacularly.  The other'
                  'is the neatest of the bunch, his dark hair greased back on a high forehead.|\nThe youngest man appears to be'
                  'cheating at the game',
        'old men': 'The two old men smile at you and wave you over.  They are well into their cups.'
    }
    tables = location.Location("table", "The tables hold a handful of patrons, a young man keeping to herself in the back,"
                                      " a group of young man playing at cards, and two older gentlemen sharing stories.  The tables"
                                      " are old, a little dirty, and a few have filthy words carved into them.", table_descriptions, [young_woman, old_men, guards])
    tables.target_aliases = {
        'room': 'tables',
        'main room': 'tavern',
        'stairway': 'stairs',
        'staircase': 'stairs',
        'table': 'tables',
        'card players': 'guards',
        'young men': 'guards',
        'patrons': 'tables',
        'farmers': 'old men',
        'storytellers': 'old men',
        'woman': 'young woman',
        'doorway': 'storage',
        'the back': 'storage',
        'drunk': 'gnome'g
    }
    return tables

def create_tavern():
    tavern_descriptions = {
        'bar': "\nThe bar is long, wooden, covered in grime.|"
               "\nThere is a gnome leaning over the bar, perched on a barstool raised for his height.  The orc bartender stands behind the bar cleaning a glass with a rag.|"
               "\nThe rag is likely dirtier than the glass, though, so maybe its more that the bartender is cleaning the rag with the glass.",
        'tavern': "\nThe air smells of stale alcohol and body odor.|\nThe dark main room of tavern is dirty.You hope that the stains on the floor are alcohol, but the color is that of "
                  "dried blood.\nThere is a long bar in the back with blocked stairs to its left and a storage room to its right. A handful of patrons"
                  "sit at the dirty tables.|"
                  "\nA staircase climbs into darkness on your right, and an open door shows a storage room to your left.",
        'storage': "\nThe storage room stands to your left, and the bars right.  It has some shelves and half opened crates spewing straw on the floor|"
                   "\nThe room is illuminated by oil lamps|\nThe walls behind the lamps are stained black with creosote.",
        'stairs': "\nThe stairway is dark, and blocked by a rope with a sign hanging from it.| The wooden sign attached to the road has 'PRIVATE' burned into it.|"
                  "\nSomeone has carved a small 's' at the end of the word",
        'tables': "A lone woman sits at a table in a far corner.  A group of young men sit to her left playing at cards, and a couple of old farmers are drinking ale and telling stories on the far side.|"
                  "The old men smile at you as you look at them, their faces darked with long hours in the sun.  They're probably quite a bit younger than they look.|\nThe young men playing at cards"
                  "are dressed like wagon guards, their side arms hung from holsters on the back of their chairs.  The one in blue is winning.|\nThe young woman is trying to keep herself in the shadows, her back to you.",
        'old men': "\nYou'll need to get closer to see anything about the old men telling stories.",
        'guards': "\nYou can't see much of the card game the men playing from here.",
        'young woman': "\nWith her back to you, you can't tell anything about the woman.",
        'other': "\nYou can't see that from here"}
    tavern_door = location.Location("tavern", "You stand in the doorway of a ramshackle tavern in a ramshackle town."
                                            "\nThe room is mostly dark, but motes of dust float on a few bars of light that comes in from the grimy windows."
                                            "\nThere is a long bar in the back of the room, stairs up to the proprietors rooms blocked by"
                                            "a rope\n-a handful of occupied tables\n-an open doorway that leads to a storage room "
                                            "in the back.", ["bar", "storage room", "staircase", "tables"], tavern_descriptions)

    tavern_door.target_aliases = {
        'storage room': 'storage',
        'room': 'tavern',
        'main room': 'tavern',
        'bartender': 'bar',
        'stairway': 'stairs',
        'staircase': 'stairs',
        'table': 'tables',
        'card players': 'guards',
        'young men': 'guards',
        'patrons': 'tables',
        'farmers': 'old men',
        'storytellers': 'old men',
        'woman': 'young woman',
        'doorway': 'storage',
        'the back': 'storage',
        'bar': 'bar'
    }
    return tavern_door
def create_gnome():
    gnome = NPC("Vorlin", 0)
    gnome.personality = "neutral"

    gnome.add_topic(
        topic_id="bartender",
        inputs=["bartender", "Myev", "orc"],
        response="Ah, she's the best.  Always keeps the good stuff for me."
    )
    gnome.add_topic(
        topic_id="woman",
        inputs=["woman"],
        response="Seen her 'round.  Heard she killed a man."
    )
    gnome.add_topic(
        topic_id="killed a man",
        inputs=["who did she kill", "killed who", "killed a man"],
        response="You'll have to ask her.  Its all just rumor."
    )
    gnome.add_topic(
        topic_id="guards",
        inputs=["young man", "guards", "card players"],
        response="Oh, I don't know.  They're new.  Showed up today.  Seem friendly enough."
    )
    return gnome
def create_woman():
    woman = NPC("Maya", 1)
    woman.personality = "scared"

def intro(player, state):


    tavern_door = create_tavern()
    bartender = create_bartender()
    gnome = create_gnome()
    bar = create_bar(bartender, gnome)
    young_woman = create_woman()
    tables = create_tables()
    state.npcs = {"bartender": bartender, "gnome": gnome}
    for npcs in bar.npc:
        state.npcs[npcs.name] = npcs
    for npcs in tavern_door.npc:
        state.npcs[npcs.name] = npcs

    places_available = {'bar': bar, 'tavern': tavern_door}
    state.current_location = tavern_door
    while True:
        state.current_location.describe()
        action, target = player.find_action()
        if not action:
            continue


        match action:
            case "look" | "examine" | "l":
                if not target:
                    state.current_location.describe()
                else:
                    normalized_target = state.current_location.normalize_target(target)
                    player.handle_look(state.current_location.can_look_at[normalized_target])
            case "go" | "move" | "walk":
                if target == state.current_location.name:
                    print("You are already there.")
                elif target not in places_available:
                    print("You can't reach there from here.")
                else:
                    state.move_to(places_available[target])
            case "talk" | "speak":
                npc = state.normalize_target(target)
                if npc == 'other':
                    print('There is no one like that here to talk to.')
                else:
                    npc.talk(player, state)
            case "help" | "?":
                pass
            case "quit" | "exit" | "q":
                return
            case _:
                print (f"{action} isn't valid here.  Type 'help' for commands")
