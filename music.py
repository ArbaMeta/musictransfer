import requests
import json
from gmusicapi import Mobileclient
import getpass
from tqdm import tqdm

class Music:
    isRunning = True

    def __init__(self):
        self.token = self.getToken()
        self.getCred()
        self.readFile()

    def chunks(self, l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def getToken(self):
        data = {"grant_type": "client_credentials"}
        auth = b"Basic OGExNTNkNjYxNjliNDBmYmJmNGEzYzAwNDMxMDA4Mzg6ZjRjNWY4NWQ0ZTE2NDI2MDg2NTYzM2FkOTY5MWI4NWI="

        result = requests.post("https://accounts.spotify.com/api/token", data=dict(grant_type="client_credentials"), headers={"Authorization": auth})
        result = json.loads(result.content)

        return result["access_token"]

    def readFile(self):
        tracks = []
        
        with open("spotify.txt") as f:
            for line in f:
                trackId = line[31:].rstrip()
                tracks.append(trackId)

        print("Found", len(tracks), "songs")
        
        self.getInfo(list(self.chunks(tracks, 30)))

    def getInfo(self, data):
        print("Getting info from Spotify")
        songs = []

        auth = "Bearer " + self.token

        for item in data:
            tracks = ",".join(item)
            url = "https://api.spotify.com/v1/tracks?ids=" + tracks
            
            resp = requests.get(url, headers={"Authorization": auth})
            data = json.loads(resp.text)

            for track in data["tracks"]:
                song = track["name"] + " " + track["artists"][0]["name"] + " " + track["album"]["name"]
                
                songs.append(song)

        self.searchSongs(songs)

    def getCred(self):
        with open('credentials.json', 'r+') as data:    
            cred = json.load(data)

            if cred["username"] == None:
                cred["username"] = input("Your Google Email please: ")
                cred["password"] = getpass.getpass(prompt='And Your Password: ')

                data.seek(0)
                json.dump(cred, data)
                data.truncate()

                self.login(cred)
            else:
                self.login(cred)

    def login(self, cred):
        print("Loging In")
        self.api = Mobileclient()
        self.user = self.api.login(cred["username"], cred["password"], Mobileclient.FROM_MAC_ADDRESS)

    def searchSongs(self, songs):
        trackIds = []

        for song in tqdm(songs, desc="Searching Google Music"):
            result = self.api.search(song)

            if result["song_hits"]:
                trackIds.append(result["song_hits"][0]["track"]["storeId"])

        self.main(trackIds)

    def main(self, songs):

        while self.isRunning:
            print('==============')
            command = input("Add, Album Name or Quit?\n>>> ")
            print('==============')

            if command == "Add":
                self.addMusic(songs)
            elif command == "Quit" or command == "quit":
                self.isRunning = False
            else:
                self.addToPlaylist(songs, command)

            print("\u001b[38;5;76mDone!\u001b[0m")
            self.isRunning = False

    def addMusic(self, songs):
        self.api.add_store_tracks(songs)

    def addToPlaylist(self, songs, name):
        playlist = self.api.create_playlist(name)
        data = self.api.add_songs_to_playlist(playlist, songs)