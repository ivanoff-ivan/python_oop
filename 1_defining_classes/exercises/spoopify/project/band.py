from spoopify.project.song import Song
from spoopify.project.album import Album

class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        try:
            album = [a for a in self.albums if a.name == album_name][0]
            if album.published:
                return f"Album has been published. It cannot be removed."
            self.albums.remove(album)
            return f"Album {album.name} has been removed."
        except:
            return f"Album {album_name} is not found."

    def details(self):
        data = f"Band {self.name}\n"
        for album in self.albums:
            data += f"{album.details()}\n"
        return data

