import sys, github
from mutagen.easyid3 import EasyID3
from colorama import Fore, Style, init

def version(args):
    print(github.version())

def tags(args):
    if len(args) == 1:
        print(f"Show {Fore.BLUE}{args[0]}{Style.RESET_ALL} for which audio, exactly?")
        exit(1)
    else:
        filepath = args[1]

    try:
        audio = EasyID3(filepath)
    except Exception:
        print("I can't read that audio, are you sure you provided the path correctly?")
        exit(1)
    brief_statement = f"artist: {audio['artist'][0]}\n"
    brief_statement += f"title: {audio['title'][0]}\n"
    brief_statement += f"album: {audio['album'][0]}\n"
    brief_statement += f"genre: {audio['genre'][0]}\n"
    brief_statement += f"date: {audio['date'][0]}"

    print(brief_statement)

def show(args):
    actions = {
        "tags": tags,
        "artist": tags,
        "version": version
    }
    if len(args) == 0:
        print("Show what, exactly?")
        exit(1)
    else:
        action = args[0]
        if action in actions:
            actions[action](args)
        else:
            print(f"I haven't been trained to show {Fore.RED}{action}{Style.RESET_ALL}.")
            exit(1)

def main():
    init()
    args = sys.argv
    actions = {
        "show": show
    }
    if len(args) == 1:
        print(f"{Fore.MAGENTA}MO, the Musicophile Owl!{Style.RESET_ALL}")
    else:
        action = args[1]
        if action in actions:
            actions[action](args[2:])
        else:
            print(f"I haven't been trained to {Fore.RED}{action}{Style.RESET_ALL}.")
            exit(1)

if __name__ == "__main__":
    main()

