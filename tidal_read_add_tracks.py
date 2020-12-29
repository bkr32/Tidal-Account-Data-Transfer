import tidalapi
import getpass
from tqdm import tqdm

filepath = 'tidalTracks.txt'

session = tidalapi.Session()
session.login(input('Username: '), getpass.getpass('Password: '))
uid = session.user.id
TidalUser = tidalapi.Favorites(session, uid)
artists = TidalUser.artists()

print('Adding ...')
with open(filepath) as f:
    lines = f.readlines()
    for i in tqdm(range(len(lines))):
        TidalUser.add_track(lines[i])
