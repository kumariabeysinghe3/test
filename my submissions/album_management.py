#create album class
class Album:
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"
    
#Create a new list called albums1, add five Album objects to it, and print out the list.
albums1 = [
    Album("Fine Line","Harry Styles", 12),
    Album("Thriller", "Michael Jackson", 9),
    Album("StarBoy", "Weeknd", 18),
    Album("25", "Adele", 11),
    Album("Happier than ever","Billie Eilish", 16)
]
print("albums1:")
for album in albums1:
    print(album)

#sort through list and print out according to number of songs
albums1.sort(key=lambda album: album.number_of_songs)

print("\nSorted albums1 (by number of songs):")
for album in albums1:
    print(album)

#swap position 1
albums1[0], albums1[1] = albums1[1], albums1[0]

print("\nAfter swapping first two elements:")
for album in albums1:
    print(album)

#create new list albums2
albums2 = [
    Album("1989", "Taylor Swift", 13),
    Album("Justice", "Justin Bieber", 16),
    Album("Planet Her", "Doja Cat", 14),
    Album("SOUR", "Olivia Rodrigo", 11),
    Album("Unorthodox Jukebox", "Bruno Mars", 10)
]
print("\nalbums2:")
for album in albums2:
    print(album)

#Copy all of the albums from albums1 into albums2 and add 2 new albums 
albums2.extend(albums1)

albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))

#Sort the albums in albums2 alphabetically according to the album name and print out the sorted list
albums2.sort(key=lambda album: album.album_name)
print("\nSorted Albums2 (alphabetically):")
for album in albums2:
    print(album)

#Search for "Dark Side of the Moon"
for i, album in enumerate(albums2):
    if album.album_name == "Dark Side of the Moon":
        print (f"\n'Dark Side of the Moon found in index:{i}")
        break 
    