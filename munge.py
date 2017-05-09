import json

albums = json.load(open("english.json"))

for album in albums:
    for song in album['songs']:
        song['album'] = album['name']
        song['vol'] = album['vol']

categories = [
    {
        "name": "The Nature of God",
        "songs": albums[0]['songs'][:11]  # Vol. 1 #1-11
    },
    {
        "name": "Creation",
        "songs": albums[0]['songs'][11:]  # Vol. 1 #12-22
    },
    {
        "name": "The Fall of Man",
        "songs": albums[1]['songs'][:13]  # Vol. 2 #1-13
    },
    {
        "name": "Salvation",
        "songs": albums[1]['songs'][13:]  # Vol. 2 #14-30
    },
    {
        "name": "Christ and His Work",
        "songs": albums[2]['songs']  # Vol. 3 All songs
    },
    {
        "name": "The Ten Commandments",
        "songs": albums[3]['songs'][:10]  # Vol. 4 #1-10
    },
    {
        "name": "The Bible",
        "songs": albums[3]['songs'][10:]  # Vol. 4 #11-16
    },
    {
        "name": "Prayer",
        "songs": albums[4]['songs'][:10]  # Vol. 5 #1-10
    },
    {
        "name": "The Sacraments",
        "songs": albums[4]['songs'][10:]  # Vol. 5 #11-21
    },
    {
        "name": "Christ and His Return",
        "songs": albums[5]['songs']  # Vol. 6 All songs
    }
]

print(json.dumps(categories))
