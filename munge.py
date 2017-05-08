import json


def lj(fn):
    with open(fn) as f:
        return json.load(f)


def sj(fn, j):
    with open(fn, 'w') as f:
        return json.dump(j, f)


def jd(j):
    return json.dumps(j, indent=2)


english = lj('english.json')

everysong = [song for album in english for song in album['songs']]

for song in everysong:
    qa = song['qa']

    # Get the question.
    song['question'] = ';'.join(a['q'] for a in qa if 'q' in a.keys())
    if song['question'] == '':
        song['question'] = None
        # print('question is None for', '\n', jd(song['qa']))

    # Get the Answer.
    song['answer'] = '\n'.join(a['a'] for a in qa if not 'v' in a.keys())
    if song['answer'] == '':
        song['answer'] = None
        # print('answer is None for', '\n', jd(song['qa']))

    # Get the verse text.
    song['verseText'] = ';'.join(a['a'] for a in qa if 'v' in a.keys())
    if song['verseText'] == '':
        song['verseText'] = None
        # print('verseText is None for', '\n', jd(song['qa']))

    # Get the verse Location.
    song['verseLocation'] = ';'.join(a['v'] for a in qa if 'v' in a.keys())
    if song['verseLocation'] == '':
        song['verseLocation'] = None
        # print('verseLocation is None for', '\n', jd(song['qa']))
    
    del song['qa']

print(jd(english))