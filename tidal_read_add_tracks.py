import tidalapi
from tqdm import tqdm

filepath = 'tidalTracks.txt'

session = tidalapi.Session()
session.login_oauth_simple()
uid = session.user.id
TidalUser = tidalapi.Favorites(session, uid)
artists = TidalUser.artists()

print('Adding ...')
with open(filepath) as f:
    lines = f.readlines()
    for i in tqdm(range(len(lines))):
        TidalUser.add_track(lines[i])
