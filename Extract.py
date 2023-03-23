import pandas as pd
import requests
from datetime import  datetime
import datetime


class getdata:

    def __init__(self):
        self.USER_ID = "315yoc5kmgplgmb7y47qlshv7ltm"
        self.TOKEN =  "BQBfw7LXSdurudxwXBBrCK_vm_bULN4GKhm79E8HDnwYxjOz3AjK7wnP7XoCxGWJ9MTyfqGHlXsdNCSrWsDf0ubB6IiAOKJa6v4VkmneJpImamccFGWXeEx0LhtzzIQPy2hqXJOG1He5HxUJ-Ye1LRHm8yihskwkWoJoRwTAEP-1D2w6kLm7cQ9eM0EFDp0BMe6HZ-PeFA"
    def extract(self):
        input_variables ={
            "Accept" : "application/json",
            "Content-Type" : "application/json",
            "Authorization" : "Bearer {token}".format(token= self.TOKEN )

        }

        today = datetime.datetime.now()
        yesterday = today - datetime.timedelta(days = 1)
        yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
        


        r = requests.get("https://api.spotify.com/v1/me/player/recently-played?limit=50&after={time}".format(time=yesterday_unix_timestamp), headers = input_variables)
        data = r.json()

        song_name = []
        artist_names = []
        played_at_list = []
        timestaps = []
        timestamps = []
        


        for song in data["items"]:
            song_name.append(song["track"]["name"])
            artist_names.append(song['track']["album"]["artists"][0]['name'])
            played_at_list.append(song["played_at"])
            timestamps.append(song["played_at"][0:10])

        song_dict ={
            "song_name" : song_name,
            "artist_name" : artist_names,
            "played_at" : played_at_list,
            "timestamp" : timestamps
        }
        
        df = pd.DataFrame.from_dict(song_dict, orient='index')
        df = df.transpose()
        return df


if __name__ == '__main__':
    dg = getdata()
    dg.extract()





    

