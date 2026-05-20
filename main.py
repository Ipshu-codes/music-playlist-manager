from song import Song
from playlist import Playlist

playlists = {}  

current_playlist = None

while True:
    print("\n--- PLAYLIST MANAGER ---")
    print("1. Create Playlist")
    print("2. Select Playlist")
    print("3. Add Song")
    print("4. Remove Song")
    print("5. Show Playlist")
    print("6. Show All Playlists")
    print("7. Exit")

    choice = input("Enter choice: ")

    
    if choice == "1":
        name = input("Enter playlist name: ")

        if name in playlists:
            print("Playlist already exists!")
        else:
            playlists[name] = Playlist(name)
            print(f"Playlist '{name}' created")

    
    elif choice == "2":
        name = input("Enter playlist name to select: ")

        if name in playlists:
            current_playlist = playlists[name]
            print(f"Selected playlist: {name}")
        else:
            print("Playlist not found")


    elif choice == "3":
        if current_playlist is None:
            print("Select a playlist first!")
        else:
            title = input("Song title: ")
            artist = input("Artist: ")

            song = Song(title, artist)
            current_playlist.add_song(song)

    
    elif choice == "4":
        if current_playlist is None:
            print("Select a playlist first!")
        else:
            title = input("Song title to remove: ")
            current_playlist.remove_song(title)

    
    elif choice == "5":
        if current_playlist is None:
            print("Select a playlist first!")
        else:
            current_playlist.show_playlist()

    
    elif choice == "6":
        if not playlists:
            print("No playlists created")
        else:
            print("\nAll Playlists:")
            for name in playlists:
                print("-", name)

    
    elif choice == "7":
        print("Have a blast!")
        break

    else:
        print("Invalid choice")