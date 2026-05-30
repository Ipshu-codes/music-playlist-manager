from song import Song
from playlist import Playlist
import random
import os
import json

playlists = {}

current_playlist = None



def save_playlists(playlists):

    data = {}

    for playlist_name, playlist in playlists.items():

        data[playlist_name] = []

        for song in playlist.songs:

            data[playlist_name].append({
                "title": song.title,
                "artist": song.artist
            })

    with open("playlists.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Playlists saved successfully!")


def load_playlists():

    playlists = {}

    try:
        with open("playlists.json", "r") as file:

            data = json.load(file)

            for playlist_name, songs in data.items():

                playlist = Playlist(playlist_name)

                for song_data in songs:

                    song = Song(
                        song_data["title"],
                        song_data["artist"]
                    )

                    playlist.add_song(song)

                playlists[playlist_name] = playlist

    except FileNotFoundError:
        pass

    return playlists


playlists = load_playlists()


while True:
    print("\n--- PLAYLIST MANAGER ---")
    print("1. Create Playlist")
    print("2. Select Playlist")
    print("3. Add Song")
    print("4. Remove Song")
    print("5. Show Playlist")
    print("6. Show All Playlists")
    print("7. Save All Playlists")
    print("8. Search Song")
    print("9. Shuffle Playlist")
    print("10. Exit")

    choice = input("Enter choice: ")

    
    if choice == "1":

        try:
            name = input("Enter playlist name: ")

            if name in playlists:
                print("Playlist already exists!")
            else:
                playlists[name] = Playlist(name)
                print(f"Playlist '{name}' created")

        except:
            print("Error creating playlist")

    
    elif choice == "2":

        try:
            name = input("Enter playlist name to select: ")

            if name in playlists:
                current_playlist = playlists[name]
                print(f"Selected playlist: {name}")
            else:
                print("Playlist not found")

        except:
            print("Error selecting playlist")

   
    elif choice == "3":

        try:
            if current_playlist is None:
                print("Select a playlist first!")
            else:
                title = input("Song title: ")
                artist = input("Artist: ")

                song = Song(title, artist)

                current_playlist.add_song(song)

        except:
            print("Error adding song")

    
    elif choice == "4":

        try:
            if current_playlist is None:
                print("Select a playlist first!")
            else:
                title = input("Song title to remove: ")

                current_playlist.remove_song(title)

        except:
            print("Error removing song")

  
    elif choice == "5":

        try:
            if current_playlist is None:
                print("Select a playlist first!")
            else:
                current_playlist.show_playlist()

        except:
            print("Error showing playlist")

    
    elif choice == "6":

        try:
            if not playlists:
                print("No playlists created")
            else:
                print("\nAll Playlists:")

                for name in playlists:
                    print("-", name)

        except:
            print("Error displaying playlists")

    
    elif choice == "7":

        try:
            save_playlists(playlists)

        except:
            print("Error saving playlists")

    elif choice == "8":

        try:
            if current_playlist is None:
                print("Select a playlist first!")

            else:
                search = input("Enter song title to search: ")

                found = False

                for song in current_playlist.songs:

                    if search.lower() in song.title.lower():

                        print(f"Found: {song.title} - {song.artist}")

                        found = True

                if not found:
                    print("Song not found")

        except:
            print("Error searching song")

    
    elif choice == "9":

        try:
            if current_playlist is None:
                print("Select a playlist first!")

            else:
                random.shuffle(current_playlist.songs)

                print("Playlist shuffled!")

        except:
            print("Error shuffling playlist")

    
    elif choice == "10":

        save_playlists(playlists)

        print("Goodbye!")
        break

    else:
        print("Invalid choice")