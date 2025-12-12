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

def intro(player):
    print("You stand in the doorway of a ramshackle tavern in a ramshackle town.  The room is "
    "mostly dark, but motes of dust float on a few bars of light that comes in from the grimy windows."
    "  There is a long bar in the back of the room, stairs up to the proprietors rooms blocks by "
          " a rope, a handful of occupied tables, and an open archway that leads to a storage room "
          "in the back.")

    while True:
        print("What do you do?")
        choice = input(">>").strip()
        if not choice:
            print("You stand and stare blankly into the room.  The room quiets for a moment "
                  "wondering what you are doing, then everyone goes back to what they"
                  "were doing.")
            continue

        action, target = get_action_target(choice)
        current_location = "door"
        match action:
            case "look" | "examine" | "l":
                handle_look(player, target, current_location)
            case "go" | "move" | "walk":
                handle_move(player, target, current_location)
                if "bar" in target or "bartender" in target:
                    current_location = "bar"
            case "talk" | "speak":
                handle_talk(player, target, current_location)
            case "help" | "?":
                show_help()
            case "quit" | "exit" | "q":
                return "quit"
            case _:
                print (f"{action} isn't valid here.  Type 'help' for commands")

def handle_look(player, target, current_location):
    result = player.roll_check("wisdom")

    if result > 5:
        print("\nThe air smells of stale alcohol and body odor.")
    if "bar" in target or "bartender" in target:
        if result > 10:
            print("The bar is long, wooden, covered in grime.  Behind it stands an orcish woman"
                      " with long black hair and scowl.  She won't meet your eyes.  There is a short "
                      "menu claiming they serve ale, wine and spirits.  They do not have a kitchen.")
        if result > 15:
            print("The bartender is casting dark looks at a table in the far corner where a "
                      "human woman sits nursing a drink in a pewter mug.  She cringes every time "
                      "the table to her left gets loud.")
    elif result > 15:
        print("You notice the bartender casting dark looks at a corner table.")

    print("You see:\n"
          "- A long bar in the back\n"
          "- Stairs blocked by a rope\n"
          "- Several occupied tables\n"
          "- An archway to a storage room\n")
    return
def handle_move(player, target, current_location):
    if "bar" in target or "bartender" in target:
        print("You step up to the bar.  The orc bartender sneers at you. There is a very drunk dwarf"
              "sitting unsteadily on a stool in front of her.")
    return

def handle_talk(player, target, current_location):
    if current_location == "bar":
        if "bartender" in target:
            print("What d'ya want?  We got what's on the sign.  And nothin' else.")