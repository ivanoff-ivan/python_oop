class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return f"Cannot add songs. Album is published."
        elif song in self.songs:
            return f"Song is already in the album."
        self.songs.append(song)  #
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        song = [x for x in self.songs if x.name == song_name]
        if self.published:
            return f"Cannot remove songs. Album is published."
        elif song_name not in map(lambda s: s.name, self.songs):
            return f"Song is not in the album."
        self.songs.remove(next(filter(lambda s: s.name == song_name, self.songs)))
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        data = f"Album {self.name}\n"
        for s in self.songs:
            data += f"== {s.get_info()}\n"
        return data
