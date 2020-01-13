import argparse
from mutagen.easyid3 import EasyID3

def metadata(option, filepath):
    audio = EasyID3(filepath)
    print(f"{audio[option]}")

def main():
    parser = argparse.ArgumentParser(description="MO, the Musicophile Owl", prog="mo")
    parser.add_argument("--tags", nargs='+', help="show tags of an audio file")
    args = vars(parser.parse_args())

    if(args["tags"]):
        metadata(args["tags"][0], args["tags"][1])

if __name__ == "__main__":
    main()

