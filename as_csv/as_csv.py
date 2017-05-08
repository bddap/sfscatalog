import json
import csv


def lj(fn):
    with open(fn) as f:
        return json.load(f)


def sc(fn, c):
    with open(fn, 'w') as f:
        w = csv.writer(f)
        w.writerows(c)


english = lj('english.json')

legend = ["n", "name", "audio", "page_name",
          "question", "answer", "verseText", "verseLocation"]

for album in english:
    fn = 'to_csv/' + \
        ' '.join(("Vol", str(album['vol']), album['name'])) + '.csv'

    rows = [[song[l] for l in legend] for song in album['songs']]

    sc(fn, [legend] + rows)
