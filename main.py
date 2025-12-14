import character
import webcolors
import sys
import intro
from game_state import GameState
from datetime import datetime
import json

def save_game(player, game_state, filename="save.json"):
    save_data = {
        "version": "0.1",
        "timestamp": datetime.now().isoformat(),
        "player": player.save_game(),
        "game_state": game_state.save_game(),
    }
    with open(filename, "w") as f:
        json.dump(save_data, f, indent=4)

def load_game(filename="save.json"):
    with open(filename, "r") as f:
        data = json.load(f)

    player = Player.load_game(data["player"])
    game_state = GameState.load_game(data["game_state"])
    return player, game_state

def parse_color(color):
    color = color.replace(" ", "").lower()
    try:
        hex_ = color.lstrip("#")
        int(hex_, 16)
        return f"#{hex_}", None
    except ValueError:
        pass

    try:
        hex_ = webcolors.name_to_hex(color.lower())
        return hex_, None
    except ValueError:
        return "#000000", color
def create_character():
    char_name = input(f"What is you name?\n")
    char_color, clr_txt = parse_color(input(f"What is your favorite color?\n"))
    char_wsv = input(f"What is the wind speed velocity of a laden swallow?\n")

    if "african or european swallow" in char_wsv.lower() or char_wsv == "":
        pass
    else:
        print("Before you're quest even begins, it ends.")
        sys.exit()

    new_player = character.Player(char_name, char_color, clr_txt)
    print(repr(new_player))
    return new_player
def menu(save_data):
    if save_data:
        show_continue = "Continue"
    else:
        show_continue = "No Save Found"

    print(f"/^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  \n"
          f"|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|  \n"
          f"| |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  \n"
          f"|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|  \n"
          f"| |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  \n"
          f"| |==| |==| |==| |==| |==| |==| |==| |==| |==| |==| |==| |==| |==| |==| |==| |  \n"
          f"              ╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐   ╔╦╗┬─┐┌─┐┬  ┬┌─┐┬  ┌─┐┬─┐                 \n"
          f"              ║║║├┤ │  │  │ ││││├┤     ║ ├┬┘├─┤└┐┌┘├┤ │  ├┤ ├┬┘                 \n"
          f"              ╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘┘   ╩ ┴└─┴ ┴ └┘ └─┘┴─┘└─┘┴└─                 \n"
          f"/^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  /^\\  \n"
          f"|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|==|^|  \n"
          f"| |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  \n"
          f"|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|--|o|  \n"
          f"| |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  \n"
          f"| |==| |==| |==| |==| |==| |==| |==| |==| |==| |==| |==| |==| |==| |==| |==| |  \n"
          f"       ··············                                                           \n"
          f"       :    MENU    :                                                           \n"
          f"       ··············                                                           \n")
    print(f"1: New Game\n"
          f"2: {show_continue}\n"
          f"3: Exit")
    return input(">>")

def main(save_data=None):
    choice = menu(save_data)
    match choice:
        case "1":
            print("Create your character")
            player = create_character()
            intro.intro(player)
            game_state = GameState(player)

        case "2":
            if save_data:
                player, game_state = load_game()add
            else:
                pass
        case "3":
            sys.exit()

if __name__ == '__main__':
    main()