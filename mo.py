import argparse

def main():
    parser = argparse.ArgumentParser(description="MO, the Musicophile Owl", prog="mo")
    parser.add_argument("-p", "--play", nargs=1, help="play an audio file")
    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()

