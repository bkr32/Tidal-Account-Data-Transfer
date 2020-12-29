import tidalapi
filepath = 'tidalTracks.txt'

session = tidalapi.Session()
session.login('user','pass')
uid = session.user.id
TidalUser = tidalapi.Favorites(session, uid)
artists = TidalUser.artists()

with open(filepath) as fp:
    cnt = 1
    for artist in fp:
        print(artist)
        TidalUser.add_track(artist)
        print(artist.id)
        cnt += 1
        