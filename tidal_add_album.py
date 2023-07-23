import tidalapi, os
from tqdm import tqdm

session = tidalapi.Session()
print('Enter your credentials for the account you want to transfer from')
session.login_oauth_simple()
uid = session.user.id
TidalUser = tidalapi.Favorites(session, uid)
albums = TidalUser.albums()

session2 = tidalapi.Session()
print('Enter your credentials for the account you want to transfer to')
session2.login_oauth_simple()
uid2 = session2.user.id
TidalUser2 = tidalapi.Favorites(session2, uid2)

print('Copying')
for i in tqdm(range(len(albums))):
    try:
        TidalUser2.add_album(albums[i].id)
    except:
        print('Skipped', albums[i].name, 'by' , albums[i].artist.name)

os.system("pause")
