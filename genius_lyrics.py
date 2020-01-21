from lyricsgenius import Genius
from colorama import init, Fore, Style
from mutagen.easyid3 import EasyID3
from genius_tokens import CLIENT_ACCESS_TOKEN
import sys

args = sys.argv

if len(args) == 1:
    print("Specify path to audio")
    exit(1)

audio_path = args[1]
audio = EasyID3(audio_path)

genius = Genius(CLIENT_ACCESS_TOKEN)
genius.verbose = False
genius.remove_section_headers = True
song = genius.search_song(audio["title"][0], audio["artist"][0])

print(song.lyrics)
