class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song.title}")

    def show_playlist(self):
        print(f"\nPlaylist: {self.name}")

        if not self.songs:
            print("No songs in playlist")
            return

        for i, song in enumerate(self.songs, start=1):
            print(f"{i}. {song.title} - {song.artist}")

    def remove_song(self, title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                self.songs.remove(song)
                print(f"Removed: {song.title}")
                return

        print("Song not found")