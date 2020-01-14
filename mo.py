import sys
from mutagen.easyid3 import EasyID3

def version():
    print("0.0.1")

def tags(filepath):
    audio = EasyID3(filepath)
    brief_statement = f"artist: {audio['artist'][0]}\n"
    brief_statement += f"title: {audio['title'][0]}\n"
    brief_statement += f"album: {audio['album'][0]}\n"
    brief_statement += f"genre: {audio['genre'][0]}\n"
    brief_statement += f"date: {audio['date'][0]}"

    print(brief_statement)

def show(args):
    actions = {
        "tags": tags,
        "version": version
    }
    if len(args) == 0:
        print("Show what, exactly?")
    else:
        action = args[0]
        if action in actions:
            if len(args) == 1:
                actions[action]()
            elif len(args) == 2:
                actions[action](args[1])
            else:
                print("Show tags for which audio, exactly?")
                exit(1)
        else:
            print(f"I haven't been trained to show {action}.")
            exit(1)

def main():
    args = sys.argv
    actions = {
        "show": show
    }
    if len(args) == 1:
        print("MO, the Musicophile Owl!")
    else:
        action = args[1]
        if action in actions:
            actions[action](args[2:])
        else:
            print(f"I haven't been trained to {action}.")
            exit(1)

if __name__ == "__main__":
    main()

