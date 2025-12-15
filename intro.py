import npc
import game_state
import location

def intro(player, state):
    look_descriptions = {
        'bar': "\nThe air smells of stale alcohol and body odor.|\nThe bar is long, wooden, covered in grime."
               "\nBehind it stands an orcish woman with long black hair and scowl.  She won't meet your eyes."
               "\nThere is a short menu claiming they serve ale, wine and spirits.  They do not have a kitchen.|"
               "\nThe bartender is casting dark looks at a table in the far corner where a human woman sits nursing a drink in a pewter mug."
               "\nThe woman cringes every time  the table to her left gets loud.",
        'tavern': "\nThe dark main room of tavern is dirty.You hope that the stains on the floor are alcohol, but the color is that of "
                  "dried blood.\nThere is a long bar in the back with blocked stairs to its left and a storage room to its right. A handful of patrons"
                  "sit at the dirty tables.|"
                  "\nA drunk gnome nurses a drink at the bar, a group of young wagon guards sit to the left of a pale woman dressed darkly in the corner.  "
                  "The bartender looks less happy to be here than you do.|\nThe storage room in the back holds half open crates, straw spewing from them to"
                  "litter the floor.  A sign on the rope blocking the stairs reads 'PRIVATE', though someone has carved a small 's' at the end.",
        'storage': "\nThe storage room stands to your left, and the bars right.  It has some shelves and half opened crates spewing straw on the floor|"
                   "\nThe room is illuminated by oil lamps, "}
    tavern_door = location.Location("tavern", "You stand in the doorway of a ramshackle tavern in a ramshackle town."
                                            "\nThe room is mostly dark, but motes of dust float on a few bars of light that comes in from the grimy windows."
                                            "\nThere is a long bar in the back of the room, stairs up to the proprietors rooms blocked by"
                                            "a rope\n-a handful of occupied tables\n-an open archway that leads to a storage room "
                                            "in the back.", ["bar", "storage room", "staircase", "tables"])
    tavern_door.can_look_at = ['bar', 'tavern', 'storage', 'stairs', 'tables']
    #bartender = npc.Bartender("Myev", 1, 3)
    #bar = location.Location("bar", "You stand before a long, mahogany bar that likely hasn't seen a good clean in months, if not years."
    #                          "\nThere is a drunk gnome sitting precariously on a stool to your left, and an orcish bartender "
    #                          "\nwho gives you a glare but says nothing.", ["tavern door"])
    state.current_location = tavern_door
    while True:
        tavern_door.describe()
        action, target = player.find_action()
        if not action:
            continue

        if 'bar' in target and 'bar' in state.current_location.can_look_at:
            target = look_descriptions['bar']
        elif ('tavern' in target or 'room' in target) and 'tavern' in state.current_location.can_look_at:
            target = look_descriptions['tavern']
        match action:
            case "look" | "examine" | "l":
                player.handle_look(target)
            case "go" | "move" | "walk":
                pass
            case "talk" | "speak":
                pass
            case "help" | "?":
                pass
            case "quit" | "exit" | "q":
                return
            case _:
                print (f"{action} isn't valid here.  Type 'help' for commands")
