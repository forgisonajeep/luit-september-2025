
import os

folder = '/Users/killa/Documents/GitHub/luit-september-2025'

entries = os.scandir(folder)

for entry in entries:
    print(entry.name)