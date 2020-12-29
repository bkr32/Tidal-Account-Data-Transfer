import tidalapi
import getpass
from tqdm import tqdm

session = tidalapi.Session()
print('Enter your credentials for the account you want to transfer from')
session.login(input('Username: '), getpass.getpass('Password: '))
uid = session.user.id
TidalUser = tidalapi.Favorites(session, uid)
artists = TidalUser.artists()

session2 = tidalapi.Session()
print('Enter your credentials for the account you want to transfer to')
session2.login(input('Username: '), getpass.getpass('Password: '))
uid2 = session2.user.id
TidalUser2 = tidalapi.Favorites(session2, uid2)
tracks = TidalUser2.tracks()

print('Removing ...')
for i in tqdm(range(len(tracks))):
    TidalUser2.remove_track(tracks[i].id)
