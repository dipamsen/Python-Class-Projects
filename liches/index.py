import requests
import bz2

x = requests.get(
    "https://database.lichess.org/standard/lichess_db_standard_rated_2020-10.pgn.bz2")
with open('games.bz2', 'wb') as f:
    f.write(x.content)
