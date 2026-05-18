from song import Song
from playlist import Playlist

playlist = Playlist("My Playlist")

while True:
    print("\n--- MUSIC PLAYLIST ---")
    print("1. Add Song")
    print("2. Show Playlist")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Song title: ")
        artist = input("Artist: ")

        song = Song(title, artist)
        playlist.add_song(song)

    elif choice == "2":
        playlist.show_playlist()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")