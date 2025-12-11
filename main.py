import character
import webcolors
import sys
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

def main():
    char_name = input(f"What is you name?\n" )
    char_color, clr_txt = parse_color(input(f"What is your favorite color?\n" ))
    char_wsv = input(f"What is the wind speed velocity of a laden swallow?\n")

    if "african or european swallow" in char_wsv.lower() or char_wsv == "":
        pass
    else:
        print("Before you're quest even begins, it ends.")
        sys.exit()

    new_player = character.Player(char_name, char_color, clr_txt)
    print(new_player)

if __name__ == '__main__':
    main()