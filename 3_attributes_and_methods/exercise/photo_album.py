class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]
        self.current_page = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    def add_photo(self, label):
        if self.current_page == self.pages:
            return f"No more free spots"

        self.photos[self.current_page].append(label)
        printing_slot = len(self.photos[self.current_page])
        printing_page = self.current_page + 1
        if len(self.photos[self.current_page]) == 4:
            self.current_page += 1
        return f"{label} photo added successfully on page {printing_page} " \
               f"slot {printing_slot}"

    def display(self):
        result = ""
        for row in self.photos:
            if len(row) > 0:
                result += "-----------\n"
                result += "[] " * (len(row) - 1) + "[]" + "\n"
            else:
                result += "-----------\n"
                result += f"\n"
        result += "-----------\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
