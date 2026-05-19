from song import Song
from playlist import Playlist

playlist = Playlist("My Playlist")

while True:
    print("\n--- MUSIC PLAYLIST ---")
    print("1. Add Song")
    print("2. Show Playlist")
    print("3. Remove Song")
    print("4. Save Playlist")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Song title: ")
        artist = input("Artist: ")

        song = Song(title, artist)
        playlist.add_song(song)

    elif choice == "2":
        playlist.show_playlist()

    elif choice == "3":
        title = input("Enter song title to remove: ")
        playlist.remove_song(title)

    elif choice == "4":
        with open("playlist.txt", "w") as file:
            for song in playlist.songs:
                file.write(f"{song.title} - {song.artist}\n")

        print("Playlist saved to playlist.txt")

    elif choice == "5":
        print("Have a blast!")
        break

    else:
        print("Invalid choice")