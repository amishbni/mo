import argparse
from mutagen.easyid3 import EasyID3

def metadata(filepath):
    audio = EasyID3(filepath)
    print(f"{audio['artist'][0]} - {audio['title'][0]}")

def main():
    parser = argparse.ArgumentParser(description="MO, the Musicophile Owl", prog="mo")
    parser.add_argument("--info", nargs=1, help="show information of an audio file")
    args = vars(parser.parse_args())

    if(args["info"]):
        metadata(args["info"][0])

if __name__ == "__main__":
    main()

