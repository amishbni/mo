import sys
from mutagen.easyid3 import EasyID3

def metadata(filepath):
    audio = EasyID3(filepath)
    brief_statement = f"artist: {audio['artist'][0]}\n"
    brief_statement += f"title: {audio['title'][0]}\n"
    brief_statement += f"album: {audio['album'][0]}\n"
    brief_statement += f"genre: {audio['genre'][0]}\n"
    brief_statement += f"date: {audio['date'][0]}"

    return brief_statement

def main():
    args = sys.argv
    if(len(args) == 1):
        print("MO, the Musicophile Owl!")
    elif(len(args) == 2):
        print("Playing...")
    else:
        print(metadata(args[1]))

if __name__ == "__main__":
    main()

