from pprint import pprint
from mutagen.easyid3 import EasyID3

pprint(list(EasyID3.valid_keys.keys()))
