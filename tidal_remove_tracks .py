session = tidalapi.Session()
session.login('user1', 'pass1')
uid = session.user.id
TidalUser = tidalapi.Favorites(session, uid)
artists = TidalUser.artists()

session2 = tidalapi.Session()
session2.login('user2','pass2')
uid2 = session2.user.id
TidalUser2 = tidalapi.Favorites(session2, uid2)
tracks = TidalUser2.tracks()

print(session2)
for track in tracks:
    TidalUser2.remove_track(track.id)
    print(track.id)