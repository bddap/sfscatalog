import json
import csv


def lj(fn):
    with open(fn) as f:
        return json.load(f)


def sc(fn, c):
    with open(fn, 'w') as f:
        w = csv.writer(f)
        w.writerows(c)


categories = lj('categories.json')

legend = ["n", "name", "audio", "page_name", "question",
          "answer", "verseText", "verseLocation", "album", "vol"]

for cat in categories:
    fn = 'as_csv/' + cat['name'] + '.csv'

    rows = [[song[l] for l in legend] for song in cat['songs']]

    sc(fn, [legend] + rows)
